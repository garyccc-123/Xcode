//
//  DataManagers.swift
//  Supermarket
//
//  Created by cheung gary on 4/5/2025.
//



import Foundation

// MARK: - 第三级 UID 映射模型
struct UIDMapping: Decodable {
    let uid: String
    let eng: String
    let norm: String
}

// MARK: - ThirdCategory 分组模型
struct ThirdCategory: Identifiable {
    let id = UUID()
    let norm: String                // 映射用的归一化 key
    let chineseName: String         // 中文显示名
    let uids: [String]              // 属于该分类的所有 UID
}

// MARK: - UIDMappingManager：缓存并提供第三层映射
final class UIDMappingManager {
    static let shared = UIDMappingManager()
    private var mappingsCache: [String: [UIDMapping]] = [:]
    /// 子分类对应的映射文件
    private let fileNamesBySub: [String: String] = [
        "水果": "filtered_fruit.json",
        "蔬菜": "filtered_vegetable.json",
        "汽水": "normalized_soda_updated.json",
        "即飲茶類、咖啡、奶茶": "normalized_tea_coffe_milktea.json",
        "奶類、乳酪飲品": "normalized_milk_yogurt.json",
        "沖調飲品": "normalized_mixed_powder_drink&tea.json",
        "果汁": "normalized_juice.json",
        "運動及能量飲品": "normalized_sports&energy_drinks.json",
        "涼茶": "normalized_herbal_tea.json",
        "植物奶、大豆飲品": "normalized_plant_milk.json",
        "啤酒": "normalized_beer.json",
        "紅酒": "normalized_red_wine.json",


    
        // 后续再添加更多子分类对应的 JSON 文件
    ]

    private init() {}

    /// 获取指定子分类的映射列表
    func mappings(for subCategory: String) -> [UIDMapping] {
        if let cache = mappingsCache[subCategory] {
            return cache
        }
        guard let fileName = fileNamesBySub[subCategory],
              let url = Bundle.main.url(
                forResource: fileName.replacingOccurrences(of: ".json", with: ""),
                withExtension: "json"
              )
        else {
            print("⚠️ 没为【\(subCategory)】配置映射文件")
            return []
        }
        do {
            let data = try Data(contentsOf: url)
            let arr = try JSONDecoder().decode([UIDMapping].self, from: data)
            mappingsCache[subCategory] = arr
            return arr
        } catch {
            print("❌ 加载 \(fileName) 映射失败: \(error)")
            return []
        }
    }
}

// MARK: - ProductDataStore：缓存所有产品数据
final class ProductDataStore {
    static let shared = ProductDataStore()
    let products: [Product]

    private init() {
        // 复制 Bundle 中的 JSON 到 Documents
        copyCombinedProductsFileToDocuments()
        // 加载并合并 Wellcome + PNS 产品
        products = loadAllProductsFromDocuments()
    }

    /// 构建第三级分类
    /// - Parameters:
    ///   - main: 主分类名称
    ///   - sub: 子分类名称
    /// - Returns: 第三级分类列表（含“其他”）
    func thirdCategories(main: String, sub: String) -> [ThirdCategory] {
        // 1. 筛选符合主/子分类的产品
        let filtered = products.filter {
            $0.mainCategory.contains(main) && $0.subCategories.contains(sub)
        }
        let allUIDs = Set(filtered.map { $0.uid })

        // 2. 加载映射并过滤
        let mappings = UIDMappingManager.shared.mappings(for: sub)
            .filter { allUIDs.contains($0.uid) }
        let mappedUIDs = Set(mappings.map { $0.uid })

        // 3. 已映射的分组
        let grouped = Dictionary(grouping: mappings, by: \UIDMapping.norm)
        var thirdCats = grouped.map { norm, entries in
            let firstUID = entries[0].uid
            let zh = filtered.first(where: { $0.uid == firstUID })?.name ?? norm
            return ThirdCategory(norm: norm,
                                 chineseName: zh,
                                 uids: entries.map { $0.uid })
        }

        // 4. 未映射的归为“其他”
        let unmapped = allUIDs.subtracting(mappedUIDs)
        if !unmapped.isEmpty {
            thirdCats.append(
                ThirdCategory(norm: "others", chineseName: "其他", uids: Array(unmapped))
            )
        }

        // 5. 按英文 norm 排序
        return thirdCats.sorted { $0.norm < $1.norm }
    }
}
