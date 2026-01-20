#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ai_running_soda.py

import os
import json
import re
import requests

def main():
    # 1️⃣ 定位 JSON 文件
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    filtered_path = os.path.join(BASE_DIR, 'filtered_soda.json')
    with open(filtered_path, encoding='utf-8') as f:
        data = json.load(f)
    if not data:
        raise ValueError("filtered_soda.json 为空！")

    # 2️⃣ 选用聚类字段：优先使用 norm，否则用 eng
    field = 'norm' if 'norm' in data[0] else 'eng'
    print(f"⚙️ 使用字段“{field}”进行汽水聚类。")

    # 3️⃣ 构造 Prompt 列表
    names = sorted({item.get(field, '') for item in data})
    soda_list = "\n".join(names)

    # 4️⃣ 发送请求到本地 LM Studio（Deepseek）
    API_URL = "http://192.168.50.98:1234/v1/chat/completions"  # 替换为你的 IP:端口
    payload = {
        "model": "llama3.2",
        "messages": [
            # 系统角色：分层聚类指令
            {"role": "system", "content": (
                "你是一个聚类助手，只返回纯 JSON，不要输出任何多余文字。\n"
                "请按照以下优先级 分层聚类 汽水产品：\n"
                "1. 品牌（如可口可乐、百事可乐）\n"
                "2. 产品系列（如经典、无糖、樱桃）\n"
                "3. 口味（如含糖、无糖）\n"
                "4. 容量（如330ml、500ml、1L）\n"
                "为每个簇指定一个“规范名称”（canonical），格式如下：\n"
                "{\n"
                "  \"1\": {\"canonical\": \"…\", \"members\": […]},\n"
                "  …\n"
                "}\n"
                "请仅返回 JSON，不要包含任何思考或多余说明。\n"
                "在思考部分和 JSON 部分之间，用一行 “----JSON----” 分隔。"
            )},
            # 用户角色：列出待聚类项
            {"role": "user", "content": (
                "下面是一组汽水名称列表，请帮我按照上述分层规则聚类，并返回纯 JSON：\n"
                + soda_list
            )}
        ],
        "temperature": 0.0,
        "max_tokens": 12508
    }
    response = requests.post(API_URL, json=payload)
    response.raise_for_status()

    # 5️⃣ 拆分思考与 JSON
    content = response.json()["choices"][0]["message"]["content"]
    parts = content.split("----JSON----", 1)
    think_part, json_part = (parts + ["", ""])[:2]

    # 写入思考到 debug.txt
    debug_path = os.path.join(BASE_DIR, "debug.txt")
    with open(debug_path, "w", encoding="utf-8") as dbg:
        dbg.write(think_part.strip())
    print(f"📝 已将模型思考写入：{debug_path}")

    # 5.1️⃣ 用深度计数截取最外层 JSON
    text = json_part.strip()
    depth = 0
    start_idx = None
    end_idx = None
    for i, ch in enumerate(text):
        if ch == '{':
            depth += 1
            if start_idx is None:
                start_idx = i
        elif ch == '}':
            depth -= 1
            if depth == 0:
                end_idx = i
                break
    if start_idx is None or end_idx is None:
        print("----JSON PART----")
        print(json_part)
        raise ValueError("无法定位最外层 JSON 的起止位置。")
    json_text = text[start_idx:end_idx+1]

    # 5.2️⃣ 解析 JSON 部分
    try:
        clusters = json.loads(json_text)
    except json.JSONDecodeError as e:
        raise ValueError(f"JSON 解析失败：{e}\nJSON 内容：\n{json_text}")

    # 6️⃣ 构建 name->canonical 的映射
    name2canon = {
        name: info.get("canonical", name)
        for info in clusters.values()
        for name in info.get("members", [])
    }

    # 7️⃣ 将 canonical_name 写回原数据
    normalized = []
    for item in data:
        raw = item.get(field, "")
        # 去括号内容并归一化小写
        norm = re.sub(r'\s*\([^)]*\)', '', raw.lower()).strip()
        # 查找映射
        canon = name2canon.get(norm, norm)
        item['canonical_name'] = canon
        normalized.append(item)

    # 8️⃣ 打印所有 unique canonical_name 便于校验
    print("🔍 聚类后的所有 unique canonical_name：")
    for canon in sorted({it['canonical_name'] for it in normalized}):
        print(f"- {canon}")

    # 9️⃣ 输出 normalized_soda.json
    output_path = os.path.join(BASE_DIR, 'normalized_soda.json')
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(normalized, f, ensure_ascii=False, indent=2)
    print(f"✅ 已生成 {output_path}，共 {len(normalized)} 条记录。")

if __name__ == "__main__":
    main()