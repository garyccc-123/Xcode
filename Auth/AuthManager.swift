//
//  AuthManager.swift
//  Supermarket
//
//  Created by cheung gary on 6/2/2025.
//

import Foundation
import Combine

/// 用户认证管理器（目前采用模拟逻辑，后续可替换为真实后端验证）
class AuthManager: ObservableObject {
    static let shared = AuthManager()
    
    @Published var isLoggedIn: Bool = false
    @Published var userName: String = ""
    
    private init() {}
    
    /// 模拟登录方法
    func login(email: String, password: String, completion: @escaping (Bool, String?) -> Void) {
        // 模拟网络延迟
        DispatchQueue.main.asyncAfter(deadline: .now() + 1) {
            // 简单验证：仅当邮箱和密码匹配时登录成功
            if email == "test@example.com" && password == "password" {
                self.userName = "测试用户"
                self.isLoggedIn = true
                completion(true, nil)
            } else {
                completion(false, "邮箱或密码错误")
            }
        }
    }
    
    /// 退出登录
    func logout() {
        self.userName = ""
        self.isLoggedIn = false
    }
}
