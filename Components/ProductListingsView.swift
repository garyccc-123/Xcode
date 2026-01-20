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
    
    // 两个合并后的 JSON 文件名
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
            let source = name.contains("wellcom") ? "Wellcome" : "PNS"
            // 给每个产品添加来源标记（确保 Product 有 var source: String? 属性）
            let sourced = wrapper.products.map { product -> Product in
                var p = product
                p.source = source
                return p
            }
            allProducts.append(contentsOf: sourced)
        } catch {
            print("❌ 加载 \(name) 失败：\(error)")
        }
    }
    return allProducts
}

/// 产品列表视图，支持三级过滤：主分类、子分类、以及 UID 列表
struct ProductListingsView: View {
    /// 主分类名称（可选），传 nil 表示不做此层过滤
    let mainCategoryName: String?
    /// 子分类名称（可选），传 nil 表示不做此层过滤
    let subCategoryName: String?
    /// 第三级允许展示的 UID 列表，传 nil 表示不做此层过滤
    let allowedUIDs: [String]?
    
    /// 用于导航的绑定路径
    @Binding var navigationPath: [Product]
    /// 当前展示的产品数组（未排序、未分页）
    @State private var products: [Product] = []
    /// 排序方式：true = 升序（从低到高），false = 降序（从高到低）
    @State private var sortAscending: Bool = true

    var body: some View {
        VStack {
            // 排序方式分段控制器
            Picker("价格排序", selection: $sortAscending) {
                Text("從低到高").tag(true)
                Text("從高到低").tag(false)
            }
            .pickerStyle(SegmentedPickerStyle())
            .padding(.horizontal)
            
            // 商品列表：使用已排序的计算属性
            List(sortedProducts) { product in
                NavigationLink(
                    destination: ProductDetailView(
                        product: product,
                        navigationPath: $navigationPath,
                        query: .constant("")
                    )
                ) {
                    HStack {
                        // 商品图片或占位
                        if let urlStr = product.image_url,
                           let url = URL(string: urlStr) {
                            AsyncImage(url: url) { image in
                                image.resizable().aspectRatio(contentMode: .fill)
                            } placeholder: {
                                Color.gray
                            }
                            .frame(width: 60, height: 60)
                            .clipped()
                        } else if let sysImg = product.imageName {
                            Image(systemName: sysImg)
                                .resizable()
                                .aspectRatio(contentMode: .fill)
                                .frame(width: 60, height: 60)
                                .clipped()
                        }
                        // 名称和价格
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
        }
        .onAppear { loadProducts() }
    }
    
    /// 计算属性：根据 sortAscending 动态返回已排序数组
    private var sortedProducts: [Product] {
        // 提取价格数字，例如 "$32.00" -> "32.00"
        let extractPrice: (String) -> Double = { str in
            let filtered = str.filter { "0123456789.".contains($0) }
            return Double(filtered) ?? 0
        }
        return products.sorted { lhs, rhs in
            sortAscending
                ? extractPrice(lhs.price) < extractPrice(rhs.price)
                : extractPrice(lhs.price) > extractPrice(rhs.price)
        }
    }

    /// 加载并按主分类、子分类、以及 UID 列表依次过滤
    private func loadProducts() {
        var filtered = loadAllProductsFromDocuments()
        
        // 1. 按主分类过滤
        if let main = mainCategoryName {
            filtered = filtered.filter { $0.mainCategory.contains(main) }
        }
        // 2. 按子分类过滤
        if let sub = subCategoryName {
            filtered = filtered.filter { $0.subCategories.contains(sub) }
        }
        // 3. 按 UID 列表过滤（仅第三级时生效）
        if let uids = allowedUIDs {
            let set = Set(uids)
            filtered = filtered.filter { set.contains($0.uid) }
        }
        
        // 4. 赋值给状态
        products = filtered
    }
}
