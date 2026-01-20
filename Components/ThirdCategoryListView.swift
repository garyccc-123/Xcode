//
//  ThirdCategoryListView.swift
//  Supermarket
//
//  Created by cheung gary on 4/5/2025.
//


import SwiftUI

struct ThirdCategoryListView: View {
    /// 来自上一层的主分类名称
    let mainCategoryName: String
    /// 来自上一层的子分类名称
    let subCategoryName: String
    /// 用于 NavigationStack 的路径绑定
    @Binding var navigationPath: [Product]

    /// 根据主/子分类从缓存中取出第三级分组，并按组内 UID 数量降序排列
    private var thirdCats: [ThirdCategory] {
        ProductDataStore
            .shared
            .thirdCategories(main: mainCategoryName, sub: subCategoryName)
            .sorted { $0.uids.count > $1.uids.count }
    }

    var body: some View {
        VStack(spacing: 0) {
            // 面包屑导航：点击任意面包屑都回到子分类页
            BreadcrumbView(crumbs: [mainCategoryName, subCategoryName]) { _ in
                navigationPath = []
            }

            List(thirdCats) { cat in
                NavigationLink {
                    ProductListingsView(
                        mainCategoryName: nil,
                        subCategoryName: nil,
                        allowedUIDs: cat.uids,
                        navigationPath: $navigationPath
                    )
                } label: {
                    HStack {
                        // 用 displayName(for:) 做中英文映射
                        Text(displayName(for: cat.norm))
                            .font(.body)
                        Spacer()
                        // 显示该分组下的商品数量
                        Text("(\(cat.uids.count))")
                            .foregroundColor(.secondary)
                    }
                }
            }
        }
        .navigationTitle(subCategoryName)
    }

    /// 将 norm 转换为中文（优先整串匹配，再拆分匹配）
    private func displayName(for norm: String) -> String {
        // 1. 清理并小写
        let key = norm.trimmingCharacters(in: .whitespacesAndNewlines)
                       .lowercased()
        // 2. 取出当前子分类的映射字典
        let dict = subCategoryNormToChinese[subCategoryName] ?? [:]
        // 3. 尝试整串匹配
        if let zh = dict[key] {
            return zh
        }
        // 4. 如果有“/”，拆分后分别映射
        let parts = key.split(separator: "/").map(String.init)
        if parts.count > 1 {
            let mapped = parts.map { dict[$0] ?? $0 }
            return mapped.joined(separator: "/")
        }
        // 5. 都没命中就返回原始 norm
        return norm
    }
}
