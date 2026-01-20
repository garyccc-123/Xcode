//
//  NearbyStoresView.swift
//  Supermarket
//
//  Created by cheung gary on 13/2/2025.
//

import SwiftUI
import MapKit

struct NearbyStoresView: View {
    @StateObject private var locationManager = LocationManager()
    @StateObject private var viewModel = StoreLocationViewModel()
    
    // 默认地图区域（如果用户位置尚未获取，则使用此默认区域，例如香港）
    @State private var region = MKCoordinateRegion(
        center: CLLocationCoordinate2D(latitude: 22.3193, longitude: 114.1694),
        span: MKCoordinateSpan(latitudeDelta: 0.1, longitudeDelta: 0.1)
    )
    
    var body: some View {
        NavigationStack {
            Map(coordinateRegion: $region, annotationItems: filteredStores()) { store in
                MapAnnotation(coordinate: store.coordinate) {
                    VStack(spacing: 4) {
                        Image(systemName: "mappin.circle.fill")
                            .foregroundColor(.red)
                            .font(.title)
                        Text(store.name)
                            .font(.caption)
                            .padding(4)
                            .background(Color.white)
                            .cornerRadius(4)
                    }
                }
            }
            .ignoresSafeArea()
            .navigationTitle("附近门市")
            .onAppear {
                // 若获取到用户位置，则更新 region 中心
                if let current = locationManager.currentLocation {
                    region.center = current.coordinate
                }
            }
            .onChange(of: locationManager.currentLocation) { newLocation in
                if let newLocation = newLocation {
                    region.center = newLocation.coordinate
                }
            }
            .alert(item: $viewModel.errorMessage) { errorMsg in
                Alert(title: Text("错误"), message: Text(errorMsg), dismissButton: .default(Text("确定")))
            }
        }
    }
    
    /// 根据用户当前位置筛选附近门店（例如半径 5000 米以内）
    func filteredStores() -> [Store] {
        guard let currentLocation = locationManager.currentLocation else {
            return viewModel.stores
        }
        return viewModel.stores.filter { store in
            let storeLocation = CLLocation(latitude: store.latitude, longitude: store.longitude)
            return currentLocation.distance(from: storeLocation) <= 5000 // 5公里内
        }
    }
}

struct NearbyStoresView_Previews: PreviewProvider {
    static var previews: some View {
        NearbyStoresView()
    }
}
