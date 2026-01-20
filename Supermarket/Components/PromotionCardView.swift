//
//  PromotionCardView.swift
//  Supermarket
//
//  Created by cheung gary on 6/2/2025.
//

import SwiftUI

struct PromotionCardView: View {
    let title: String
    let description: String
    
    var body: some View {
        Button(action: {
            // TODO: 处理优惠活动详情的跳转
        }) {
            VStack(alignment: .leading, spacing: 6) {
                Text(title)
                    .font(.subheadline)
                    .bold()
                    .foregroundColor(.white)
                Text(description)
                    .font(.caption)
                    .foregroundColor(.white.opacity(0.85))
            }
            .padding()
            .frame(width: 200, height: 100)
            .background(LinearGradient(gradient: Gradient(colors: [.red, .orange]),
                                       startPoint: .topLeading, endPoint: .bottomTrailing))
            .cornerRadius(12)
            .shadow(radius: 4)
        }
    }
}

struct PromotionCardView_Previews: PreviewProvider {
    static var previews: some View {
        PromotionCardView(title: "示例标题", description: "示例描述")
            .previewLayout(.sizeThatFits)
    }
}
