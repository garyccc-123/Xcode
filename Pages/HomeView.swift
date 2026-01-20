//
//  HomeView.swift
//  Supermarket
//
//  Created by cheung gary on 6/2/2025.
//

import SwiftUI

import SwiftUI

struct HomeView: View {
    // 搜索相關狀態
    @State private var query: String = ""
    @State private var searchResults: [Product] = []
    @State private var isLoading: Bool = false
    @State private var errorMessage: String?
    @State private var searchTask: Task<Void, Never>? = nil
    
    // 導航堆疊管理
    @State private var navigationPath: [Product] = []
    
    var body: some View {
        NavigationStack(path: $navigationPath) {
            VStack {
                // 搜索欄區域
                HStack(spacing: 8) {
                    Image(systemName: "magnifyingglass")
                        .foregroundColor(.gray)
                    TextField("Search products...", text: $query)
                        .disableAutocorrection(true)
                        .autocapitalization(.none)
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
                                    await performSearch(query: newValue)
                                }
                            }
                        }
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
                
                if isLoading {
                    ProgressView("Searching...")
                        .padding()
                }
                if let errorMessage = errorMessage {
                    Text(errorMessage)
                        .foregroundColor(.red)
                        .padding()
                }
                
                if query.isEmpty {
                    // 預設首頁內容
                    ScrollView {
                        VStack(spacing: 20) {
                            LoginBannerView()
                            QuickAccessView()
                            PromotionsView()
                            
                            // 使用新的 ProductListingsView 初始化
                            ProductListingsView(
                                mainCategoryName: nil,
                                subCategoryName: nil,
                                navigationPath: $navigationPath
                            )
                        }
                        .padding()
                    }
                } else {
                    // 顯示搜索結果列表
                    List(searchResults) { product in
                        NavigationLink(destination: ProductDetailView(
                            product: product,
                            navigationPath: $navigationPath,
                            query: $query
                        )) {
                            ProductRowView(product: product)
                        }
                    }
                    .listStyle(PlainListStyle())
                }
            }
            .navigationTitle("")
            .navigationDestination(for: Product.self) { product in
                ProductDetailView(
                    product: product,
                    navigationPath: $navigationPath,
                    query: $query
                )
            }
        }
        .onAppear {
            copyCombinedProductsFileToDocuments()
        }
    }
    
   
    func performSearch(query: String) async {
        do {
            try await Task.sleep(nanoseconds: 500_000_000)
            let allProducts = loadAllProductsFromDocuments()
            let filtered = allProducts.filter { product in
                product.name.localizedCaseInsensitiveContains(query)
            }
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
    
    /// 从 Documents 加载 Wellcome 与 PNS 两个 JSON，并给每个 product 填充 source 字段
    private func loadAllProductsFromDocuments() -> [Product] {
        let fileManager = FileManager.default
        guard let docsUrl = fileManager.urls(for: .documentDirectory, in: .userDomainMask).first else {
            print("无法取得 Documents 目录")
            return []
        }
        
        // 两个文件名
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
                // 解码外层结构
                let wrapper = try decoder.decode(CombinedProducts.self, from: data)
                
                // 根据文件名判断来源
                let src = name.contains("wellcom") ? "Wellcome" : "PNS"
                
                // 给每个 product 赋值 source
                let productsWithSource = wrapper.products.map { product -> Product in
                    var p = product
                    p.source = src
                    return p
                }
                
                allProducts.append(contentsOf: productsWithSource)
            } catch {
                print("❌ 加载 \(name) 失败：\(error)")
            }
        }
        
        return allProducts
    }
}
