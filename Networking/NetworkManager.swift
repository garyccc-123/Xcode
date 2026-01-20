//
//  NetworkManager.swift
//  Supermarket
//
//  Created by cheung gary on 6/2/2025.
//

import Foundation

class NetworkManager {
    static let shared = NetworkManager()
    
    // 示例接口地址，实际项目中请替换为真实 API 地址
    let baseURL = "https://example.com/api/products"
    
    // 使用 async/await 获取产品数据
    func fetchProducts() async throws -> [Product] {
        guard let url = URL(string: baseURL) else {
            throw URLError(.badURL)
        }
        
        let (data, response) = try await URLSession.shared.data(from: url)
        
        // 检查 HTTP 状态码是否为 200
        guard let httpResponse = response as? HTTPURLResponse,
              httpResponse.statusCode == 200 else {
            throw URLError(.badServerResponse)
        }
        
        let decoder = JSONDecoder()
        // 假設遠端回傳的 JSON 結構與本地一致，即一個包含 update_date 與 products 的字典
        let combined = try decoder.decode(CombinedProducts.self, from: data)
        return combined.products
    }
}
