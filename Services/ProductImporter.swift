//
//  ProductImporter.swift
//  Supermarket
//
//  Created by cheung gary on 7/3/2025.
//



import CoreData
import Foundation

// MARK: - 定義 JSON 的最外層結構（包含更新日期與產品陣列）
// 使用自定义 init 跳過格式錯誤或 null 的條目
struct CombinedProducts: Decodable {
    let update_date: String
    let products: [Product]

    enum CodingKeys: String, CodingKey {
        case update_date, products
    }

    init(from decoder: Decoder) throws {
        let container = try decoder.container(keyedBy: CodingKeys.self)
        // 1. 正常解碼 update_date
        update_date = try container.decode(String.self, forKey: .update_date)

        // 2. 解碼 products 陣列，跳過解碼失敗的條目
        var array = try container.nestedUnkeyedContainer(forKey: .products)
        var validProducts: [Product] = []

        while !array.isAtEnd {
            do {
                let p = try array.decode(Product.self)
                validProducts.append(p)
            } catch {
                // 解碼失敗，例如必需字段為 null，使用 EmptyCodable 吞掉該條
                _ = try? array.decode(EmptyCodable.self)
                // 可選：打印 log 以便調試
                // print("跳過無效產品：\(error)")
            }
        }
        products = validProducts
    }
}

/// 用來吞掉解碼失敗的無用結構
private struct EmptyCodable: Decodable {}

/// 將匯入的 JSON 資料導入 Core Data
/// - Parameters:
///   - jsonURL: 指向 JSON 檔案的 URL
///   - context: NSManagedObjectContext（一般使用 PersistenceController.shared.viewContext）
func importProducts(from jsonURL: URL, into context: NSManagedObjectContext) {
    do {
        // 1. 讀取 JSON
        let data = try Data(contentsOf: jsonURL)
        let decoder = JSONDecoder()
        
        // 2. 解碼並過濾無效記錄
        let combined = try decoder.decode(CombinedProducts.self, from: data)
        let products = combined.products
        
        // 3. 清除舊資料（可依需求調整）
        let fetchRequest: NSFetchRequest<NSFetchRequestResult> = NSFetchRequest(entityName: "ProductEntity")
        let deleteRequest = NSBatchDeleteRequest(fetchRequest: fetchRequest)
        try context.execute(deleteRequest)
        
        // 4. 匯入或更新每筆產品
        for product in products {
            let fetch: NSFetchRequest<ProductEntity> = ProductEntity.fetchRequest()
            fetch.predicate = NSPredicate(format: "url == %@", product.url)
            let results = try context.fetch(fetch)

            let entity: ProductEntity
            if let existing = results.first {
                entity = existing
            } else {
                entity = ProductEntity(context: context)
                entity.url = product.url
            }

            // 基本屬性
            entity.name = product.name
            entity.price = product.price
            entity.offer = product.offer
            entity.date = product.date
            entity.image_url = product.image_url

            // categories：合併主分類與子分類
            let cats = (product.mainCategory ?? []) + (product.subCategories ?? [])
            entity.categories = cats.joined(separator: ",")

            // prices：確保 Value Transformer 設為 NSSecureUnarchiveFromData
            entity.prices = product.prices as NSDictionary
        }
        
        // 5. 保存
        try context.save()
        print("匯入成功，共 \(products.count) 筆產品，更新時間：\(combined.update_date)")
    } catch {
        print("匯入失敗：\(error)")
    }
}
