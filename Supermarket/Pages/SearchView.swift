//
//  SearchView.swift
//  Supermarket
//
//  Created by cheung gary on 6/2/2025.
//

import SwiftUI

struct SearchView: View {
    @State private var query: String = ""
    @State private var searchResults: [Product] = []
    @State private var isLoading: Bool = false
    @State private var errorMessage: String?
    @State private var searchTask: Task<Void, Never>? = nil
    
    // 独立搜索页的导航堆栈管理
    @State private var navigationPath: [Product] = []

    var body: some View {
        NavigationStack(path: $navigationPath) {
            VStack {
                HStack(spacing: 8) {
                    Image(systemName: "magnifyingglass")
                        .foregroundColor(.gray)
                    TextField("Search products...", text: $query, onCommit: {
                        triggerSearch()
                    })
                    .disableAutocorrection(true)
                    .autocapitalization(.none)
                    if !query.isEmpty {
                        Button(action: {
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
                .onChange(of: query) { newValue in
                    searchTask?.cancel()
                    if newValue.isEmpty {
                        searchResults = []
                        errorMessage = nil
                        isLoading = false
                    } else {
                        isLoading = true
                        searchTask = Task {
                            try? await Task.sleep(nanoseconds: 500_000_000)
                            await searchProducts(query: newValue)
                        }
                    }
                }
                
                if isLoading {
                    ProgressView("Searching...")
                        .padding()
                }
                if let errorMessage = errorMessage {
                    Text(errorMessage)
                        .foregroundColor(.red)
                        .padding()
                }
                List(searchResults) { product in
                    NavigationLink(value: product) {
                        ProductRowView(product: product)
                    }
                }
                .listStyle(PlainListStyle())
            }
            .navigationTitle("Search")
            .navigationDestination(for: Product.self) { product in
                ProductDetailView(product: product, navigationPath: $navigationPath)
            }
        }
    }
    
    private func triggerSearch() {
        guard !query.isEmpty else { return }
        isLoading = true
        searchTask?.cancel()
        searchTask = Task {
            await searchProducts(query: query)
        }
    }
    
    func searchProducts(query: String) async {
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

struct SearchView_Previews: PreviewProvider {
    static var previews: some View {
        SearchView()
    }
}
