import SwiftUI

struct LoginView: View {
    @Environment(\.presentationMode) var presentationMode
    @ObservedObject var authManager = AuthManager.shared
    @State private var email: String = ""
    @State private var password: String = ""
    @State private var errorMessage: String?
    @State private var isLoading: Bool = false
    @State private var showRegistration: Bool = false

    var body: some View {
        NavigationView {
            VStack {
                Spacer()
                
                // 顶部 Logo 与标题（请替换为你自己的 logo）
                VStack(spacing: 12) {
                    Image("instagram_logo")
                        .resizable()
                        .scaledToFit()
                        .frame(width: 120, height: 120)
                        .clipShape(Circle())
                        .shadow(radius: 8)
                    Text("登录 Supermarket")
                        .font(.system(size: 26, weight: .semibold))
                        .foregroundColor(.black)
                }
                .padding(.bottom, 30)
                
                // 表单卡片
                VStack(spacing: 15) {
                    // 邮箱输入框
                    TextField("手机号、用户名或邮箱", text: $email)
                        .autocapitalization(.none)
                        .padding(12)
                        .background(Color(.systemGray6))
                        .cornerRadius(5)
                        .overlay(
                            RoundedRectangle(cornerRadius: 5)
                                .stroke(Color.gray.opacity(0.3), lineWidth: 1)
                        )
                    
                    // 密码输入框
                    SecureField("密码", text: $password)
                        .padding(12)
                        .background(Color(.systemGray6))
                        .cornerRadius(5)
                        .overlay(
                            RoundedRectangle(cornerRadius: 5)
                                .stroke(Color.gray.opacity(0.3), lineWidth: 1)
                        )
                    
                    if let errorMessage = errorMessage {
                        Text(errorMessage)
                            .foregroundColor(.red)
                            .font(.footnote)
                    }
                    
                    // 登录按钮
                    Button(action: { login() }) {
                        if isLoading {
                            ProgressView()
                                .progressViewStyle(CircularProgressViewStyle())
                                .frame(maxWidth: .infinity)
                                .padding()
                        } else {
                            Text("登录")
                                .foregroundColor(.white)
                                .fontWeight(.bold)
                                .frame(maxWidth: .infinity)
                                .padding()
                        }
                    }
                    .background(Color.blue)
                    .cornerRadius(5)
                }
                .padding()
                .background(Color.white)
                .cornerRadius(8)
                .shadow(color: Color.black.opacity(0.1), radius: 8, x: 0, y: 4)
                .padding(.horizontal, 30)
                
                // 忘记密码（可选）
                Button(action: {
                    // 此处可添加找回密码逻辑
                }) {
                    Text("忘记密码?")
                        .font(.footnote)
                        .foregroundColor(.blue)
                }
                .padding(.top, 10)
                
                Spacer()
                
                // 底部提示“没有账号？注册”
                HStack {
                    Text("还没有账号?")
                        .font(.footnote)
                        .foregroundColor(.gray)
                    Button(action: { showRegistration = true }) {
                        Text("注册")
                            .font(.footnote)
                            .fontWeight(.bold)
                            .foregroundColor(.blue)
                    }
                }
                .padding(.bottom, 20)
            }
            .background(Color.white.edgesIgnoringSafeArea(.all))
            .navigationBarHidden(true)
            .sheet(isPresented: $showRegistration) {
                RegistrationView()
            }
        }
    }
    
    /// 模拟登录操作（可替换为真实的网络请求）
    func login() {
        errorMessage = nil
        isLoading = true
        authManager.login(email: email, password: password) { success, error in
            isLoading = false
            if success {
                presentationMode.wrappedValue.dismiss()
            } else {
                errorMessage = error
            }
        }
    }
}

struct LoginView_Previews: PreviewProvider {
    static var previews: some View {
        LoginView()
    }
}
