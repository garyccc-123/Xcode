//
//  ContentView.swift
//  Supermarket
//
//  Created by cheung gary on 6/2/2025.
//

import SwiftUI

struct ContentView: View {
    var body: some View {
        TabView {
            HomeView() // 首页
                .tabItem {
                    Image(systemName: "house.fill")
                    Text("主页")
                }
            
            SearchView() // 搜索页
                .tabItem {
                    Image(systemName: "magnifyingglass")
                    Text("搜索")
                }
            
            FavoritesView() // 收藏页
                .tabItem {
                    Image(systemName: "heart.fill")
                    Text("收藏")
                }
            
            ProfileView() // 我的帐户页
                .tabItem {
                    Image(systemName: "person.crop.circle")
                    Text("我的帐户")
                }
        }
    }
}


