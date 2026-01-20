import SwiftUI

final class FavoritesManager: ObservableObject {
    static let shared = FavoritesManager()
    
    @Published var favoriteProducts: [Product] = []
    
    private init() { }
    
    func add(product: Product) {
        // 如果该产品尚未被收藏，则添加到收藏列表中
        if !favoriteProducts.contains(where: { $0.id == product.id }) {
            favoriteProducts.append(product)
        }
    }
    
    func remove(product: Product) {
        // 根据产品 id 查找并删除收藏
        if let index = favoriteProducts.firstIndex(where: { $0.id == product.id }) {
            favoriteProducts.remove(at: index)
        }
    }
    
    func toggle(product: Product) {
        // 切换收藏状态：如果已收藏则移除，否则添加
        if isFavorite(product: product) {
            remove(product: product)
        } else {
            add(product: product)
        }
    }
    
    func isFavorite(product: Product) -> Bool {
        return favoriteProducts.contains(where: { $0.id == product.id })
    }
}

// 可选扩展：模拟返回收藏数量（仅作示例）
extension FavoritesManager {
    func favoriteCount(for product: Product) -> Int {
        // 这里仅做模拟：如果该产品已被收藏，返回 123，否则返回 0
        return isFavorite(product: product) ? 123 : 0
    }
}
