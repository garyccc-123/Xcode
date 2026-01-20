import SwiftUI

struct RegistrationView: View {
    @Environment(\.presentationMode) var presentationMode

    // 基本信息
    @State private var username: String = ""
    @State private var email: String = ""
    
    // 额外信息（下拉选择）
    @State private var gender: String = ""
    @State private var ageRange: String = ""
    @State private var jobType: String = ""
    
    // 可选项数组（扩展选项）
    private let genderOptions = ["Male", "Female"]
    private let ageRangeOptions = ["Under 18", "18-24", "25-34", "35-44", "45-54", "55-64", "65+"]
    private let jobTypeOptions = ["Student", "Employee", "Self-employed", "Freelancer", "Retired", "Homemaker", "Other"]
    
    // 密码信息
    @State private var password: String = ""
    @State private var confirmPassword: String = ""
    
    // 状态变量
    @State private var errorMessage: String?
    @State private var isLoading: Bool = false

    var body: some View {
        NavigationView {
            ZStack {
                // 背景渐变（可替换为你自己的颜色资源）
                LinearGradient(
                    gradient: Gradient(colors: [Color("LoginBGStart"), Color("LoginBGEnd")]),
                    startPoint: .topLeading,
                    endPoint: .bottomTrailing
                )
                .edgesIgnoringSafeArea(.all)
                .overlay(Color.black.opacity(0.1))
                
                ScrollView {
                    VStack(spacing: 20) {
                        Spacer().frame(height: 20)
                        
                        // 顶部 Logo 与标题
                        VStack(spacing: 12) {
                            Image("instagram_logo") // 替换为你自己的 logo
                                .resizable()
                                .scaledToFit()
                                .frame(width: 120, height: 120)
                                .clipShape(Circle())
                                .shadow(radius: 8)
                            Text("Register Supermarket")
                                .font(.system(size: 26, weight: .semibold))
                                .foregroundColor(.black)
                        }
                        .padding(.bottom, 30)
                        
                        // 表单卡片区域
                        VStack(spacing: 15) {
                            // 用户名输入
                            VStack(alignment: .leading, spacing: 6) {
                                Text("Username")
                                    .font(.caption)
                                    .foregroundColor(.gray)
                                TextField("Enter your username", text: $username)
                                    .padding(12)
                                    .background(Color(.systemGray6))
                                    .cornerRadius(5)
                                    .overlay(
                                        RoundedRectangle(cornerRadius: 5)
                                            .stroke(Color.gray.opacity(0.3), lineWidth: 1)
                                    )
                            }
                            
                            // 邮箱输入
                            VStack(alignment: .leading, spacing: 6) {
                                Text("Email")
                                    .font(.caption)
                                    .foregroundColor(.gray)
                                TextField("Enter your email", text: $email)
                                    .keyboardType(.emailAddress)
                                    .autocapitalization(.none)
                                    .padding(12)
                                    .background(Color(.systemGray6))
                                    .cornerRadius(5)
                                    .overlay(
                                        RoundedRectangle(cornerRadius: 5)
                                            .stroke(Color.gray.opacity(0.3), lineWidth: 1)
                                    )
                            }
                            
                            // 额外信息区域标题与分隔线
                            VStack(alignment: .leading, spacing: 4) {
                                Text("Additional Information")
                                    .font(.caption)
                                    .foregroundColor(.gray)
                                    .padding(.top, 5)
                                    .padding(.bottom, 2)
                                Divider()
                            }
                            
                            // 性别选择
                            DropdownField(title: "Select Gender", options: genderOptions, selection: $gender)
                            
                            // 年龄范围选择
                            DropdownField(title: "Select Age Range", options: ageRangeOptions, selection: $ageRange)
                            
                            // 职业选择
                            DropdownField(title: "Select Job", options: jobTypeOptions, selection: $jobType)
                            
                            // 密码输入
                            VStack(alignment: .leading, spacing: 6) {
                                Text("Password")
                                    .font(.caption)
                                    .foregroundColor(.gray)
                                SecureField("Enter your password", text: $password)
                                    .padding(12)
                                    .background(Color(.systemGray6))
                                    .cornerRadius(5)
                                    .overlay(
                                        RoundedRectangle(cornerRadius: 5)
                                            .stroke(Color.gray.opacity(0.3), lineWidth: 1)
                                    )
                            }
                            
                            // 确认密码输入
                            VStack(alignment: .leading, spacing: 6) {
                                Text("Confirm Password")
                                    .font(.caption)
                                    .foregroundColor(.gray)
                                SecureField("Confirm your password", text: $confirmPassword)
                                    .padding(12)
                                    .background(Color(.systemGray6))
                                    .cornerRadius(5)
                                    .overlay(
                                        RoundedRectangle(cornerRadius: 5)
                                            .stroke(Color.gray.opacity(0.3), lineWidth: 1)
                                    )
                            }
                            
                            // 错误提示
                            if let errorMessage = errorMessage {
                                Text(errorMessage)
                                    .foregroundColor(.red)
                                    .font(.footnote)
                                    .padding(.horizontal)
                            }
                            
                            // 注册按钮
                            Button(action: { register() }) {
                                if isLoading {
                                    ProgressView()
                                        .progressViewStyle(CircularProgressViewStyle(tint: .white))
                                        .frame(maxWidth: .infinity)
                                        .padding(12)
                                } else {
                                    Text("Register")
                                        .font(.headline)
                                        .fontWeight(.bold)
                                        .frame(maxWidth: .infinity)
                                        .padding(12)
                                        .foregroundColor(.white)
                                }
                            }
                            .background(Color.blue)
                            .cornerRadius(5)
                        }
                        .padding()
                        .background(Color.white.opacity(0.95))
                        .cornerRadius(8)
                        .shadow(color: Color.black.opacity(0.1), radius: 8, x: 0, y: 4)
                        .padding(.horizontal, 30)
                        
                        Spacer()
                        
                        // 底部提示“Already have an account? Login”
                        HStack {
                            Text("Already have an account?")
                                .font(.footnote)
                                .foregroundColor(.gray)
                            Button(action: {
                                presentationMode.wrappedValue.dismiss()
                            }) {
                                Text("Login")
                                    .font(.footnote)
                                    .fontWeight(.bold)
                                    .foregroundColor(.blue)
                            }
                        }
                        .padding(.bottom, 20)
                    }
                    .padding(.top, 20)
                }
            }
            .navigationBarTitle("")
            .navigationBarHidden(true)
        }
    }
    
    /// 模拟注册操作（实际开发中请替换为真实网络请求）
    func register() {
        errorMessage = nil
        guard !username.isEmpty,
              !email.isEmpty,
              !password.isEmpty,
              !confirmPassword.isEmpty else {
            errorMessage = "Please fill in all fields"
            return
        }
        guard password == confirmPassword else {
            errorMessage = "Passwords do not match"
            return
        }
        isLoading = true
        DispatchQueue.main.asyncAfter(deadline: .now() + 1.5) {
            isLoading = false
            // 模拟注册成功后自动登录
            AuthManager.shared.userName = username
            AuthManager.shared.isLoggedIn = true
            presentationMode.wrappedValue.dismiss()
        }
    }
}

struct DropdownField: View {
    var title: String
    var options: [String]
    @Binding var selection: String
    @State private var showOptions: Bool = false

    var body: some View {
        Button(action: {
            showOptions = true
        }) {
            HStack {
                Text(selection.isEmpty ? title : selection)
                    .foregroundColor(selection.isEmpty ? Color.gray : Color.black)
                Spacer()
                Image(systemName: "chevron.down")
                    .foregroundColor(Color.gray)
            }
            .padding(12)
            .frame(height: 44) // 固定高度，与其他输入框一致
            .background(Color(.systemGray6))
            .cornerRadius(5)
            .overlay(
                RoundedRectangle(cornerRadius: 5)
                    .stroke(Color.gray.opacity(0.3), lineWidth: 1)
            )
        }
        .confirmationDialog(title, isPresented: $showOptions, actions: {
            ForEach(options, id: \.self) { option in
                Button(option) {
                    selection = option
                }
            }
            Button("Cancel", role: .cancel) {}
        })
    }
}

struct RegistrationView_Previews: PreviewProvider {
    static var previews: some View {
        RegistrationView()
    }
}
