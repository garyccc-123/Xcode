//
//  ProductRowView.swift
//  Supermarket
//
//  Created by cheung gary on 7/2/2025.
//

import SwiftUI

struct ProductRowView: View {
    let product: Product
    
    var body: some View {
        HStack {
            // 显示产品图标：若 product.imageName 为 nil，则使用 "photo" 作为默认图标
            Image(systemName: product.imageName ?? "photo")
                .resizable()
                .aspectRatio(contentMode: .fit)
                .frame(width: 50, height: 50)
                .padding(4)
            
            VStack(alignment: .leading, spacing: 4) {
                // 产品名称
                Text(product.name)
                    .font(.headline)
                    .lineLimit(1)
                
                // 显示价格信息（多个超市价格信息横向排列）
                HStack {
                    ForEach(product.prices.sorted(by: { $0.key < $1.key }), id: \.key) { key, value in
                        Text("\(key): \(value)")
                            .font(.caption)
                            .foregroundColor(.secondary)
                    }
                }
            }
            
            Spacer()
        }
        .padding(.vertical, 8)
    }
}

