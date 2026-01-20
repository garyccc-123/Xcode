//
//  FileManagerHelper.swift
//  Supermarket
//
//  Created by cheung gary on 6/3/2025.
//


import Foundation

/// 将 Wellcome 与 PNS 两个合并后的 JSON 文件从 Bundle 复制到 Documents 目录
func copyCombinedProductsFileToDocuments() {
    let fileManager = FileManager.default
    guard let docsUrl = fileManager.urls(for: .documentDirectory, in: .userDomainMask).first else {
        print("無法取得 Documents 目錄")
        return
    }

    // 要复制的 JSON 文件名列表
    let jsonFileNames = [
        "combined_products_wellcom_with_eng.json",
        "combined_products_pns_with_eng.json"
    ]

    for fileName in jsonFileNames {
        let destinationUrl = docsUrl.appendingPathComponent(fileName)
        // 如果已存在，则跳过
        if fileManager.fileExists(atPath: destinationUrl.path) {
            print("\(fileName) 已存在於 Documents")
            continue
        }
        // 从 Bundle 中查找源文件
        let baseName = fileName.replacingOccurrences(of: ".json", with: "")
        if let bundleUrl = Bundle.main.url(forResource: baseName, withExtension: "json") {
            do {
                try fileManager.copyItem(at: bundleUrl, to: destinationUrl)
                print("\(fileName) 複製成功到 Documents")
            } catch {
                print("複製 \(fileName) 失敗: \(error)")
            }
        } else {
            print("在 Bundle 中未找到 \(fileName)")
        }
    }
}
