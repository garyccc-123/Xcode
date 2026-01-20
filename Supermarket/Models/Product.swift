//
//  Product.swift
//  Supermarket
//
//  Created by cheung gary on 6/2/2025.
//

import Foundation

struct Product: Identifiable, Hashable, Decodable {
    let id = UUID()
    let name: String
    let imageName: String
    let prices: [String: String]
}
