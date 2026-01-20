//
//  ProfileView.swift
//  Supermarket
//
//  Created by cheung gary on 6/2/2025.
//

import SwiftUI

struct ProfileView: View {
    @ObservedObject var authManager = AuthManager.shared
    @State private var showLogin: Bool = false
    
    var body: some View {
        NavigationView {
            VStack(spacing: 20) {
                if authManager.isLoggedIn {
                    // 登录后的界面
                    Image(systemName: "person.crop.circle")
                        .font(.system(size: 100))
                        .foregroundColor(.blue)
                    Text(authManager.userName)
                        .font(.title)
                        .bold()
                    Button("退出登录") {
                        authManager.logout()
                    }
                    .foregroundColor(.red)
                    .padding()
                    .background(Color(.systemGray5))
                    .cornerRadius(8)
                } else {
                    // 未登录时显示登录提示
                    Image(systemName: "person.crop.circle.badge.questionmark")
                        .font(.system(size: 100))
                        .foregroundColor(.gray)
                    Text("未登录")
                        .font(.title)
                        .foregroundColor(.gray)
                    Button("点击登录") {
                        showLogin = true
                    }
                    .padding()
                    .background(Color.blue)
                    .foregroundColor(.white)
                    .cornerRadius(8)
                    .sheet(isPresented: $showLogin) {
                        LoginView()
                    }
                }
                Spacer()
            }
            .padding()
            .navigationTitle("我的帐户")
        }
    }
}

struct ProfileView_Previews: PreviewProvider {
    static var previews: some View {
        ProfileView()
    }
}
