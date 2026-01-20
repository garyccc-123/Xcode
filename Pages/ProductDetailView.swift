//
//  ProductDetailView.swift
//  Supermarket
//
//  Created by cheung gary on 6/2/2025.
//

import SwiftUI

struct ProductDetailView: View {
    let product: Product
    @Binding var navigationPath: [Product]
    @Binding var query: String
    
    @ObservedObject var favoritesManager = FavoritesManager.shared
    @Environment(\.dismiss) var dismiss
    
    @State private var targetPrice: Double? = nil
    @State private var showPriceCheckAlert: Bool = false
    @State private var priceCheckMessage: String = ""
    
    // 相似產品陣列 (根據真實數據進行篩選)
    @State private var similarProducts: [Product] = []
    
    init(product: Product, navigationPath: Binding<[Product]>, query: Binding<String> = .constant("")) {
        self.product = product
        self._navigationPath = navigationPath
        self._query = query
    }
    
    var body: some View {
        ScrollView {
            VStack(spacing: 24) {
                
                // MARK: - 主商品圖片
                if let imageUrl = product.image_url,
                   let url = URL(string: imageUrl) {
                    AsyncImage(url: url) { image in
                        image.resizable().scaledToFit()
                    } placeholder: {
                        ProgressView()
                    }
                    .frame(height: 220)
                    .background(Color(.systemGray5))
                    .cornerRadius(16)
                    .shadow(radius: 6)
                    .padding(.horizontal)
                } else if let systemImage = product.imageName {
                    Image(systemName: systemImage)
                        .resizable()
                        .scaledToFit()
                        .frame(height: 220)
                        .background(Color(.systemGray5))
                        .cornerRadius(16)
                        .shadow(radius: 6)
                        .padding(.horizontal)
                }
                
                // MARK: - 商品名稱、收藏、分享
                HStack {
                    Text(product.name)
                        .font(.title)
                        .fontWeight(.bold)
                    Spacer()
                    Button {
                        withAnimation {
                            favoritesManager.toggle(product: product)
                            if favoritesManager.isFavorite(product: product), targetPrice == nil {
                                if let priceStr = product.prices["Store A"],
                                   let price = Double(priceStr.replacingOccurrences(of: "¥", with: "")) {
                                    targetPrice = price
                                }
                            }
                        }
                    } label: {
                        Image(systemName: favoritesManager.isFavorite(product: product) ? "heart.fill" : "heart")
                            .font(.title2)
                            .foregroundColor(favoritesManager.isFavorite(product: product) ? .red : .gray)
                    }
                    
                    Text("收藏数: \(favoritesManager.favoriteCount(for: product))")
                        .font(.subheadline)
                        .foregroundColor(.gray)
                    
                    Button(action: shareProduct) {
                        Image(systemName: "square.and.arrow.up")
                            .font(.title2)
                            .foregroundColor(.blue)
                    }
                }
                .padding(.horizontal)
                
                // MARK: - 橫向價格對比
                ScrollView(.horizontal, showsIndicators: false) {
                    HStack(spacing: 16) {
                        ForEach(product.prices.sorted(by: { $0.key < $1.key }), id: \.key) { key, value in
                            VStack(spacing: 4) {
                                Text(key)
                                    .font(.caption)
                                    .foregroundColor(.secondary)
                                Text(value)
                                    .font(.headline)
                                    .foregroundColor(.primary)
                            }
                            .padding(8)
                            .background(Color(.systemGray6))
                            .cornerRadius(8)
                        }
                    }
                    .padding(.horizontal)
                }
                
                Divider().padding(.horizontal)
                
                // MARK: - 促銷資訊
                VStack(alignment: .leading, spacing: 8) {
                    Text("促銷信息：")
                        .font(.headline)
                    Text(product.offer)
                        .font(.body)
                        .foregroundColor(.primary)
                    
                    Text("更新日期：\(product.date)")
                        .font(.caption)
                        .foregroundColor(.secondary)
                }
                .padding(.horizontal)
                
                // MARK: - 相似產品
                VStack(alignment: .leading, spacing: 8) {
                    Text("相似产品推荐")
                        .font(.headline)
                        .padding(.horizontal)
                    
                    if similarProducts.isEmpty {
                        Text("暂无相似产品")
                            .foregroundColor(.secondary)
                            .padding(.horizontal)
                    } else {
                        // 使用橫向 ScrollView 顯示相似商品
                        ScrollView(.horizontal, showsIndicators: false) {
                            HStack(spacing: 16) {
                                ForEach(similarProducts) { similar in
                                    NavigationLink(destination: ProductDetailView(product: similar,
                                                                                  navigationPath: .constant([]),
                                                                                  query: .constant(""))) {
                                        // 這裡直接示範自訂 AsyncImage phase，排查圖片無法顯示
                                        VStack {
                                            if let urlStr = similar.image_url,
                                               let url = URL(string: urlStr) {
                                                AsyncImage(url: url) { phase in
                                                    switch phase {
                                                    case .empty:
                                                        ProgressView()
                                                    case .success(let loadedImage):
                                                        loadedImage
                                                            .resizable()
                                                            .scaledToFit()
                                                    case .failure(let error):
                                                        // 顯示錯誤訊息或替代圖示
                                                        VStack {
                                                            Image(systemName: "exclamationmark.triangle")
                                                                .resizable()
                                                                .scaledToFit()
                                                                .frame(height: 40)
                                                            Text("載入失敗")
                                                                .font(.caption)
                                                            // 也可印出 error.debugDescription 幫助除錯
                                                            // Text("\(error.localizedDescription)").font(.caption)
                                                        }
                                                    @unknown default:
                                                        EmptyView()
                                                    }
                                                }
                                                .frame(height: 100)
                                            } else {
                                                // 如果無 image_url，就顯示預設圖示
                                                Image(systemName: "photo")
                                                    .resizable()
                                                    .scaledToFit()
                                                    .frame(height: 100)
                                                    .foregroundColor(.gray)
                                            }
                                            
                                            // 顯示商品名稱
                                            Text(similar.name)
                                                .font(.subheadline)
                                                .foregroundColor(.primary)
                                                .padding(.top, 4)
                                        }
                                        .frame(width: 120)
                                    }
                                }
                            }
                            .padding(.horizontal)
                        }
                    }
                }
            }
            .padding(.vertical)
            .background(Color.white.opacity(0.95))
            .cornerRadius(12)
            .shadow(radius: 4)
            .padding()
        }
        .navigationTitle("")
        .navigationBarBackButtonHidden(true)
        .toolbar {
            ToolbarItem(placement: .navigationBarLeading) {
                Button(action: { dismiss() }) {
                    HStack {
                        Image(systemName: "chevron.backward")
                        Text("Back")
                    }
                }
            }
        }
        .onAppear {
            loadSimilarProducts()
        }
        .onDisappear {
            if query != "" {
                query = ""
            }
        }
        .alert("价格提醒", isPresented: $showPriceCheckAlert) {
            Button("确定", role: .cancel) { }
        } message: {
            Text(priceCheckMessage)
        }
    }
    
    // MARK: - 分享產品
    func shareProduct() {
        let message = "Check out \(product.name) on Supermarket App!"
        let activityVC = UIActivityViewController(activityItems: [message], applicationActivities: nil)
        if let scene = UIApplication.shared.connectedScenes.first as? UIWindowScene,
           let rootVC = scene.windows.first?.rootViewController {
            rootVC.present(activityVC, animated: true, completion: nil)
        }
    }
    
    // MARK: - 價格檢查
    func checkPriceDrop() {
        guard let priceStr = product.prices["Store A"],
              let basePrice = Double(priceStr.replacingOccurrences(of: "¥", with: "")),
              let target = targetPrice else {
            return
        }
        let randomFactor = Double.random(in: 0.8...1.2)
        let currentPrice = basePrice * randomFactor
        
        if currentPrice < target {
            priceCheckMessage = "价格下降！当前价格：¥\(String(format: "%.2f", currentPrice))"
        } else {
            priceCheckMessage = "价格未下降。当前价格：¥\(String(format: "%.2f", currentPrice))"
        }
        showPriceCheckAlert = true
    }
    
    /// MARK: - 载入相似产品（示例：基于分类交集）
    func loadSimilarProducts() {
        // 1. 本产品的分类数组
        let cats = product.categories
        guard !cats.isEmpty else {
            similarProducts = []
            return
        }
        
        // 2. 加载所有产品
        let allProducts = loadAllProductsFromDocuments()
        
        // 3. 过滤出相似产品
        let filtered = allProducts.filter { candidate in
            // 3.1 不能是本产品自己
            guard candidate.url != product.url else { return false }
            // 3.2 候选产品也必须有分类
            let candidateCats = candidate.categories
            guard !candidateCats.isEmpty else { return false }
            // 3.3 至少有一个分类交集
            let intersection = Set(cats).intersection(Set(candidateCats))
            return !intersection.isEmpty
        }
        
        // 4. 调试输出
        print("=== 相似产品清单 (拥有交集的) ===")
        for p in filtered {
            print(" - \(p.name) : \(String(describing: p.image_url))")
        }
        
        // 5. 取前 5 条
        similarProducts = Array(filtered.shuffled().prefix(5))
    }
    
    // MARK: - 從 Documents 中載入所有 products
    private func loadAllProductsFromDocuments() -> [Product] {
        let fileManager = FileManager.default
        guard let docsUrl = fileManager.urls(for: .documentDirectory, in: .userDomainMask).first else {
            print("無法取得 Documents 目錄")
            return []
        }
        
        // 要加载的两份 JSON
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
