//
//  LoginBannerView.swift
//  Supermarket
//
//  Created by cheung gary on 6/2/2025.
//

import SwiftUI

enum AuthSheet: Identifiable {
    case login, register
    var id: Int { hashValue }
}

struct LoginBannerView: View {
    @State private var authSheet: AuthSheet?
    
    var body: some View {
        HStack {
            Image(systemName: "person.crop.circle.badge.checkmark")
                .font(.system(size: 40))
                .foregroundColor(.white)
                .padding(.leading, 8)
            Text("📣 登入即可獲取每日特價推送！")
                .foregroundColor(.white)
                .font(.headline)
                .lineLimit(2)
                .padding(.horizontal, 8)
            Spacer()
            VStack(spacing: 8) {
                Button(action: {
                    authSheet = .login
                }) {
                    Text("登录")
                        .font(.subheadline)
                        .foregroundColor(.blue)
                        .padding(8)
                        .background(Color.white)
                        .cornerRadius(8)
                }
                
            }
            .padding(.trailing, 8)
        }
        .padding(.vertical, 12)
        .background(
            LinearGradient(gradient: Gradient(colors: [.blue, .purple]),
                           startPoint: .leading,
                           endPoint: .trailing)
        )
        .cornerRadius(12)
        .shadow(radius: 4)
        .sheet(item: $authSheet) { sheet in
            switch sheet {
            case .login:
                LoginView()
            case .register:
                RegistrationView()
            }
        }
    }
}

struct LoginBannerView_Previews: PreviewProvider {
    static var previews: some View {
        LoginBannerView()
            .padding()
            .previewLayout(.sizeThatFits)
    }
}
