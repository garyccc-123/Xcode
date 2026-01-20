#!/usr/bin/env python3
# ai_running.py

import os
import json
import requests

# 1️⃣ 定位 JSON 文件
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
filtered_path = os.path.join(BASE_DIR, 'filtered_fruit.json')
with open(filtered_path, encoding='utf-8') as f:
    data = json.load(f)
if not data:
    raise ValueError("filtered_fruit.json 为空！")

# 2️⃣ 选用聚类字段：优先使用 norm，否则使用 eng
field = 'norm' if 'norm' in data[0] else 'eng'
print(f"⚙️ 使用字段“{field}”进行聚类。")

# 3️⃣ 构造 Prompt，并强制模型仅返回纯 JSON
names = sorted({item.get(field, '') for item in data})
prompt = (
    "下面是一组水果名称列表，请帮我：\n"
    "1. 按语义或拼写相似度分簇；\n"
    "2. 为每个簇指定一个‘规范名称’；\n"
    "**请仅返回纯 JSON，不要包含任何多余说明。**\n"
    "JSON 格式：{\n"
    "  \"1\": {\"canonical\": \"…\", \"members\": […]},\n"
    "  …\n"
    "}\n\n水果列表：\n"
    + "\n".join(names)
)

# 4️⃣ 发送请求到本地 LM Studio（Deepseek）
API_URL = "http://192.168.50.98:1234/v1/chat/completions"
payload = {
    "model": "llama3.2",
    "messages": [{"role": "user", "content": prompt}],
    "temperature": 0.0,
    "max_tokens": 2048
}
response = requests.post(API_URL, json=payload)
response.raise_for_status()

# 5️⃣ 解析模型返回，增加容错并调试输出
content = response.json().get("choices", [])[0].get("message", {}).get("content", "").strip()
print("🔍 模型原始返回内容：", content)
try:
    clusters = json.loads(content)
except json.JSONDecodeError:
    # 尝试提取 JSON 部分
    start = content.find('{')
    end = content.rfind('}')
    if start != -1 and end != -1:
        json_str = content[start:end+1]
        clusters = json.loads(json_str)
        print("✅ 已提取并解析 JSON 部分。")
    else:
        raise

# 6️⃣ 合并原始数据并添加 canonical_name
name2canon = {
    nm: info["canonical"]
    for info in clusters.values()
    for nm in info.get("members", [])
}
normalized = []
for item in data:
    raw = item.get(field, "")
    item["canonical_name"] = name2canon.get(raw, raw)
    normalized.append(item)

# 7️⃣ 输出 normalized_fruit.json
output_path = os.path.join(BASE_DIR, 'normalized_fruit.json')
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(normalized, f, ensure_ascii=False, indent=2)
print(f"✅ 已生成 {output_path}，共 {len(normalized)} 条记录。")
