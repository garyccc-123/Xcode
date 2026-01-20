import SwiftUI

struct HomeView: View {
    // 搜索相关状态
    @State private var query: String = ""
    @State private var searchResults: [Product] = []
    @State private var isLoading: Bool = false
    @State private var errorMessage: String?
    @State private var searchTask: Task<Void, Never>? = nil
    
    // 导航堆栈管理
    @State private var navigationPath: [Product] = []
    
    var body: some View {
        NavigationStack(path: $navigationPath) {
            VStack {
                // 搜索栏区域
                HStack(spacing: 8) {
                    Image(systemName: "magnifyingglass")
                        .foregroundColor(.gray)
                    TextField("Search products...", text: $query)
                        .disableAutocorrection(true)
                        .autocapitalization(.none)
                        .onChange(of: query) { newValue in
                            // 取消之前的任务，防止频繁请求
                            searchTask?.cancel()
                            if newValue.isEmpty {
                                // 当搜索内容为空时，清空搜索结果和错误提示
                                searchResults = []
                                errorMessage = nil
                                isLoading = false
                            } else {
                                isLoading = true
                                // 防抖延时 0.5 秒后执行搜索
                                searchTask = Task {
                                    try? await Task.sleep(nanoseconds: 500_000_000)
                                    await performSearch(query: newValue)
                                }
                            }
                        }
                    if !query.isEmpty {
                        Button(action: {
                            // 清除搜索内容与结果
                            query = ""
                            searchResults = []
                            errorMessage = nil
                        }) {
                            Image(systemName: "xmark.circle.fill")
                                .foregroundColor(.gray)
                        }
                    }
                }
                .padding(10)
                .background(Color(.systemGray6))
                .cornerRadius(8)
                .padding(.horizontal)
                .padding(.top, 10)
                
                // 显示加载状态或错误提示
                if isLoading {
                    ProgressView("Searching...")
                        .padding()
                }
                if let errorMessage = errorMessage {
                    Text(errorMessage)
                        .foregroundColor(.red)
                        .padding()
                }
                
                // 根据 query 是否为空显示不同内容
                if query.isEmpty {
                    // 默认首页内容
                    ScrollView {
                        VStack(spacing: 20) {
                            LoginBannerView()
                            QuickAccessView()
                            PromotionsView()
                            ProductListingsView(navigationPath: $navigationPath)
                        }
                        .padding()
                    }
                } else {
                    // 显示搜索结果列表
                    List(searchResults) { product in
                        NavigationLink(destination: ProductDetailView(product: product,
                                                                        navigationPath: $navigationPath,
                                                                        query: $query)) {
                            ProductRowView(product: product)
                        }
                    }
                    .listStyle(PlainListStyle())
                }
            }
            //.navigationTitle("Home")  // 如不需要标题，可删除或设置为空字符串
            .navigationTitle("")
            .navigationDestination(for: Product.self) { product in
                ProductDetailView(product: product, navigationPath: $navigationPath, query: $query)
            }
        }
    }
    
    /// 模拟搜索产品的方法（实际开发中请替换为真实 API 请求）
    func performSearch(query: String) async {
        do {
            try await Task.sleep(nanoseconds: 500_000_000)
            let allProducts = SampleData.products
            let filtered = allProducts.filter { $0.name.localizedCaseInsensitiveContains(query) }
            await MainActor.run {
                searchResults = filtered
                isLoading = false
            }
        } catch {
            if error is CancellationError { return }
            await MainActor.run {
                errorMessage = "Search failed: \(error.localizedDescription)"
                isLoading = false
            }
        }
    }
}

struct HomeView_Previews: PreviewProvider {
    static var previews: some View {
        HomeView()
    }
}
