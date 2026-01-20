//
//  SearchView.swift
//  Supermarket
//
//  Created by cheung gary on 6/2/2025.
//



import SwiftUI

struct SearchView: View {
    @State private var query: String = ""
    @State private var searchResults: [Product] = []
    @State private var isLoading: Bool = false
    @State private var errorMessage: String?
    @State private var searchTask: Task<Void, Never>? = nil
    
    // 獨立搜索頁的導航堆疊管理
    @State private var navigationPath: [Product] = []
    
    var body: some View {
        NavigationStack(path: $navigationPath) {
            VStack {
                // 搜索框
                HStack(spacing: 8) {
                    Image(systemName: "magnifyingglass")
                        .foregroundColor(.gray)
                    
                    TextField("Search products...", text: $query, onCommit: {
                        triggerSearch()
                    })
                    .disableAutocorrection(true)
                    .autocapitalization(.none)
                    
                    if !query.isEmpty {
                        Button(action: {
                            query = ""
                            searchResults = []
                            errorMessage = nil
                        }) {
                            Image(systemName: "xmark.circle.fill")
                                .foregroundColor(.gray)
                        }
                    }
                }
                .padding(10)
                .background(Color(.systemGray6))
                .cornerRadius(8)
                .padding(.horizontal)
                .padding(.top, 10)
                // 在使用者輸入時，0.5 秒後再執行搜尋
                .onChange(of: query) { newValue in
                    searchTask?.cancel()
                    if newValue.isEmpty {
                        searchResults = []
                        errorMessage = nil
                        isLoading = false
                    } else {
                        isLoading = true
                        searchTask = Task {
                            try? await Task.sleep(nanoseconds: 500_000_000)
                            await searchProducts(query: newValue)
                        }
                    }
                }
                
                // 顯示搜尋進度或錯誤
                if isLoading {
                    ProgressView("Searching...")
                        .padding()
                }
                if let errorMessage = errorMessage {
                    Text(errorMessage)
                        .foregroundColor(.red)
                        .padding()
                }
                
                // 搜尋結果列表
                List(searchResults) { product in
                    NavigationLink(value: product) {
                        ProductRowView(product: product)
                    }
                }
                .listStyle(PlainListStyle())
            }
            .navigationTitle("Search")
            .navigationDestination(for: Product.self) { product in
                ProductDetailView(product: product, navigationPath: $navigationPath)
            }
        }
    }
    
    /// 使用者按下「搜尋」或鍵盤「Return」時
    private func triggerSearch() {
        guard !query.isEmpty else { return }
        isLoading = true
        searchTask?.cancel()
        searchTask = Task {
            await searchProducts(query: query)
        }
    }
    
    /// 依照關鍵字搜尋產品
    func searchProducts(query: String) async {
        do {
            // 模擬輸入延遲
            try await Task.sleep(nanoseconds: 500_000_000)
            
            let allProducts = loadProductsFromSingleFile()
            
            // 過濾符合關鍵字的產品（以 name 為例）
            let filtered = allProducts.filter { product in
                product.name.localizedCaseInsensitiveContains(query)
            }
            
            // 回到主執行緒更新 UI
            await MainActor.run {
                searchResults = filtered
                isLoading = false
            }
        } catch {
            if error is CancellationError { return }
            await MainActor.run {
                errorMessage = "Search failed: \(error.localizedDescription)"
                isLoading = false
            }
        }
    }
    
    /// MARK: - 从 Documents 中一次性加载 Wellcome & PNS 两个 JSON，并合并返回
    private func loadProductsFromSingleFile() -> [Product] {
        let fileManager = FileManager.default
        guard let docsUrl = fileManager.urls(for: .documentDirectory, in: .userDomainMask).first else {
            print("无法取得 Documents 目录")
            return []
        }
        
        // 要加载的两份 JSON 文件名
        let fileNames = [
            "combined_products_wellcom_with_eng.json",
            "combined_products_pns_with_eng.json"
        ]
        
        var allProducts: [Product] = []
        let decoder = JSONDecoder()
        
        for name in fileNames {
            let fileURL = docsUrl.appendingPathComponent(name)
            do {
                let data = try Data(contentsOf: fileURL)
                let wrapper = try decoder.decode(CombinedProducts.self, from: data)
                // 根据文件名打上来源标签
                let src = name.contains("wellcom") ? "Wellcome" : "PNS"
                let withSource = wrapper.products.map { product -> Product in
                    var p = product
                    p.source = src
                    return p
                }
                allProducts.append(contentsOf: withSource)
            } catch {
                print("❌ 加载 \(name) 失败：\(error)")
            }
        }
        
        return allProducts
    }
}
