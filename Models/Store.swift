//
//  Store.swift
//  Supermarket
//
//  Created by cheung gary on 13/2/2025.
//

import Foundation
import CoreLocation

struct Store: Identifiable, Decodable, Hashable {
    // 新增：brand，用於區分「百佳」或「惠康」
    // 使用 var 而非 let，這樣後續可以在載入後再更新 brand
    var brand: String
    
    let id: String
    let name: String
    let address: String
    let phone: String
    let openingHours: String
    let latitude: Double
    let longitude: Double
    
    func distance(from userLocation: CLLocation?) -> Double? {
        guard let userLocation = userLocation else { return nil }
        let storeLocation = CLLocation(latitude: latitude, longitude: longitude)
        return userLocation.distance(from: storeLocation)
    }

    // 計算屬性，返回 CLLocationCoordinate2D
    var coordinate: CLLocationCoordinate2D {
        CLLocationCoordinate2D(latitude: latitude, longitude: longitude)
    }
    
    enum CodingKeys: String, CodingKey {
        case id
        case name = "名称"
        case address = "地址"
        case phone = "电话"
        case openingHours = "营业时间"
        case latitude
        case longitude
    }
    
    // 自定義解碼器：若 JSON 中沒有 id，則使用 UUID() 生成
    // 同時處理營業時間可能為陣列或字串的情況
    init(from decoder: Decoder) throws {
        let container = try decoder.container(keyedBy: CodingKeys.self)
        
        // 如果 JSON 中沒有 id，就用 UUID
        self.id = (try? container.decode(String.self, forKey: .id)) ?? UUID().uuidString
        self.name = try container.decode(String.self, forKey: .name)
        self.address = try container.decode(String.self, forKey: .address)
        self.phone = try container.decode(String.self, forKey: .phone)
        
        if let hoursArray = try? container.decode([String].self, forKey: .openingHours) {

            self.openingHours = hoursArray.joined(separator: " ")
        } else {
            // 若是一般字串，直接解碼
            self.openingHours = try container.decode(String.self, forKey: .openingHours)
        }
        
        self.latitude = try container.decode(Double.self, forKey: .latitude)
        self.longitude = try container.decode(Double.self, forKey: .longitude)
        
        self.brand = ""
    }
    
}
