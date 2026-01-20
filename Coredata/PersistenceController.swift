//
//  PersistenceController.swift
//  Supermarket
//
//  Created by cheung gary on 7/3/2025.
//

import CoreData
import Foundation

struct PersistenceController {
    // 共用的實例
    static let shared = PersistenceController()

    // NSPersistentContainer 會載入你的 .xcdatamodeld（此處名稱為 "SupermarketModel"，
    // 請根據你自己的資料模型名稱進行修改）
    let container: NSPersistentContainer

    // 初始化函式，可指定 inMemory 模式（例如用於測試）
    init(inMemory: Bool = false) {
        container = NSPersistentContainer(name: "SupermarketModel")
        if inMemory {
            // 若使用 inMemory 模式，則存儲位置設為 /dev/null
            container.persistentStoreDescriptions.first?.url = URL(fileURLWithPath: "/dev/null")
        }
        // 載入 Persistent Stores
        container.loadPersistentStores { storeDescription, error in
            if let error = error as NSError? {
                // 在生產環境中，請依需求改用適當的錯誤處理機制
                fatalError("Unresolved error \(error), \(error.userInfo)")
            }
        }
        
        // 設置自動合併父上下文的變更，方便多執行緒更新
        container.viewContext.automaticallyMergesChangesFromParent = true
        // 設置合併策略，當有衝突時，以物件屬性值為準（根據需求可調整）
        container.viewContext.mergePolicy = NSMergeByPropertyObjectTrumpMergePolicy
    }

    // 提供一個共用的 viewContext 屬性
    var viewContext: NSManagedObjectContext {
        return container.viewContext
    }
}
