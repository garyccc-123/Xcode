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
        QuickAccessItem(icon: "tag", title: "分類瀏覽"),
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
                        
                        // 根據 item.title 顯示 NavigationLink 或 Button
                        if item.title == "分類瀏覽" {
                            // 使用 NavigationLink 导航到 CategoryListView
                            NavigationLink(destination: CategoryListView()) {
                                Image(systemName: item.icon)
                                    .font(.system(size: 28))
                                    .foregroundColor(.white)
                                    .padding()
                                    .background(LinearGradient(gradient: Gradient(colors: [.blue, .purple]),
                                                               startPoint: .topLeading,
                                                               endPoint: .bottomTrailing))
                                    .clipShape(Circle())
                            }
                        } else if item.title == "附近门市" {
                            // 使用 NavigationLink 导航到 NearbyStoresView
                            NavigationLink(destination: NearbyStoresView()) {
                                Image(systemName: item.icon)
                                    .font(.system(size: 28))
                                    .foregroundColor(.white)
                                    .padding()
                                    .background(LinearGradient(gradient: Gradient(colors: [.blue, .purple]),
                                                               startPoint: .topLeading,
                                                               endPoint: .bottomTrailing))
                                    .clipShape(Circle())
                            }
                        } else {
                            // 其他项目使用 Button
                            Button(action: {
                                // TODO: 其他快捷功能点击处理
                            }) {
                                Image(systemName: item.icon)
                                    .font(.system(size: 28))
                                    .foregroundColor(.white)
                                    .padding()
                                    .background(LinearGradient(gradient: Gradient(colors: [.blue, .purple]),
                                                               startPoint: .topLeading,
                                                               endPoint: .bottomTrailing))
                                    .clipShape(Circle())
                            }
                        }
                        
                        // 按钮下方的文字
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
        // 为确保 NavigationLink 正常工作，需放在 NavigationStack 中预览
        NavigationStack {
            QuickAccessView()
        }
    }
}
