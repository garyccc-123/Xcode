//
//  ProductImporter.swift
//  Supermarket
//
//  Created by cheung gary on 7/3/2025.
//


import CoreData
import Foundation

// MARK: - 定義 JSON 的最外層結構（包含更新日期與產品陣列）
struct CombinedProducts: Decodable {
    let update_date: String
    let products: [Product]
}

// 如果你有單獨的 ProductJSON 結構也可以定義，但這裡直接用 Product 作解碼

/// 將合併後的 JSON 數據匯入到 Core Data 中
/// - Parameters:
///   - context: NSManagedObjectContext，通常為 PersistenceController.shared.viewContext
func importProducts(from jsonURL: URL, into context: NSManagedObjectContext) {
    do {
        let data = try Data(contentsOf: jsonURL)
        let decoder = JSONDecoder()
        
        // 1. 使用 CombinedProducts 結構進行解碼
        let combined = try decoder.decode(CombinedProducts.self, from: data)
        let products = combined.products
        
        // 2. 根據需求決定是否清除舊資料，以下使用 batch delete
        let fetchRequest: NSFetchRequest<NSFetchRequestResult> = NSFetchRequest(entityName: "ProductEntity")
        let deleteRequest = NSBatchDeleteRequest(fetchRequest: fetchRequest)
        try context.execute(deleteRequest)
        
        // 3. 將 JSON 中的每筆產品數據匯入 Core Data
        for product in products {
            // 根據唯一約束 (例如 url) 檢查是否已有相同產品
            let fetch: NSFetchRequest<ProductEntity> = ProductEntity.fetchRequest()
            fetch.predicate = NSPredicate(format: "url == %@", product.url)
            let results = try context.fetch(fetch)
            
            let productEntity: ProductEntity
            if let existing = results.first {
                // 若已存在則更新
                productEntity = existing
            } else {
                // 若不存在則新增
                productEntity = ProductEntity(context: context)
                productEntity.url = product.url
            }
            
            productEntity.name = product.name
            productEntity.price = product.price
            productEntity.offer = product.offer
            productEntity.date = product.date
            productEntity.image_url = product.image_url
            // 將 categories 陣列轉換為逗號分隔字串存儲
            productEntity.categories = product.categories.joined(separator: ",")
            
            // 注意：請確保在 Data Model 中，ProductEntity 的 prices 屬性已設定 Value Transformer 為 "NSSecureUnarchiveFromData"
            productEntity.prices = product.prices as NSDictionary
        }
        
        try context.save()
        print("匯入成功，共 \(products.count) 筆產品，更新時間：\(combined.update_date)")
    } catch {
        print("匯入失敗：\(error)")
    }
}
