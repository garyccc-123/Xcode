//
//  NearbyStoresView.swift
//  Supermarket
//
//  Created by cheung gary on 13/2/2025.
//
//

import SwiftUI
import MapKit
import CoreLocation
import UIKit

struct NearbyStoresView: View {
    @StateObject private var viewModel = StoreLocationViewModel()
    @StateObject private var locationManager = LocationManager()
    
    // 地圖區域設定（香港附近，縮放較近）
    @State private var region = MKCoordinateRegion(
        center: CLLocationCoordinate2D(latitude: 22.3, longitude: 114.2),
        span: MKCoordinateSpan(latitudeDelta: 0.01, longitudeDelta: 0.01)
    )
    
    @State private var didCenterMapOnce = false
    
    private enum BottomSheetMode: CaseIterable { case tip, half, full }
    @State private var currentMode: BottomSheetMode = .half
    @State private var currentOffset: CGFloat = 0
    @GestureState private var dragTranslation: CGFloat = 0
    @State private var lastGeoSize: CGSize = .zero
    
    // 點擊店家後顯示詳細頁
    @State private var selectedStore: Store? = nil
    
    // 分段控制器：選擇超市品牌
    @State private var selectedBrand: String = "百佳"
    let brands = ["百佳", "惠康"]
    
    var body: some View {
        GeometryReader { geo in
            ZStack {
                // 地圖背景：只顯示過濾後的店家標註
                Map(coordinateRegion: $region,
                    showsUserLocation: true,
                    annotationItems: filteredStores()) { store in
                    MapAnnotation(coordinate: store.coordinate) {
                        // 根據品牌決定標註顏色：藍色代表百佳，紅色代表惠康
                        let pinColor: Color = store.brand.lowercased() == "百佳" ? .blue : .red
                        Image(systemName: "mappin.circle.fill")
                            .resizable()
                            .frame(width: 30, height: 30)
                            .foregroundColor(pinColor)
                            .onTapGesture {
                                selectedStore = store
                            }
                    }
                }
                .ignoresSafeArea()
                
                // 半透明遮罩（隨底部卡片位置改變）
                Color.black.opacity(overlayOpacity(in: geo.size))
                    .ignoresSafeArea()
                
                // 底部可拖曳卡片
                bottomSheetCard(in: geo)
            }
            .navigationTitle("附近分店")
            .navigationBarTitleDisplayMode(.inline)
            .onAppear {
                if let loc = locationManager.currentLocation, !didCenterMapOnce {
                    region.center = loc.coordinate
                    didCenterMapOnce = true
                }
                lastGeoSize = geo.size
                currentMode = .half
                currentOffset = offset(for: .half, in: geo.size)
            }
            .onChange(of: locationManager.currentLocation) { newLoc in
                if let loc = newLoc, !didCenterMapOnce {
                    region.center = loc.coordinate
                    didCenterMapOnce = true
                }
            }
            .onChange(of: geo.size) { newSize in
                lastGeoSize = newSize
                currentOffset = offset(for: currentMode, in: newSize)
            }
            .sheet(item: $selectedStore) { store in
                StoreDetailView(store: store)
                    .presentationDetents([.fraction(0.5), .large])
                    .presentationDragIndicator(.visible)
            }
        }
    }
    
    // MARK: - 底部卡片視圖
    private func bottomSheetCard(in geo: GeometryProxy) -> some View {
        ZStack(alignment: .top) {
            BlurView(style: .systemMaterial)
                .clipShape(RoundedRectangle(cornerRadius: 16))
                .shadow(radius: 5)
            
            VStack(spacing: 0) {
                RoundedRectangle(cornerRadius: 2.5)
                    .frame(width: 40, height: 5)
                    .foregroundColor(.secondary)
                    .padding(.vertical, 8)
                
                Divider()
                
                // 分段控制器：選擇品牌
                Picker("超市品牌", selection: $selectedBrand) {
                    ForEach(brands, id: \.self) { brand in
                        Text(brand)
                    }
                }
                .pickerStyle(SegmentedPickerStyle())
                .padding(.horizontal)
                
                Divider()
                
                Text("店家列表")
                    .font(.headline)
                    .padding(.vertical, 8)
                Divider()
                
                if viewModel.stores.isEmpty {
                    Text("尚無店家資料")
                        .padding()
                } else {
                    List(filteredStores(), id: \.id) { store in
                        storeRow(store)
                            .onTapGesture {
                                selectedStore = store
                            }
                    }
                }
            }
        }
        .frame(width: geo.size.width, height: cardHeight(in: geo.size))
        .position(x: geo.size.width / 2, y: cardPositionY(in: geo.size))
        .animation(.interactiveSpring(), value: dragTranslation)
        .gesture(
            DragGesture()
                .updating($dragTranslation) { value, state, _ in
                    state = value.translation.height
                }
                .onEnded { drag in
                    handleDragEnd(drag.translation.height, geoSize: geo.size)
                }
        )
    }
    
    // MARK: - 根據所選品牌過濾店家，並依據距離排序
    private func filteredStores() -> [Store] {
        return viewModel.stores
            .filter { store in
                store.brand.lowercased() == selectedBrand.lowercased()
            }
            .sorted { s1, s2 in
                let d1 = s1.distance(from: locationManager.currentLocation) ?? Double.greatestFiniteMagnitude
                let d2 = s2.distance(from: locationManager.currentLocation) ?? Double.greatestFiniteMagnitude
                return d1 < d2
            }
    }
    
    // MARK: - 列表中單行視圖
    private func storeRow(_ store: Store) -> some View {
        let dist = store.distance(from: locationManager.currentLocation)
        return VStack(alignment: .leading, spacing: 4) {
            Text(store.name).bold()
            if let m = dist {
                Text(String(format: "距離：%.2f 公里", m / 1000.0))
                    .font(.caption)
                    .foregroundColor(.secondary)
            } else {
                Text("距離：無法取得")
                    .font(.caption)
                    .foregroundColor(.secondary)
            }
            Text(store.address)
                .font(.caption)
                .foregroundColor(.secondary)
        }
        .padding(.vertical, 4)
    }
    
    // MARK: - 底部卡片高度計算
    private func offset(for mode: BottomSheetMode, in size: CGSize) -> CGFloat {
        switch mode {
        case .tip:
            return size.height * 0.85
        case .half:
            return size.height * 0.68
        case .full:
            return 60
        }
    }
    
    private func cardHeight(in size: CGSize) -> CGFloat {
        let topY = offsetY()
        return max(size.height - topY, 0)
    }
    
    private func cardPositionY(in size: CGSize) -> CGFloat {
        offsetY() + cardHeight(in: size) / 2
    }
    
    private func offsetY() -> CGFloat {
        currentOffset + dragTranslation
    }
    
    private func handleDragEnd(_ dragEnd: CGFloat, geoSize: CGSize) {
        let newY = offsetY() + dragEnd
        let states = BottomSheetMode.allCases.map { ($0, offset(for: $0, in: geoSize)) }
        if let (bestMode, _) = states.min(by: { abs($0.1 - newY) < abs($1.1 - newY) }) {
            currentMode = bestMode
            currentOffset = offset(for: bestMode, in: geoSize)
        }
    }
    
    private func overlayOpacity(in size: CGSize) -> Double {
        let minY = offset(for: .full, in: size)
        let maxY = offset(for: .tip, in: size)
        let curY = offsetY()
        let ratio = (curY - minY) / (maxY - minY)
        let alpha = 0.6 - (0.6 * ratio)
        return max(0, min(0.6, alpha))
    }
}

private struct BlurView: UIViewRepresentable {
    let style: UIBlurEffect.Style
    func makeUIView(context: Context) -> UIVisualEffectView {
        UIVisualEffectView(effect: UIBlurEffect(style: style))
    }
    func updateUIView(_ uiView: UIVisualEffectView, context: Context) {}
}
