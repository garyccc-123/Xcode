//
//  SearchBarView.swift
//  Supermarket
//
//  Created by cheung gary on 6/2/2025.
//

import SwiftUI

struct SearchBarView: View {
    @State private var isActive: Bool = false
    
    var body: some View {
        ZStack {
            // 隐藏的 NavigationLink，当 isActive 为 true 时跳转到 SearchView
            NavigationLink(destination: SearchView(), isActive: $isActive) {
                EmptyView()
            }
            // 外观类似搜索输入框的按钮
            HStack(spacing: 8) {
                Image(systemName: "magnifyingglass")
                    .foregroundColor(.gray)
                Text("Search products...")
                    .foregroundColor(.gray)
                Spacer()
            }
            .padding(12)
            .background(Color(.systemGray6))
            .cornerRadius(8)
            .onTapGesture {
                isActive = true
            }
        }
    }
}

struct SearchBarView_Previews: PreviewProvider {
    static var previews: some View {
        NavigationView {
            SearchBarView()
                .padding()
        }
    }
}
