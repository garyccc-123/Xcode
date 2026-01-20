//
//  BreadcrumbView.swift
//  Supermarket
//
//  Created by cheung gary on 4/5/2025.
//


import SwiftUI

/// 一个简单的面包屑导航
struct BreadcrumbView: View {
  let crumbs: [String]
  let onTap: (Int) -> Void

  var body: some View {
    HStack(spacing: 4) {
      ForEach(Array(crumbs.enumerated()), id: \.offset) { idx, title in
        Button(action: { onTap(idx) }) {
          Text(title)
            .font(.caption)
            .foregroundColor(.blue)
        }
        if idx < crumbs.count - 1 {
          Image(systemName: "chevron.right")
            .font(.caption2)
            .foregroundColor(.gray)
        }
      }
    }
    .padding(.horizontal)
    .padding(.vertical, 4)
  }
}
