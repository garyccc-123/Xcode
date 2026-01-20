//
//  Store.swift
//  Supermarket
//
//  Created by cheung gary on 13/2/2025.
//

import Foundation
import CoreLocation

struct Store: Identifiable, Decodable, Hashable {
    let id: String
    let name: String
    let address: String
    let latitude: Double
    let longitude: Double
    let phone: String
    let openingHours: String
    
    // 计算属性：返回 CLLocationCoordinate2D
    var coordinate: CLLocationCoordinate2D {
        CLLocationCoordinate2D(latitude: latitude, longitude: longitude)
    }
}
