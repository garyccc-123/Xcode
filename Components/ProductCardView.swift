//
//  ProductCardView.swift
//  Supermarket
//
//  Created by cheung gary on 6/2/2025.
//

//
//  ProductCardView.swift
//  Supermarket
//
//  Created by cheung gary on 6/2/2025.
//

import SwiftUI

struct ProductCardView: View {
    let product: Product
    
    var body: some View {
        VStack(alignment: .leading, spacing: 8) {
            // 商品图片
            // 若 product.imageName 為 nil，就使用 "photo" 作為預設圖示
            Image(systemName: product.imageName ?? "photo")
                .resizable()
                .scaledToFit()
                .frame(height: 80)
                .background(Color(.systemGray5))
                .cornerRadius(8)
            
            Text(product.name)
                .font(.headline)
                .lineLimit(1)
            
            // 超市价格对比列表
            ForEach(product.prices.sorted(by: { $0.key < $1.key }), id: \.key) { key, value in
                HStack {
                    Text(key)
                        .font(.caption2)
                        .foregroundColor(.secondary)
                    Spacer()
                    Text(value)
                        .font(.caption2)
                        .bold()
                        .foregroundColor(.primary)
                }
            }
            
            // 优惠标签（示例：折扣、热门）
            HStack(spacing: 4) {
                Text("💰折扣")
                    .font(.caption2)
                    .padding(4)
                    .background(Color.green.opacity(0.3))
                    .cornerRadius(4)
                Text("🔥热门")
                    .font(.caption2)
                    .padding(4)
                    .background(Color.red.opacity(0.3))
                    .cornerRadius(4)
            }
            
            // 价格趋势图示例（实际可集成图表组件）
            RoundedRectangle(cornerRadius: 4)
                .fill(Color.blue.opacity(0.2))
                .frame(height: 30)
                .overlay(
                    Text("价格趋势")
                        .font(.caption2)
                        .foregroundColor(.blue)
                )
        }
        .padding()
        .background(Color.white)
        .cornerRadius(12)
        .shadow(color: Color(.systemGray4), radius: 4, x: 0, y: 2)
    }
}
