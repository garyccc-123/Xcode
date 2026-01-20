//
//  ProductListingsView.swift
//  Supermarket
//
//  Created by cheung gary on 7/2/2025.
//

import SwiftUI

/// 从 Documents 加载 Wellcome + PNS 两个 JSON，并统一返回标注了来源的产品列表
func loadAllProductsFromDocuments() -> [Product] {
    let fileManager = FileManager.default
    guard let docsUrl = fileManager.urls(for: .documentDirectory, in: .userDomainMask).first else {
        print("无法取得 Documents 目录")
        return []
    }
    
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

struct ProductListingsView: View {
    /// 主分類選擇（例如傳自上層的 NavigationLink）
    let mainCategoryName: String?
    /// 子分類選擇
    let subCategoryName: String?
    
    @State private var products: [Product] = []
    @Binding var navigationPath: [Product]

    var body: some View {
        List(products) { product in
            NavigationLink(
                destination: ProductDetailView(
                    product: product,
                    navigationPath: $navigationPath,
                    query: .constant("")
                )
            ) {
                HStack {
                    if let imageUrl = product.image_url, let url = URL(string: imageUrl) {
                        AsyncImage(url: url) { image in
                            image.resizable().aspectRatio(contentMode: .fill)
                        } placeholder: {
                            Color.gray
                        }
                        .frame(width: 60, height: 60)
                        .clipped()
                    } else if let systemImage = product.imageName {
                        Image(systemName: systemImage)
                            .resizable()
                            .aspectRatio(contentMode: .fill)
                            .frame(width: 60, height: 60)
                            .clipped()
                    }

                    VStack(alignment: .leading) {
                        Text(product.name)
                            .font(.headline)
                        Text(product.price)
                            .font(.subheadline)
                    }
                }
            }
        }
        .navigationTitle(mainCategoryName ?? subCategoryName ?? "所有產品")
        .onAppear {
            loadProducts()
        }
    }

    /// 加载并按主/子分类过滤产品
    func loadProducts() {
        // 1. 加载所有来源的产品
        let allProducts = loadAllProductsFromDocuments()
        
        // 2. 按主分类和子分类依次过滤
        var filtered = allProducts
        
        if let main = mainCategoryName {
            filtered = filtered.filter { $0.mainCategory.contains(main) }
        }
        
        if let sub = subCategoryName {
            filtered = filtered.filter { $0.subCategories.contains(sub) }
        }
        
        // 3. 赋值给列表
        products = filtered
    }
}
