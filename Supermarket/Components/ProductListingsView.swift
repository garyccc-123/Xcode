//
//  ProductListingsView.swift
//  Supermarket
//
//  Created by cheung gary on 6/2/2025.
//

import SwiftUI

struct ProductListingsView: View {
    @Binding var navigationPath: [Product]
    @State private var products: [Product] = []
    @State private var isLoading: Bool = true
    @State private var errorMessage: String?
    
    
    // 两列自适应网格布局
    let columns = [
        GridItem(.flexible(), spacing: 16),
        GridItem(.flexible(), spacing: 16)
    ]
    
    var body: some View {
        VStack {
            if isLoading {
                ProgressView("加载中...")
                    .task {
                        await fetchProducts()
                    }
            } else if let errorMessage = errorMessage {
                Text(errorMessage)
                    .foregroundColor(.red)
                    .padding()
            } else {
                LazyVGrid(columns: columns, spacing: 16) {
                    ForEach(products) { product in
                        NavigationLink(destination: ProductDetailView(product: product, navigationPath: $navigationPath)) {
                            ProductCardView(product: product)
                        }
                        .buttonStyle(PlainButtonStyle())
                    }
                }
                .padding(.horizontal)
            }
        }
    }
    
    func fetchProducts() async {
        do {
            products = try await NetworkManager.shared.fetchProducts()
            isLoading = false
        } catch {
            errorMessage = "加载数据失败: \(error.localizedDescription)"
            isLoading = false
        }
    }
}

struct ProductListingsView_Previews: PreviewProvider {
    static var previews: some View {
        // 预览时传入一个空的 binding
        ProductListingsView(navigationPath: .constant([]))
    }
}
