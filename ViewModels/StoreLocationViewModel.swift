//
//  StoreLocationViewModel.swift
//  Supermarket
//
//  Created by cheung gary on 13/2/2025.
//

import Foundation

class StoreLocationViewModel: ObservableObject {
    @Published var stores: [Store] = []
    
    init() {
        loadAllStores()
    }
    
    private func loadAllStores() {
        var allStores: [Store] = []
        
        if let pnsStores = loadStores(from: "store_location_pns") {
            allStores.append(contentsOf: pnsStores)
        } else {
            print("未能載入 store_location_pns.json")
        }
        
        if let hkStores = loadStores(from: "store_location") {
            allStores.append(contentsOf: hkStores)
        } else {
            print("未能載入 store_location.json")
        }
        
        print("總共載入 \(allStores.count) 筆資料")
        self.stores = allStores
    }
    
    /// 從指定 JSON 檔案載入 Store 資料，並依據檔案名稱設定 brand 屬性
    private func loadStores(from fileName: String) -> [Store]? {
        guard let url = Bundle.main.url(forResource: fileName, withExtension: "json") else {
            print("找不到 \(fileName).json")
            return nil
        }
        do {
            let data = try Data(contentsOf: url)
            let decoder = JSONDecoder()
            var stores = try decoder.decode([Store].self, from: data)
            // 根據檔案名稱設定品牌
            let brand = fileName == "store_location_pns" ? "百佳" : "惠康"
            stores = stores.map { store in
                var s = store
                s.brand = brand
                return s
            }
            print("成功載入 \(fileName).json，共 \(stores.count) 筆資料")
            return stores
        } catch {
            print("解析 \(fileName).json 錯誤: \(error)")
            return nil
        }
    }
}
