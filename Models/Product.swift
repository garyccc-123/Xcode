import Foundation


struct Product: Identifiable, Hashable, Decodable {
    let id = UUID()
    let uid: String
    let url: String
    let name: String
    let productEngName: String?
    let price: String
    let offer: String
    let date: String
    let image_url: String?
    let imageName: String?
    
    /// 新格式字段
    let mainCategory: [String]
    let subCategories: [String]
    
    /// 方便使用的合并分类
    var categories: [String] {
        return mainCategory + subCategories
    }
    
    let prices: [String: String]
    let history: [HistoryItem]?
    
    /// 标识来源，加载时赋值
    var source: String = ""
    
    enum CodingKeys: String, CodingKey {
        case uid, url, name
        case productEngName  = "product_eng_name"
        case price, offer, date
        case image_url, imageName
        case mainCategory    = "main_category"
        case subCategories   = "sub_categories"
        case prices, history
    }
    
    init(from decoder: Decoder) throws {
        let c = try decoder.container(keyedBy: CodingKeys.self)
        uid             = try c.decode(String.self, forKey: .uid)
        url             = try c.decode(String.self, forKey: .url)
        name            = try c.decode(String.self, forKey: .name)
        productEngName  = try c.decodeIfPresent(String.self, forKey: .productEngName)
        price           = try c.decode(String.self, forKey: .price)
        offer           = try c.decode(String.self, forKey: .offer)
        date            = try c.decode(String.self, forKey: .date)
        image_url       = try c.decodeIfPresent(String.self, forKey: .image_url)
        imageName       = try c.decodeIfPresent(String.self, forKey: .imageName)
        
        mainCategory    = try c.decode([String].self, forKey: .mainCategory)
        subCategories   = try c.decode([String].self, forKey: .subCategories)
        
        prices = (try? c.decode([String: String].self, forKey: .prices)) ?? [:]
        history = try c.decodeIfPresent([HistoryItem].self, forKey: .history)
        // source 留空，稍后在加载时赋值
    }
}

struct HistoryItem: Decodable, Hashable, Identifiable {
    let id = UUID()
    let name: String
    let price: String
    let offer: String
    let date: String
    let image_url: String?
    let productEngName: String?

    enum CodingKeys: String, CodingKey {
        case name, price, offer, date, image_url
        case productEngName = "product_eng_name"
    }
    
    init(from decoder: Decoder) throws {
        let c = try decoder.container(keyedBy: CodingKeys.self)
        name            = try c.decode(String.self, forKey: .name)
        price           = try c.decode(String.self, forKey: .price)
        offer           = try c.decode(String.self, forKey: .offer)
        date            = try c.decode(String.self, forKey: .date)
        image_url       = try c.decodeIfPresent(String.self, forKey: .image_url)
        productEngName  = try c.decodeIfPresent(String.self, forKey: .productEngName)
    }
}
