
import os
import json
import re
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

def extract_json_block(text):
    """
    更強力正則抓第一個合法 JSON 物件（可跨行/去除 markdown 包裝）
    """
    # 去除常見 markdown
    text = text.replace("```json", "").replace("```", "").strip()
    # 抓最早的 { ... }
    match = re.search(r'\{[\s\S]+\}', text)
    if not match:
        raise ValueError("⚠️ JSON object not found")
    try:
        return json.loads(match.group(0))
    except Exception as e:
        # 詳細錯誤提示方便除錯
        raise ValueError(f"⚠️ JSON parse error: {e}\nContent: {match.group(0)[:300]}")

def main():
    base = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(base, "filtered_tea_coffe_milktea.json")
    with open(src, encoding="utf-8") as f:
        data = json.load(f)
    if not data:
        raise ValueError("filtered_tea_coffe_milktea.json 為空！")

    eng_list = [item["eng"] for item in data]
    input_count = len(eng_list)

    system_prompt = (
        "You are a product normalization AI. Strictly follow these grouping rules step-by-step:\n"
        "1. Brand Normalization:\n"
        "- Standardize brand names consistently (e.g., 'Coca Cola', 'coca-cola' → 'coca-cola').\n"
        "- Use lowercase, remove unnecessary spaces, punctuation, typos.\n"
        "- If a brand reference list exists, match strictly; otherwise auto-judge.\n\n"
        "2. Removal of Capacity/Packaging:\n"
        "- Remove all capacity (300ml, 500ML), quantity (6x, 12-pack), packaging (box, can, bottle).\n"
        "- Keep only 'brand + series' if product explicitly includes capacity details.\n\n"
        "3. Main Series/Flavor Extraction:\n"
        "- Extract main series/flavor/variant (original, zero, lemon tea, almond, oat).\n"
        "- Unify synonyms and correct misspellings ('mirco sugar' → 'micro sugar').\n"
        "- All series/flavor lowercase, no punctuation.\n"
        "- Merge multi-layered brand (e.g., 'Vita Vitasoy' → 'vita vitasoy').\n\n"
        "4. Grouping & Deduplication:\n"
        "- Group identical brand+series/flavor despite capacity/packaging/order differences.\n"
        "- Only 'brand + series' form norm; remove other info.\n\n"
        "5. Minor/Special Brands:\n"
        "- For niche brands, norm = 'brand + primary keyword'.\n\n"
        "6. Synonym Normalization/Spelling Correction:\n"
        "- Correct synonyms/spelling errors (Chrystanthemum → chrysanthemum).\n\n"
        "7. Lowercase Output:\n"
        "- Entire norm lowercase only.\n\n"
        "8. Field Completion:\n"
        "- Auto-generate norm if missing.\n\n"
        "9. Sorting Results:\n"
        "- (Not required here. Keep exactly the input order.)\n\n"
        "10. Preserve Only Norm Info:\n"
        "- Norm = 'brand + series/flavor'; remove unnecessary descriptions, numbers, symbols.\n\n"
        "---\n"
        "Return **only a JSON object** with two fields:\n"
        "- \"norms\": an array of normalized names (in the EXACT same order as input)\n"
        "- \"length\": the integer number of items in the array\n"
        "If the output length is less than the input, you MUST continue and output all the rest until the array length equals the input count. "
        "If you cannot normalize a product, output 'unknown' in its place.\n"
        "No explanations, only the JSON object.\n"
        "Example:\n"
        "{\"norms\": [\"vita lemon tea\", \"coca-cola lemon tea\"], \"length\": 2}"
    )

    api_url = "http://192.168.50.98:1234/v1/chat/completions"
    payload = {
        "model": "meta-llama-3-8b-instruct",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": "Products:\n" + "\n".join(eng_list)}
        ],
        "temperature": 0.1,
        "max_tokens": 72432
    }

    sess = requests.Session()
    sess.mount("http://", HTTPAdapter(max_retries=Retry(
        total=3, backoff_factor=1, status_forcelist=[502, 503, 504], allowed_methods=["POST"])))

    max_try = 3
    for attempt in range(max_try):
        try:
            res = sess.post(api_url, json=payload)
            res.raise_for_status()
        except Exception as exc:
            raise RuntimeError(f"🚨 LLM call failed: {exc}")

        content = res.json()["choices"][0]["message"]["content"]
        print(f"\n=== LLM RAW (Attempt {attempt+1}) ===\n", content[:2000])

        # 強化版自動提取
        try:
            result = extract_json_block(content)
            norm_array = result["norms"]
            length = result["length"]
        except Exception as e:
            print(f"⚠️ {e}")
            if attempt == max_try - 1:
                raise
            else:
                continue

        if length == input_count == len(norm_array):
            break  # 成功
        print(f"⚠️ Output length mismatch: {length} (norms) vs {input_count} (input)")
        if attempt == max_try - 1:
            raise ValueError("Retry limit reached. LLM still returned mismatched length.")

    for rec, norm in zip(data, norm_array):
        rec["norm"] = norm

    out = os.path.join(base, "normalized_tea_coffe_milktea.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"\n✅ Done! {len(data)} records written to {out}")

if __name__ == "__main__":
    main()