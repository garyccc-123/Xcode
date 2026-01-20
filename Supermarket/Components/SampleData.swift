//
//  SampleData.swift
//  Supermarket
//
//  Created by cheung gary on 7/2/2025.
//

import Foundation
import SwiftUI


struct SampleData {
    static let products: [Product] = [
        Product(name: "Apple", imageName: "applelogo", prices: ["Supermarket A": "¥5", "Supermarket B": "¥4.5"]),
        Product(name: "Milk", imageName: "carton", prices: ["Supermarket A": "¥3", "Supermarket B": "¥2.8"]),
        Product(name: "Bread", imageName: "bag.fill", prices: ["Supermarket A": "¥2", "Supermarket B": "¥2.2"]),
        Product(name: "Orange", imageName: "sun.max.fill", prices: ["Supermarket A": "¥4", "Supermarket B": "¥3.8"]),
        // 你可以在这里增加更多示例数据
    ]
}
