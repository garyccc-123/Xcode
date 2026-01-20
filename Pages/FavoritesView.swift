import SwiftUI

struct FavoritesView: View {
    @ObservedObject var favoritesManager = FavoritesManager.shared
    @State private var navigationPath: [Product] = []  // 用于管理导航堆栈
    @State private var showShareSheet: Bool = false    // 是否显示分享界面

    var body: some View {
        NavigationStack(path: $navigationPath) {
            VStack {
                if favoritesManager.favoriteProducts.isEmpty {
                    VStack {
                        Spacer()
                        Text("No favorites yet.")
                            .foregroundColor(.gray)
                            .font(.title3)
                        Spacer()
                    }
                    .frame(maxWidth: .infinity, maxHeight: .infinity)
                } else {
                    List {
                        ForEach(favoritesManager.favoriteProducts, id: \.id) { product in
                            NavigationLink(value: product) {
                                ProductRowView(product: product)
                            }
                        }
                        .onDelete(perform: deleteFavorites)
                    }
                    .listStyle(PlainListStyle())
                }
            }
            .navigationTitle("收藏 (\(favoritesManager.favoriteProducts.count))")
            .toolbar {
                // 左侧管理按钮，使用系统 EditButton 切换编辑模式
                ToolbarItem(placement: .navigationBarLeading) {
                    EditButton()
                }
                // 右侧分享按钮
                ToolbarItem(placement: .navigationBarTrailing) {
                    Button(action: {
                        showShareSheet = true
                    }) {
                        Image(systemName: "square.and.arrow.up")
                    }
                }
            }
            .navigationDestination(for: Product.self) { product in
                ProductDetailView(product: product, navigationPath: $navigationPath)
            }
            .sheet(isPresented: $showShareSheet) {
                let shareMessage = "我在 Supermarket App 收藏了 \(favoritesManager.favoriteProducts.count) 个产品，快来看看吧！"
                ActivityView(activityItems: [shareMessage])
            }
        }
    }
    
    func deleteFavorites(at offsets: IndexSet) {
        for index in offsets {
            let product = favoritesManager.favoriteProducts[index]
            favoritesManager.remove(product: product)
        }
    }
}

struct FavoritesView_Previews: PreviewProvider {
    static var previews: some View {
        FavoritesView()
    }
}
