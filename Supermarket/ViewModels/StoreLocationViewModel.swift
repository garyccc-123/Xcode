//
//  StoreLocationViewModel.swift
//  Supermarket
//
//  Created by cheung gary on 13/2/2025.
//

import Foundation

class StoreLocationViewModel: ObservableObject {
    @Published var stores: [Store] = []
    @Published var errorMessage: String?
    
    init() {
        loadStores()
    }
    
    func loadStores() {
        // 注意：文件名为 "store_location.json"
        guard let url = Bundle.main.url(forResource: "store_location", withExtension: "json") else {
            errorMessage = "找不到 store_location.json 文件"
            return
        }
        
        do {
            let data = try Data(contentsOf: url)
            let decoder = JSONDecoder()
            let loadedStores = try decoder.decode([Store].self, from: data)
            DispatchQueue.main.async {
                self.stores = loadedStores
            }
        } catch {
            DispatchQueue.main.async {
                self.errorMessage = error.localizedDescription
            }
        }
    }
}
