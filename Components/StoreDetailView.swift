//
//  StoreDetailView.swift
//  Supermarket
//
//  Created by cheung gary on 19/2/2025.
//

import SwiftUI
import MapKit

struct StoreDetailView: View, Identifiable {
    let store: Store
    
    var id: String { store.id }
    
    // 用來觸發「選擇地圖」對話框
    @State private var showMapOptions = false
    
    // 檢查是否安裝 Google Maps
    private var canOpenGoogleMaps: Bool {
        if let url = URL(string: "comgooglemaps://"),
           UIApplication.shared.canOpenURL(url) {
            return true
        }
        return false
    }
    
    var body: some View {
        ScrollView {
            VStack(spacing: 0) {
                // 頂部橫幅
                ZStack(alignment: .bottomLeading) {
                    LinearGradient(
                        gradient: Gradient(colors: [Color.blue, Color.purple]),
                        startPoint: .topLeading,
                        endPoint: .bottomTrailing
                    )
                    .frame(height: 160)
                    
                    VStack(alignment: .leading, spacing: 8) {
                        Text(store.name)
                            .font(.largeTitle)
                            .bold()
                            .foregroundColor(.white)
                        
                        Text(store.address)
                            .foregroundColor(.white.opacity(0.9))
                            .font(.subheadline)
                    }
                    .padding(.horizontal)
                    .padding(.bottom, 12)
                }
                
                VStack(alignment: .leading, spacing: 16) {
                    // 電話
                    if !store.phone.isEmpty {
                        HStack(spacing: 8) {
                            Image(systemName: "phone.fill").foregroundColor(.green)
                            Text(store.phone).font(.headline)
                        }
                    }
                    
                    // 營業時間
                    if !store.openingHours.isEmpty {
                        HStack(spacing: 8) {
                            Image(systemName: "clock").foregroundColor(.orange)
                            Text(store.openingHours).font(.headline)
                        }
                    }
                    
                    Divider()
                    
                    // 導航按鈕，彈出選擇對話框
                    Button {
                        showMapOptions = true
                    } label: {
                        Label("在地圖中導航", systemImage: "map")
                            .font(.headline)
                            .frame(maxWidth: .infinity)
                            .padding()
                            .background(Color.blue)
                            .foregroundColor(.white)
                            .cornerRadius(8)
                    }
                    
                    Divider()
                    
                    Text("更多介紹:")
                        .font(.headline)
                    Text("店家更多描述或特色...")
                        .font(.subheadline)
                        .foregroundColor(.secondary)
                }
                .padding()
            }
        }
        .edgesIgnoringSafeArea(.top)
        
        // iOS 15+ ConfirmationDialog
        // 選擇「Google Maps」或「Apple Maps」
        .confirmationDialog("選擇地圖", isPresented: $showMapOptions, actions: {
            // 若使用者安裝 Google Maps => 提供此選項
            if canOpenGoogleMaps {
                Button("Google Maps") {
                    openGoogleMaps()
                }
            }
            // 不管有沒有 Google Maps 都可以 Apple
            Button("Apple Maps") {
                openAppleMaps()
            }
            // 取消自動生成
        }, message: {
            Text("請選擇地圖 App")
        })
    }
    
    // MARK: - 開 Google Maps
    private func openGoogleMaps() {
        let lat = store.latitude
        let lon = store.longitude
        let urlString = "comgooglemaps://?daddr=\(lat),\(lon)&directionsmode=driving"
        if let url = URL(string: urlString) {
            UIApplication.shared.open(url)
        }
    }
    
    // MARK: - 開 Apple Maps
    private func openAppleMaps() {
        let coord = CLLocationCoordinate2D(latitude: store.latitude, longitude: store.longitude)
        let placemark = MKPlacemark(coordinate: coord)
        let mapItem = MKMapItem(placemark: placemark)
        mapItem.name = store.name
        mapItem.openInMaps(launchOptions: [
            MKLaunchOptionsDirectionsModeKey: MKLaunchOptionsDirectionsModeDriving
        ])
    }
}
