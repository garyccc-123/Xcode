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
    
    // 移除模擬詳細資訊狀態，這裡保留模擬加載以便後續測試
    @State private var details: ProductDetail?
    @State private var isLoading: Bool = true
    @State private var errorMessage: String?
    
    @ObservedObject var favoritesManager = FavoritesManager.shared
    @Environment(\.dismiss) var dismiss
    
    @State private var targetPrice: Double? = nil
    @State private var showPriceCheckAlert: Bool = false
    @State private var priceCheckMessage: String = ""
    
    // 相似產品（暫時預留，後續根據實際數據實作）
    @State private var similarProducts: [Product] = []
    
    init(product: Product, navigationPath: Binding<[Product]>, query: Binding<String> = .constant("")) {
        self.product = product
        self._navigationPath = navigationPath
        self._query = query
    }
    
    var body: some View {
        ScrollView {
            VStack(spacing: 24) {
                // 顯示網路圖片或系統預設圖片
                if let imageUrl = product.image_url, let url = URL(string: imageUrl) {
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
                
                // 產品名稱、收藏、分享區域
                HStack {
                    Text(product.name)
                        .font(.title)
                        .fontWeight(.bold)
                    Spacer()
                    Button(action: {
                        withAnimation {
                            favoritesManager.toggle(product: product)
                            if favoritesManager.isFavorite(product: product), targetPrice == nil {
                                if let priceStr = product.prices["Store A"],
                                   let price = Double(priceStr.replacingOccurrences(of: "¥", with: "")) {
                                    targetPrice = price
                                }
                            }
                        }
                    }) {
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
                
                // 橫向價格對比區域
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
                
                // 產品詳細資訊展示：這裡用促銷資訊與更新日期來展示
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
                // 相似產品推薦區域
                VStack(alignment: .leading, spacing: 8) {
                    Text("相似产品推荐")
                        .font(.headline)
                        .padding(.horizontal)
                    if similarProducts.isEmpty {
                        Text("暂无相似产品")
                            .foregroundColor(.secondary)
                            .padding(.horizontal)
                    } else {
                        ScrollView(.horizontal, showsIndicators: false) {
                            HStack(spacing: 16) {
                                ForEach(similarProducts) { similar in
                                    NavigationLink(destination: ProductDetailView(product: similar, navigationPath: .constant([]), query: .constant(""))) {
                                        ProductCardView(product: similar)
                                            .frame(width: 150)
                                    }
                                }
                            }
                            .padding(.horizontal)
                        }
                    }
                }
            } // VStack 結束
            .padding(.vertical)
            .background(Color.white.opacity(0.95))
            .cornerRadius(12)
            .shadow(radius: 4)
            .padding()
        } // ScrollView 結束
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
            // 由於真實數據已經存在於 JSON 中，因此不再需要 loadDetails() 的模擬延遲
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
    
    func shareProduct() {
        let message = "Check out \(product.name) on Supermarket App!"
        let activityVC = UIActivityViewController(activityItems: [message], applicationActivities: nil)
        if let scene = UIApplication.shared.connectedScenes.first as? UIWindowScene,
           let rootVC = scene.windows.first?.rootViewController {
            rootVC.present(activityVC, animated: true, completion: nil)
        }
    }
    
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
    
    // MARK: - 載入相似產品 (根據第一個分類進行篩選)
    func loadSimilarProducts() {
        if let categoryArr = product.categories, let firstCategory = categoryArr.first, !firstCategory.isEmpty {
            // TODO: 從真實數據中篩選出與 product 類似的產品，目前暫時設為空陣列
            similarProducts = []
        } else {
            similarProducts = []
        }
    }
}

// 模擬的 ProductDetail 結構目前不再使用；若未來有真實詳細資訊，可直接從 product 中讀取
struct ProductDetail: Identifiable {
    var id = UUID()
    let description: String
}
