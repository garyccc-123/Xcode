//
//  PromotionsView.swift
//  Supermarket
//
//  Created by cheung gary on 6/2/2025.
//

import SwiftUI

struct PromotionsView: View {
    var body: some View {
        VStack(alignment: .leading, spacing: 8) {
            Text("精选优惠")
                .font(.headline)
                .padding(.horizontal)
            
            ScrollView(.horizontal, showsIndicators: false) {
                HStack(spacing: 16) {
                    PromotionCardView(title: "🔥 本周热门折扣", description: "精选超市特价商品")
                    PromotionCardView(title: "🎉 期間限定優惠", description: "买一送一、限时9折等活动")
                    PromotionCardView(title: "⭐ 新人专享", description: "注册会员专享优惠")
                }
                .padding(.horizontal)
            }
        }
    }
}

struct PromotionsView_Previews: PreviewProvider {
    static var previews: some View {
        PromotionsView()
    }
}
