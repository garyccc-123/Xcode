//
//  QuickAccessView.swift
//  Supermarket
//
//  Created by cheung gary on 6/2/2025.
//

import SwiftUI

struct QuickAccessView: View {
    // 定义快捷功能项数据
    let items: [QuickAccessItem] = [
        QuickAccessItem(icon: "tag", title: "超市比价"),
        QuickAccessItem(icon: "sparkles", title: "今日特价"),
        QuickAccessItem(icon: "heart", title: "我的最爱"),
        QuickAccessItem(icon: "bell", title: "价格通知"),
        QuickAccessItem(icon: "location", title: "附近门市")
    ]
    
    var body: some View {
        ScrollView(.horizontal, showsIndicators: false) {
            HStack(spacing: 30) {
                ForEach(items, id: \.title) { item in
                    VStack(spacing: 8) {
                        Button(action: {
                            // TODO: 快捷功能按钮点击处理
                        }) {
                            Image(systemName: item.icon)
                                .font(.system(size: 28))
                                .foregroundColor(.white)
                                .padding()
                                .background(LinearGradient(gradient: Gradient(colors: [.blue, .purple]),
                                                           startPoint: .topLeading, endPoint: .bottomTrailing))
                                .clipShape(Circle())
                        }
                        Text(item.title)
                            .font(.caption)
                            .foregroundColor(.primary)
                    }
                }
            }
            .padding(.horizontal)
        }
    }
}

struct QuickAccessView_Previews: PreviewProvider {
    static var previews: some View {
        QuickAccessView()
    }
}
