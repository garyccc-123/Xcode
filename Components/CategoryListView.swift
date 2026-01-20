import SwiftUI

// MARK: - 數據模型

struct MainCategory: Identifiable {
    let id = UUID()
    let name: String
    let subcategories: [SubCategory]
}

struct SubCategory: Identifiable {
    let id = UUID()
    let name: String
}




// 根據您提供的分類資料，構造主分類和子分類數據
let categories: [MainCategory] = [
    MainCategory(name: "水果/蔬菜", subcategories: [
        SubCategory(name: "水果"),
        SubCategory(name: "蔬菜")
    ]),
    MainCategory(name: "飲品", subcategories: [
        SubCategory(name: "汽水"),
        SubCategory(name: "即飲茶類、咖啡、奶茶"),
        SubCategory(name: "奶類、乳酪飲品"),
        SubCategory(name: "植物奶、大豆飲品"),
        SubCategory(name: "沖調飲品"),
        SubCategory(name: "果汁"),
        SubCategory(name: "運動及能量飲品"),
        SubCategory(name: "涼茶"),
        SubCategory(name: "原箱飲品")
    ]),
    MainCategory(name: "酒精飲品", subcategories: [
        SubCategory(name: "啤酒"),
        SubCategory(name: "蘋果酒、果酒、雞尾酒"),
        SubCategory(name: "紅酒"),
        SubCategory(name: "白酒"),
        SubCategory(name: "香檳、有氣酒"),
        SubCategory(name: "氈酒、甜酒"),
        SubCategory(name: "白蘭地、干邑"),
        SubCategory(name: "清酒、燒酒、果味米酒"),
        SubCategory(name: "無酒精酒")
    ]),
    MainCategory(name: "糧油", subcategories: [
        SubCategory(name: "米"),
        SubCategory(name: "即食粉麵/飯"),
        SubCategory(name: "油"),
        SubCategory(name: "麵粉、烘焙用料、梳打粉")
    ]),
    MainCategory(name: "零食", subcategories: [
        SubCategory(name: "餅乾、曲奇"),
        SubCategory(name: "薯片、蝦片、爆谷"),
        SubCategory(name: "朱古力、糖果、香口膠"),
        SubCategory(name: "果乾、果仁、紫菜"),
        SubCategory(name: "魚肉腸、肉乾"),
        SubCategory(name: "蛋卷、糕點"),
        SubCategory(name: "布丁、啫喱、糖水")
    ]),
    MainCategory(name: "調味料、醬料", subcategories: [
        SubCategory(name: "鹽、糖、其他調味料"),
        SubCategory(name: "豉油"),
        SubCategory(name: "醬料")
    ]),
    MainCategory(name: "罐頭", subcategories: [
        SubCategory(name: "罐頭肉"),
        SubCategory(name: "罐頭海鮮"),
        SubCategory(name: "罐頭鮑魚"),
        SubCategory(name: "罐頭水果"),
        SubCategory(name: "罐頭湯"),
        SubCategory(name: "罐頭蔬菜、豆")
    ]),
    MainCategory(name: "早餐、果醬", subcategories: [
        SubCategory(name: "麵包糕點"),
        SubCategory(name: "燕麥、穀類"),
        SubCategory(name: "果醬")
    ]),
    MainCategory(name: "冷凍食品(乳製品,豆製品,蛋類)", subcategories: [
        SubCategory(name: "蛋類"),
        SubCategory(name: "豆製品"),
        SubCategory(name: "乳製品"),
        SubCategory(name: "冷凍飲品")
    ]),
    MainCategory(name: "急凍食品", subcategories: [
        SubCategory(name: "急凍海鮮"),
        SubCategory(name: "急凍肉類"),
        SubCategory(name: "丸類、冷盤"),
        SubCategory(name: "餃子、雲吞"),
        SubCategory(name: "點心、湯丸"),
        SubCategory(name: "薄餅、急凍小食"),
        SubCategory(name: "急凍麵食、年糕")
    ]),
    MainCategory(name: "肉類", subcategories: [
        SubCategory(name: "牛肉"),
        SubCategory(name: "豬肉"),
        SubCategory(name: "家禽")
    ]),
    MainCategory(name: "個人護理", subcategories: [
        SubCategory(name: "牙膏"),
        SubCategory(name: "漱口水"),
        SubCategory(name: "沐浴露"),
        SubCategory(name: "防曬用品"),
        SubCategory(name: "止汗、香體用品"),
        SubCategory(name: "潤膚產品"),
        SubCategory(name: "洗髮水"),
        SubCategory(name: "護髮素"),
        SubCategory(name: "修護、焗油、精華"),
        SubCategory(name: "洗手液")
    ]),
    MainCategory(name: "女士衛生護理", subcategories: [
        SubCategory(name: "衛生巾、護墊"),
        SubCategory(name: "女士衛生潔膚液")
    ]),
    MainCategory(name: "剃鬚用品", subcategories: [
        SubCategory(name: "剃鬚刀"),
        SubCategory(name: "補充刀片"),
        SubCategory(name: "剃鬚膏、泡沫、啫喱")
    ]),
    MainCategory(name: "紙巾", subcategories: [
        SubCategory(name: "廁紙、卷紙"),
        SubCategory(name: "盒裝紙巾、抹手紙"),
        SubCategory(name: "廚房紙"),
        SubCategory(name: "紙手巾"),
        SubCategory(name: "清潔濕紙巾"),
        SubCategory(name: "濕紙巾及濕廁紙")
    ]),
    MainCategory(name: "家居清潔", subcategories: [
        SubCategory(name: "漂白水、清潔劑"),
        SubCategory(name: "清潔工具"),
        SubCategory(name: "抽濕用品")
    ]),
    MainCategory(name: "廚房清潔", subcategories: [
        SubCategory(name: "百潔綿布、海綿"),
        SubCategory(name: "洗潔精"),
        SubCategory(name: "廚房清潔劑")
    ]),
    MainCategory(name: "浴室清潔", subcategories: [
        SubCategory(name: "潔廁劑"),
        SubCategory(name: "浴室清潔劑"),
        SubCategory(name: "通渠用品")
    ]),
    MainCategory(name: "洗衣用品", subcategories: [
        SubCategory(name: "洗衣液"),
        SubCategory(name: "洗衣粉"),
        SubCategory(name: "洗衣珠、洗衣紙"),
        SubCategory(name: "柔順劑"),
        SubCategory(name: "衣物清香、除菌噴霧"),
        SubCategory(name: "去漬、漂白")
    ]),
    MainCategory(name: "廚房用品", subcategories: [
        SubCategory(name: "食物儲存、保鮮紙"),
        SubCategory(name: "垃圾袋")
    ])
]

// MARK: - 介面實現

struct CategoryListView: View {
    // 用於導航的產品陣列綁定（預留給產品列表頁面使用）
    @State private var navigationPath: [Product] = []
    
    var body: some View {
        NavigationView {
            List(categories) { mainCat in
                NavigationLink(destination: SubCategoryListView(mainCategory: mainCat, navigationPath: $navigationPath)) {
                    Text(mainCat.name)
                        .font(.headline)
                }
            }
            .navigationTitle("產品分類")
        }
    }
}

struct SubCategoryListView: View {
    let mainCategory: MainCategory
    @Binding var navigationPath: [Product]
    
    var body: some View {
        List(mainCategory.subcategories) { subCat in
            NavigationLink(
                destination: ProductListingsView(
                    mainCategoryName: mainCategory.name,
                    subCategoryName: subCat.name,
                    navigationPath: $navigationPath
                )
            ) {
                Text(subCat.name)
                    .font(.subheadline)
            }
        }
        .navigationTitle(mainCategory.name)
    }
}
