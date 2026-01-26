import json

# ==============================================================================
# 請將您的資料完整貼在下方 source_data 的中括號 [] 內
# ==============================================================================
source_data = [
      {
      "url": "https://www.wellcome.com.hk/zh-hant/p/De%20Cecco%E6%84%8F%E5%A4%A7%E5%88%A9%E7%B2%89n12%20500GM/i/101322714.html",
      "uid": "5394a8125dcef1350abd89cb2450f191",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "De Cecco意大利粉n12 500GM",
          "price": "$29",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240917/d229d442-fbc1-3302-a3e7-c1d4d3c37d2c",
          "product_eng_name": "De Cecco Spaghetti N12 500GM"
        },
        {
          "name": "De Cecco意大利粉n12 500GM",
          "price": "$29",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240917/d229d442-fbc1-3302-a3e7-c1d4d3c37d2c",
          "product_eng_name": "De Cecco Spaghetti N12 500GM"
        }
      ],
      "name": "De Cecco意大利粉n12 500GM",
      "price": "$29",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240917/d229d442-fbc1-3302-a3e7-c1d4d3c37d2c",
      "product_eng_name": "De Cecco Spaghetti N12 500GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E9%87%91%E6%BB%BF%E5%AE%B6%E6%9D%B1%E5%8C%97%E5%A4%A7%E7%B1%B3%203KG/i/101350093.html",
      "uid": "61b4dc728123f52f414f819175e4e144",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "金滿家東北大米 3KG",
          "price": "$106",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240312/0c63352e-a4bf-33ba-b0d0-75af77a9e47b",
          "product_eng_name": "Golden Home Medium Grain White Rice 3KG"
        }
      ],
      "name": "金滿家東北大米 3KG",
      "price": "$106",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240312/0c63352e-a4bf-33ba-b0d0-75af77a9e47b",
      "product_eng_name": "Golden Home Medium Grain White Rice 3KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%97%A5%E6%B8%85%E5%90%88%E5%91%B3%E9%81%93%E9%A6%99%E8%BE%A3%E6%B5%B7%E9%AE%AE%E8%BF%B7%E4%BD%A0%E6%9D%AF%E9%BA%B5%2045GM/i/101322999.html",
      "uid": "857b8cfbcf1e6eb263b7dab929bbb544",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "日清合味道香辣海鮮迷你杯麵 45GM",
          "price": "$6",
          "offer": "【3件$17】$17任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220713/176f8136-15c4-404e-a3c1-6f70b0d66e0a",
          "product_eng_name": "Nissin Cup Noodles Spicy Seafood Mini 45GM"
        },
        {
          "name": "日清合味道香辣海鮮迷你杯麵 45GM",
          "price": "$6",
          "offer": "【3件$17】$17任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220713/176f8136-15c4-404e-a3c1-6f70b0d66e0a",
          "product_eng_name": "Nissin Cup Noodles Spicy Seafood Mini 45GM"
        }
      ],
      "name": "日清合味道香辣海鮮迷你杯麵 45GM",
      "price": "$6",
      "offer": "【3件$17】$17任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20220713/176f8136-15c4-404e-a3c1-6f70b0d66e0a",
      "product_eng_name": "Nissin Cup Noodles Spicy Seafood Mini 45GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E5%87%BA%E5%89%8D%E4%B8%80%E4%B8%81%E5%8C%97%E6%B5%B7%E9%81%93%20%E5%B0%8F%E9%BA%A5%E7%B2%89%E9%BA%BB%E6%B2%B9%E9%BA%B5%20500%20GM/i/113557459.html",
      "uid": "ec0cc83a59a1755eace50fd48acc0121",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱出前一丁北海道 小麥粉麻油麵 500 GM",
          "price": "$120",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231013/2d147a62-bf87-3e12-9719-84e29525ca87",
          "product_eng_name": "Nissin Demae Iccho Hokkaido Wheat Flour Sesame Oil Noodles Case 30 x 100GM"
        },
        {
          "name": "原箱出前一丁北海道 小麥粉麻油麵 500 GM",
          "price": "$120",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231013/2d147a62-bf87-3e12-9719-84e29525ca87",
          "product_eng_name": "Nissin Demae Iccho Hokkaido Wheat Flour Sesame Oil Noodles Case 30 x 100GM"
        }
      ],
      "name": "原箱出前一丁北海道 小麥粉麻油麵 500 GM",
      "price": "$120",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20231013/2d147a62-bf87-3e12-9719-84e29525ca87",
      "product_eng_name": "Nissin Demae Iccho Hokkaido Wheat Flour Sesame Oil Noodles Case 30 x 100GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%8B%89%E9%9D%A2%E8%AA%AA%20%E6%B3%B0%E5%BC%8F%E6%B5%B7%E9%AE%AE%E5%86%AC%E9%99%B0%E5%8A%9F%E6%8B%89%E9%BA%B5%20149.5GM/i/101341288.html",
      "uid": "49914e6459d00e9aaf9a3a0c515ab2c3",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "拉面說 泰式海鮮冬陰功拉麵 149.5GM",
          "price": "$16",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240124/759957ec-f684-3d48-b244-68c8d221fb22",
          "product_eng_name": "Ramen Talk Seafood Tom Yum Ramen 149.5GM"
        }
      ],
      "name": "拉面說 泰式海鮮冬陰功拉麵 149.5GM",
      "price": "$16",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240124/759957ec-f684-3d48-b244-68c8d221fb22",
      "product_eng_name": "Ramen Talk Seafood Tom Yum Ramen 149.5GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%AE%97%E5%AE%B6%E5%BA%9C%E5%B9%B4%E7%B3%95%E7%89%87%201KG/i/101339633.html",
      "uid": "5b5c35a695ae031743b82287ae33f132",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "宗家府年糕片 1KG",
          "price": "$42",
          "offer": "【2件$49.9】$49.9任揀2件；數量有限，售完即止; 【指定分類享$25換購】每買1件，即可以$25換購1件人氣產品；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20221014/8f2ecbd2-cdfc-4a14-b24f-d1f808cee495",
          "product_eng_name": "Jongga Sliced Rice Cake 1KG"
        }
      ],
      "name": "宗家府年糕片 1KG",
      "price": "$42",
      "offer": "【2件$49.9】$49.9任揀2件；數量有限，售完即止; 【指定分類享$25換購】每買1件，即可以$25換購1件人氣產品；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20221014/8f2ecbd2-cdfc-4a14-b24f-d1f808cee495",
      "product_eng_name": "Jongga Sliced Rice Cake 1KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%BE%A1%E5%93%81%E7%9A%87%20%E8%97%A4%E6%A4%92%E6%8B%8C%E9%BA%B5%20109GM/i/114331536.html",
      "uid": "7873b657b85e68e06b07c8b09810e252",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "御品皇 藤椒拌麵 109GM",
          "price": "$8",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20241106/8873c189-9e69-3a41-8753-57e2977b484b",
          "product_eng_name": "Yu Pin King Green Peppercorn Dry-stirred Noodles 109G"
        },
        {
          "name": "御品皇 藤椒拌麵 109GM",
          "price": "$8",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20241106/8873c189-9e69-3a41-8753-57e2977b484b",
          "product_eng_name": "Yu Pin King Green Peppercorn Dry-stirred Noodles 109G"
        }
      ],
      "name": "御品皇 藤椒拌麵 109GM",
      "price": "$8",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20241106/8873c189-9e69-3a41-8753-57e2977b484b",
      "product_eng_name": "Yu Pin King Green Peppercorn Dry-stirred Noodles 109G"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%97%A5%E6%B8%85%E5%87%BA%E5%89%8D%E4%B8%80%E4%B8%81%E6%9D%B1%E4%BA%AC%E9%86%AC%E6%B2%B9%E5%8D%B3%E9%A3%9F%E9%BA%B5%20100GM/i/101352127.html",
      "uid": "ee0f9dee492050a2207ef1d5aab335c3",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "日清出前一丁東京醬油即食麵 100GM",
          "price": "$5",
          "offer": "【8件$28.5】$28.5任揀8件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250407/734aa892-3edc-369c-a933-4edb669f6e0a",
          "product_eng_name": "Nissin Demae Iccho Tokyo Shoyu Tonkotsu Noodles 100GM"
        },
        {
          "name": "日清出前一丁東京醬油即食麵 100GM",
          "price": "$5",
          "offer": "【8件$28.5】$28.5任揀8件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250407/734aa892-3edc-369c-a933-4edb669f6e0a",
          "product_eng_name": "Nissin Demae Iccho Tokyo Shoyu Tonkotsu Noodles 100GM"
        }
      ],
      "name": "日清出前一丁東京醬油即食麵 100GM",
      "price": "$5",
      "offer": "【8件$28.5】$28.5任揀8件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250407/734aa892-3edc-369c-a933-4edb669f6e0a",
      "product_eng_name": "Nissin Demae Iccho Tokyo Shoyu Tonkotsu Noodles 100GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E8%AE%9A%E5%B7%9E%E8%AE%9A%E5%B2%90%E4%BA%94%E4%BA%BA%E9%BA%B5%E9%BA%A5%E9%BA%B5%20460GM/i/101352672.html",
      "uid": "63c7ceeb7fae8ccabe1b3b1551222a8e",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "讚州讚岐五人麵麥麵 460GM",
          "price": "$40",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240429/31cfa728-7c7f-34e6-aba6-d119b625e272",
          "product_eng_name": "Sanuki Honpo Soba Ramen 460GM"
        },
        {
          "name": "讚州讚岐五人麵麥麵 460GM",
          "price": "$40",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240429/31cfa728-7c7f-34e6-aba6-d119b625e272",
          "product_eng_name": "Sanuki Honpo Soba Ramen 460GM"
        }
      ],
      "name": "讚州讚岐五人麵麥麵 460GM",
      "price": "$40",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240429/31cfa728-7c7f-34e6-aba6-d119b625e272",
      "product_eng_name": "Sanuki Honpo Soba Ramen 460GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E8%81%96%E8%B3%A2%E6%AF%8D%E6%84%8F%E5%A4%A7%E5%88%A9%E7%B2%89%235%20500GM/i/101347115.html",
      "uid": "cfea4532af35fdfb7ab40dd1f8e9a862",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "聖賢母意大利粉#5 500GM",
          "price": "$15",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240913/99b09232-fdd5-39eb-b47a-ea53276e5f22",
          "product_eng_name": "San Remo Spaghetti #5 500GM"
        },
        {
          "name": "聖賢母意大利粉#5 500GM",
          "price": "$15",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240913/99b09232-fdd5-39eb-b47a-ea53276e5f22",
          "product_eng_name": "San Remo Spaghetti #5 500GM"
        }
      ],
      "name": "聖賢母意大利粉#5 500GM",
      "price": "$15",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240913/99b09232-fdd5-39eb-b47a-ea53276e5f22",
      "product_eng_name": "San Remo Spaghetti #5 500GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%A3%BD%E6%A1%83qq%E9%AE%91%E9%AD%9A%E9%9B%9E%E7%B2%89%E7%B5%B2%205%20X%2070GM/i/101338187.html",
      "uid": "526bb5c4d4f513f8598c0d2c6770de51",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "壽桃qq鮑魚雞粉絲 5 X 70GM",
          "price": "$20",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220505/9c8f7fb4-1c0e-4497-af65-ae47ae171650",
          "product_eng_name": "Sau Tao QQ Abalone & Chicken Bean Vermicelli 5 X 70GM"
        },
        {
          "name": "壽桃qq鮑魚雞粉絲 5 X 70GM",
          "price": "$20",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220505/9c8f7fb4-1c0e-4497-af65-ae47ae171650",
          "product_eng_name": "Sau Tao QQ Abalone & Chicken Bean Vermicelli 5 X 70GM"
        }
      ],
      "name": "壽桃qq鮑魚雞粉絲 5 X 70GM",
      "price": "$20",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20220505/9c8f7fb4-1c0e-4497-af65-ae47ae171650",
      "product_eng_name": "Sau Tao QQ Abalone & Chicken Bean Vermicelli 5 X 70GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E7%87%9F%E5%A4%9A%E5%82%B3%E7%B5%B1%E5%8D%B0%E5%B0%BC%E6%92%88%E9%BA%B5%2040%20X%2085GM/i/101342378.html",
      "uid": "036f71a5f61512190c9f1f3897b0a6a4",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱營多傳統印尼撈麵 40 X 85GM",
          "price": "$114",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230620/a7d08e0b-f6e5-40b6-b4d1-01841e9c7865",
          "product_eng_name": "Indomie Mi Goreng Fried Noodles Case 40 x 85GM"
        },
        {
          "name": "原箱營多傳統印尼撈麵 40 X 85GM",
          "price": "$114",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230620/a7d08e0b-f6e5-40b6-b4d1-01841e9c7865",
          "product_eng_name": "Indomie Mi Goreng Fried Noodles Case 40 x 85GM"
        }
      ],
      "name": "原箱營多傳統印尼撈麵 40 X 85GM",
      "price": "$114",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230620/a7d08e0b-f6e5-40b6-b4d1-01841e9c7865",
      "product_eng_name": "Indomie Mi Goreng Fried Noodles Case 40 x 85GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E4%B8%89%E5%A5%BD%E7%B1%B3%E4%BA%94%E7%A9%80%E7%B1%B3%201.8KG/i/101341454.html",
      "uid": "96d9ff056effefb8104b7d65a1868a8d",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "三好米五穀米 1.8KG",
          "price": "$69",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210426/17ece9fc-ccfe-485d-8df2-b71a014ee912",
          "product_eng_name": "San Hao Rice 5 Cereal Rice 1.8KG"
        }
      ],
      "name": "三好米五穀米 1.8KG",
      "price": "$69",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210426/17ece9fc-ccfe-485d-8df2-b71a014ee912",
      "product_eng_name": "San Hao Rice 5 Cereal Rice 1.8KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E8%BE%B2%E5%BF%83%E8%BE%A3%E5%91%B3%E7%83%8F%E9%BE%8D%E9%BA%B5%205%20X%20120GM/i/101358116.html",
      "uid": "1e922aa79d3538cf899a37ea2e1e1619",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "農心辣味烏龍麵 5 X 120GM",
          "price": "$20",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210520/3805374c-5eb3-4344-b812-6763edacf19e",
          "product_eng_name": "Nong Shim Hot Neoguri Noodles 5 X 120GM"
        },
        {
          "name": "農心辣味烏龍麵 5 X 120GM",
          "price": "$20",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210520/3805374c-5eb3-4344-b812-6763edacf19e",
          "product_eng_name": "Nong Shim Hot Neoguri Noodles 5 X 120GM"
        }
      ],
      "name": "農心辣味烏龍麵 5 X 120GM",
      "price": "$20",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210520/3805374c-5eb3-4344-b812-6763edacf19e",
      "product_eng_name": "Nong Shim Hot Neoguri Noodles 5 X 120GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%A4%A9%E9%B5%9D%E7%89%8C%20%E6%98%9F%E6%B4%B2%E7%82%92%E7%B1%B3%E7%B2%89%20500%20GM/i/113337963.html",
      "uid": "a49f98466995adb5f24dd17c75df0ca5",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "天鵝牌 星洲炒米粉 500 GM",
          "price": "$17",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230606/41ad7024-42ec-4269-97d3-85f65458ed76",
          "product_eng_name": "Swan Deied Rice Stick 500GM"
        },
        {
          "name": "天鵝牌 星洲炒米粉 500 GM",
          "price": "$17",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230606/41ad7024-42ec-4269-97d3-85f65458ed76",
          "product_eng_name": "Swan Deied Rice Stick 500GM"
        }
      ],
      "name": "天鵝牌 星洲炒米粉 500 GM",
      "price": "$17",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230606/41ad7024-42ec-4269-97d3-85f65458ed76",
      "product_eng_name": "Swan Deied Rice Stick 500GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%97%A5%E6%B8%85%E5%87%BA%E5%89%8D%E4%B8%80%E4%B8%81%E6%97%A5%E5%BC%8F%E8%B1%AC%E9%AA%A8%E6%BF%83%E6%B9%AF%E7%A2%97%E9%BA%B5%20120GM/i/101338374.html",
      "uid": "8a8bab1771b6a376451a86fad90851b9",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "日清出前一丁日式豬骨濃湯碗麵 120GM",
          "price": "$10",
          "offer": "【2件$18】$18任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210518/25310146-eeca-48c5-a110-75386cb966da",
          "product_eng_name": "Nissin Demae Iccho Tonkotsu Bowl Noodles 120GM"
        },
        {
          "name": "日清出前一丁日式豬骨濃湯碗麵 120GM",
          "price": "$10",
          "offer": "【2件$18】$18任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210518/25310146-eeca-48c5-a110-75386cb966da",
          "product_eng_name": "Nissin Demae Iccho Tonkotsu Bowl Noodles 120GM"
        }
      ],
      "name": "日清出前一丁日式豬骨濃湯碗麵 120GM",
      "price": "$10",
      "offer": "【2件$18】$18任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210518/25310146-eeca-48c5-a110-75386cb966da",
      "product_eng_name": "Nissin Demae Iccho Tonkotsu Bowl Noodles 120GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E8%BE%B2%E5%BF%83%20%E8%BE%9B%E8%BE%A3%E6%8B%89%E9%BA%B5%E5%8E%9F%E7%AE%B1%2040%20X%20120GM/i/113559424.html",
      "uid": "221c58de7e6515d19140e6add91be46c",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "農心 辛辣拉麵原箱 40 X 120GM",
          "price": "$158",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231013/a37593c7-d003-37b5-9cba-dc4674ab902d",
          "product_eng_name": "Nong Shim Shin Ramyun Case 40 x 120GM"
        },
        {
          "name": "農心 辛辣拉麵原箱 40 X 120GM",
          "price": "$158",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231013/a37593c7-d003-37b5-9cba-dc4674ab902d",
          "product_eng_name": "Nong Shim Shin Ramyun Case 40 x 120GM"
        }
      ],
      "name": "農心 辛辣拉麵原箱 40 X 120GM",
      "price": "$158",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20231013/a37593c7-d003-37b5-9cba-dc4674ab902d",
      "product_eng_name": "Nong Shim Shin Ramyun Case 40 x 120GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%88%80%E5%98%9C%20%E9%87%91%E8%A3%9D%E6%A9%84%E6%AC%96%E8%8A%B1%E7%94%9F%E6%B2%B9900MLX3%20900%20ML/i/101360227.html",
      "uid": "132fb2bb8ac272f274f2715951e0d424",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "刀嘜 金裝橄欖花生油900MLX3 900 ML",
          "price": "$119",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240520/1f58750a-b1c4-39b0-b3c7-b3c461d16ee3",
          "product_eng_name": "Knife Supreme Olive Peanut Oil 3 x 900ML"
        },
        {
          "name": "刀嘜 金裝橄欖花生油900MLX3 900 ML",
          "price": "$119",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240520/1f58750a-b1c4-39b0-b3c7-b3c461d16ee3",
          "product_eng_name": "Knife Supreme Olive Peanut Oil 3 x 900ML"
        }
      ],
      "name": "刀嘜 金裝橄欖花生油900MLX3 900 ML",
      "price": "$119",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240520/1f58750a-b1c4-39b0-b3c7-b3c461d16ee3",
      "product_eng_name": "Knife Supreme Olive Peanut Oil 3 x 900ML"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E8%BE%B2%E5%BF%83%E8%BE%A3%E7%99%BD%E8%8F%9C%E8%8A%9D%E5%A3%AB%E9%BA%B5%205%20X%20120GM/i/101359568.html",
      "uid": "6f7566bdd9b22dd7bdda2cd6157dd15c",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "農心辣白菜芝士麵 5 X 120GM",
          "price": "$20",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210520/463b3f1b-ffaf-4fc1-b4ca-944275c837b0",
          "product_eng_name": "Nong Shim Kimchi Cheese Noodles 5 X 120GM"
        },
        {
          "name": "農心辣白菜芝士麵 5 X 120GM",
          "price": "$20",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210520/463b3f1b-ffaf-4fc1-b4ca-944275c837b0",
          "product_eng_name": "Nong Shim Kimchi Cheese Noodles 5 X 120GM"
        }
      ],
      "name": "農心辣白菜芝士麵 5 X 120GM",
      "price": "$20",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210520/463b3f1b-ffaf-4fc1-b4ca-944275c837b0",
      "product_eng_name": "Nong Shim Kimchi Cheese Noodles 5 X 120GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%B5%B1%E4%B8%80%E6%BB%BF%E6%BC%A2%E5%A4%A7%E9%A4%90%E7%8F%8D%E5%91%B3%E7%89%9B%E8%82%89%E5%A4%A7%E7%A2%97%E9%BA%B5%20192GM/i/101325786.html",
      "uid": "0a61f543efd96b3b262fcb8375b64710",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "統一滿漢大餐珍味牛肉大碗麵 192GM",
          "price": "$32",
          "offer": "【2件$32】$32任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20200413/f7fcfd8f-fd0f-4093-9c03-d2820e4760e5",
          "product_eng_name": "Uni President Imperial Big Meal Hot Beef Bowl Noodle 192GM"
        },
        {
          "name": "統一滿漢大餐珍味牛肉大碗麵 192GM",
          "price": "$32",
          "offer": "【2件$32】$32任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20200413/f7fcfd8f-fd0f-4093-9c03-d2820e4760e5",
          "product_eng_name": "Uni President Imperial Big Meal Hot Beef Bowl Noodle 192GM"
        }
      ],
      "name": "統一滿漢大餐珍味牛肉大碗麵 192GM",
      "price": "$32",
      "offer": "【2件$32】$32任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20200413/f7fcfd8f-fd0f-4093-9c03-d2820e4760e5",
      "product_eng_name": "Uni President Imperial Big Meal Hot Beef Bowl Noodle 192GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%97%A5%E6%B8%85%E5%87%BA%E5%89%8D%E4%B8%80%E4%B8%81%E9%BB%91%E8%92%9C%E8%B1%AC%E9%AA%A8%E6%B9%AF%E5%8D%B3%E9%A3%9F%E9%BA%B5%20100GM/i/101330936.html",
      "uid": "7cf6dc0611522f1aae3759971a872c9e",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "日清出前一丁黑蒜豬骨湯即食麵 100GM",
          "price": "$5",
          "offer": "【8件$28.5】$28.5任揀8件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250407/64f2211d-c427-337a-9d3c-1bdf7fae4dee",
          "product_eng_name": "Nissin Demae Iccho Black Garlic Oil Tonkotsu Noodle 100GM"
        },
        {
          "name": "日清出前一丁黑蒜豬骨湯即食麵 100GM",
          "price": "$5",
          "offer": "【8件$28.5】$28.5任揀8件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250407/64f2211d-c427-337a-9d3c-1bdf7fae4dee",
          "product_eng_name": "Nissin Demae Iccho Black Garlic Oil Tonkotsu Noodle 100GM"
        }
      ],
      "name": "日清出前一丁黑蒜豬骨湯即食麵 100GM",
      "price": "$5",
      "offer": "【8件$28.5】$28.5任揀8件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250407/64f2211d-c427-337a-9d3c-1bdf7fae4dee",
      "product_eng_name": "Nissin Demae Iccho Black Garlic Oil Tonkotsu Noodle 100GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%88%80%E5%98%9C%E7%B4%94%E6%AD%A3%E8%8A%B1%E7%94%9F%E6%B2%B9%203%20X%20900ML/i/101340701.html",
      "uid": "436a267560de6ffd3844e253958396bb",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "刀嘜純正花生油 3 X 900ML",
          "price": "$99",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240726/d859885b-fb2e-3a26-8118-e7b4b5bb5b4f",
          "product_eng_name": "Knife Pure Peanut Oil 3 X 900ML"
        },
        {
          "name": "刀嘜純正花生油 3 X 900ML",
          "price": "$99",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240726/d859885b-fb2e-3a26-8118-e7b4b5bb5b4f",
          "product_eng_name": "Knife Pure Peanut Oil 3 X 900ML"
        }
      ],
      "name": "刀嘜純正花生油 3 X 900ML",
      "price": "$99",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240726/d859885b-fb2e-3a26-8118-e7b4b5bb5b4f",
      "product_eng_name": "Knife Pure Peanut Oil 3 X 900ML"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8F%B0%E9%85%92%E8%8A%B1%E9%9B%95%E9%9B%9E%E7%A2%97%E9%BA%B5%20200GM/i/101345157.html",
      "uid": "7998d7b3e50e419ab498ceb6764361d4",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "台酒花雕雞碗麵 200GM",
          "price": "$32",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230518/c4cd9fc5-4de1-4f55-b609-65d5a1be9ff2",
          "product_eng_name": "TTL Hua Tiao Chiew Chicken Noodles 200GM"
        },
        {
          "name": "台酒花雕雞碗麵 200GM",
          "price": "$32",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230518/c4cd9fc5-4de1-4f55-b609-65d5a1be9ff2",
          "product_eng_name": "TTL Hua Tiao Chiew Chicken Noodles 200GM"
        }
      ],
      "name": "台酒花雕雞碗麵 200GM",
      "price": "$32",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230518/c4cd9fc5-4de1-4f55-b609-65d5a1be9ff2",
      "product_eng_name": "TTL Hua Tiao Chiew Chicken Noodles 200GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E5%87%BA%E5%89%8D%E4%B8%80%E4%B8%81%E5%8C%97%E6%B5%B7%E9%81%93%20%E5%B0%8F%E9%BA%A5%E7%B2%89%E8%B1%AC%E9%AA%A8%E6%B9%AF%E9%BA%B5%20500%20GM/i/113557469.html",
      "uid": "a49d08e3549a6508afb30d72e8aed80b",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱出前一丁北海道 小麥粉豬骨湯麵 500 GM",
          "price": "$120",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231013/ab0bf6c8-820e-31e6-9dec-e7561650c15e",
          "product_eng_name": "Nissin Demae Iccho Hokkaido Wheat Flour Tonkotsu Noodles Case 30 x 100GM"
        },
        {
          "name": "原箱出前一丁北海道 小麥粉豬骨湯麵 500 GM",
          "price": "$120",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231013/ab0bf6c8-820e-31e6-9dec-e7561650c15e",
          "product_eng_name": "Nissin Demae Iccho Hokkaido Wheat Flour Tonkotsu Noodles Case 30 x 100GM"
        }
      ],
      "name": "原箱出前一丁北海道 小麥粉豬骨湯麵 500 GM",
      "price": "$120",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20231013/ab0bf6c8-820e-31e6-9dec-e7561650c15e",
      "product_eng_name": "Nissin Demae Iccho Hokkaido Wheat Flour Tonkotsu Noodles Case 30 x 100GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E4%B8%89%E9%A4%8A%E8%8A%9D%E5%A3%AB%E7%82%92%E9%BA%B5%E7%89%B9%E8%BE%A3%E9%9B%9E%E8%82%89%205%20X%20140GM/i/101352231.html",
      "uid": "142ab08fc63e3a75fa12b4e03762a406",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "三養芝士炒麵特辣雞肉 5 X 140GM",
          "price": "$36",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230209/c4083ff6-9775-42fc-a1a8-de93514256f0",
          "product_eng_name": "Samyang Cheese Hot Chicken 5 X 140GM"
        },
        {
          "name": "三養芝士炒麵特辣雞肉 5 X 140GM",
          "price": "$36",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230209/c4083ff6-9775-42fc-a1a8-de93514256f0",
          "product_eng_name": "Samyang Cheese Hot Chicken 5 X 140GM"
        }
      ],
      "name": "三養芝士炒麵特辣雞肉 5 X 140GM",
      "price": "$36",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230209/c4083ff6-9775-42fc-a1a8-de93514256f0",
      "product_eng_name": "Samyang Cheese Hot Chicken 5 X 140GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%A3%BD%E6%A1%83%E7%95%AA%E8%8C%84%E8%82%89%E9%86%AC%E9%AE%AE%E6%84%8F%E7%B2%89%20225GM/i/101325315.html",
      "uid": "53269754aa3c6f2cba970af1d07d6650",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "壽桃番茄肉醬鮮意粉 225GM",
          "price": "$6",
          "offer": "【3件$22】$22任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220505/21916ffa-2275-4d55-819e-9058ca4d228e",
          "product_eng_name": "Sau Tao Fresh Pasta Minced Pork with Tomato Sauce 225GM"
        },
        {
          "name": "壽桃番茄肉醬鮮意粉 225GM",
          "price": "$6",
          "offer": "【3件$22】$22任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220505/21916ffa-2275-4d55-819e-9058ca4d228e",
          "product_eng_name": "Sau Tao Fresh Pasta Minced Pork with Tomato Sauce 225GM"
        }
      ],
      "name": "壽桃番茄肉醬鮮意粉 225GM",
      "price": "$6",
      "offer": "【3件$22】$22任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20220505/21916ffa-2275-4d55-819e-9058ca4d228e",
      "product_eng_name": "Sau Tao Fresh Pasta Minced Pork with Tomato Sauce 225GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%97%A5%E6%B8%85%E5%87%BA%E5%89%8D%E4%B8%80%E4%B8%81%E9%9B%9E%E8%93%89%E5%91%B3%E7%A2%97%E9%BA%B5%20103GM/i/101357032.html",
      "uid": "81954313f93d10d561ef2275adbee357",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "日清出前一丁雞蓉味碗麵 103GM",
          "price": "$10",
          "offer": "【2件$18】$18任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210518/0c060ac5-5267-40bd-ab9e-25a0b8476870",
          "product_eng_name": "Nissin Demae Iccho Chicken Bowl Noodle 103GM"
        },
        {
          "name": "日清出前一丁雞蓉味碗麵 103GM",
          "price": "$10",
          "offer": "【2件$18】$18任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210518/0c060ac5-5267-40bd-ab9e-25a0b8476870",
          "product_eng_name": "Nissin Demae Iccho Chicken Bowl Noodle 103GM"
        }
      ],
      "name": "日清出前一丁雞蓉味碗麵 103GM",
      "price": "$10",
      "offer": "【2件$18】$18任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210518/0c060ac5-5267-40bd-ab9e-25a0b8476870",
      "product_eng_name": "Nissin Demae Iccho Chicken Bowl Noodle 103GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E4%B8%8D%E7%AD%89%20%E9%A6%99%E8%BE%A3%E8%9F%B9%E9%BB%83%E9%BA%B5%20198%20GM/i/113623231.html",
      "uid": "c3f5d804fee5620d4109ac48171406a4",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "不等 香辣蟹黃麵 198 GM",
          "price": "$22",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240930/7d72b356-8023-3586-a837-9622ef9c2d28",
          "product_eng_name": "Budeng Crab Spicy Flavor Crab Noodles 198GM"
        },
        {
          "name": "不等 香辣蟹黃麵 198 GM",
          "price": "$22",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240930/7d72b356-8023-3586-a837-9622ef9c2d28",
          "product_eng_name": "Budeng Crab Spicy Flavor Crab Noodles 198GM"
        }
      ],
      "name": "不等 香辣蟹黃麵 198 GM",
      "price": "$22",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240930/7d72b356-8023-3586-a837-9622ef9c2d28",
      "product_eng_name": "Budeng Crab Spicy Flavor Crab Noodles 198GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E8%B6%85%E5%8A%9B%20%E9%9B%AA%E8%8F%9C%E8%82%89%E7%B5%B2%E5%91%B3%E7%A2%97%E7%B1%B3%E7%B2%89%2096%20GM/i/114326956.html",
      "uid": "167ca922e0fe3ca9e70ba5848ca8eeda",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "超力 雪菜肉絲味碗米粉 96 GM",
          "price": "$12",
          "offer": "【2件$14.5】$14.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240823/41f8c689-6119-3341-bb4e-90925ecb66a8",
          "product_eng_name": "Chewy Pickled Vegetable Pork Bowl Vermicelli 96GM"
        },
        {
          "name": "超力 雪菜肉絲味碗米粉 96 GM",
          "price": "$12",
          "offer": "【2件$14.5】$14.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240823/41f8c689-6119-3341-bb4e-90925ecb66a8",
          "product_eng_name": "Chewy Pickled Vegetable Pork Bowl Vermicelli 96GM"
        }
      ],
      "name": "超力 雪菜肉絲味碗米粉 96 GM",
      "price": "$12",
      "offer": "【2件$14.5】$14.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240823/41f8c689-6119-3341-bb4e-90925ecb66a8",
      "product_eng_name": "Chewy Pickled Vegetable Pork Bowl Vermicelli 96GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E9%87%91%E9%B3%B3%E6%B3%B0%E5%9C%8B%E9%A0%82%E7%B4%9A%E9%A6%99%E7%B1%B3%205KG/i/101327889.html",
      "uid": "400a9f51b4b415651e4002cffe3a02cc",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "金鳳泰國頂級香米 5KG",
          "price": "$83",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240506/55b48501-0cea-31d6-8326-494c16723687",
          "product_eng_name": "Golden Phoenix Thailand Hom Mali Rice 5KG"
        }
      ],
      "name": "金鳳泰國頂級香米 5KG",
      "price": "$83",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240506/55b48501-0cea-31d6-8326-494c16723687",
      "product_eng_name": "Golden Phoenix Thailand Hom Mali Rice 5KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%87%9F%E5%A4%9A%E5%82%B3%E7%B5%B1%E5%8A%A0%E8%BE%A3%E6%92%88%E9%BA%B5%205%20X%2080GM/i/101324159.html",
      "uid": "f97137b0c12751eec3fe87717e9c8ccc",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "營多傳統加辣撈麵 5 X 80GM",
          "price": "$13",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240726/cb5ee929-7639-3083-aaa2-10147764be4b",
          "product_eng_name": "Indomie Mi Goreng Hot & Spicy 5 X 80GM"
        },
        {
          "name": "營多傳統加辣撈麵 5 X 80GM",
          "price": "$13",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240726/cb5ee929-7639-3083-aaa2-10147764be4b",
          "product_eng_name": "Indomie Mi Goreng Hot & Spicy 5 X 80GM"
        }
      ],
      "name": "營多傳統加辣撈麵 5 X 80GM",
      "price": "$13",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240726/cb5ee929-7639-3083-aaa2-10147764be4b",
      "product_eng_name": "Indomie Mi Goreng Hot & Spicy 5 X 80GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E8%90%AC%E6%AD%B2%E7%B2%9F%E7%B1%B3%E6%B2%B9%203.5LT/i/101323070.html",
      "uid": "d7876f316d0e85dce4f453a41ab52d65",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "萬歲粟米油 3.5LT",
          "price": "$80",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240729/b6bcbbf9-00b8-339c-8a75-d20f84f42dd9",
          "product_eng_name": "Mazola Corn Oil 3.5LT"
        },
        {
          "name": "萬歲粟米油 3.5LT",
          "price": "$80",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240729/b6bcbbf9-00b8-339c-8a75-d20f84f42dd9",
          "product_eng_name": "Mazola Corn Oil 3.5LT"
        }
      ],
      "name": "萬歲粟米油 3.5LT",
      "price": "$80",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240729/b6bcbbf9-00b8-339c-8a75-d20f84f42dd9",
      "product_eng_name": "Mazola Corn Oil 3.5LT"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%AF%8C%E7%94%B0%E7%B2%BE%E7%B1%B3%20%E5%B2%A9%E6%89%8B%E7%B8%A3%E7%B4%94%E6%83%85%E7%84%A1%E6%B4%97%E7%B1%B3%202%20KG/i/113486554.html",
      "uid": "0b2e2289c016c3c9de1ec55da861838e",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "富田精米 岩手縣純情無洗米 2 KG",
          "price": "$65",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230721/1de21c99-c284-41a7-9ef9-e7ba39b60ce2",
          "product_eng_name": "Tomita Brand Iwate Hitomebore Rinse Free Rice 2KG"
        }
      ],
      "name": "富田精米 岩手縣純情無洗米 2 KG",
      "price": "$65",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230721/1de21c99-c284-41a7-9ef9-e7ba39b60ce2",
      "product_eng_name": "Tomita Brand Iwate Hitomebore Rinse Free Rice 2KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%91%B3%E5%8D%83%E6%8B%89%E9%BA%B5%E6%BF%83%E5%8E%9A%E8%B1%9A%E9%AA%A8%E6%B9%AF%E6%8B%89%E9%BA%B52%E4%BA%BA%E4%BB%BD%20303GM/i/113247924.html",
      "uid": "203e6e6b8a897d2bcbb2d11a9d94585c",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "味千拉麵濃厚豚骨湯拉麵2人份 303GM",
          "price": "$19",
          "offer": "【指定分類享$25換購】每買1件，即可以$25換購1件人氣產品；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20221108/a5a5c87f-6ee6-475f-93cd-73bbcdf4c844",
          "product_eng_name": "Ajisen Ramen Pork Broth Ramen 2 Serving 303GM"
        },
        {
          "name": "味千拉麵濃厚豚骨湯拉麵2人份 303GM",
          "price": "$19",
          "offer": "【指定分類享$25換購】每買1件，即可以$25換購1件人氣產品；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20221108/a5a5c87f-6ee6-475f-93cd-73bbcdf4c844",
          "product_eng_name": "Ajisen Ramen Pork Broth Ramen 2 Serving 303GM"
        }
      ],
      "name": "味千拉麵濃厚豚骨湯拉麵2人份 303GM",
      "price": "$19",
      "offer": "【指定分類享$25換購】每買1件，即可以$25換購1件人氣產品；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20221108/a5a5c87f-6ee6-475f-93cd-73bbcdf4c844",
      "product_eng_name": "Ajisen Ramen Pork Broth Ramen 2 Serving 303GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%BE%97%E5%AF%B6%E9%A6%99%E7%B1%B3%208KG/i/101359041.html",
      "uid": "9281160121e2693b37b24918edad4438",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "得寶香米 8KG",
          "price": "$73",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230321/70b831bb-de83-4758-99a8-56686dfd55d1",
          "product_eng_name": "Treasure Fragrant Rice 8KG"
        }
      ],
      "name": "得寶香米 8KG",
      "price": "$73",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230321/70b831bb-de83-4758-99a8-56686dfd55d1",
      "product_eng_name": "Treasure Fragrant Rice 8KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E7%99%BE%E5%BE%97%E9%98%BF%E5%A7%A8%20%E8%9E%BA%E7%B5%B2%E7%B2%8912%20X%20500%20GM/i/101335842.html",
      "uid": "6612a17a04eab13bd68e36761dbab400",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱百得阿姨 螺絲粉12 X 500 GM",
          "price": "$248",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231221/42aa75a2-2121-3f14-80e9-365559806dc6",
          "product_eng_name": "Barilla Fusilli #98 Case 12 X 500 GM"
        },
        {
          "name": "原箱百得阿姨 螺絲粉12 X 500 GM",
          "price": "$248",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231221/42aa75a2-2121-3f14-80e9-365559806dc6",
          "product_eng_name": "Barilla Fusilli #98 Case 12 X 500 GM"
        }
      ],
      "name": "原箱百得阿姨 螺絲粉12 X 500 GM",
      "price": "$248",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20231221/42aa75a2-2121-3f14-80e9-365559806dc6",
      "product_eng_name": "Barilla Fusilli #98 Case 12 X 500 GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%A9%97%E4%B9%8B%E9%A6%99%E7%89%8C%E9%AB%98%E7%B4%9A%E6%97%A5%E6%9C%AC%E5%93%81%E7%A8%AE%E7%8F%8D%E7%8F%A0%E7%B1%B3%202KG/i/102105936.html",
      "uid": "dd7bf7c0eada6556b0bb8eda592f4b2e",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "穗之香牌高級日本品種珍珠米 2KG",
          "price": "$28",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220419/f0bf19a5-58a6-47e0-9cc5-978c2d562a83",
          "product_eng_name": "Honokaori Premium Japonica Species 2KG"
        }
      ],
      "name": "穗之香牌高級日本品種珍珠米 2KG",
      "price": "$28",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20220419/f0bf19a5-58a6-47e0-9cc5-978c2d562a83",
      "product_eng_name": "Honokaori Premium Japonica Species 2KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%85%AC%E4%BB%94%E9%A6%99%E8%91%89%E8%82%89%E7%A2%8E%E5%91%B3%E5%8D%B3%E9%A3%9F%E9%BA%B5%20102GM/i/113249254.html",
      "uid": "9928fe303b8071718bc867bcd5fff61e",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "公仔香葉肉碎味即食麵 102GM",
          "price": "$7",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250320/84c121f7-11d4-3a2b-9338-643640335306",
          "product_eng_name": "Doll Fried Noodle Minced Pork With Basil Flavour 102GM"
        },
        {
          "name": "公仔香葉肉碎味即食麵 102GM",
          "price": "$7",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250320/84c121f7-11d4-3a2b-9338-643640335306",
          "product_eng_name": "Doll Fried Noodle Minced Pork With Basil Flavour 102GM"
        }
      ],
      "name": "公仔香葉肉碎味即食麵 102GM",
      "price": "$7",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250320/84c121f7-11d4-3a2b-9338-643640335306",
      "product_eng_name": "Doll Fried Noodle Minced Pork With Basil Flavour 102GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%97%A5%E6%B8%85%20%E5%92%9A%E5%85%B5%E8%A1%9B%E6%97%A5%E5%BC%8F%E8%85%90%E7%9A%AE%E6%89%8B%E6%89%93%E9%A2%A8%E7%83%8F%E5%86%AC%E7%A2%97%20211%20GM/i/113340668.html",
      "uid": "0f07739796950f9474a25732272a1e04",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "日清 咚兵衛日式腐皮手打風烏冬碗 211 GM",
          "price": "$16",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240823/f92fe49b-c0d7-3c4b-a1d3-31f4fbc10292",
          "product_eng_name": "Nissin Donbei Kitsune Handmade Style Udon 211GM"
        },
        {
          "name": "日清 咚兵衛日式腐皮手打風烏冬碗 211 GM",
          "price": "$16",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240823/f92fe49b-c0d7-3c4b-a1d3-31f4fbc10292",
          "product_eng_name": "Nissin Donbei Kitsune Handmade Style Udon 211GM"
        }
      ],
      "name": "日清 咚兵衛日式腐皮手打風烏冬碗 211 GM",
      "price": "$16",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240823/f92fe49b-c0d7-3c4b-a1d3-31f4fbc10292",
      "product_eng_name": "Nissin Donbei Kitsune Handmade Style Udon 211GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%86%8A%E4%BA%95%20%E6%9C%89%E6%A9%9F%E9%87%8E%E7%B1%B3%20500%20GM/i/101352458.html",
      "uid": "8fa9f06c13c35b1c19cb90db2270b4fa",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "熊井 有機野米 500 GM",
          "price": "$129",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210511/aab05f2a-fbde-467e-a007-69a86f860f03",
          "product_eng_name": "KUMAI ORGANIC WILD RICE 500 GM"
        }
      ],
      "name": "熊井 有機野米 500 GM",
      "price": "$129",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210511/aab05f2a-fbde-467e-a007-69a86f860f03",
      "product_eng_name": "KUMAI ORGANIC WILD RICE 500 GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/Costa%20d'Oro%E5%88%9D%E6%A6%A8%E6%A9%84%E6%AC%96%E6%B2%B9%201LT/i/101381332.html",
      "uid": "aae1c67dccb217d4caf17b3846712063",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "Costa d'Oro初榨橄欖油 1LT",
          "price": "$181",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210513/6bdedce6-fb4c-44ad-8935-652d7ec6f607",
          "product_eng_name": "Costa d'Oro Extra Virgin Olive Oil 1LT"
        },
        {
          "name": "Costa d'Oro初榨橄欖油 1LT",
          "price": "$181",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210513/6bdedce6-fb4c-44ad-8935-652d7ec6f607",
          "product_eng_name": "Costa d'Oro Extra Virgin Olive Oil 1LT"
        }
      ],
      "name": "Costa d'Oro初榨橄欖油 1LT",
      "price": "$181",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210513/6bdedce6-fb4c-44ad-8935-652d7ec6f607",
      "product_eng_name": "Costa d'Oro Extra Virgin Olive Oil 1LT"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E4%BA%94%E6%9C%A8%E6%B5%B7%E5%B8%B6%E7%83%8F%E5%86%AC%E7%A2%97%E9%BA%B5%20163GM/i/101350724.html",
      "uid": "66d70d399860496b55b54b69c223e083",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "五木海帶烏冬碗麵 163GM",
          "price": "$10",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20200501/10939c15-9110-43c2-8ff8-d755b7c9a64e",
          "product_eng_name": "Itsuki Cup Wakame Goma Udon 163GM"
        },
        {
          "name": "五木海帶烏冬碗麵 163GM",
          "price": "$10",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20200501/10939c15-9110-43c2-8ff8-d755b7c9a64e",
          "product_eng_name": "Itsuki Cup Wakame Goma Udon 163GM"
        }
      ],
      "name": "五木海帶烏冬碗麵 163GM",
      "price": "$10",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20200501/10939c15-9110-43c2-8ff8-d755b7c9a64e",
      "product_eng_name": "Itsuki Cup Wakame Goma Udon 163GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%A4%A7%E5%9C%B0%E4%B9%8B%E4%BD%9C%20%E6%B5%B7%E8%97%BB%E8%8A%8B%E7%B5%B2%20200%20GM/i/113340653.html",
      "uid": "5151a314fa98493dc508dced5e7ef93e",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "大地之作 海藻芋絲 200 GM",
          "price": "$10",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240919/c360c355-5a0d-3db4-af50-898dde9bbc50",
          "product_eng_name": "Natures Creat Konnyaku Seaweed Noodle 200GM"
        },
        {
          "name": "大地之作 海藻芋絲 200 GM",
          "price": "$10",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240919/c360c355-5a0d-3db4-af50-898dde9bbc50",
          "product_eng_name": "Natures Creat Konnyaku Seaweed Noodle 200GM"
        }
      ],
      "name": "大地之作 海藻芋絲 200 GM",
      "price": "$10",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240919/c360c355-5a0d-3db4-af50-898dde9bbc50",
      "product_eng_name": "Natures Creat Konnyaku Seaweed Noodle 200GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%99%BE%E7%9B%8A%E6%B8%85%E6%B7%A1%E6%A9%84%E6%AC%96%E6%B2%B9%201.5LT/i/113318653.html",
      "uid": "406f71412c54aaf25cae562d9fb93f06",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "百益清淡橄欖油 1.5LT",
          "price": "$229",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240930/092e2289-8265-35a8-bc73-eea9b3e2e405",
          "product_eng_name": "Filippo Berio Ex Light Olive Oil 1.5LT"
        },
        {
          "name": "百益清淡橄欖油 1.5LT",
          "price": "$229",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240930/092e2289-8265-35a8-bc73-eea9b3e2e405",
          "product_eng_name": "Filippo Berio Ex Light Olive Oil 1.5LT"
        }
      ],
      "name": "百益清淡橄欖油 1.5LT",
      "price": "$229",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240930/092e2289-8265-35a8-bc73-eea9b3e2e405",
      "product_eng_name": "Filippo Berio Ex Light Olive Oil 1.5LT"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%20%E5%BE%A1%E5%93%81%E7%9A%87%E6%A4%92%E9%BA%BB%E6%8B%8C%E9%BA%B5%2030x101GM/i/101362433.html",
      "uid": "765848e102c92ece8ecd0493b6920e87",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱 御品皇椒麻拌麵 30x101GM",
          "price": "$120",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250206/4e162cd5-8f17-3fa8-b838-4e39c37e3d70",
          "product_eng_name": "Yu Pin King Chili Peppercorn Noodles Case 30X101GM"
        },
        {
          "name": "原箱 御品皇椒麻拌麵 30x101GM",
          "price": "$120",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250206/4e162cd5-8f17-3fa8-b838-4e39c37e3d70",
          "product_eng_name": "Yu Pin King Chili Peppercorn Noodles Case 30X101GM"
        }
      ],
      "name": "原箱 御品皇椒麻拌麵 30x101GM",
      "price": "$120",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250206/4e162cd5-8f17-3fa8-b838-4e39c37e3d70",
      "product_eng_name": "Yu Pin King Chili Peppercorn Noodles Case 30X101GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%85%AC%E4%BB%94%E9%BB%9E%E5%BF%83%E9%BA%B5%E7%B4%85%E7%87%92%E7%89%9B%E8%82%89%E5%91%B3%E5%8D%B3%E9%A3%9F%E9%BA%B5%2041GM/i/101384608.html",
      "uid": "44daaae793c14eb0f5d7c932d0fcb02b",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "公仔點心麵紅燒牛肉味即食麵 41GM",
          "price": "$4",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210125/6fcc1cc9-0006-4a57-8699-893de39533d7",
          "product_eng_name": "Doll Dim Sum Noodle Braised Beef Flavour 41GM"
        },
        {
          "name": "公仔點心麵紅燒牛肉味即食麵 41GM",
          "price": "$4",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210125/6fcc1cc9-0006-4a57-8699-893de39533d7",
          "product_eng_name": "Doll Dim Sum Noodle Braised Beef Flavour 41GM"
        }
      ],
      "name": "公仔點心麵紅燒牛肉味即食麵 41GM",
      "price": "$4",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210125/6fcc1cc9-0006-4a57-8699-893de39533d7",
      "product_eng_name": "Doll Dim Sum Noodle Braised Beef Flavour 41GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/Meadows%E5%88%9D%E6%90%BE%E6%A9%84%E6%AC%96%E8%91%B5%E8%8A%B1%E7%B1%BD%E6%B2%B91L/i/114303991.html",
      "uid": "3ded8436c14092a9e17e2e7ec4cdf81e",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "Meadows初搾橄欖葵花籽油1L",
          "price": "$38",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240703/bb4cdf36-8edf-3448-a531-41b4f9814f44",
          "product_eng_name": "Meadows Extra Virgin Olive Oil & Sunflower Oil 1L"
        },
        {
          "name": "Meadows初搾橄欖葵花籽油1L",
          "price": "$38",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240703/bb4cdf36-8edf-3448-a531-41b4f9814f44",
          "product_eng_name": "Meadows Extra Virgin Olive Oil & Sunflower Oil 1L"
        }
      ],
      "name": "Meadows初搾橄欖葵花籽油1L",
      "price": "$38",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240703/bb4cdf36-8edf-3448-a531-41b4f9814f44",
      "product_eng_name": "Meadows Extra Virgin Olive Oil & Sunflower Oil 1L"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E8%BE%B2%E5%BF%83%E8%96%AF%E4%BB%94%E9%BA%B5%20100GM/i/101355400.html",
      "uid": "2369a0f473348524d62e19982bea7c28",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "農心薯仔麵 100GM",
          "price": "$20",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230913/6f58c475-c311-3d50-99de-64518476c23b",
          "product_eng_name": "Nong Shim Potato Noodles 100GM"
        },
        {
          "name": "農心薯仔麵 100GM",
          "price": "$20",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230913/6f58c475-c311-3d50-99de-64518476c23b",
          "product_eng_name": "Nong Shim Potato Noodles 100GM"
        }
      ],
      "name": "農心薯仔麵 100GM",
      "price": "$20",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230913/6f58c475-c311-3d50-99de-64518476c23b",
      "product_eng_name": "Nong Shim Potato Noodles 100GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/GROVE%20%E7%89%9B%E6%B2%B9%E6%9E%9C%E6%B2%B9%20500%E6%AF%AB%E5%8D%87/i/101346902.html",
      "uid": "ee0a0354ddf34f054a3b9b482b31c836",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "GROVE 牛油果油 500毫升",
          "price": "$163",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240312/9115dd90-b99c-3fb6-af79-9f6b46da50b9",
          "product_eng_name": "GOOD By Grove Everday Use Avocado Oil 500ML"
        },
        {
          "name": "GROVE 牛油果油 500毫升",
          "price": "$163",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240312/9115dd90-b99c-3fb6-af79-9f6b46da50b9",
          "product_eng_name": "GOOD By Grove Everday Use Avocado Oil 500ML"
        }
      ],
      "name": "GROVE 牛油果油 500毫升",
      "price": "$163",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240312/9115dd90-b99c-3fb6-af79-9f6b46da50b9",
      "product_eng_name": "GOOD By Grove Everday Use Avocado Oil 500ML"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E5%AE%B6%E6%A8%82%E7%89%8C%20%E9%AE%91%E9%AD%9A%E9%9B%9E%E9%80%9A%E5%BF%83%E7%B2%89%2030%20X%2080GM/i/101342391.html",
      "uid": "68a119f339ee69d4315a8034c8741900",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱家樂牌 鮑魚雞通心粉 30 X 80GM",
          "price": "$150",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230213/b7e60d5f-5280-42c6-b031-10bbbd9db60d",
          "product_eng_name": "Knorr Abalone & Chicken Quick Serve Macaroni Case 30 x 80GM"
        },
        {
          "name": "原箱家樂牌 鮑魚雞通心粉 30 X 80GM",
          "price": "$150",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230213/b7e60d5f-5280-42c6-b031-10bbbd9db60d",
          "product_eng_name": "Knorr Abalone & Chicken Quick Serve Macaroni Case 30 x 80GM"
        }
      ],
      "name": "原箱家樂牌 鮑魚雞通心粉 30 X 80GM",
      "price": "$150",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230213/b7e60d5f-5280-42c6-b031-10bbbd9db60d",
      "product_eng_name": "Knorr Abalone & Chicken Quick Serve Macaroni Case 30 x 80GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%BE%A1%E5%93%81%E7%9A%87%20%E8%8A%9D%E9%BA%BB%E9%BA%BB%E9%86%AC%E6%8B%8C%E9%BA%B5%20124GM/i/114331526.html",
      "uid": "c6a45570b4f9cb4385dd3357870f3bcc",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "御品皇 芝麻麻醬拌麵 124GM",
          "price": "$8",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20241113/d3668333-da89-3436-bd3a-61b1f6786482",
          "product_eng_name": "Yu Pin King Sesame Peanut Sauce Dry-stirred Noodles 124G"
        },
        {
          "name": "御品皇 芝麻麻醬拌麵 124GM",
          "price": "$8",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20241113/d3668333-da89-3436-bd3a-61b1f6786482",
          "product_eng_name": "Yu Pin King Sesame Peanut Sauce Dry-stirred Noodles 124G"
        }
      ],
      "name": "御品皇 芝麻麻醬拌麵 124GM",
      "price": "$8",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20241113/d3668333-da89-3436-bd3a-61b1f6786482",
      "product_eng_name": "Yu Pin King Sesame Peanut Sauce Dry-stirred Noodles 124G"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E8%BE%B2%E5%BF%83%E9%AE%AE%E8%9D%A6%E8%BE%9B%E8%BE%A3%E9%BA%B5%205%20X%20120GM/i/101346339.html",
      "uid": "f118d06041cf61e4f00973f868e45e3d",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "農心鮮蝦辛辣麵 5 X 120GM",
          "price": "$20",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20211020/90a9906f-bd70-471b-bdf4-b0065c4b5a4e",
          "product_eng_name": "Nong Shim Shrimp Shin Noodles 5 X 120GM"
        },
        {
          "name": "農心鮮蝦辛辣麵 5 X 120GM",
          "price": "$20",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20211020/90a9906f-bd70-471b-bdf4-b0065c4b5a4e",
          "product_eng_name": "Nong Shim Shrimp Shin Noodles 5 X 120GM"
        }
      ],
      "name": "農心鮮蝦辛辣麵 5 X 120GM",
      "price": "$20",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20211020/90a9906f-bd70-471b-bdf4-b0065c4b5a4e",
      "product_eng_name": "Nong Shim Shrimp Shin Noodles 5 X 120GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E9%9B%99%E7%BE%8A%E7%89%8C%E7%99%BE%E6%90%AD%E7%B1%B3%E7%8E%8B%202KG/i/101577967.html",
      "uid": "a8ce5314ded228db606f632c98a1e1e3",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "雙羊牌百搭米王 2KG",
          "price": "$52",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20241218/62418b7f-4ffb-3e2f-a8b2-56068a8ac544",
          "product_eng_name": "Double Ram Calrose Rice 2KG"
        }
      ],
      "name": "雙羊牌百搭米王 2KG",
      "price": "$52",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20241218/62418b7f-4ffb-3e2f-a8b2-56068a8ac544",
      "product_eng_name": "Double Ram Calrose Rice 2KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E4%B8%8D%E5%80%92%E7%BF%81%E5%8D%B3%E9%A3%9F%E5%A3%BD%E5%8F%B8%E9%A3%AF%20210GM/i/101328618.html",
      "uid": "91f4c71299c8a539449cb1015f6fa198",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "不倒翁即食壽司飯 210GM",
          "price": "$9",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240917/d456ef2e-7c8b-33c9-8b2e-869d18639bf9",
          "product_eng_name": "Ottogi Cooked Rice 210GM"
        },
        {
          "name": "不倒翁即食壽司飯 210GM",
          "price": "$9",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240917/d456ef2e-7c8b-33c9-8b2e-869d18639bf9",
          "product_eng_name": "Ottogi Cooked Rice 210GM"
        }
      ],
      "name": "不倒翁即食壽司飯 210GM",
      "price": "$9",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240917/d456ef2e-7c8b-33c9-8b2e-869d18639bf9",
      "product_eng_name": "Ottogi Cooked Rice 210GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%97%A5%E6%B8%85%E5%87%BA%E5%89%8D%E4%B8%80%E4%B8%81%E9%BA%BB%E6%B2%B9%E9%BA%B5%205%20X%20100GM%20(%E6%AC%BE%E5%BC%8F%E9%9A%A8%E6%A9%9F%E7%99%BC%E8%B2%A8)/i/101353645.html",
      "uid": "cfcc43f1be1d9f8e03ffb36adcb1ac15",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "日清出前一丁麻油麵 5 X 100GM (款式隨機發貨)",
          "price": "$20",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20241101/a511f0d7-3c28-3a85-9366-0b3f817d67d4",
          "product_eng_name": "Nissin Demae Iccho Sesame Oil Noodle 5 X 100GM (random Package Delivery)"
        },
        {
          "name": "日清出前一丁麻油麵 5 X 100GM (款式隨機發貨)",
          "price": "$20",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20241101/a511f0d7-3c28-3a85-9366-0b3f817d67d4",
          "product_eng_name": "Nissin Demae Iccho Sesame Oil Noodle 5 X 100GM (random Package Delivery)"
        }
      ],
      "name": "日清出前一丁麻油麵 5 X 100GM (款式隨機發貨)",
      "price": "$20",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20241101/a511f0d7-3c28-3a85-9366-0b3f817d67d4",
      "product_eng_name": "Nissin Demae Iccho Sesame Oil Noodle 5 X 100GM (random Package Delivery)"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%99%BE%E5%BE%97%E9%98%BF%E5%A7%A8%E6%89%81%E6%84%8F%E7%B2%89%20500GM/i/101326071.html",
      "uid": "5e76306e7d2af65698fddca604fe6d35",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "百得阿姨扁意粉 500GM",
          "price": "$22",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240916/b27fd009-5ac9-35e7-b679-984cebaf1ded",
          "product_eng_name": "Barilla Linguine No 500GM"
        },
        {
          "name": "百得阿姨扁意粉 500GM",
          "price": "$22",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240916/b27fd009-5ac9-35e7-b679-984cebaf1ded",
          "product_eng_name": "Barilla Linguine No 500GM"
        }
      ],
      "name": "百得阿姨扁意粉 500GM",
      "price": "$22",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240916/b27fd009-5ac9-35e7-b679-984cebaf1ded",
      "product_eng_name": "Barilla Linguine No 500GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%B5%B1%E4%B8%80%E6%BB%BF%E6%BC%A2%E5%A4%A7%E9%A4%90%E7%B4%85%E7%87%92%E7%89%9B%E8%82%89%E5%A4%A7%E7%A2%97%E9%BA%B5%20187GM/i/101325781.html",
      "uid": "4da0523ea64e60acce7859332fb69a6d",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "統一滿漢大餐紅燒牛肉大碗麵 187GM",
          "price": "$32",
          "offer": "【2件$32】$32任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20200413/f77dc1bc-b2fc-421d-a8f7-3ce8b003606b",
          "product_eng_name": "Uni President Imperial Big Meal Beef Bowl Noodle 187GM"
        },
        {
          "name": "統一滿漢大餐紅燒牛肉大碗麵 187GM",
          "price": "$32",
          "offer": "【2件$32】$32任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20200413/f77dc1bc-b2fc-421d-a8f7-3ce8b003606b",
          "product_eng_name": "Uni President Imperial Big Meal Beef Bowl Noodle 187GM"
        }
      ],
      "name": "統一滿漢大餐紅燒牛肉大碗麵 187GM",
      "price": "$32",
      "offer": "【2件$32】$32任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20200413/f77dc1bc-b2fc-421d-a8f7-3ce8b003606b",
      "product_eng_name": "Uni President Imperial Big Meal Beef Bowl Noodle 187GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%20%E5%BE%A1%E5%93%81%E7%9A%87%E8%97%A4%E6%A4%92%E6%8B%8C%E9%BA%B5%E7%A2%97%E8%A3%9D%2012x109GM/i/101362441.html",
      "uid": "e755cee0b20084b5e25e0f9377c90338",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱 御品皇藤椒拌麵碗裝 12x109GM",
          "price": "$96",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250206/ce1a710c-3758-3182-9bd4-ecffdaf52d55",
          "product_eng_name": "Yu Pin King Green Peppercorn Case 12X109GM"
        },
        {
          "name": "原箱 御品皇藤椒拌麵碗裝 12x109GM",
          "price": "$96",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250206/ce1a710c-3758-3182-9bd4-ecffdaf52d55",
          "product_eng_name": "Yu Pin King Green Peppercorn Case 12X109GM"
        }
      ],
      "name": "原箱 御品皇藤椒拌麵碗裝 12x109GM",
      "price": "$96",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250206/ce1a710c-3758-3182-9bd4-ecffdaf52d55",
      "product_eng_name": "Yu Pin King Green Peppercorn Case 12X109GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E9%A7%B1%E9%A7%9D%E5%98%9C%E7%89%B9%E9%A6%99%E7%B4%94%E6%AD%A3%E8%8A%B1%E7%94%9F%E6%B2%B9%205LT/i/101343751.html",
      "uid": "d8b371dd46ff47c8dda5234df5017644",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "駱駝嘜特香純正花生油 5LT",
          "price": "$146",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230215/542e483b-98b5-4d57-b4dc-17e3bc905a61",
          "product_eng_name": "Camel Peanut Oil 5LT"
        },
        {
          "name": "駱駝嘜特香純正花生油 5LT",
          "price": "$146",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230215/542e483b-98b5-4d57-b4dc-17e3bc905a61",
          "product_eng_name": "Camel Peanut Oil 5LT"
        }
      ],
      "name": "駱駝嘜特香純正花生油 5LT",
      "price": "$146",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230215/542e483b-98b5-4d57-b4dc-17e3bc905a61",
      "product_eng_name": "Camel Peanut Oil 5LT"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E8%81%96%E8%B3%A2%E6%AF%8D%E9%80%9A%E5%BF%83%E7%B2%89%2335%20500GM/i/101349522.html",
      "uid": "790ba76f466689d56def49e19c39aec9",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "聖賢母通心粉#35 500GM",
          "price": "$16",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240913/35a910ac-6900-31d1-b07b-d97ae86a009b",
          "product_eng_name": "San Remo Elbows#35 500GM"
        },
        {
          "name": "聖賢母通心粉#35 500GM",
          "price": "$16",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240913/35a910ac-6900-31d1-b07b-d97ae86a009b",
          "product_eng_name": "San Remo Elbows#35 500GM"
        }
      ],
      "name": "聖賢母通心粉#35 500GM",
      "price": "$16",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240913/35a910ac-6900-31d1-b07b-d97ae86a009b",
      "product_eng_name": "San Remo Elbows#35 500GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E8%B6%85%E5%8A%9B%E7%87%92%E7%83%8F%E5%86%AC%E6%B7%BA%E8%8D%89%E7%87%92%E6%B1%81%E5%91%B3%20420GM/i/101348935.html",
      "uid": "3012ef0bd8beff170e7dc2cb2d40a685",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "超力燒烏冬淺草燒汁味 420GM",
          "price": "$24",
          "offer": "【2件$22】$22任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210429/3c56880d-f34f-474a-a95c-43f574da2964",
          "product_eng_name": "Chewy Japanese Fried Udon 420GM"
        },
        {
          "name": "超力燒烏冬淺草燒汁味 420GM",
          "price": "$24",
          "offer": "【2件$22】$22任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210429/3c56880d-f34f-474a-a95c-43f574da2964",
          "product_eng_name": "Chewy Japanese Fried Udon 420GM"
        }
      ],
      "name": "超力燒烏冬淺草燒汁味 420GM",
      "price": "$24",
      "offer": "【2件$22】$22任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210429/3c56880d-f34f-474a-a95c-43f574da2964",
      "product_eng_name": "Chewy Japanese Fried Udon 420GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E8%BE%B2%E5%BF%83%E7%82%B8%E9%86%AC%E9%BA%B5%20140GM/i/101371305.html",
      "uid": "572d2367c3301c25645b3a334c26c351",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "農心炸醬麵 140GM",
          "price": "$32",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240916/fa9dfa68-99a6-3af9-9adb-4ecf18291532",
          "product_eng_name": "Nong Shim Chapagetti Noodles 140GM"
        },
        {
          "name": "農心炸醬麵 140GM",
          "price": "$32",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240916/fa9dfa68-99a6-3af9-9adb-4ecf18291532",
          "product_eng_name": "Nong Shim Chapagetti Noodles 140GM"
        }
      ],
      "name": "農心炸醬麵 140GM",
      "price": "$32",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240916/fa9dfa68-99a6-3af9-9adb-4ecf18291532",
      "product_eng_name": "Nong Shim Chapagetti Noodles 140GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%99%BE%E5%8B%9D%E5%BB%9A%E5%8F%BB%E6%B2%99%E6%8B%89%E9%BA%B5%20185GM/i/101322794.html",
      "uid": "6b49a247cfa477e6a0b9fb0d7288000a",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "百勝廚叻沙拉麵 185GM",
          "price": "$31",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240315/ff338782-c4dc-3afd-965a-f96bdefb6df6",
          "product_eng_name": "Prima Taste Laksa La Mian 185GM"
        },
        {
          "name": "百勝廚叻沙拉麵 185GM",
          "price": "$31",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240315/ff338782-c4dc-3afd-965a-f96bdefb6df6",
          "product_eng_name": "Prima Taste Laksa La Mian 185GM"
        }
      ],
      "name": "百勝廚叻沙拉麵 185GM",
      "price": "$31",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240315/ff338782-c4dc-3afd-965a-f96bdefb6df6",
      "product_eng_name": "Prima Taste Laksa La Mian 185GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%85%AC%E4%BB%94%20%E9%BA%BB%E6%B2%B9%E4%B8%8A%E7%B4%A0%E7%A2%97%E9%BA%B5%20107GM/i/101343744.html",
      "uid": "2a3ba0fe22cd048705fccc5447f28b4d",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "公仔 麻油上素碗麵 107GM",
          "price": "$7",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250320/45803ba1-0aaf-3ca1-8e38-8bb22d800d1c",
          "product_eng_name": "Doll Vegetable Bowl Noodle 107GM"
        },
        {
          "name": "公仔 麻油上素碗麵 107GM",
          "price": "$7",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250320/45803ba1-0aaf-3ca1-8e38-8bb22d800d1c",
          "product_eng_name": "Doll Vegetable Bowl Noodle 107GM"
        }
      ],
      "name": "公仔 麻油上素碗麵 107GM",
      "price": "$7",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250320/45803ba1-0aaf-3ca1-8e38-8bb22d800d1c",
      "product_eng_name": "Doll Vegetable Bowl Noodle 107GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E6%9D%8E%E9%8C%A6%E8%A8%98%E6%A4%92%E9%BA%BB%E6%8B%8C%E9%BA%B512x110GM/i/114211826.html",
      "uid": "716aa6ffddc2016d2df0046eec821fc1",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱李錦記椒麻拌麵12x110GM",
          "price": "$384",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240719/aa6eafef-13a5-32bb-99a9-3ad411b718b7",
          "product_eng_name": "Lee Kum Kee Peppercorn Noodle Case 12 x 110GM"
        },
        {
          "name": "原箱李錦記椒麻拌麵12x110GM",
          "price": "$384",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240719/aa6eafef-13a5-32bb-99a9-3ad411b718b7",
          "product_eng_name": "Lee Kum Kee Peppercorn Noodle Case 12 x 110GM"
        }
      ],
      "name": "原箱李錦記椒麻拌麵12x110GM",
      "price": "$384",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240719/aa6eafef-13a5-32bb-99a9-3ad411b718b7",
      "product_eng_name": "Lee Kum Kee Peppercorn Noodle Case 12 x 110GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%85%83%E7%A5%96%E5%8D%81%E5%89%B2%E8%95%8E%E9%BA%A5%E9%BA%B5%20200GM/i/101578303.html",
      "uid": "23ce51409efa75d26e53d2a28227d0e0",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "元祖十割蕎麥麵 200GM",
          "price": "$50",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240529/04f141da-517e-302d-be81-b668be3a91bf",
          "product_eng_name": "Yamamoto Kajino 100% Buckwheat Soba 200GM"
        },
        {
          "name": "元祖十割蕎麥麵 200GM",
          "price": "$50",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240529/04f141da-517e-302d-be81-b668be3a91bf",
          "product_eng_name": "Yamamoto Kajino 100% Buckwheat Soba 200GM"
        }
      ],
      "name": "元祖十割蕎麥麵 200GM",
      "price": "$50",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240529/04f141da-517e-302d-be81-b668be3a91bf",
      "product_eng_name": "Yamamoto Kajino 100% Buckwheat Soba 200GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8F%B0%E9%85%92%E9%BA%BB%E6%B2%B9%E9%9B%9E%E7%A2%97%E9%BA%B5%20200GM/i/101354926.html",
      "uid": "65fc5cbc8f88566ad56d97b7ae6963b9",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "台酒麻油雞碗麵 200GM",
          "price": "$32",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230518/d513d729-07de-4427-8fa6-5b23e9c44d38",
          "product_eng_name": "(無法擷取英文名稱)"
        },
        {
          "name": "台酒麻油雞碗麵 200GM",
          "price": "$32",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230518/d513d729-07de-4427-8fa6-5b23e9c44d38",
          "product_eng_name": "TTL Sesame Oil Chicken Noodles 200GM"
        }
      ],
      "name": "台酒麻油雞碗麵 200GM",
      "price": "$32",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230518/d513d729-07de-4427-8fa6-5b23e9c44d38",
      "product_eng_name": "TTL Sesame Oil Chicken Noodles 200GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E8%BE%B2%E5%BF%83%20%E8%BE%9B%E8%BE%A3%E8%BE%A3%E9%9B%9E%E9%BA%B54%E5%8C%85%E8%A3%9D%20120GM/i/101328385.html",
      "uid": "7fa6125778ce596cd87ab3984653ff6e",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "農心 辛辣辣雞麵4包裝 120GM",
          "price": "$26",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240807/570eb19d-0688-3170-a6f0-682ae6c39c72",
          "product_eng_name": "Nong Shim Shin Spicy Chicken Noodle 4 X 120GM"
        },
        {
          "name": "農心 辛辣辣雞麵4包裝 120GM",
          "price": "$26",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240807/570eb19d-0688-3170-a6f0-682ae6c39c72",
          "product_eng_name": "Nong Shim Shin Spicy Chicken Noodle 4 X 120GM"
        }
      ],
      "name": "農心 辛辣辣雞麵4包裝 120GM",
      "price": "$26",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240807/570eb19d-0688-3170-a6f0-682ae6c39c72",
      "product_eng_name": "Nong Shim Shin Spicy Chicken Noodle 4 X 120GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E7%B5%B1%E4%B8%80%E6%BB%BF%E6%BC%A2%E5%A4%A7%E9%A4%90%20%E7%8F%8D%E5%91%B3%E7%89%9B%E8%82%89%E7%A2%97%E9%BA%B5%2012%20X%20192GM/i/113465664.html",
      "uid": "b196fcd8a5636c25de5926f7d83ca8fe",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱統一滿漢大餐 珍味牛肉碗麵 12 X 192GM",
          "price": "$180",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230728/2c6acf2b-0f9c-3678-93c1-ce95ab11ed4c",
          "product_eng_name": "Imperial Big Meal Hot Beef Bowl Noodle Case 12 x 192GM"
        },
        {
          "name": "原箱統一滿漢大餐 珍味牛肉碗麵 12 X 192GM",
          "price": "$180",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230728/2c6acf2b-0f9c-3678-93c1-ce95ab11ed4c",
          "product_eng_name": "Imperial Big Meal Hot Beef Bowl Noodle Case 12 x 192GM"
        }
      ],
      "name": "原箱統一滿漢大餐 珍味牛肉碗麵 12 X 192GM",
      "price": "$180",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230728/2c6acf2b-0f9c-3678-93c1-ce95ab11ed4c",
      "product_eng_name": "Imperial Big Meal Hot Beef Bowl Noodle Case 12 x 192GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E5%BE%A1%E5%93%81%E7%9A%87%20%E8%94%A5%E6%B2%B9%E6%8B%8C%E9%BA%B5%20103%20GM/i/113612031.html",
      "uid": "6627c8937670997ed5c45dcae08e84ec",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱御品皇 蔥油拌麵 103 GM",
          "price": "$120",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230926/f66d4f7e-cb00-3c03-9ec1-9ab6efa598c0",
          "product_eng_name": "Yu Pin King Scallion Oil Dry-Stirred Noodles Case 30 x 103GM"
        },
        {
          "name": "原箱御品皇 蔥油拌麵 103 GM",
          "price": "$120",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230926/f66d4f7e-cb00-3c03-9ec1-9ab6efa598c0",
          "product_eng_name": "Yu Pin King Scallion Oil Dry-Stirred Noodles Case 30 x 103GM"
        }
      ],
      "name": "原箱御品皇 蔥油拌麵 103 GM",
      "price": "$120",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230926/f66d4f7e-cb00-3c03-9ec1-9ab6efa598c0",
      "product_eng_name": "Yu Pin King Scallion Oil Dry-Stirred Noodles Case 30 x 103GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%97%A5%E6%B8%85%20%E5%86%AC%E8%94%AD%E5%8A%9F%E6%B9%AF%E9%BA%B5%205%20X%20%2068GM%20(%E5%88%B0%E6%9C%9F%E6%97%A5%3A%202025%E5%B9%B45%E6%9C%8812%E6%97%A5)/i/101844712.html",
      "uid": "a808b4d0044e6f8077cc35461da43352",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "日清 冬蔭功湯麵 5 X 68GM (到期日: 2025年5月12日)",
          "price": "$8",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210928/e0591aa6-c2fa-4b74-b6d8-0e3a1f20727e",
          "product_eng_name": "Nissin Thai Tomyum Goong Noodles 5 X 68GM (Expiry date: 12 May 2025)"
        },
        {
          "name": "日清 冬蔭功湯麵 5 X 68GM (到期日: 2025年5月12日)",
          "price": "$8",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210928/e0591aa6-c2fa-4b74-b6d8-0e3a1f20727e",
          "product_eng_name": "Nissin Thai Tomyum Goong Noodles 5 X 68GM (Expiry date: 12 May 2025)"
        }
      ],
      "name": "日清 冬蔭功湯麵 5 X 68GM (到期日: 2025年5月12日)",
      "price": "$8",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210928/e0591aa6-c2fa-4b74-b6d8-0e3a1f20727e",
      "product_eng_name": "Nissin Thai Tomyum Goong Noodles 5 X 68GM (Expiry date: 12 May 2025)"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%85%AB%E9%81%93%E7%89%9B%E9%AA%A8%E6%B9%AF%E9%BA%B5%205%20X%20102GM/i/101342483.html",
      "uid": "a6ec1d516ae8f2269605ae15687cb49d",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "八道牛骨湯麵 5 X 102GM",
          "price": "$27",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240916/f5730f43-83a8-3c38-b11d-5fe659f903a5",
          "product_eng_name": "Paldo Gomtang Beef Noodle 5 X 102GM"
        },
        {
          "name": "八道牛骨湯麵 5 X 102GM",
          "price": "$27",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240916/f5730f43-83a8-3c38-b11d-5fe659f903a5",
          "product_eng_name": "Paldo Gomtang Beef Noodle 5 X 102GM"
        }
      ],
      "name": "八道牛骨湯麵 5 X 102GM",
      "price": "$27",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240916/f5730f43-83a8-3c38-b11d-5fe659f903a5",
      "product_eng_name": "Paldo Gomtang Beef Noodle 5 X 102GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E5%85%AB%E9%81%93%20%E7%89%9B%E9%AA%A8%E6%B9%AF%E9%BA%B5%20510%20GM/i/113559459.html",
      "uid": "6579bce66c4b51ccba7437a110165ee2",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱八道 牛骨湯麵 510 GM",
          "price": "$104",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231013/57d12b09-9f60-3a12-8be8-b6be3b49d19c",
          "product_eng_name": "PALDO* GOMTANG BEEF NOODLE\\4 CS\\ 510 GM"
        },
        {
          "name": "原箱八道 牛骨湯麵 510 GM",
          "price": "$104",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231013/57d12b09-9f60-3a12-8be8-b6be3b49d19c",
          "product_eng_name": "PALDO* GOMTANG BEEF NOODLE\\4 CS\\ 510 GM"
        }
      ],
      "name": "原箱八道 牛骨湯麵 510 GM",
      "price": "$104",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20231013/57d12b09-9f60-3a12-8be8-b6be3b49d19c",
      "product_eng_name": "PALDO* GOMTANG BEEF NOODLE\\4 CS\\ 510 GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E8%9E%BA%E9%9C%B8%E7%8E%8B%20%E6%9F%B3%E5%B7%9E%E8%9E%BA%E8%9E%84%E7%B2%89306%E5%85%8B%E8%95%83%E8%8C%84%E5%91%B3%20306%20GM/i/102125806.html",
      "uid": "f9484f8ea66cc5d70771d9e01238993b",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "螺霸王 柳州螺螄粉306克蕃茄味 306 GM",
          "price": "$15",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240124/662312c5-510a-3a7e-b4b1-eb53491ecfb3",
          "product_eng_name": "NO WANG LIUZHOU RICE NOODLE 306GM TOMATO 306 GM"
        },
        {
          "name": "螺霸王 柳州螺螄粉306克蕃茄味 306 GM",
          "price": "$15",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240124/662312c5-510a-3a7e-b4b1-eb53491ecfb3",
          "product_eng_name": "NO WANG LIUZHOU RICE NOODLE 306GM TOMATO 306 GM"
        }
      ],
      "name": "螺霸王 柳州螺螄粉306克蕃茄味 306 GM",
      "price": "$15",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240124/662312c5-510a-3a7e-b4b1-eb53491ecfb3",
      "product_eng_name": "NO WANG LIUZHOU RICE NOODLE 306GM TOMATO 306 GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%A3%BD%E6%A1%83%20%E9%AE%91%E9%AD%9A%E9%9B%9E%E6%B9%AF%E5%91%B3%E6%B7%AE%E5%B1%B1%E9%BA%B5%20180%20GM/i/101378768.html",
      "uid": "17a5fdc998d5c12d3001123eebbb023f",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "壽桃 鮑魚雞湯味淮山麵 180 GM",
          "price": "$9",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240823/2bd89450-ecfc-366a-915d-0191c444ee56",
          "product_eng_name": "Sau Tao Abalone Chicken Soup Flavour Yam Noodles 180GM"
        },
        {
          "name": "壽桃 鮑魚雞湯味淮山麵 180 GM",
          "price": "$9",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240823/2bd89450-ecfc-366a-915d-0191c444ee56",
          "product_eng_name": "Sau Tao Abalone Chicken Soup Flavour Yam Noodles 180GM"
        }
      ],
      "name": "壽桃 鮑魚雞湯味淮山麵 180 GM",
      "price": "$9",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240823/2bd89450-ecfc-366a-915d-0191c444ee56",
      "product_eng_name": "Sau Tao Abalone Chicken Soup Flavour Yam Noodles 180GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%A3%BD%E6%A1%83%E7%89%8C%E7%82%B8%E8%8F%9C%E8%82%89%E7%B5%B2%E5%B0%8F%E6%A9%8B%E7%B1%B3%E7%B7%9A%204%20X%20215GM/i/101346456.html",
      "uid": "fcdf266e9af57dbd1ed25897866a5f19",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "壽桃牌炸菜肉絲小橋米線 4 X 215GM",
          "price": "$14",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220505/b26c9f3c-f2da-4efa-83a6-f913c7ed604d",
          "product_eng_name": "Sau Tao Pork & Pickled Veg Noodles 4 X 215GM"
        },
        {
          "name": "壽桃牌炸菜肉絲小橋米線 4 X 215GM",
          "price": "$14",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220505/b26c9f3c-f2da-4efa-83a6-f913c7ed604d",
          "product_eng_name": "Sau Tao Pork & Pickled Veg Noodles 4 X 215GM"
        }
      ],
      "name": "壽桃牌炸菜肉絲小橋米線 4 X 215GM",
      "price": "$14",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20220505/b26c9f3c-f2da-4efa-83a6-f913c7ed604d",
      "product_eng_name": "Sau Tao Pork & Pickled Veg Noodles 4 X 215GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%97%A5%E6%B8%85%E5%90%88%E5%91%B3%E9%81%93%E5%92%96%E5%96%B1%E6%B5%B7%E9%AE%AE%E5%91%B3%E5%A4%A7%E6%9D%AF%E9%BA%B5%20101GM/i/102126986.html",
      "uid": "7aa539028d7df449ffd623787581fbbc",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "日清合味道咖喱海鮮味大杯麵 101GM",
          "price": "$11",
          "offer": "【2件$18】$18任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240711/cb977f30-ee92-39e7-a75e-36b0972b7a96",
          "product_eng_name": "Nissin Big Cup Curry Noodles 101GM"
        },
        {
          "name": "日清合味道咖喱海鮮味大杯麵 101GM",
          "price": "$11",
          "offer": "【2件$18】$18任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240711/cb977f30-ee92-39e7-a75e-36b0972b7a96",
          "product_eng_name": "Nissin Big Cup Curry Noodles 101GM"
        }
      ],
      "name": "日清合味道咖喱海鮮味大杯麵 101GM",
      "price": "$11",
      "offer": "【2件$18】$18任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240711/cb977f30-ee92-39e7-a75e-36b0972b7a96",
      "product_eng_name": "Nissin Big Cup Curry Noodles 101GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/Meadows%E9%80%9A%E5%BF%83%E7%B2%89%20N41%20500GM/i/101579431.html",
      "uid": "f5be015917afe45d0590dc7a8b97b4e7",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "Meadows通心粉 N41 500GM",
          "price": "$16",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231204/4b35cd3f-f5df-350a-83d5-438d845307b4",
          "product_eng_name": "Meadows Macaroni N41 500GM"
        },
        {
          "name": "Meadows通心粉 N41 500GM",
          "price": "$16",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231204/4b35cd3f-f5df-350a-83d5-438d845307b4",
          "product_eng_name": "Meadows Macaroni N41 500GM"
        }
      ],
      "name": "Meadows通心粉 N41 500GM",
      "price": "$16",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20231204/4b35cd3f-f5df-350a-83d5-438d845307b4",
      "product_eng_name": "Meadows Macaroni N41 500GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%96%9C%E9%81%94%E7%89%8C%20%E5%8E%9F%E5%91%B3%E6%92%88%E9%BA%B5%205%20X%2090GM/i/101350511.html",
      "uid": "0398de72eda5d087d319edeca84e05ec",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "喜達牌 原味撈麵 5 X 90GM",
          "price": "$24",
          "offer": "【2件$25.9】$25.9任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240829/5bd57c89-d705-3b40-9619-0cb325285081",
          "product_eng_name": "Sedaap Fried Noodles 5 X 90GM"
        },
        {
          "name": "喜達牌 原味撈麵 5 X 90GM",
          "price": "$24",
          "offer": "【2件$25.9】$25.9任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240829/5bd57c89-d705-3b40-9619-0cb325285081",
          "product_eng_name": "Sedaap Fried Noodles 5 X 90GM"
        }
      ],
      "name": "喜達牌 原味撈麵 5 X 90GM",
      "price": "$24",
      "offer": "【2件$25.9】$25.9任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240829/5bd57c89-d705-3b40-9619-0cb325285081",
      "product_eng_name": "Sedaap Fried Noodles 5 X 90GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%8E%96%E6%9F%92%E7%89%8C%E9%BE%8D%E5%8F%A3%E7%B2%89%E7%B5%B2%20227GM/i/101354178.html",
      "uid": "4f46c9ebe7115b17d84037996408dab2",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "玖柒牌龍口粉絲 227GM",
          "price": "$26",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210125/4de223b0-9879-4d34-a205-35604ea09f71",
          "product_eng_name": "Nine Seven Longkou Vermicelli 227GM"
        },
        {
          "name": "玖柒牌龍口粉絲 227GM",
          "price": "$26",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210125/4de223b0-9879-4d34-a205-35604ea09f71",
          "product_eng_name": "Nine Seven Longkou Vermicelli 227GM"
        }
      ],
      "name": "玖柒牌龍口粉絲 227GM",
      "price": "$26",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210125/4de223b0-9879-4d34-a205-35604ea09f71",
      "product_eng_name": "Nine Seven Longkou Vermicelli 227GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E7%B5%B1%E4%B8%80%E6%BB%BF%E6%BC%A2%E5%A4%A7%E9%A4%90%20%E9%BA%BB%E8%BE%A3%E7%89%9B%E8%82%89%E7%A2%97%E9%BA%B5%2012%20X%20204GM/i/113465654.html",
      "uid": "66e85121d7361c3efa114230d1bf8dc9",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱統一滿漢大餐 麻辣牛肉碗麵 12 X 204GM",
          "price": "$180",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230728/bb42d844-bbb5-32dc-aaff-2d81f483ee9b",
          "product_eng_name": "Imperial Big Meal Hot Pot Bowl Noodle Case 12 x 204GM"
        },
        {
          "name": "原箱統一滿漢大餐 麻辣牛肉碗麵 12 X 204GM",
          "price": "$180",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230728/bb42d844-bbb5-32dc-aaff-2d81f483ee9b",
          "product_eng_name": "Imperial Big Meal Hot Pot Bowl Noodle Case 12 x 204GM"
        }
      ],
      "name": "原箱統一滿漢大餐 麻辣牛肉碗麵 12 X 204GM",
      "price": "$180",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230728/bb42d844-bbb5-32dc-aaff-2d81f483ee9b",
      "product_eng_name": "Imperial Big Meal Hot Pot Bowl Noodle Case 12 x 204GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%B0%B8%E6%A8%82%E7%B2%89%E9%BA%B5%E5%BB%A0%E7%89%B9%E6%BF%83%E8%9D%A6%E5%AD%90%E9%BA%B5%2012PC/i/113323263.html",
      "uid": "2a03719463b12dfa328f8a26384c5f5c",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "永樂粉麵廠特濃蝦子麵 12PC",
          "price": "$90",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230411/c8109d3b-611a-4331-aaca-32a663d65342",
          "product_eng_name": "Wing Lok Shrimp Roe Noodle 12PC"
        },
        {
          "name": "永樂粉麵廠特濃蝦子麵 12PC",
          "price": "$90",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230411/c8109d3b-611a-4331-aaca-32a663d65342",
          "product_eng_name": "Wing Lok Shrimp Roe Noodle 12PC"
        }
      ],
      "name": "永樂粉麵廠特濃蝦子麵 12PC",
      "price": "$90",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230411/c8109d3b-611a-4331-aaca-32a663d65342",
      "product_eng_name": "Wing Lok Shrimp Roe Noodle 12PC"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E6%97%A5%E6%B8%85%E5%90%88%E5%91%B3%E9%81%93%20%E4%BA%94%E9%A6%99%E7%89%9B%E8%82%89%E6%9D%AF%E9%BA%B5%2024%20X%2075GM/i/101363779.html",
      "uid": "637aae473dee786e08ee377958f5afe4",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱日清合味道 五香牛肉杯麵 24 X 75GM",
          "price": "$170",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230202/086741e8-3b59-4c31-9be4-04e14a8ce838",
          "product_eng_name": "Nissin Beef Cup Noodle 24 X 75GM"
        },
        {
          "name": "原箱日清合味道 五香牛肉杯麵 24 X 75GM",
          "price": "$170",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230202/086741e8-3b59-4c31-9be4-04e14a8ce838",
          "product_eng_name": "Nissin Beef Cup Noodle 24 X 75GM"
        }
      ],
      "name": "原箱日清合味道 五香牛肉杯麵 24 X 75GM",
      "price": "$170",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230202/086741e8-3b59-4c31-9be4-04e14a8ce838",
      "product_eng_name": "Nissin Beef Cup Noodle 24 X 75GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E5%87%BA%E5%89%8D%E4%B8%80%E4%B8%81%E5%8C%97%E6%B5%B7%E9%81%93%20%E5%B0%8F%E9%BA%A5%E7%B2%89%E9%BB%91%E8%92%9C%E8%B1%AC%20500%20GM/i/113557474.html",
      "uid": "385bc0be35f3a3d9eedc621139901892",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱出前一丁北海道 小麥粉黑蒜豬 500 GM",
          "price": "$120",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231013/f2c133a6-083c-3e00-b06e-909d441f8328",
          "product_eng_name": "Nissin Demae Iccho Hokkaido Wheat Flour Black Garlic Oil Tonkotsu Noodles Case 30 x 100GM"
        },
        {
          "name": "原箱出前一丁北海道 小麥粉黑蒜豬 500 GM",
          "price": "$120",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231013/f2c133a6-083c-3e00-b06e-909d441f8328",
          "product_eng_name": "Nissin Demae Iccho Hokkaido Wheat Flour Black Garlic Oil Tonkotsu Noodles Case 30 x 100GM"
        }
      ],
      "name": "原箱出前一丁北海道 小麥粉黑蒜豬 500 GM",
      "price": "$120",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20231013/f2c133a6-083c-3e00-b06e-909d441f8328",
      "product_eng_name": "Nissin Demae Iccho Hokkaido Wheat Flour Black Garlic Oil Tonkotsu Noodles Case 30 x 100GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E9%98%BF%E6%9B%BC%E5%BA%A6%20%E6%84%8F%E5%A4%A7%E5%88%A9%E7%B2%891.7MM%20500GM/i/101322773.html",
      "uid": "168ab25784f19a46d9c6f0a22c5bc401",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "阿曼度 意大利粉1.7MM 500GM",
          "price": "$18",
          "offer": "【3件$50】$50任揀3件；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240529/495355b6-0cc3-3580-8756-879fba19896b",
          "product_eng_name": "Armando Spaghetti 1.7MM 500GM"
        },
        {
          "name": "阿曼度 意大利粉1.7MM 500GM",
          "price": "$18",
          "offer": "【3件$50】$50任揀3件；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240529/495355b6-0cc3-3580-8756-879fba19896b",
          "product_eng_name": "Armando Spaghetti 1.7MM 500GM"
        }
      ],
      "name": "阿曼度 意大利粉1.7MM 500GM",
      "price": "$18",
      "offer": "【3件$50】$50任揀3件；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240529/495355b6-0cc3-3580-8756-879fba19896b",
      "product_eng_name": "Armando Spaghetti 1.7MM 500GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/Meadows%E5%88%9D%E6%A6%A8%E6%A9%84%E6%AC%96%E6%B2%B9%201LT/i/101837277.html",
      "uid": "d7a5206a44fc215859b58e1a9abb3902",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "Meadows初榨橄欖油 1LT",
          "price": "$142",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231204/ff00c282-a754-307c-9e4c-fe243b9dbd5f",
          "product_eng_name": "Meadows Extra Virgin Olive Oil 1LT"
        },
        {
          "name": "Meadows初榨橄欖油 1LT",
          "price": "$142",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231204/ff00c282-a754-307c-9e4c-fe243b9dbd5f",
          "product_eng_name": "Meadows Extra Virgin Olive Oil 1LT"
        }
      ],
      "name": "Meadows初榨橄欖油 1LT",
      "price": "$142",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20231204/ff00c282-a754-307c-9e4c-fe243b9dbd5f",
      "product_eng_name": "Meadows Extra Virgin Olive Oil 1LT"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%A3%BD%E6%A1%83%E9%AE%91%E9%AD%9A%E9%9B%9E%E5%9B%9B%E5%B7%9D%E6%93%94%E6%93%94%E9%BA%B5%20160GM/i/101327040.html",
      "uid": "ff9e1238a4c29b0bb10f6b3920b54d30",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "壽桃鮑魚雞四川擔擔麵 160GM",
          "price": "$5",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220505/8cb0ef7b-5a77-476f-aa24-5be2010b5f76",
          "product_eng_name": "Sau Tao Abalone & Chicken Sichuan Spicy Noodle 160GM"
        },
        {
          "name": "壽桃鮑魚雞四川擔擔麵 160GM",
          "price": "$5",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220505/8cb0ef7b-5a77-476f-aa24-5be2010b5f76",
          "product_eng_name": "Sau Tao Abalone & Chicken Sichuan Spicy Noodle 160GM"
        }
      ],
      "name": "壽桃鮑魚雞四川擔擔麵 160GM",
      "price": "$5",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20220505/8cb0ef7b-5a77-476f-aa24-5be2010b5f76",
      "product_eng_name": "Sau Tao Abalone & Chicken Sichuan Spicy Noodle 160GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/SANUKIHONP%20%E8%AE%9A%E5%B2%90%E5%86%B7%E9%BA%B5%20500GM/i/101322701.html",
      "uid": "6c33f37578f851320a53c5b02cabfb06",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "SANUKIHONP 讚岐冷麵 500GM",
          "price": "$20",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240426/b99a7697-bbc4-3929-9168-02dfa932dd41",
          "product_eng_name": "Sanuki Honpo Sanuki Hiyamugi 500GM"
        },
        {
          "name": "SANUKIHONP 讚岐冷麵 500GM",
          "price": "$20",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240426/b99a7697-bbc4-3929-9168-02dfa932dd41",
          "product_eng_name": "Sanuki Honpo Sanuki Hiyamugi 500GM"
        }
      ],
      "name": "SANUKIHONP 讚岐冷麵 500GM",
      "price": "$20",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240426/b99a7697-bbc4-3929-9168-02dfa932dd41",
      "product_eng_name": "Sanuki Honpo Sanuki Hiyamugi 500GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E5%85%AC%E4%BB%94%20%E8%A0%94%E6%B2%B9%E6%B5%B7%E9%AE%AE%E7%82%92%E9%BA%B5%E7%8E%8B%2012%20X%20118GM/i/113294364.html",
      "uid": "8abe4cbe91fef4601c194c23993a795b",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱公仔 蠔油海鮮炒麵王 12 X 118GM",
          "price": "$78",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230209/0bce967e-8f33-4855-b958-064e11176653",
          "product_eng_name": "(無法擷取英文名稱)"
        },
        {
          "name": "原箱公仔 蠔油海鮮炒麵王 12 X 118GM",
          "price": "$78",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230209/0bce967e-8f33-4855-b958-064e11176653",
          "product_eng_name": "Doll Fried Noodle Oyster Case 12 x 118GM"
        }
      ],
      "name": "原箱公仔 蠔油海鮮炒麵王 12 X 118GM",
      "price": "$78",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230209/0bce967e-8f33-4855-b958-064e11176653",
      "product_eng_name": "Doll Fried Noodle Oyster Case 12 x 118GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%AA%BD%E5%92%AA%20%E8%83%A1%E6%A4%92%E6%B9%AF%E9%BA%B5%E7%89%B9%E6%83%A0%E8%A3%9D%2080GM/i/101333496.html",
      "uid": "31d1b444859259a7a7b1ece5e2368264",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "媽咪 胡椒湯麵特惠裝 80GM",
          "price": "$21",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240723/a9f34e83-67a5-31b2-b6b0-5edf011dc308",
          "product_eng_name": "Mamee Pepper Noodles Value Pack 80GM"
        },
        {
          "name": "媽咪 胡椒湯麵特惠裝 80GM",
          "price": "$21",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240723/a9f34e83-67a5-31b2-b6b0-5edf011dc308",
          "product_eng_name": "Mamee Pepper Noodles Value Pack 80GM"
        }
      ],
      "name": "媽咪 胡椒湯麵特惠裝 80GM",
      "price": "$21",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240723/a9f34e83-67a5-31b2-b6b0-5edf011dc308",
      "product_eng_name": "Mamee Pepper Noodles Value Pack 80GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%BE%A1%E5%93%81%E7%9A%87%20%E9%BB%83%E7%87%9C%E9%B7%84%E6%8B%8C%E9%BA%B5%20111GM/i/114331541.html",
      "uid": "a8070e9f0e8f75edab34e5e7539b79f9",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "御品皇 黃燜鷄拌麵 111GM",
          "price": "$8",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20241113/656963b3-75bf-39b8-bdda-5fe14eb278d7",
          "product_eng_name": "Yu Pin King Braised Chicken Flavour Dry-stirred Noodles 111G"
        },
        {
          "name": "御品皇 黃燜鷄拌麵 111GM",
          "price": "$8",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20241113/656963b3-75bf-39b8-bdda-5fe14eb278d7",
          "product_eng_name": "Yu Pin King Braised Chicken Flavour Dry-stirred Noodles 111G"
        }
      ],
      "name": "御品皇 黃燜鷄拌麵 111GM",
      "price": "$8",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20241113/656963b3-75bf-39b8-bdda-5fe14eb278d7",
      "product_eng_name": "Yu Pin King Braised Chicken Flavour Dry-stirred Noodles 111G"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E8%BE%B2%E5%BF%83%20%E8%96%AF%E4%BB%94%E9%BA%B5%20400%20GM/i/113559439.html",
      "uid": "32f3094bcfbf0164029852e08eb38cfe",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱農心 薯仔麵 400 GM",
          "price": "$240",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231013/729784bd-a8ae-34bb-ac75-799120c226ae",
          "product_eng_name": "Nong Shim Potato Noodles Case 48 x 100GM"
        },
        {
          "name": "原箱農心 薯仔麵 400 GM",
          "price": "$240",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231013/729784bd-a8ae-34bb-ac75-799120c226ae",
          "product_eng_name": "Nong Shim Potato Noodles Case 48 x 100GM"
        }
      ],
      "name": "原箱農心 薯仔麵 400 GM",
      "price": "$240",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20231013/729784bd-a8ae-34bb-ac75-799120c226ae",
      "product_eng_name": "Nong Shim Potato Noodles Case 48 x 100GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%AE%B6%E6%A8%82%E7%89%8C%E9%80%9A%E5%BF%83%E7%B2%895%E5%8C%85%E8%A3%9D%20(%E9%AE%91%E9%AD%9A%E9%9B%9E)%205%20x%2080GM/i/101336104.html",
      "uid": "3976e7b302594a53a1d016ec79540de5",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "家樂牌通心粉5包裝 (鮑魚雞) 5 x 80GM",
          "price": "$26",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20241115/667209a1-f56f-362d-a664-5b4661f1c6a6",
          "product_eng_name": "Knorr Quick Serve Macaroni Abalone & Chicken Flavour 5 x 80GM"
        },
        {
          "name": "家樂牌通心粉5包裝 (鮑魚雞) 5 x 80GM",
          "price": "$26",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20241115/667209a1-f56f-362d-a664-5b4661f1c6a6",
          "product_eng_name": "Knorr Quick Serve Macaroni Abalone & Chicken Flavour 5 x 80GM"
        }
      ],
      "name": "家樂牌通心粉5包裝 (鮑魚雞) 5 x 80GM",
      "price": "$26",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20241115/667209a1-f56f-362d-a664-5b4661f1c6a6",
      "product_eng_name": "Knorr Quick Serve Macaroni Abalone & Chicken Flavour 5 x 80GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%A5%BD%E6%AD%A1%E8%9E%BA%20%E5%8A%A0%E8%BE%A3%E7%89%88%E6%9F%B3%E5%B7%9E%E8%9E%BA%E8%9E%84%E7%B2%89%20380GM/i/102692751.html",
      "uid": "9b6f064d076e2835691f4985a6804ef8",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "好歡螺 加辣版柳州螺螄粉 380GM",
          "price": "$17",
          "offer": "【3件$50】$50任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20241014/17186d0b-a552-3ec8-9b7e-b79d3c8b4fba",
          "product_eng_name": "HAO HUAN LUO SNAIL RICE NOODLES SPICY PLUS 380GM"
        },
        {
          "name": "好歡螺 加辣版柳州螺螄粉 380GM",
          "price": "$17",
          "offer": "【3件$50】$50任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20241014/17186d0b-a552-3ec8-9b7e-b79d3c8b4fba",
          "product_eng_name": "HAO HUAN LUO SNAIL RICE NOODLES SPICY PLUS 380GM"
        }
      ],
      "name": "好歡螺 加辣版柳州螺螄粉 380GM",
      "price": "$17",
      "offer": "【3件$50】$50任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20241014/17186d0b-a552-3ec8-9b7e-b79d3c8b4fba",
      "product_eng_name": "HAO HUAN LUO SNAIL RICE NOODLES SPICY PLUS 380GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%9D%8E%E9%8C%A6%E8%A8%98%E6%A4%92%E9%BA%BB%E6%8B%8C%E9%BA%B5%20110GM/i/113249224.html",
      "uid": "7b8eb4e43f1919d243307dd93dd1b973",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "李錦記椒麻拌麵 110GM",
          "price": "$8",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20241227/2ace65a5-8ce5-317a-843d-bf3071ba3266",
          "product_eng_name": "Lee Kum Kee Noodle With Pepper Corn Oil 110GM"
        },
        {
          "name": "李錦記椒麻拌麵 110GM",
          "price": "$8",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20241227/2ace65a5-8ce5-317a-843d-bf3071ba3266",
          "product_eng_name": "Lee Kum Kee Noodle With Pepper Corn Oil 110GM"
        }
      ],
      "name": "李錦記椒麻拌麵 110GM",
      "price": "$8",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20241227/2ace65a5-8ce5-317a-843d-bf3071ba3266",
      "product_eng_name": "Lee Kum Kee Noodle With Pepper Corn Oil 110GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E8%A2%8B%E9%BC%A0%E7%89%8C%E7%B2%BE%E9%81%B8%E7%B5%B2%E8%8B%97%205KG/i/101348095.html",
      "uid": "508a98c4bcebd7a5f1bf90394d4ea368",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "袋鼠牌精選絲苗 5KG",
          "price": "$66",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230726/4da940c1-3ddb-48c2-b973-23dfd94830e3",
          "product_eng_name": "Kangaroo Seemew Rice 5KG"
        }
      ],
      "name": "袋鼠牌精選絲苗 5KG",
      "price": "$66",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230726/4da940c1-3ddb-48c2-b973-23dfd94830e3",
      "product_eng_name": "Kangaroo Seemew Rice 5KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%BE%A1%E5%93%81%E7%9A%87%E7%B3%AF%E7%B1%B3%202KG/i/101572860.html",
      "uid": "a6485433faaed586960314c5143bcdf7",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "御品皇糯米 2KG",
          "price": "$55",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250306/a2437522-48ab-3db6-aa9f-b959423a2ac4",
          "product_eng_name": "Yu Pin King Glutinous Rice 2KG"
        }
      ],
      "name": "御品皇糯米 2KG",
      "price": "$55",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250306/a2437522-48ab-3db6-aa9f-b959423a2ac4",
      "product_eng_name": "Yu Pin King Glutinous Rice 2KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%99%BE%E5%BE%97%E9%98%BF%E5%A7%A8%E7%9B%B4%E9%80%9A%E7%B2%89%20500GM/i/101326066.html",
      "uid": "9d7b93a00da8ee688d6f206d620f0b1c",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "百得阿姨直通粉 500GM",
          "price": "$22",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210222/91c80d21-73a8-4277-9950-d39e521c2132",
          "product_eng_name": "Barilla Penne Rigate 500GM"
        },
        {
          "name": "百得阿姨直通粉 500GM",
          "price": "$22",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210222/91c80d21-73a8-4277-9950-d39e521c2132",
          "product_eng_name": "Barilla Penne Rigate 500GM"
        }
      ],
      "name": "百得阿姨直通粉 500GM",
      "price": "$22",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210222/91c80d21-73a8-4277-9950-d39e521c2132",
      "product_eng_name": "Barilla Penne Rigate 500GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%A3%BD%E6%A1%83%E5%AF%AC%E8%9D%A6%E5%AD%90%E9%BA%B5%20454GM/i/101342537.html",
      "uid": "a84daee692634f21f5f3c551c9e6e533",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "壽桃寬蝦子麵 454GM",
          "price": "$14",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220505/a56d2570-506c-48fe-9805-d3ef450c13ad",
          "product_eng_name": "Sau Tao Flat Shrimp Noodle 454GM"
        },
        {
          "name": "壽桃寬蝦子麵 454GM",
          "price": "$14",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220505/a56d2570-506c-48fe-9805-d3ef450c13ad",
          "product_eng_name": "Sau Tao Flat Shrimp Noodle 454GM"
        }
      ],
      "name": "壽桃寬蝦子麵 454GM",
      "price": "$14",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20220505/a56d2570-506c-48fe-9805-d3ef450c13ad",
      "product_eng_name": "Sau Tao Flat Shrimp Noodle 454GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%87%BA%E5%89%8D%E4%B8%80%E4%B8%81%20%E5%B0%8F%E9%BA%A5%E7%B2%89%E9%9B%9E%E7%99%BD%E6%B9%AF%E9%BA%B5%205%20X%20100GM/i/101352464.html",
      "uid": "cb2458235333b9bcc575b42e7e247ceb",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "出前一丁 小麥粉雞白湯麵 5 X 100GM",
          "price": "$21",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230905/1ee4001b-4345-36ed-a07f-9f8904b736a6",
          "product_eng_name": "Nissin Demae Iccho Hokkaido Wheat Flour Tori Paitan 5 X 100GM"
        },
        {
          "name": "出前一丁 小麥粉雞白湯麵 5 X 100GM",
          "price": "$21",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230905/1ee4001b-4345-36ed-a07f-9f8904b736a6",
          "product_eng_name": "Nissin Demae Iccho Hokkaido Wheat Flour Tori Paitan 5 X 100GM"
        }
      ],
      "name": "出前一丁 小麥粉雞白湯麵 5 X 100GM",
      "price": "$21",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230905/1ee4001b-4345-36ed-a07f-9f8904b736a6",
      "product_eng_name": "Nissin Demae Iccho Hokkaido Wheat Flour Tori Paitan 5 X 100GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%85%AC%E4%BB%94%E9%BA%BB%E6%B2%B9%E5%8D%B3%E9%A3%9F%E9%BA%B5%205%20X%20100GM/i/101352820.html",
      "uid": "825e79d3b4737dc4d9f96d4e2a991e73",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "公仔麻油即食麵 5 X 100GM",
          "price": "$18",
          "offer": "【2件$28】$28任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231011/8daa2e01-48d4-3e55-9662-042f07f49073",
          "product_eng_name": "Doll Sesame Oil Noodles 5 X 100GM"
        },
        {
          "name": "公仔麻油即食麵 5 X 100GM",
          "price": "$18",
          "offer": "【2件$28】$28任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231011/8daa2e01-48d4-3e55-9662-042f07f49073",
          "product_eng_name": "Doll Sesame Oil Noodles 5 X 100GM"
        }
      ],
      "name": "公仔麻油即食麵 5 X 100GM",
      "price": "$18",
      "offer": "【2件$28】$28任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20231011/8daa2e01-48d4-3e55-9662-042f07f49073",
      "product_eng_name": "Doll Sesame Oil Noodles 5 X 100GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%99%BE%E7%9B%8A%E7%B4%94%E6%A9%84%E6%AC%96%E6%B2%B9%201.5LT/i/113318658.html",
      "uid": "2a892dcaa3bed083e07c385665407263",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "百益純橄欖油 1.5LT",
          "price": "$229",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240930/d6082244-7ba9-3e02-b90a-660e565c423d",
          "product_eng_name": "Filippo Berio Pure Olive Oil 1.5LT"
        },
        {
          "name": "百益純橄欖油 1.5LT",
          "price": "$229",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240930/d6082244-7ba9-3e02-b90a-660e565c423d",
          "product_eng_name": "Filippo Berio Pure Olive Oil 1.5LT"
        }
      ],
      "name": "百益純橄欖油 1.5LT",
      "price": "$229",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240930/d6082244-7ba9-3e02-b90a-660e565c423d",
      "product_eng_name": "Filippo Berio Pure Olive Oil 1.5LT"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E4%B8%89%E9%A4%8A%E9%A6%99%E8%BE%A3%E9%9B%9E%E8%82%89%E5%91%B3%E7%A2%97%E9%BA%B5%20105GM/i/101346259.html",
      "uid": "3c9af533db381215f61378864962b0cd",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "三養香辣雞肉味碗麵 105GM",
          "price": "$11",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220614/899d8480-5d1b-4e52-af76-b4b2fd4bd5ea",
          "product_eng_name": "Samyang Hot Chicken Bowl 105GM"
        },
        {
          "name": "三養香辣雞肉味碗麵 105GM",
          "price": "$11",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220614/899d8480-5d1b-4e52-af76-b4b2fd4bd5ea",
          "product_eng_name": "Samyang Hot Chicken Bowl 105GM"
        }
      ],
      "name": "三養香辣雞肉味碗麵 105GM",
      "price": "$11",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20220614/899d8480-5d1b-4e52-af76-b4b2fd4bd5ea",
      "product_eng_name": "Samyang Hot Chicken Bowl 105GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%85%AC%E4%BB%94%E9%9B%9E%E8%93%89%E5%8D%B3%E9%A3%9F%E9%BA%B55%E5%8C%85%E8%A3%9D%205%20X%20103GM/i/101352821.html",
      "uid": "9c3e035d6bd252ebf4fcb32423e44191",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "公仔雞蓉即食麵5包裝 5 X 103GM",
          "price": "$12",
          "offer": "【2件$28】$28任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231011/7e7b3c63-fd61-31d3-a4ce-b841bf93b524",
          "product_eng_name": "Doll Chicken Noodle 5 X 103GM"
        },
        {
          "name": "公仔雞蓉即食麵5包裝 5 X 103GM",
          "price": "$12",
          "offer": "【2件$28】$28任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231011/7e7b3c63-fd61-31d3-a4ce-b841bf93b524",
          "product_eng_name": "(無法擷取英文名稱)"
        }
      ],
      "name": "公仔雞蓉即食麵5包裝 5 X 103GM",
      "price": "$12",
      "offer": "【2件$28】$28任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20231011/7e7b3c63-fd61-31d3-a4ce-b841bf93b524",
      "product_eng_name": "(無法擷取英文名稱)"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%9D%8E%E9%8C%A6%E8%A8%98%E8%8A%9D%E9%BA%BB%E6%B2%B9%20207ML/i/101341563.html",
      "uid": "fd61f9c173e53fc92bf1bb90bb429f02",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "李錦記芝麻油 207ML",
          "price": "$18",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240509/66f8a59f-df66-398c-9bef-3ffd7198c6f2",
          "product_eng_name": "Lee Kum Kee Sesame Oil 207ML"
        },
        {
          "name": "李錦記芝麻油 207ML",
          "price": "$18",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240509/66f8a59f-df66-398c-9bef-3ffd7198c6f2",
          "product_eng_name": "Lee Kum Kee Sesame Oil 207ML"
        }
      ],
      "name": "李錦記芝麻油 207ML",
      "price": "$18",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240509/66f8a59f-df66-398c-9bef-3ffd7198c6f2",
      "product_eng_name": "Lee Kum Kee Sesame Oil 207ML"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E5%85%AC%E4%BB%94%20%E9%BA%BB%E6%B2%B9%E5%8D%B3%E9%A3%9F%E9%BA%B5%20100%20GM/i/101342355.html",
      "uid": "79361f82915ef315beb2713ce8427be6",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱公仔 麻油即食麵 100 GM",
          "price": "$80",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231013/e6b84e56-6740-3a0f-91d1-b13b05e3e1c0",
          "product_eng_name": "Doll Sesame Oil Noodle Case 30 x 100GM"
        },
        {
          "name": "原箱公仔 麻油即食麵 100 GM",
          "price": "$80",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231013/e6b84e56-6740-3a0f-91d1-b13b05e3e1c0",
          "product_eng_name": "Doll Sesame Oil Noodle Case 30 x 100GM"
        }
      ],
      "name": "原箱公仔 麻油即食麵 100 GM",
      "price": "$80",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20231013/e6b84e56-6740-3a0f-91d1-b13b05e3e1c0",
      "product_eng_name": "Doll Sesame Oil Noodle Case 30 x 100GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%A3%BD%E6%A1%83%E7%94%9F%E9%BA%B5%E7%9A%87%E9%AE%91%E9%AD%9A%E9%9B%9E%E6%B9%AF%E5%91%B3%E7%A2%97%E9%BA%B5%2082GM/i/101344142.html",
      "uid": "f5e2a8f5224d2c1bbfefda884d80c6bd",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "壽桃生麵皇鮑魚雞湯味碗麵 82GM",
          "price": "$6",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220505/fb6e3be2-9dc2-47cb-beb8-62cf632607e3",
          "product_eng_name": "Sau Tao Noodle King Abalone Chicken Bowl Noodle 82GM"
        },
        {
          "name": "壽桃生麵皇鮑魚雞湯味碗麵 82GM",
          "price": "$6",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220505/fb6e3be2-9dc2-47cb-beb8-62cf632607e3",
          "product_eng_name": "Sau Tao Noodle King Abalone Chicken Bowl Noodle 82GM"
        }
      ],
      "name": "壽桃生麵皇鮑魚雞湯味碗麵 82GM",
      "price": "$6",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20220505/fb6e3be2-9dc2-47cb-beb8-62cf632607e3",
      "product_eng_name": "Sau Tao Noodle King Abalone Chicken Bowl Noodle 82GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%BE%8E%E5%91%B3%E6%A3%A7%E7%B4%94%E6%AD%A3%E9%A6%99%E9%BA%BB%E6%B2%B9%20150ML/i/101329685.html",
      "uid": "493649f3cc8e5c1b2ed5f2afd38b08c9",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "美味棧純正香麻油 150ML",
          "price": "$25",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210527/09eae9e2-d0b5-49e7-adb2-c8d6b7abf261",
          "product_eng_name": "Yummy House Pure Sesame Oil 150ML"
        },
        {
          "name": "美味棧純正香麻油 150ML",
          "price": "$25",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210527/09eae9e2-d0b5-49e7-adb2-c8d6b7abf261",
          "product_eng_name": "Yummy House Pure Sesame Oil 150ML"
        }
      ],
      "name": "美味棧純正香麻油 150ML",
      "price": "$25",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210527/09eae9e2-d0b5-49e7-adb2-c8d6b7abf261",
      "product_eng_name": "Yummy House Pure Sesame Oil 150ML"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E4%B8%8D%E5%80%92%E7%BF%81%E8%8A%9D%E9%BA%BB%E6%B2%B9%20110ML/i/101382401.html",
      "uid": "aebd28be43e675563d1199bc77ece765",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "不倒翁芝麻油 110ML",
          "price": "$50",
          "offer": "【2件$60】$60任揀2件；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20201105/a9392fe7-600f-47c0-b1ce-e602d4e7ccde",
          "product_eng_name": "Ottogi Sesame Oil 110ML"
        },
        {
          "name": "不倒翁芝麻油 110ML",
          "price": "$50",
          "offer": "【2件$60】$60任揀2件；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20201105/a9392fe7-600f-47c0-b1ce-e602d4e7ccde",
          "product_eng_name": "Ottogi Sesame Oil 110ML"
        }
      ],
      "name": "不倒翁芝麻油 110ML",
      "price": "$50",
      "offer": "【2件$60】$60任揀2件；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20201105/a9392fe7-600f-47c0-b1ce-e602d4e7ccde",
      "product_eng_name": "Ottogi Sesame Oil 110ML"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%AE%B6%E6%A8%82%E7%89%8C%E9%AE%AE%E5%8C%97%E8%8F%87%E5%BF%AB%E7%86%9F%E9%80%9A%E5%BF%83%E7%B2%89%2080GM/i/101356767.html",
      "uid": "c4aafadf5ef2c1838a5147508bb97dc0",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "家樂牌鮮北菇快熟通心粉 80GM",
          "price": "$7",
          "offer": "【3件$17】$17任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220705/5958abef-5063-476f-8368-0c3cd7ee6ed2",
          "product_eng_name": "Knorr Mushroom Macaroni 80GM"
        },
        {
          "name": "家樂牌鮮北菇快熟通心粉 80GM",
          "price": "$7",
          "offer": "【3件$17】$17任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220705/5958abef-5063-476f-8368-0c3cd7ee6ed2",
          "product_eng_name": "Knorr Mushroom Macaroni 80GM"
        }
      ],
      "name": "家樂牌鮮北菇快熟通心粉 80GM",
      "price": "$7",
      "offer": "【3件$17】$17任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20220705/5958abef-5063-476f-8368-0c3cd7ee6ed2",
      "product_eng_name": "Knorr Mushroom Macaroni 80GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%A3%BD%E6%A1%83%E7%89%8C%E5%B9%BC%E6%BB%91%E9%AE%AE%E7%B1%B3%E7%B7%9A%203%20X%20200GM/i/101328520.html",
      "uid": "d02c56e7513a6c1f0d94d69e31292e24",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "壽桃牌幼滑鮮米線 3 X 200GM",
          "price": "$10",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220505/641fa818-7977-4275-9b69-d77bbdf610fa",
          "product_eng_name": "Sau Tao Rice Vermicelli 3 X 200GM"
        },
        {
          "name": "壽桃牌幼滑鮮米線 3 X 200GM",
          "price": "$10",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220505/641fa818-7977-4275-9b69-d77bbdf610fa",
          "product_eng_name": "Sau Tao Rice Vermicelli 3 X 200GM"
        }
      ],
      "name": "壽桃牌幼滑鮮米線 3 X 200GM",
      "price": "$10",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20220505/641fa818-7977-4275-9b69-d77bbdf610fa",
      "product_eng_name": "Sau Tao Rice Vermicelli 3 X 200GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%A3%BD%E6%A1%83%E8%95%8E%E9%BA%A5%E9%BA%B512%E5%80%8B%E6%89%8B%E6%8F%90%E7%AE%B1%E8%A3%9D/i/101380335.html",
      "uid": "e9a2fe6f9a656f8393e9cc97a1e9668d",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "壽桃蕎麥麵12個手提箱裝",
          "price": "$23",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240904/9de9bec1-01b7-38fb-aeb2-39f1bf3086b0",
          "product_eng_name": "Buckwheat Noodle"
        },
        {
          "name": "壽桃蕎麥麵12個手提箱裝",
          "price": "$23",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240904/9de9bec1-01b7-38fb-aeb2-39f1bf3086b0",
          "product_eng_name": "Buckwheat Noodle"
        }
      ],
      "name": "壽桃蕎麥麵12個手提箱裝",
      "price": "$23",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240904/9de9bec1-01b7-38fb-aeb2-39f1bf3086b0",
      "product_eng_name": "Buckwheat Noodle"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%BE%A1%E5%93%81%E7%9A%87%E5%81%A5%E5%BA%B7%E4%B8%89%E8%89%B2%E7%B1%B3%205KG/i/101572857.html",
      "uid": "02d1622cb234d45d4ebaf85b4ab0cf59",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "御品皇健康三色米 5KG",
          "price": "$76",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250306/69f547ac-d6da-3087-a698-418463d23f2d",
          "product_eng_name": "Yu Pin King Healthy Mixed Rice 5KG"
        }
      ],
      "name": "御品皇健康三色米 5KG",
      "price": "$76",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250306/69f547ac-d6da-3087-a698-418463d23f2d",
      "product_eng_name": "Yu Pin King Healthy Mixed Rice 5KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E4%B8%8D%E5%80%92%E7%BF%81%E8%8A%9D%E5%A3%AB%E6%8B%89%E9%BA%B5%204%20X%20111GM/i/101349351.html",
      "uid": "c915a1360dc339d856ba689e0c80957b",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "不倒翁芝士拉麵 4 X 111GM",
          "price": "$42",
          "offer": "【2件$48】$48任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240729/ddcae77d-a611-39b3-9f89-3fa86f17cf17",
          "product_eng_name": "Ottogi Cheese Ramen 4 X 111GM"
        },
        {
          "name": "不倒翁芝士拉麵 4 X 111GM",
          "price": "$42",
          "offer": "【2件$48】$48任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240729/ddcae77d-a611-39b3-9f89-3fa86f17cf17",
          "product_eng_name": "Ottogi Cheese Ramen 4 X 111GM"
        }
      ],
      "name": "不倒翁芝士拉麵 4 X 111GM",
      "price": "$42",
      "offer": "【2件$48】$48任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240729/ddcae77d-a611-39b3-9f89-3fa86f17cf17",
      "product_eng_name": "Ottogi Cheese Ramen 4 X 111GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E7%A6%8F%E5%AD%97%20%E9%9B%9E%E6%B1%81%E4%BC%8A%E9%BA%B5%20%2030%20X%2065GM/i/101334409.html",
      "uid": "468917bf339e81e5e5f7fd11c9609b70",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱福字 雞汁伊麵 30 X 65GM",
          "price": "$57",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231013/337d6c29-3628-3894-a738-511b7a4207a3",
          "product_eng_name": "Fuku Chicken Noodle Case 30 x 65GM"
        },
        {
          "name": "原箱福字 雞汁伊麵 30 X 65GM",
          "price": "$57",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231013/337d6c29-3628-3894-a738-511b7a4207a3",
          "product_eng_name": "Fuku Chicken Noodle Case 30 x 65GM"
        }
      ],
      "name": "原箱福字 雞汁伊麵 30 X 65GM",
      "price": "$57",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20231013/337d6c29-3628-3894-a738-511b7a4207a3",
      "product_eng_name": "Fuku Chicken Noodle Case 30 x 65GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%85%AC%E4%BB%94%E6%B2%99%E7%88%B9%E7%89%9B%E8%82%89%E7%A2%97%E9%BA%B5%20120GM/i/101343740.html",
      "uid": "a15a8d459656f41263aef3a6406abab9",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "公仔沙爹牛肉碗麵 120GM",
          "price": "$7",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250320/dfcb8fb4-4e6d-3d68-8d1a-f55ed99b2400",
          "product_eng_name": "Doll Satay Beef Bowl Noodle 120GM"
        },
        {
          "name": "公仔沙爹牛肉碗麵 120GM",
          "price": "$7",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250320/dfcb8fb4-4e6d-3d68-8d1a-f55ed99b2400",
          "product_eng_name": "Doll Satay Beef Bowl Noodle 120GM"
        }
      ],
      "name": "公仔沙爹牛肉碗麵 120GM",
      "price": "$7",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250320/dfcb8fb4-4e6d-3d68-8d1a-f55ed99b2400",
      "product_eng_name": "Doll Satay Beef Bowl Noodle 120GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%A5%A7%E5%B0%BC%E7%89%8C%E8%91%A1%E8%90%84%E7%B1%BD%E6%B2%B9%201%E5%85%AC%E5%8D%87/i/101348496.html",
      "uid": "a338e4d09955d41e2450a9d117c4540f",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "奧尼牌葡萄籽油 1公升",
          "price": "$107",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20241227/a5ad319e-b9bb-36e1-acec-1ab129b07b0d",
          "product_eng_name": "Olitalia Grape Seed Oil 1L"
        },
        {
          "name": "奧尼牌葡萄籽油 1公升",
          "price": "$107",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20241227/a5ad319e-b9bb-36e1-acec-1ab129b07b0d",
          "product_eng_name": "Olitalia Grape Seed Oil 1L"
        }
      ],
      "name": "奧尼牌葡萄籽油 1公升",
      "price": "$107",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20241227/a5ad319e-b9bb-36e1-acec-1ab129b07b0d",
      "product_eng_name": "Olitalia Grape Seed Oil 1L"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/ACE%20%E6%92%AD%E6%B4%B2%E8%95%8E%E9%BA%A5%E9%BA%B5%20400%20GM/i/101343680.html",
      "uid": "7e3705e3fae7cddd3266d1b5472e527a",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "ACE 播洲蕎麥麵 400 GM",
          "price": "$26",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230508/10cc4bc0-c774-449a-a2c5-26529c45b854",
          "product_eng_name": "ACE Banshu Style Soba 400GM"
        },
        {
          "name": "ACE 播洲蕎麥麵 400 GM",
          "price": "$26",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230508/10cc4bc0-c774-449a-a2c5-26529c45b854",
          "product_eng_name": "ACE Banshu Style Soba 400GM"
        }
      ],
      "name": "ACE 播洲蕎麥麵 400 GM",
      "price": "$26",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230508/10cc4bc0-c774-449a-a2c5-26529c45b854",
      "product_eng_name": "ACE Banshu Style Soba 400GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%97%A5%E6%9C%AC%E7%B4%A0%E9%BA%B5%20600GM/i/101359742.html",
      "uid": "c8b088f6ab46b11f21f1ed95aba5a34a",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "日本素麵 600GM",
          "price": "$15",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240916/5f1d1f4a-7b06-3d13-93e3-0356340de585",
          "product_eng_name": "Yoshiya Hyande Somen Noodle 600GM"
        },
        {
          "name": "日本素麵 600GM",
          "price": "$15",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240916/5f1d1f4a-7b06-3d13-93e3-0356340de585",
          "product_eng_name": "Yoshiya Hyande Somen Noodle 600GM"
        }
      ],
      "name": "日本素麵 600GM",
      "price": "$15",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240916/5f1d1f4a-7b06-3d13-93e3-0356340de585",
      "product_eng_name": "Yoshiya Hyande Somen Noodle 600GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%B3%B6%E5%8E%9F%E6%97%A5%E6%9C%AC%E6%89%8B%E5%BB%B6%E5%B3%B6%E5%8E%9F%E7%B4%A0%E9%BA%B5%20250GM/i/101842007.html",
      "uid": "e8505a791635490e3c128ff55af7e080",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "島原日本手延島原素麵 250GM",
          "price": "$10",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250203/fd233d71-206f-3ca2-bd40-a399787d5d05",
          "product_eng_name": "Shimabara Tenobe Somen 250GM"
        },
        {
          "name": "島原日本手延島原素麵 250GM",
          "price": "$10",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250203/fd233d71-206f-3ca2-bd40-a399787d5d05",
          "product_eng_name": "Shimabara Tenobe Somen 250GM"
        }
      ],
      "name": "島原日本手延島原素麵 250GM",
      "price": "$10",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250203/fd233d71-206f-3ca2-bd40-a399787d5d05",
      "product_eng_name": "Shimabara Tenobe Somen 250GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%97%A5%E6%B8%85%E5%87%BA%E5%89%8D%E4%B8%80%E4%B8%81%E9%BA%BB%E6%B2%B9%E5%8D%B3%E9%A3%9F%E9%BA%B5%20100GM/i/101322566.html",
      "uid": "5d2ea5793c3cddc8dba5ddb6eebb8b0e",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "日清出前一丁麻油即食麵 100GM",
          "price": "$5",
          "offer": "【8件$28.5】$28.5任揀8件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250407/15c0a8b1-6ffb-3456-bb5a-f0cba7e852b9",
          "product_eng_name": "Nissin Demae Iccho Sesame Oil Noodle 100GM"
        },
        {
          "name": "日清出前一丁麻油即食麵 100GM",
          "price": "$5",
          "offer": "【8件$28.5】$28.5任揀8件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250407/15c0a8b1-6ffb-3456-bb5a-f0cba7e852b9",
          "product_eng_name": "Nissin Demae Iccho Sesame Oil Noodle 100GM"
        }
      ],
      "name": "日清出前一丁麻油即食麵 100GM",
      "price": "$5",
      "offer": "【8件$28.5】$28.5任揀8件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250407/15c0a8b1-6ffb-3456-bb5a-f0cba7e852b9",
      "product_eng_name": "Nissin Demae Iccho Sesame Oil Noodle 100GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%9D%8E%E9%8C%A6%E8%A8%98%E8%94%A5%E6%B2%B9%E6%8B%8C%E9%BA%B5%20110GM/i/113249229.html",
      "uid": "0da7aa51ec914603c7f2693fe5a4af33",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "李錦記蔥油拌麵 110GM",
          "price": "$8",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20241227/99c7699e-f006-35db-b3fd-d1691e0180ff",
          "product_eng_name": "Lee Kum Kee Noodles With Shallot Oil 110GM"
        },
        {
          "name": "李錦記蔥油拌麵 110GM",
          "price": "$8",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20241227/99c7699e-f006-35db-b3fd-d1691e0180ff",
          "product_eng_name": "Lee Kum Kee Noodles With Shallot Oil 110GM"
        }
      ],
      "name": "李錦記蔥油拌麵 110GM",
      "price": "$8",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20241227/99c7699e-f006-35db-b3fd-d1691e0180ff",
      "product_eng_name": "Lee Kum Kee Noodles With Shallot Oil 110GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%9D%8E%E9%8C%A6%E8%A8%98%E6%93%94%E6%93%94%E6%B9%AF%E9%BA%B5%20210GM/i/113249234.html",
      "uid": "e4435971e80bc2c5e6ee48d07ea56ae3",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "李錦記擔擔湯麵 210GM",
          "price": "$8",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20241227/c84b87fe-cabe-362b-93ba-7bea279a7626",
          "product_eng_name": "Lee Kum Kee Noodles In Dan Dan Soup 210GM"
        },
        {
          "name": "李錦記擔擔湯麵 210GM",
          "price": "$8",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20241227/c84b87fe-cabe-362b-93ba-7bea279a7626",
          "product_eng_name": "Lee Kum Kee Noodles In Dan Dan Soup 210GM"
        }
      ],
      "name": "李錦記擔擔湯麵 210GM",
      "price": "$8",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20241227/c84b87fe-cabe-362b-93ba-7bea279a7626",
      "product_eng_name": "Lee Kum Kee Noodles In Dan Dan Soup 210GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%A3%BD%E6%A1%83%E5%88%80%E5%89%8A%E9%BA%B5%203%20X%20200GM/i/101332364.html",
      "uid": "c541ebfa1a5e433967a89514b8ed6522",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "壽桃刀削麵 3 X 200GM",
          "price": "$9",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220505/f0e62b12-0d76-438b-8973-1f40443bcaef",
          "product_eng_name": "Sau Tao Sliced Noodle 3 X 200GM"
        },
        {
          "name": "壽桃刀削麵 3 X 200GM",
          "price": "$9",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220505/f0e62b12-0d76-438b-8973-1f40443bcaef",
          "product_eng_name": "Sau Tao Sliced Noodle 3 X 200GM"
        }
      ],
      "name": "壽桃刀削麵 3 X 200GM",
      "price": "$9",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20220505/f0e62b12-0d76-438b-8973-1f40443bcaef",
      "product_eng_name": "Sau Tao Sliced Noodle 3 X 200GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%85%AC%E4%BB%94%E9%9B%AA%E8%8F%9C%E8%82%89%E7%B5%B2%E7%A2%97%E7%B1%B3%E7%B2%89%2077GM/i/101333806.html",
      "uid": "b730e5f848c744eaa2b6c2be40feab81",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "公仔雪菜肉絲碗米粉 77GM",
          "price": "$6",
          "offer": "【2件$9.5】$9.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250320/c78a1bd2-8aaa-37c8-aa2c-6fc4358dac9c",
          "product_eng_name": "Doll Pickled Vegetable Pork Flavour Instant Mifun 77GM"
        },
        {
          "name": "公仔雪菜肉絲碗米粉 77GM",
          "price": "$6",
          "offer": "【2件$9.5】$9.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250320/c78a1bd2-8aaa-37c8-aa2c-6fc4358dac9c",
          "product_eng_name": "Doll Pickled Vegetable Pork Flavour Instant Mifun 77GM"
        }
      ],
      "name": "公仔雪菜肉絲碗米粉 77GM",
      "price": "$6",
      "offer": "【2件$9.5】$9.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250320/c78a1bd2-8aaa-37c8-aa2c-6fc4358dac9c",
      "product_eng_name": "Doll Pickled Vegetable Pork Flavour Instant Mifun 77GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/La%20Molisana%E6%84%8F%E5%A4%A7%E5%88%A9%E7%B2%89%2315%20%20500GM/i/101381094.html",
      "uid": "517d5d6d20d5b566eb2b5cda7952c3ca",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "La Molisana意大利粉#15 500GM",
          "price": "$23",
          "offer": "【2件$30】$30任揀2件；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230714/4a025ae9-275a-4616-ac59-88eb0a3ae108",
          "product_eng_name": "La Molisana Spaghetti #15 500GM"
        },
        {
          "name": "La Molisana意大利粉#15 500GM",
          "price": "$23",
          "offer": "【2件$30】$30任揀2件；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230714/4a025ae9-275a-4616-ac59-88eb0a3ae108",
          "product_eng_name": "La Molisana Spaghetti #15 500GM"
        }
      ],
      "name": "La Molisana意大利粉#15 500GM",
      "price": "$23",
      "offer": "【2件$30】$30任揀2件；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230714/4a025ae9-275a-4616-ac59-88eb0a3ae108",
      "product_eng_name": "La Molisana Spaghetti #15 500GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%B2%A9%E7%94%B0%E8%A3%BD%E9%BA%B5%E6%89%80%20%E7%84%A1%E9%B9%BD%E8%A3%BD%E9%BA%B5%E7%83%8F%E5%86%AC%20250%20GM/i/114215801.html",
      "uid": "e4c1f980f418a772ca2524da121bd346",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "岩田製麵所 無鹽製麵烏冬 250 GM",
          "price": "$18",
          "offer": "【4件$50】$50任揀4件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240429/f2054cef-091c-3f67-8ae0-3995b0f223ad",
          "product_eng_name": "Aoi Foods Muenseiho Udon 250GM"
        },
        {
          "name": "岩田製麵所 無鹽製麵烏冬 250 GM",
          "price": "$18",
          "offer": "【4件$50】$50任揀4件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240429/f2054cef-091c-3f67-8ae0-3995b0f223ad",
          "product_eng_name": "Aoi Foods Muenseiho Udon 250GM"
        }
      ],
      "name": "岩田製麵所 無鹽製麵烏冬 250 GM",
      "price": "$18",
      "offer": "【4件$50】$50任揀4件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240429/f2054cef-091c-3f67-8ae0-3995b0f223ad",
      "product_eng_name": "Aoi Foods Muenseiho Udon 250GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E4%B8%8D%E5%80%92%E7%BF%81%E8%B6%85%E6%BF%83%E8%8A%9D%E5%A3%AB%E6%8B%89%E9%BA%B5%204%20X%20135GM/i/101360287.html",
      "uid": "d2fc94f4b3e6080931de3c6a2bcad777",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "不倒翁超濃芝士拉麵 4 X 135GM",
          "price": "$38",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240917/d64a9558-748f-34af-8b88-b5da80ffe9b3",
          "product_eng_name": "Ottogi Real Cheese Ramen 4 x 135GM"
        },
        {
          "name": "不倒翁超濃芝士拉麵 4 X 135GM",
          "price": "$38",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240917/d64a9558-748f-34af-8b88-b5da80ffe9b3",
          "product_eng_name": "Ottogi Real Cheese Ramen 4 x 135GM"
        }
      ],
      "name": "不倒翁超濃芝士拉麵 4 X 135GM",
      "price": "$38",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240917/d64a9558-748f-34af-8b88-b5da80ffe9b3",
      "product_eng_name": "Ottogi Real Cheese Ramen 4 x 135GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E5%AE%B6%E6%A8%82%E7%89%8C%20%E9%9B%9E%E6%B9%AF%E5%91%B3%E5%BF%AB%E7%86%9F%E9%80%9A%E5%BF%83%E7%B2%89%2030%20X%2080GM/i/101346825.html",
      "uid": "c11ba61581866d18070fdfe5e1bd990b",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱家樂牌 雞湯味快熟通心粉 30 X 80GM",
          "price": "$150",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230213/f5838f1b-983b-421f-8287-966c2ae4672f",
          "product_eng_name": "Knorr Chicken Macaroni Case 30 X 80GM"
        },
        {
          "name": "原箱家樂牌 雞湯味快熟通心粉 30 X 80GM",
          "price": "$150",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230213/f5838f1b-983b-421f-8287-966c2ae4672f",
          "product_eng_name": "Knorr Chicken Macaroni Case 30 X 80GM"
        }
      ],
      "name": "原箱家樂牌 雞湯味快熟通心粉 30 X 80GM",
      "price": "$150",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230213/f5838f1b-983b-421f-8287-966c2ae4672f",
      "product_eng_name": "Knorr Chicken Macaroni Case 30 X 80GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E7%99%BE%E5%BE%97%E9%98%BF%E5%A7%A8%20%E6%84%8F%E5%A4%A7%E5%88%A9%E7%B2%89%235%2024%20X%20500%20GM/i/101335843.html",
      "uid": "15ee2b30127e23a1ec9471c902b4da76",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱百得阿姨 意大利粉#5 24 X 500 GM",
          "price": "$500",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231215/c46bb18c-e029-3d42-a0a6-5d527da58aa1",
          "product_eng_name": "Barilla Spaghetti #5 Case 24 X 500 GM"
        },
        {
          "name": "原箱百得阿姨 意大利粉#5 24 X 500 GM",
          "price": "$500",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231215/c46bb18c-e029-3d42-a0a6-5d527da58aa1",
          "product_eng_name": "Barilla Spaghetti #5 Case 24 X 500 GM"
        }
      ],
      "name": "原箱百得阿姨 意大利粉#5 24 X 500 GM",
      "price": "$500",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20231215/c46bb18c-e029-3d42-a0a6-5d527da58aa1",
      "product_eng_name": "Barilla Spaghetti #5 Case 24 X 500 GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%A5%A7%E5%B0%BC%E7%89%8C%E7%89%B9%E7%B4%9A%E7%85%8E%E7%82%B8%E6%B2%B9%201%E5%85%AC%E5%8D%87/i/101348497.html",
      "uid": "df50fb57b8c2e483a98b2d75ffd87779",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "奧尼牌特級煎炸油 1公升",
          "price": "$44",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20241101/1d10a067-50f6-3cea-a87c-b56d6f1f4014",
          "product_eng_name": "Olitalia Frienn Frying Oil 1L"
        },
        {
          "name": "奧尼牌特級煎炸油 1公升",
          "price": "$44",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20241101/1d10a067-50f6-3cea-a87c-b56d6f1f4014",
          "product_eng_name": "Olitalia Frienn Frying Oil 1L"
        }
      ],
      "name": "奧尼牌特級煎炸油 1公升",
      "price": "$44",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20241101/1d10a067-50f6-3cea-a87c-b56d6f1f4014",
      "product_eng_name": "Olitalia Frienn Frying Oil 1L"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/De%20Cecco%E6%84%8F%E5%A4%A7%E5%88%A9%E5%A4%A9%E4%BD%BF%E9%BA%B5n9%20500GM/i/101322513.html",
      "uid": "eca45ab6a1522f92dea511a531b9c190",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "De Cecco意大利天使麵n9 500GM",
          "price": "$29",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240917/b0e6cc09-9a5d-334a-8fd2-63abe255ca7b",
          "product_eng_name": "Dececco Capellini N9 500GM"
        },
        {
          "name": "De Cecco意大利天使麵n9 500GM",
          "price": "$29",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240917/b0e6cc09-9a5d-334a-8fd2-63abe255ca7b",
          "product_eng_name": "Dececco Capellini N9 500GM"
        }
      ],
      "name": "De Cecco意大利天使麵n9 500GM",
      "price": "$29",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240917/b0e6cc09-9a5d-334a-8fd2-63abe255ca7b",
      "product_eng_name": "Dececco Capellini N9 500GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E9%9B%99%E6%9D%BE%E7%89%8C%E7%B6%A0%E8%B1%86%E6%98%A5%E9%9B%A8%E7%B2%89%E7%B5%B2%2040GM/i/113344748.html",
      "uid": "7081edbcae4703fe480466ad627bb768",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "雙松牌綠豆春雨粉絲 40GM",
          "price": "$40",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240916/efd50cc4-147e-3b5d-867a-4166259dcffc",
          "product_eng_name": "Pine Brand Bean Vermicelli Bleached 40GM"
        },
        {
          "name": "雙松牌綠豆春雨粉絲 40GM",
          "price": "$40",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240916/efd50cc4-147e-3b5d-867a-4166259dcffc",
          "product_eng_name": "Pine Brand Bean Vermicelli Bleached 40GM"
        }
      ],
      "name": "雙松牌綠豆春雨粉絲 40GM",
      "price": "$40",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240916/efd50cc4-147e-3b5d-867a-4166259dcffc",
      "product_eng_name": "Pine Brand Bean Vermicelli Bleached 40GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%87%BA%E5%89%8D%E4%B8%80%E4%B8%81%20%E9%9D%92%E5%92%96%E5%96%B1%E5%91%B3%E5%8D%B3%E9%A3%9F%E9%BA%B5%20100GM/i/101328604.html",
      "uid": "630ce87612818a6ed3a18c553f06ece2",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "出前一丁 青咖喱味即食麵 100GM",
          "price": "$5",
          "offer": "【8件$28.5】$28.5任揀8件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250407/9ec2fa88-7d6e-3398-892a-51beab549d84",
          "product_eng_name": "Nissin Demae Iccho Thai Green Curry Flavour Instant Noodle 100GM"
        },
        {
          "name": "出前一丁 青咖喱味即食麵 100GM",
          "price": "$5",
          "offer": "【8件$28.5】$28.5任揀8件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250407/9ec2fa88-7d6e-3398-892a-51beab549d84",
          "product_eng_name": "Nissin Demae Iccho Thai Green Curry Flavour Instant Noodle 100GM"
        }
      ],
      "name": "出前一丁 青咖喱味即食麵 100GM",
      "price": "$5",
      "offer": "【8件$28.5】$28.5任揀8件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250407/9ec2fa88-7d6e-3398-892a-51beab549d84",
      "product_eng_name": "Nissin Demae Iccho Thai Green Curry Flavour Instant Noodle 100GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E9%A7%B1%E9%A7%9D%E5%98%9C%E8%8A%A5%E8%8A%B1%E7%B1%BD%E6%B2%B9%203%20X%20900ML/i/101324851.html",
      "uid": "f0269a55b65b7668f5a5c041b1f6791d",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "駱駝嘜芥花籽油 3 X 900ML",
          "price": "$65",
          "offer": "【買1件送1件贈品】購買每1件，即送1件人氣贈品；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210521/5cb0903e-dc77-4126-9b9b-fef378a3acff",
          "product_eng_name": "Camel Canola Oil 3 X 900ML"
        },
        {
          "name": "駱駝嘜芥花籽油 3 X 900ML",
          "price": "$65",
          "offer": "【買1件送1件贈品】購買每1件，即送1件人氣贈品；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210521/5cb0903e-dc77-4126-9b9b-fef378a3acff",
          "product_eng_name": "Camel Canola Oil 3 X 900ML"
        }
      ],
      "name": "駱駝嘜芥花籽油 3 X 900ML",
      "price": "$65",
      "offer": "【買1件送1件贈品】購買每1件，即送1件人氣贈品；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210521/5cb0903e-dc77-4126-9b9b-fef378a3acff",
      "product_eng_name": "Camel Canola Oil 3 X 900ML"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8C%A0%E6%8B%8C%E9%BA%B5%E9%B5%9D%E9%A6%99%E9%87%91%E8%94%A53x125gm/i/101328267.html",
      "uid": "d7a4d1036f42c6f9d5a33fe0ea9adfb7",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "匠拌麵鵝香金蔥3x125gm",
          "price": "$60",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240903/724586f5-68fc-3695-989b-1d7f883b0d82",
          "product_eng_name": "KUNGFOOD Sun-Dried Noodles-Premium Goose Oil Flavor 3x125gm"
        },
        {
          "name": "匠拌麵鵝香金蔥3x125gm",
          "price": "$60",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240903/724586f5-68fc-3695-989b-1d7f883b0d82",
          "product_eng_name": "KUNGFOOD Sun-Dried Noodles-Premium Goose Oil Flavor 3x125gm"
        }
      ],
      "name": "匠拌麵鵝香金蔥3x125gm",
      "price": "$60",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240903/724586f5-68fc-3695-989b-1d7f883b0d82",
      "product_eng_name": "KUNGFOOD Sun-Dried Noodles-Premium Goose Oil Flavor 3x125gm"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%8D%85%E7%90%83%E5%98%9C%20%E8%8A%A5%E8%8A%B1%E7%B1%BD%E6%B2%B9%E5%84%AA%E6%83%A0%E8%A3%9D%20900ML/i/101342842.html",
      "uid": "01dcfb5072affa03a1b5f11f3004bb5b",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "獅球嘜 芥花籽油優惠裝 900ML",
          "price": "$98",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240909/18c2f402-640f-372e-9856-c53e7d21a889",
          "product_eng_name": "Lion & Globe Pure Canola Oil 4x900ML"
        },
        {
          "name": "獅球嘜 芥花籽油優惠裝 900ML",
          "price": "$98",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240909/18c2f402-640f-372e-9856-c53e7d21a889",
          "product_eng_name": "Lion & Globe Pure Canola Oil 4x900ML"
        }
      ],
      "name": "獅球嘜 芥花籽油優惠裝 900ML",
      "price": "$98",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240909/18c2f402-640f-372e-9856-c53e7d21a889",
      "product_eng_name": "Lion & Globe Pure Canola Oil 4x900ML"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%8D%85%E7%90%83%E5%98%9C%E8%8A%A5%E8%8A%B1%E7%B1%BD%E6%B2%B9%205LT/i/101337990.html",
      "uid": "15873005c811f9700675cadcffc99cbf",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "獅球嘜芥花籽油 5LT",
          "price": "$135",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230915/b3476d8f-0972-3931-9708-6d6d1768ef97",
          "product_eng_name": "Lion & Globe Canola Oil 5LT"
        },
        {
          "name": "獅球嘜芥花籽油 5LT",
          "price": "$135",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230915/b3476d8f-0972-3931-9708-6d6d1768ef97",
          "product_eng_name": "Lion & Globe Canola Oil 5LT"
        }
      ],
      "name": "獅球嘜芥花籽油 5LT",
      "price": "$135",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230915/b3476d8f-0972-3931-9708-6d6d1768ef97",
      "product_eng_name": "Lion & Globe Canola Oil 5LT"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%A3%BD%E6%A1%83%E7%89%8C%20%E9%9B%B2%E8%85%BF%E9%AE%91%E9%AD%9A%E5%85%A8%E8%9B%8B%E4%BC%8A%E9%BA%B5%20160%20GM/i/101361519.html",
      "uid": "d6c3c4fc896dbf41024cbbfa8e8455e0",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "壽桃牌 雲腿鮑魚全蛋伊麵 160 GM",
          "price": "$19",
          "offer": "【2件$22】$22任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230606/2e4be262-6720-416e-bf13-8b996d2beb3e",
          "product_eng_name": "Sau Tao Abalone Soup Flavour E-Fu Noodles 160GM"
        },
        {
          "name": "壽桃牌 雲腿鮑魚全蛋伊麵 160 GM",
          "price": "$19",
          "offer": "【2件$22】$22任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230606/2e4be262-6720-416e-bf13-8b996d2beb3e",
          "product_eng_name": "Sau Tao Abalone Soup Flavour E-Fu Noodles 160GM"
        }
      ],
      "name": "壽桃牌 雲腿鮑魚全蛋伊麵 160 GM",
      "price": "$19",
      "offer": "【2件$22】$22任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230606/2e4be262-6720-416e-bf13-8b996d2beb3e",
      "product_eng_name": "Sau Tao Abalone Soup Flavour E-Fu Noodles 160GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%8F%A0%E6%B1%9F%E6%A9%8B%E7%89%8C%E6%9D%B1%E8%8E%9E%E7%B1%B3%E7%B2%89%20454GM/i/101361485.html",
      "uid": "3538964c958a60cbca81d8d3dd9b904f",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "珠江橋牌東莞米粉 454GM",
          "price": "$11",
          "offer": "【2件$19】$19任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240917/81474f47-a8b3-3850-b383-8d4686caefdf",
          "product_eng_name": "Pearl River Bridge Dongguan Rice Stick 454GM"
        },
        {
          "name": "珠江橋牌東莞米粉 454GM",
          "price": "$11",
          "offer": "【2件$19】$19任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240917/81474f47-a8b3-3850-b383-8d4686caefdf",
          "product_eng_name": "Pearl River Bridge Dongguan Rice Stick 454GM"
        }
      ],
      "name": "珠江橋牌東莞米粉 454GM",
      "price": "$11",
      "offer": "【2件$19】$19任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240917/81474f47-a8b3-3850-b383-8d4686caefdf",
      "product_eng_name": "Pearl River Bridge Dongguan Rice Stick 454GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/Yopokki%20%E9%9F%93%E5%9C%8B%E7%94%9C%E8%BE%A3%E5%91%B3%E5%B9%B4%E7%B3%95%E8%A2%8B%E8%A3%9D%20280GM/i/101343737.html",
      "uid": "c2220ceb1885613d0a57147665fa7c72",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "Yopokki 韓國甜辣味年糕袋裝 280GM",
          "price": "$18",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20200914/40e7a5e6-c53a-4f76-8f9b-8dc71b6097f3",
          "product_eng_name": "Yopokki Sweet & Spicy Ricecake Pack 280GM"
        }
      ],
      "name": "Yopokki 韓國甜辣味年糕袋裝 280GM",
      "price": "$18",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20200914/40e7a5e6-c53a-4f76-8f9b-8dc71b6097f3",
      "product_eng_name": "Yopokki Sweet & Spicy Ricecake Pack 280GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%AE%B6%E6%A8%82%E7%89%8C%E8%B1%AC%E9%AA%A8%E5%91%B3%E5%BF%AB%E7%86%9F%E9%80%9A%E5%BF%83%E7%B2%89%2080GM/i/101322063.html",
      "uid": "6e6e94ea7e495f42e46730419c556ae7",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "家樂牌豬骨味快熟通心粉 80GM",
          "price": "$7",
          "offer": "【3件$17】$17任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220705/91749f28-fc6c-4f5e-a031-39bffa030ca1",
          "product_eng_name": "Knorr Japanese Pork Bone Quick Serve Macaroni 80GM"
        },
        {
          "name": "家樂牌豬骨味快熟通心粉 80GM",
          "price": "$7",
          "offer": "【3件$17】$17任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220705/91749f28-fc6c-4f5e-a031-39bffa030ca1",
          "product_eng_name": "Knorr Japanese Pork Bone Quick Serve Macaroni 80GM"
        }
      ],
      "name": "家樂牌豬骨味快熟通心粉 80GM",
      "price": "$7",
      "offer": "【3件$17】$17任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20220705/91749f28-fc6c-4f5e-a031-39bffa030ca1",
      "product_eng_name": "Knorr Japanese Pork Bone Quick Serve Macaroni 80GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E4%B8%89%E9%A4%8A%E8%BE%A3%E9%9B%9E%E8%8A%9D%E5%A3%AB%E7%A2%97%E9%BA%B5%20105GM/i/101324086.html",
      "uid": "ba8c777c5b3548ea00812639fc27aa1d",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "三養辣雞芝士碗麵 105GM",
          "price": "$11",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20200430/3f492d4c-3190-49ac-be33-08ffe13ae014",
          "product_eng_name": "Samyang Hot Chicken Cheese Bowl 105GM"
        },
        {
          "name": "三養辣雞芝士碗麵 105GM",
          "price": "$11",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20200430/3f492d4c-3190-49ac-be33-08ffe13ae014",
          "product_eng_name": "Samyang Hot Chicken Cheese Bowl 105GM"
        }
      ],
      "name": "三養辣雞芝士碗麵 105GM",
      "price": "$11",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20200430/3f492d4c-3190-49ac-be33-08ffe13ae014",
      "product_eng_name": "Samyang Hot Chicken Cheese Bowl 105GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E4%B8%8D%E5%80%92%E7%BF%81%E8%8A%9D%E5%A3%AB%E6%8B%89%E9%BA%B5%2032%20X%20111GM/i/101342427.html",
      "uid": "4f82de3bb133413fa084f56e012ba0b1",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "原箱不倒翁芝士拉麵 32 X 111GM",
          "price": "$192",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230202/91cada8c-30f9-455a-a3de-f52e90609e18",
          "product_eng_name": "Ottogi Cheese Ramen 32 X 111GM"
        }
      ],
      "name": "原箱不倒翁芝士拉麵 32 X 111GM",
      "price": "$192",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230202/91cada8c-30f9-455a-a3de-f52e90609e18",
      "product_eng_name": "Ottogi Cheese Ramen 32 X 111GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E9%BB%9E%E9%BB%9E%E7%B6%A0%E6%9C%89%E6%A9%9F%E8%8C%89%E8%8E%89%E9%A6%99%E7%B1%B3%E7%99%BD%E7%B1%B3%201KG/i/101349131.html",
      "uid": "6755721d494bb69e964a4cdeb908e952",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "點點綠有機茉莉香米白米 1KG",
          "price": "$43",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250320/d5b240ef-fc84-3ad7-810e-21b7201f2861",
          "product_eng_name": "Green Dot Dot Organic Jasmine White Rice 1KG"
        }
      ],
      "name": "點點綠有機茉莉香米白米 1KG",
      "price": "$43",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250320/d5b240ef-fc84-3ad7-810e-21b7201f2861",
      "product_eng_name": "Green Dot Dot Organic Jasmine White Rice 1KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E4%B8%8D%E5%80%92%E7%BF%81%20%E8%8A%9D%E5%A3%AB%E6%9D%AF%E8%A3%9D%E6%92%88%E9%BA%B5%2055%20GM/i/101328276.html",
      "uid": "05ca6130a5a3e60af5f0a8eab98b33a6",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "不倒翁 芝士杯裝撈麵 55 GM",
          "price": "$14",
          "offer": "【2件$15.5】$15.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240823/559e5490-d323-3cb6-a1dc-c2d9c4adfaf4",
          "product_eng_name": "Ottogi Cheese Bokki Cup 55GM"
        }
      ],
      "name": "不倒翁 芝士杯裝撈麵 55 GM",
      "price": "$14",
      "offer": "【2件$15.5】$15.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240823/559e5490-d323-3cb6-a1dc-c2d9c4adfaf4",
      "product_eng_name": "Ottogi Cheese Bokki Cup 55GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E8%BE%B2%E5%BF%83%E7%9F%B3%E9%8D%8B%E6%8B%89%E9%BA%B5%205%20X%20120GM/i/101354127.html",
      "uid": "c32a158eddb05e4217b8183de0e7c221",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "農心石鍋拉麵 5 X 120GM",
          "price": "$20",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210520/8ea1e54c-0453-4db8-bced-e00491eea4f7",
          "product_eng_name": "Nong Shimclay Pot Ramyun 5 X 120GM"
        },
        {
          "name": "農心石鍋拉麵 5 X 120GM",
          "price": "$20",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210520/8ea1e54c-0453-4db8-bced-e00491eea4f7",
          "product_eng_name": "Nong Shimclay Pot Ramyun 5 X 120GM"
        }
      ],
      "name": "農心石鍋拉麵 5 X 120GM",
      "price": "$20",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210520/8ea1e54c-0453-4db8-bced-e00491eea4f7",
      "product_eng_name": "Nong Shimclay Pot Ramyun 5 X 120GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E9%A4%8A%E9%A4%8A%E7%89%8C%E9%85%B8%E8%BE%A3%E5%91%B3%E6%B9%AF%E9%BA%B5%205%20X%2070GM/i/101340604.html",
      "uid": "8c9a5e0a549ba275aa499c3232c28744",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "養養牌酸辣味湯麵 5 X 70GM",
          "price": "$14",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240916/2e40ed19-374d-3ab2-a61c-9b3a04288e87",
          "product_eng_name": "Yum Yum Tomyum Shrimp Noodle 5 X 70GM"
        },
        {
          "name": "養養牌酸辣味湯麵 5 X 70GM",
          "price": "$14",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240916/2e40ed19-374d-3ab2-a61c-9b3a04288e87",
          "product_eng_name": "(無法擷取英文名稱)"
        }
      ],
      "name": "養養牌酸辣味湯麵 5 X 70GM",
      "price": "$14",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240916/2e40ed19-374d-3ab2-a61c-9b3a04288e87",
      "product_eng_name": "(無法擷取英文名稱)"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E6%9D%8E%E9%8C%A6%E8%A8%98%E8%BE%9B%E8%BE%A3%E7%95%AA%E8%8C%84%E6%B9%AF%E9%BA%B512x193GM/i/114211806.html",
      "uid": "8395440385020093c464725ef5884bca",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "原箱李錦記辛辣番茄湯麵12x193GM",
          "price": "$384",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240719/b1afafb0-b423-31f0-b822-f7dbce7f838e",
          "product_eng_name": "Lee Kum Kee Spicy Tomato Soup Noodle Case 12 x 193GM"
        }
      ],
      "name": "原箱李錦記辛辣番茄湯麵12x193GM",
      "price": "$384",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240719/b1afafb0-b423-31f0-b822-f7dbce7f838e",
      "product_eng_name": "Lee Kum Kee Spicy Tomato Soup Noodle Case 12 x 193GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%A5%A7%E5%B0%BC%E7%89%8C%E7%B1%B3%E7%B3%A0%E6%B2%B9%201%E5%85%AC%E5%8D%87/i/101348528.html",
      "uid": "e02a3a6652fe39a51d03bad768a8e7dc",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "奧尼牌米糠油 1公升",
          "price": "$92",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250407/af67a00f-e5dc-3b84-a5cf-143cd6f29377",
          "product_eng_name": "Olitalia Rice Bran Oil 1L"
        },
        {
          "name": "奧尼牌米糠油 1公升",
          "price": "$92",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250407/af67a00f-e5dc-3b84-a5cf-143cd6f29377",
          "product_eng_name": "Olitalia Rice Bran Oil 1L"
        }
      ],
      "name": "奧尼牌米糠油 1公升",
      "price": "$92",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250407/af67a00f-e5dc-3b84-a5cf-143cd6f29377",
      "product_eng_name": "Olitalia Rice Bran Oil 1L"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%98%8E%E6%B4%9E%E6%B3%A1%E8%8F%9C%E9%BA%B5%205%20X%20120GM/i/101350456.html",
      "uid": "2d0b27afc31ad4eb2fde58e794fb26f3",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "明洞泡菜麵 5 X 120GM",
          "price": "$26",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240729/48ccc052-84dd-3e3d-99ec-4593a2c05dc6",
          "product_eng_name": "Myung Dong Kimchi Ramen 5 X 120GM"
        },
        {
          "name": "明洞泡菜麵 5 X 120GM",
          "price": "$26",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240729/48ccc052-84dd-3e3d-99ec-4593a2c05dc6",
          "product_eng_name": "Myung Dong Kimchi Ramen 5 X 120GM"
        }
      ],
      "name": "明洞泡菜麵 5 X 120GM",
      "price": "$26",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240729/48ccc052-84dd-3e3d-99ec-4593a2c05dc6",
      "product_eng_name": "Myung Dong Kimchi Ramen 5 X 120GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%20%E5%8C%97%E6%B5%B7%E9%81%93%E6%89%8B%E6%89%93%E9%A2%A8%E7%83%8F%E5%86%AC%2064%20X%20200%20GM/i/113654206.html",
      "uid": "a4d2b668bd4d85dd01e6125788333ad0",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱 北海道手打風烏冬 64 X 200 GM",
          "price": "$265",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231229/0f754ead-06b0-3d12-96d7-d6c642919a5a",
          "product_eng_name": "ACE Hokkaido Udon Case 64 x 200GM"
        },
        {
          "name": "原箱 北海道手打風烏冬 64 X 200 GM",
          "price": "$265",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231229/0f754ead-06b0-3d12-96d7-d6c642919a5a",
          "product_eng_name": "ACE Hokkaido Udon Case 64 x 200GM"
        }
      ],
      "name": "原箱 北海道手打風烏冬 64 X 200 GM",
      "price": "$265",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20231229/0f754ead-06b0-3d12-96d7-d6c642919a5a",
      "product_eng_name": "ACE Hokkaido Udon Case 64 x 200GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%AE%B6%E6%A8%82%E7%89%8C%E5%BF%AB%E7%86%9F%E9%80%9A%E5%BF%83%E7%B2%89%20400GM/i/101354669.html",
      "uid": "4b7f06cc0a2846d74b09212e075a8033",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "家樂牌快熟通心粉 400GM",
          "price": "$15",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220705/94d8b2c9-3f77-4a4e-ae88-bb9c26112d0d",
          "product_eng_name": "Knorr Quick Serve Macaroni 400GM"
        },
        {
          "name": "家樂牌快熟通心粉 400GM",
          "price": "$15",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220705/94d8b2c9-3f77-4a4e-ae88-bb9c26112d0d",
          "product_eng_name": "Knorr Quick Serve Macaroni 400GM"
        }
      ],
      "name": "家樂牌快熟通心粉 400GM",
      "price": "$15",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20220705/94d8b2c9-3f77-4a4e-ae88-bb9c26112d0d",
      "product_eng_name": "Knorr Quick Serve Macaroni 400GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E6%97%A5%E6%B8%85%E5%90%88%E5%91%B3%E9%81%93%20%E8%BE%A3%E6%B5%B7%E9%AE%AE%E5%A4%A7%E6%9D%AF%E9%BA%B5%2012%20X%20103GM/i/113465544.html",
      "uid": "f29a985d7af00a819ab5d80eff1b6d67",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱日清合味道 辣海鮮大杯麵 12 X 103GM",
          "price": "$105",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230728/67f34e72-2cc3-37f6-aaa8-924a07e7f19f",
          "product_eng_name": "Nissin Big Cup Spicy Seafood Case 12 x 103GM"
        },
        {
          "name": "原箱日清合味道 辣海鮮大杯麵 12 X 103GM",
          "price": "$105",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230728/67f34e72-2cc3-37f6-aaa8-924a07e7f19f",
          "product_eng_name": "Nissin Big Cup Spicy Seafood Case 12 x 103GM"
        }
      ],
      "name": "原箱日清合味道 辣海鮮大杯麵 12 X 103GM",
      "price": "$105",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230728/67f34e72-2cc3-37f6-aaa8-924a07e7f19f",
      "product_eng_name": "Nissin Big Cup Spicy Seafood Case 12 x 103GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E4%BF%9D%E5%BE%97%20%E7%B4%94%E6%A9%84%E6%AC%96%E6%B2%B9%201%20LT/i/101346828.html",
      "uid": "9c77fd91102e0a7aae2a330d84787874",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "保得 純橄欖油 1 LT",
          "price": "$99",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250313/bcabcd72-e189-3e4b-940e-81d9412629e9",
          "product_eng_name": "Bontaste Pure Olive Oil 1LT"
        },
        {
          "name": "保得 純橄欖油 1 LT",
          "price": "$99",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250313/bcabcd72-e189-3e4b-940e-81d9412629e9",
          "product_eng_name": "Bontaste Pure Olive Oil 1LT"
        }
      ],
      "name": "保得 純橄欖油 1 LT",
      "price": "$99",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250313/bcabcd72-e189-3e4b-940e-81d9412629e9",
      "product_eng_name": "Bontaste Pure Olive Oil 1LT"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E9%BB%9E%E9%BB%9E%E7%B6%A0%E6%9C%89%E6%A9%9F%E7%9F%AD%E7%B3%99%E7%B1%B3%201KG/i/101360065.html",
      "uid": "2333dcd696ecbd30b5f7e83bd97f878d",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "點點綠有機短糙米 1KG",
          "price": "$42",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250320/2604b16d-5497-3027-a6f1-5beede4e0b08",
          "product_eng_name": "Green Dot Dot Organic Brown Rice S 1KG"
        }
      ],
      "name": "點點綠有機短糙米 1KG",
      "price": "$42",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250320/2604b16d-5497-3027-a6f1-5beede4e0b08",
      "product_eng_name": "Green Dot Dot Organic Brown Rice S 1KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%A3%BD%E6%A1%83%E5%A2%A8%E9%AD%9A%E8%82%89%E9%86%AC%E9%AE%AE%E6%84%8F%E7%B2%89%20220GM/i/101384602.html",
      "uid": "5e586bd4dc86b817eda606040d330e5f",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "壽桃墨魚肉醬鮮意粉 220GM",
          "price": "$6",
          "offer": "【3件$22】$22任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220505/75ace235-4391-4927-b6e9-bdd71ea689e2",
          "product_eng_name": "Sau Tao Fresh Pasta Cuttlefish In Squid Ink Sauce 220GM"
        },
        {
          "name": "壽桃墨魚肉醬鮮意粉 220GM",
          "price": "$6",
          "offer": "【3件$22】$22任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220505/75ace235-4391-4927-b6e9-bdd71ea689e2",
          "product_eng_name": "Sau Tao Fresh Pasta Cuttlefish In Squid Ink Sauce 220GM"
        }
      ],
      "name": "壽桃墨魚肉醬鮮意粉 220GM",
      "price": "$6",
      "offer": "【3件$22】$22任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20220505/75ace235-4391-4927-b6e9-bdd71ea689e2",
      "product_eng_name": "Sau Tao Fresh Pasta Cuttlefish In Squid Ink Sauce 220GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%97%A5%E6%9C%AC%E5%86%B7%E8%95%8E%E9%BA%A5%E9%BA%B5%20600GM/i/101359741.html",
      "uid": "de787093118130ffa7c6f2c46d460e5a",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "日本冷蕎麥麵 600GM",
          "price": "$15",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240916/d0ec08f4-f874-374a-8835-1c9fc9611d92",
          "product_eng_name": "Yoshiya Hyande Hiyamugi Noodle 600GM"
        },
        {
          "name": "日本冷蕎麥麵 600GM",
          "price": "$15",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240916/d0ec08f4-f874-374a-8835-1c9fc9611d92",
          "product_eng_name": "Yoshiya Hyande Hiyamugi Noodle 600GM"
        }
      ],
      "name": "日本冷蕎麥麵 600GM",
      "price": "$15",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240916/d0ec08f4-f874-374a-8835-1c9fc9611d92",
      "product_eng_name": "Yoshiya Hyande Hiyamugi Noodle 600GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%88%80%E5%98%9C%E7%B4%94%E6%AD%A3%E8%8A%B1%E7%94%9F%E6%B2%B9%205LT/i/101360763.html",
      "uid": "e90c08aa280f3608f287b183e52c9248",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "刀嘜純正花生油 5LT",
          "price": "$168",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20200526/08a54b1c-cd0c-4567-bb5c-369c293fdd92",
          "product_eng_name": "Knife Pure Peanut Oil 5LT"
        },
        {
          "name": "刀嘜純正花生油 5LT",
          "price": "$168",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20200526/08a54b1c-cd0c-4567-bb5c-369c293fdd92",
          "product_eng_name": "Knife Pure Peanut Oil 5LT"
        }
      ],
      "name": "刀嘜純正花生油 5LT",
      "price": "$168",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20200526/08a54b1c-cd0c-4567-bb5c-369c293fdd92",
      "product_eng_name": "Knife Pure Peanut Oil 5LT"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/Vifon%20%E8%B6%8A%E5%8D%97%E7%89%9B%E8%82%89%E6%B9%AF%E7%A2%97%E6%B2%B3%E7%B2%89%20120GM/i/101359824.html",
      "uid": "40b35bcd3052ba5ddbfff8cb4e764ec5",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "Vifon 越南牛肉湯碗河粉 120GM",
          "price": "$14",
          "offer": "【2件$20】$20任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210125/39019147-12fa-408f-ac54-36e20899824d",
          "product_eng_name": "Vifon Rice Noodle Beef 120GM"
        },
        {
          "name": "Vifon 越南牛肉湯碗河粉 120GM",
          "price": "$14",
          "offer": "【2件$20】$20任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210125/39019147-12fa-408f-ac54-36e20899824d",
          "product_eng_name": "Vifon Rice Noodle Beef 120GM"
        }
      ],
      "name": "Vifon 越南牛肉湯碗河粉 120GM",
      "price": "$14",
      "offer": "【2件$20】$20任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210125/39019147-12fa-408f-ac54-36e20899824d",
      "product_eng_name": "Vifon Rice Noodle Beef 120GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%AB%BB%E5%9F%8E%E7%89%8C%E6%97%A5%E6%9C%AC%E5%93%81%E7%A8%AE%E7%8F%8D%E7%8F%A0%E7%B1%B3%205KG/i/101352940.html",
      "uid": "ba89b1244b0d4a3d71f71f93aa19c78f",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "櫻城牌日本品種珍珠米 5KG",
          "price": "$66",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250407/dc1ce7e0-c94c-33f2-9632-31438443ecf4",
          "product_eng_name": "Cherry Blossom Japonica Pearl Rice 5KG"
        }
      ],
      "name": "櫻城牌日本品種珍珠米 5KG",
      "price": "$66",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250407/dc1ce7e0-c94c-33f2-9632-31438443ecf4",
      "product_eng_name": "Cherry Blossom Japonica Pearl Rice 5KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E6%97%A5%E6%B8%85%E5%90%88%E5%91%B3%E9%81%93%20XO%E9%86%AC%E5%A4%A7%E6%9D%AF%E9%BA%B5%2012%20X%20105GM/i/113465604.html",
      "uid": "f42dea27374b082f88c955d5ea1509c8",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱日清合味道 XO醬大杯麵 12 X 105GM",
          "price": "$105",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230728/1c9cb76f-e85c-34f7-894c-3e39e9f2fc8b",
          "product_eng_name": "Nissin Big Cup XO Seafood Case 12 X 105GM"
        },
        {
          "name": "原箱日清合味道 XO醬大杯麵 12 X 105GM",
          "price": "$105",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230728/1c9cb76f-e85c-34f7-894c-3e39e9f2fc8b",
          "product_eng_name": "Nissin Big Cup XO Seafood Case 12 X 105GM"
        }
      ],
      "name": "原箱日清合味道 XO醬大杯麵 12 X 105GM",
      "price": "$105",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230728/1c9cb76f-e85c-34f7-894c-3e39e9f2fc8b",
      "product_eng_name": "Nissin Big Cup XO Seafood Case 12 X 105GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%8D%85%E7%90%83%E5%98%9C%E7%B2%9F%E7%B1%B3%E6%B2%B9%203%20X%20900ML/i/101340736.html",
      "uid": "9b966a9b4e34e9f229b511740b76a8fa",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "獅球嘜粟米油 3 X 900ML",
          "price": "$85",
          "offer": "【買1件送1件贈品】購買每1件，即送1件人氣贈品；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250407/7a96fca5-13ff-386c-873b-8a925288696e",
          "product_eng_name": "Lion & Globe Corn Oil 3 X 900ML"
        },
        {
          "name": "獅球嘜粟米油 3 X 900ML",
          "price": "$85",
          "offer": "【買1件送1件贈品】購買每1件，即送1件人氣贈品；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250407/7a96fca5-13ff-386c-873b-8a925288696e",
          "product_eng_name": "Lion & Globe Corn Oil 3 X 900ML"
        }
      ],
      "name": "獅球嘜粟米油 3 X 900ML",
      "price": "$85",
      "offer": "【買1件送1件贈品】購買每1件，即送1件人氣贈品；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250407/7a96fca5-13ff-386c-873b-8a925288696e",
      "product_eng_name": "Lion & Globe Corn Oil 3 X 900ML"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/La%20Molisana%E9%80%9A%E5%BF%83%E7%B2%89%2355%20500GM/i/101381095.html",
      "uid": "583875bd81de94595cde7febf9dc6301",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "La Molisana通心粉#55 500GM",
          "price": "$23",
          "offer": "【2件$30】$30任揀2件；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230714/fb17303e-0568-4c61-a6ad-e99799317780",
          "product_eng_name": "La Molisana Chifferi Rigate #55 500GM"
        },
        {
          "name": "La Molisana通心粉#55 500GM",
          "price": "$23",
          "offer": "【2件$30】$30任揀2件；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230714/fb17303e-0568-4c61-a6ad-e99799317780",
          "product_eng_name": "La Molisana Chifferi Rigate #55 500GM"
        }
      ],
      "name": "La Molisana通心粉#55 500GM",
      "price": "$23",
      "offer": "【2件$30】$30任揀2件；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230714/fb17303e-0568-4c61-a6ad-e99799317780",
      "product_eng_name": "La Molisana Chifferi Rigate #55 500GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E6%97%A5%E6%B8%85%E5%87%BA%E5%89%8D%E4%B8%80%E4%B8%81%20%E9%BB%91%E8%92%9C%E8%B1%AC%E9%AA%A8%E9%BA%B5%20100GM/i/101360271.html",
      "uid": "dbe470d6ae597a1c1fcb57c1f155f6f8",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱日清出前一丁 黑蒜豬骨麵 100GM",
          "price": "$105",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230202/6fd17019-078a-436a-84d5-0c1cbad8e0f4",
          "product_eng_name": "Nissin Demae Iccho Black Garlic Oil Tonkotsu Noodle Case 30 x 100GM"
        },
        {
          "name": "原箱日清出前一丁 黑蒜豬骨麵 100GM",
          "price": "$105",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230202/6fd17019-078a-436a-84d5-0c1cbad8e0f4",
          "product_eng_name": "Nissin Demae Iccho Black Garlic Oil Tonkotsu Noodle Case 30 x 100GM"
        }
      ],
      "name": "原箱日清出前一丁 黑蒜豬骨麵 100GM",
      "price": "$105",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230202/6fd17019-078a-436a-84d5-0c1cbad8e0f4",
      "product_eng_name": "Nissin Demae Iccho Black Garlic Oil Tonkotsu Noodle Case 30 x 100GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%A3%BD%E6%A1%83%20%E7%95%B6%E6%AD%B8%E5%91%B3%E6%B7%AE%E5%B1%B1%E9%BA%B5%20180%20GM/i/101328393.html",
      "uid": "a5ac8136a98ee0f09f442d8feb75b699",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "壽桃 當歸味淮山麵 180 GM",
          "price": "$9",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240823/0a4ef526-b472-35fd-8f2e-47274f88923b",
          "product_eng_name": "Sau Tao Chinese Angelica Flavour Yam Noodles 180GM"
        },
        {
          "name": "壽桃 當歸味淮山麵 180 GM",
          "price": "$9",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240823/0a4ef526-b472-35fd-8f2e-47274f88923b",
          "product_eng_name": "Sau Tao Chinese Angelica Flavour Yam Noodles 180GM"
        }
      ],
      "name": "壽桃 當歸味淮山麵 180 GM",
      "price": "$9",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240823/0a4ef526-b472-35fd-8f2e-47274f88923b",
      "product_eng_name": "Sau Tao Chinese Angelica Flavour Yam Noodles 180GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%9C%9F%E9%BA%B5%E5%A0%82%20%E8%B1%86%E8%BE%A6%E9%A2%A8%E5%91%B3%E4%B9%BE%E9%BA%B5%2084GM/i/101334102.html",
      "uid": "821fc03c710e148f6b39d2021b94859c",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "真麵堂 豆辦風味乾麵 84GM",
          "price": "$18",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20241203/6b7c7aa9-fe7f-367b-a58e-061faafd1f8f",
          "product_eng_name": "Jhenmiantang Chili Bean Noodle 84GM"
        },
        {
          "name": "真麵堂 豆辦風味乾麵 84GM",
          "price": "$18",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20241203/6b7c7aa9-fe7f-367b-a58e-061faafd1f8f",
          "product_eng_name": "Jhenmiantang Chili Bean Noodle 84GM"
        }
      ],
      "name": "真麵堂 豆辦風味乾麵 84GM",
      "price": "$18",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20241203/6b7c7aa9-fe7f-367b-a58e-061faafd1f8f",
      "product_eng_name": "Jhenmiantang Chili Bean Noodle 84GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%88%80%E5%98%9C%E9%87%91%E8%A3%9D%E6%BF%83%E9%A6%99%E8%8A%B1%E7%94%9F%E6%B2%B9%205LT/i/101360256.html",
      "uid": "4a118eb2ea83c89785fce347875c6bfe",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "刀嘜金裝濃香花生油 5LT",
          "price": "$179",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230714/e0ee9b12-732a-42de-bd20-bbf4b6c3f7b7",
          "product_eng_name": "Knife Supreme Peanut Oil 5LT"
        },
        {
          "name": "刀嘜金裝濃香花生油 5LT",
          "price": "$179",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230714/e0ee9b12-732a-42de-bd20-bbf4b6c3f7b7",
          "product_eng_name": "Knife Supreme Peanut Oil 5LT"
        }
      ],
      "name": "刀嘜金裝濃香花生油 5LT",
      "price": "$179",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230714/e0ee9b12-732a-42de-bd20-bbf4b6c3f7b7",
      "product_eng_name": "Knife Supreme Peanut Oil 5LT"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%97%A5%E6%B8%85%E5%90%88%E5%91%B3%E9%81%93%E6%B5%B7%E9%AE%AE%E8%BF%B7%E4%BD%A0%E6%9D%AF%E9%BA%B5%2045GM/i/101322938.html",
      "uid": "79aea131f62c7929045188d9aa2996b2",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "日清合味道海鮮迷你杯麵 45GM",
          "price": "$6",
          "offer": "【3件$17】$17任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220713/6d4de1af-c17f-4079-936c-bc177dfb7306",
          "product_eng_name": "Nissin Cup Noodles Seafood Mini 45GM"
        },
        {
          "name": "日清合味道海鮮迷你杯麵 45GM",
          "price": "$6",
          "offer": "【3件$17】$17任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220713/6d4de1af-c17f-4079-936c-bc177dfb7306",
          "product_eng_name": "Nissin Cup Noodles Seafood Mini 45GM"
        }
      ],
      "name": "日清合味道海鮮迷你杯麵 45GM",
      "price": "$6",
      "offer": "【3件$17】$17任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20220713/6d4de1af-c17f-4079-936c-bc177dfb7306",
      "product_eng_name": "Nissin Cup Noodles Seafood Mini 45GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%A3%BD%E6%A1%83%E6%B7%AE%E5%B1%B1%E9%BA%B512%E5%80%8B%E8%A3%9D/i/101326622.html",
      "uid": "cd3f105f11a6620be8b0949e123d059d",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "壽桃淮山麵12個裝",
          "price": "$30",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250102/0170cd37-93e3-3224-bc5f-eb8ffbad863e",
          "product_eng_name": "Sau Tao Yam Noodles 12pcs"
        },
        {
          "name": "壽桃淮山麵12個裝",
          "price": "$30",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250102/0170cd37-93e3-3224-bc5f-eb8ffbad863e",
          "product_eng_name": "Sau Tao Yam Noodles 12pcs"
        }
      ],
      "name": "壽桃淮山麵12個裝",
      "price": "$30",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250102/0170cd37-93e3-3224-bc5f-eb8ffbad863e",
      "product_eng_name": "Sau Tao Yam Noodles 12pcs"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%84%A1%E9%9B%99%E9%85%B8%E8%8F%9C%E9%AD%9A%E7%B2%89%E6%9D%AF%E8%A3%9D%20150GM/i/102126391.html",
      "uid": "6ad7c7f734e59ebad95b4440bfaedbd9",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "無雙酸菜魚粉杯裝 150GM",
          "price": "$16",
          "offer": "【2件$15】$15任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240502/3ebfdb42-f61a-3639-aa48-64d170a9493f",
          "product_eng_name": "Muso Pickle & Fish Flavor Sweet Potato Noodles 150GM"
        },
        {
          "name": "無雙酸菜魚粉杯裝 150GM",
          "price": "$16",
          "offer": "【2件$15】$15任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240502/3ebfdb42-f61a-3639-aa48-64d170a9493f",
          "product_eng_name": "Muso Pickle & Fish Flavor Sweet Potato Noodles 150GM"
        }
      ],
      "name": "無雙酸菜魚粉杯裝 150GM",
      "price": "$16",
      "offer": "【2件$15】$15任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240502/3ebfdb42-f61a-3639-aa48-64d170a9493f",
      "product_eng_name": "Muso Pickle & Fish Flavor Sweet Potato Noodles 150GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%8B%89%E9%9D%A2%E8%AA%AA%E6%8B%9B%E7%89%8C%E8%B1%9A%E9%AA%A8%E5%8F%89%E7%87%92%E6%8B%89%E9%BA%B5%20141.4GM/i/101851005.html",
      "uid": "9637f837abb4462f53fcddd40d1d3aba",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "拉面說招牌豚骨叉燒拉麵 141.4GM",
          "price": "$16",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240916/2e12f898-8c9e-375f-b18c-c89556462660",
          "product_eng_name": "Ramen Talk BBQ Pork Noodles 141.4GM"
        },
        {
          "name": "拉面說招牌豚骨叉燒拉麵 141.4GM",
          "price": "$16",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240916/2e12f898-8c9e-375f-b18c-c89556462660",
          "product_eng_name": "Ramen Talk BBQ Pork Noodles 141.4GM"
        }
      ],
      "name": "拉面說招牌豚骨叉燒拉麵 141.4GM",
      "price": "$16",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240916/2e12f898-8c9e-375f-b18c-c89556462660",
      "product_eng_name": "Ramen Talk BBQ Pork Noodles 141.4GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%9D%8E%E9%8C%A6%E8%A8%98%E6%A5%B5%E7%B4%94%E9%BB%91%E8%8A%9D%E9%BA%BB%E6%B2%B9%20207ML/i/101358631.html",
      "uid": "a97baaef6e182bdcbe07782724214f8c",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "李錦記極純黑芝麻油 207ML",
          "price": "$30",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210524/2d1bdb22-fae4-440b-a542-ba140ccb2bec",
          "product_eng_name": "Lee Kum Kee Pure Black Sesame Oil 207ML"
        },
        {
          "name": "李錦記極純黑芝麻油 207ML",
          "price": "$30",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210524/2d1bdb22-fae4-440b-a542-ba140ccb2bec",
          "product_eng_name": "Lee Kum Kee Pure Black Sesame Oil 207ML"
        }
      ],
      "name": "李錦記極純黑芝麻油 207ML",
      "price": "$30",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210524/2d1bdb22-fae4-440b-a542-ba140ccb2bec",
      "product_eng_name": "Lee Kum Kee Pure Black Sesame Oil 207ML"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%BE%A1%E5%93%81%E7%9A%87%20%E9%BB%91%E8%83%A1%E6%A4%92%E6%8B%8C%E9%BA%B5%20104GM/i/113463979.html",
      "uid": "f525004adefe50710b551417bba97b48",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "御品皇 黑胡椒拌麵 104GM",
          "price": "$4",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240925/394e10ca-0e2e-3211-be5b-65afa70f6156",
          "product_eng_name": "Yu Pin King Black Pepper Noodles 104GM"
        },
        {
          "name": "御品皇 黑胡椒拌麵 104GM",
          "price": "$4",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240925/394e10ca-0e2e-3211-be5b-65afa70f6156",
          "product_eng_name": "Yu Pin King Black Pepper Noodles 104GM"
        }
      ],
      "name": "御品皇 黑胡椒拌麵 104GM",
      "price": "$4",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240925/394e10ca-0e2e-3211-be5b-65afa70f6156",
      "product_eng_name": "Yu Pin King Black Pepper Noodles 104GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%97%A5%E6%B8%85%E5%87%BA%E5%89%8D%E4%B8%80%E4%B8%81%E6%97%A5%E6%9C%AC%E7%89%88%E9%BA%BB%E6%B2%B9%E9%BA%B5%205%20X%20102GM/i/101354706.html",
      "uid": "4cadcc040e7d994a7c5fe6a0332cedb2",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "日清出前一丁日本版麻油麵 5 X 102GM",
          "price": "$37",
          "offer": "【2件$49.9】$49.9任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230321/054cc5eb-cc93-4614-a0ae-601b8740521d",
          "product_eng_name": "Nissin Japan Demae Iccho Sesame Oil Noodles 5 X 102GM"
        },
        {
          "name": "日清出前一丁日本版麻油麵 5 X 102GM",
          "price": "$37",
          "offer": "【2件$49.9】$49.9任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230321/054cc5eb-cc93-4614-a0ae-601b8740521d",
          "product_eng_name": "Nissin Japan Demae Iccho Sesame Oil Noodles 5 X 102GM"
        }
      ],
      "name": "日清出前一丁日本版麻油麵 5 X 102GM",
      "price": "$37",
      "offer": "【2件$49.9】$49.9任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230321/054cc5eb-cc93-4614-a0ae-601b8740521d",
      "product_eng_name": "Nissin Japan Demae Iccho Sesame Oil Noodles 5 X 102GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E6%97%A5%E6%B8%85%E5%87%BA%E5%89%8D%E4%B8%80%E4%B8%81%20%E6%97%A5%E6%9C%AC%E7%89%88%E9%BA%BB%E6%B2%B9%E9%BA%B5%2030%20X%20102GM/i/101336300.html",
      "uid": "639901d5f9919baabd2dce7d3039e171",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱日清出前一丁 日本版麻油麵 30 X 102GM",
          "price": "$150",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231101/71c6a01c-10eb-3e45-9360-8fdcbc7c69ac",
          "product_eng_name": "Nissin Japan Demae Iccho Sesame Oil Noodle Case 30 X 102GM"
        },
        {
          "name": "原箱日清出前一丁 日本版麻油麵 30 X 102GM",
          "price": "$150",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231101/71c6a01c-10eb-3e45-9360-8fdcbc7c69ac",
          "product_eng_name": "Nissin Japan Demae Iccho Sesame Oil Noodle Case 30 X 102GM"
        }
      ],
      "name": "原箱日清出前一丁 日本版麻油麵 30 X 102GM",
      "price": "$150",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20231101/71c6a01c-10eb-3e45-9360-8fdcbc7c69ac",
      "product_eng_name": "Nissin Japan Demae Iccho Sesame Oil Noodle Case 30 X 102GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%AA%BD%E5%92%AA%E8%83%A1%E6%A4%92%E6%9D%AF%E9%BA%B5%2060GM/i/101339997.html",
      "uid": "e58479eca5a8d3876187f5e19f6132ef",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "媽咪胡椒杯麵 60GM",
          "price": "$6",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20200430/6390ae00-6aa8-4ef3-9f83-7cb9e778f33c",
          "product_eng_name": "Mamee Pepper Cup Noodle 60GM"
        },
        {
          "name": "媽咪胡椒杯麵 60GM",
          "price": "$6",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20200430/6390ae00-6aa8-4ef3-9f83-7cb9e778f33c",
          "product_eng_name": "Mamee Pepper Cup Noodle 60GM"
        }
      ],
      "name": "媽咪胡椒杯麵 60GM",
      "price": "$6",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20200430/6390ae00-6aa8-4ef3-9f83-7cb9e778f33c",
      "product_eng_name": "Mamee Pepper Cup Noodle 60GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%B5%B1%E4%B8%80%E8%8C%84%E7%9A%87%20%E7%95%AA%E8%8C%84%E9%9B%9E%E8%9B%8B%E9%9D%A2%20580GM/i/101346848.html",
      "uid": "d2add7650224119c74bfdfdd5f78bd01",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "統一茄皇 番茄雞蛋面 580GM",
          "price": "$27",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240124/26801560-5d8a-3de5-ae98-54a2ed4d639d",
          "product_eng_name": "Uni President Tomato Egg Noodles 580GM"
        },
        {
          "name": "統一茄皇 番茄雞蛋面 580GM",
          "price": "$27",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240124/26801560-5d8a-3de5-ae98-54a2ed4d639d",
          "product_eng_name": "Uni President Tomato Egg Noodles 580GM"
        }
      ],
      "name": "統一茄皇 番茄雞蛋面 580GM",
      "price": "$27",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240124/26801560-5d8a-3de5-ae98-54a2ed4d639d",
      "product_eng_name": "Uni President Tomato Egg Noodles 580GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E9%9B%99%E7%BE%8A%E7%89%8C%E7%99%BE%E6%90%AD%E7%B1%B3%E7%8E%8B%205KG/i/101330959.html",
      "uid": "33503fb2bb7122c92c8f43641c14ae3f",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "雙羊牌百搭米王 5KG",
          "price": "$82",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20241218/13894ede-25e5-35df-a9f4-5685dcfee552",
          "product_eng_name": "Double Ram Calrose Rice 5KG"
        }
      ],
      "name": "雙羊牌百搭米王 5KG",
      "price": "$82",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20241218/13894ede-25e5-35df-a9f4-5685dcfee552",
      "product_eng_name": "Double Ram Calrose Rice 5KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%A4%A9%E7%87%9F%E5%9D%8A%E6%B7%AE%E5%B1%B1%E9%BA%B5%20480GM/i/101379695.html",
      "uid": "bb6677481bd304af1a56866b8dbdd3e3",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "天營坊淮山麵 480GM",
          "price": "$34",
          "offer": "【2件$49】$49任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210125/0dca0bd6-b4db-41d5-8b04-8c890a754e6c",
          "product_eng_name": "Natural Nutrition Area Yam Noodle 480GM"
        },
        {
          "name": "天營坊淮山麵 480GM",
          "price": "$34",
          "offer": "【2件$49】$49任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210125/0dca0bd6-b4db-41d5-8b04-8c890a754e6c",
          "product_eng_name": "Natural Nutrition Area Yam Noodle 480GM"
        }
      ],
      "name": "天營坊淮山麵 480GM",
      "price": "$34",
      "offer": "【2件$49】$49任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210125/0dca0bd6-b4db-41d5-8b04-8c890a754e6c",
      "product_eng_name": "Natural Nutrition Area Yam Noodle 480GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/ALLGROO%20%E8%AE%9A%E5%B2%90%E6%80%A5%E5%87%8D%E7%83%8F%E5%86%AC%20230%20GM/i/101577435.html",
      "uid": "5ba50252fade625fba2cd95ae6db0ff6",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "ALLGROO 讚岐急凍烏冬 230 GM",
          "price": "$29",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230518/8525ed08-9733-48b7-a62f-ba47d89edab3",
          "product_eng_name": "allgroo Korean Sanuki Udon 5 x 230GM"
        },
        {
          "name": "ALLGROO 讚岐急凍烏冬 230 GM",
          "price": "$29",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230518/8525ed08-9733-48b7-a62f-ba47d89edab3",
          "product_eng_name": "allgroo Korean Sanuki Udon 5 x 230GM"
        }
      ],
      "name": "ALLGROO 讚岐急凍烏冬 230 GM",
      "price": "$29",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230518/8525ed08-9733-48b7-a62f-ba47d89edab3",
      "product_eng_name": "allgroo Korean Sanuki Udon 5 x 230GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%91%9E%E8%8C%B2%E7%B1%B3%E7%B3%A0%E6%B2%B9%201LT/i/101343341.html",
      "uid": "1ce3ba824cc9353b18a6f8e15c973e22",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "瑞茲米糠油 1LT",
          "price": "$80",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240726/f42f0def-3e9c-3476-8270-72bc8f74b94a",
          "product_eng_name": "Rizi Rice Bran Oil 1LT"
        },
        {
          "name": "瑞茲米糠油 1LT",
          "price": "$80",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240726/f42f0def-3e9c-3476-8270-72bc8f74b94a",
          "product_eng_name": "Rizi Rice Bran Oil 1LT"
        }
      ],
      "name": "瑞茲米糠油 1LT",
      "price": "$80",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240726/f42f0def-3e9c-3476-8270-72bc8f74b94a",
      "product_eng_name": "Rizi Rice Bran Oil 1LT"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%85%AB%E9%81%93%E5%BE%A1%E8%86%B3%E7%82%B8%E9%86%AC%E9%BA%B5%204%20X%20200GM/i/101336177.html",
      "uid": "80b09e5cdf24ca9a21305612e1189c44",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "八道御膳炸醬麵 4 X 200GM",
          "price": "$34",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240916/996c0302-c278-317e-985b-025ac36295f0",
          "product_eng_name": "Paldo Blackbean Ramen 4 X 200GM"
        },
        {
          "name": "八道御膳炸醬麵 4 X 200GM",
          "price": "$34",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240916/996c0302-c278-317e-985b-025ac36295f0",
          "product_eng_name": "Paldo Blackbean Ramen 4 X 200GM"
        }
      ],
      "name": "八道御膳炸醬麵 4 X 200GM",
      "price": "$34",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240916/996c0302-c278-317e-985b-025ac36295f0",
      "product_eng_name": "Paldo Blackbean Ramen 4 X 200GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E4%B8%8D%E5%80%92%E7%BF%81%20%E8%8A%9D%E5%A3%AB%E7%A2%97%E8%A3%9D%E6%8B%89%E9%BA%B5%2090%20GM/i/101328285.html",
      "uid": "044db285c34706e81735d24ff2ef4d72",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "不倒翁 芝士碗裝拉麵 90 GM",
          "price": "$16",
          "offer": "【2件$20】$20任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240823/90787fad-cea3-37e1-8299-09aabb730f07",
          "product_eng_name": "Ottogi Cheese Bowl Ramen 90GM"
        },
        {
          "name": "不倒翁 芝士碗裝拉麵 90 GM",
          "price": "$16",
          "offer": "【2件$20】$20任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240823/90787fad-cea3-37e1-8299-09aabb730f07",
          "product_eng_name": "Ottogi Cheese Bowl Ramen 90GM"
        }
      ],
      "name": "不倒翁 芝士碗裝拉麵 90 GM",
      "price": "$16",
      "offer": "【2件$20】$20任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240823/90787fad-cea3-37e1-8299-09aabb730f07",
      "product_eng_name": "Ottogi Cheese Bowl Ramen 90GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E4%BB%8A%E9%BA%A5%E9%83%8E%20%E9%9B%9E%E6%B9%AF%E7%83%8F%E5%86%AC%E9%BA%B5%20140GM/i/101353629.html",
      "uid": "b644e059825124fdc669da6cb6934762",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "今麥郎 雞湯烏冬麵 140GM",
          "price": "$22",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240124/53d700d6-dd9c-34c6-a104-c072ffa6d546",
          "product_eng_name": "Jinmailang Chicken Udon 140GM"
        },
        {
          "name": "今麥郎 雞湯烏冬麵 140GM",
          "price": "$22",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240124/53d700d6-dd9c-34c6-a104-c072ffa6d546",
          "product_eng_name": "Jinmailang Chicken Udon 140GM"
        }
      ],
      "name": "今麥郎 雞湯烏冬麵 140GM",
      "price": "$22",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240124/53d700d6-dd9c-34c6-a104-c072ffa6d546",
      "product_eng_name": "Jinmailang Chicken Udon 140GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%97%A5%E6%B8%85%E5%90%88%E5%91%B3%E9%81%93%E9%AE%AE%E8%9D%A6%E8%B1%AC%E9%AA%A8%E6%B9%AF%E5%91%B3%E6%9D%AF%E9%BA%B5%2075GM/i/101843869.html",
      "uid": "da8a5b8a55b7b3e407a0907f5d2a83ab",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "日清合味道鮮蝦豬骨湯味杯麵 75GM",
          "price": "$8",
          "offer": "【2件$14.5】$14.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250327/ef17d89d-5c6f-3449-81a2-2cf9de95f479",
          "product_eng_name": "Nissin Cup Noodles Shrimp&Tonkutsu 75GM"
        },
        {
          "name": "日清合味道鮮蝦豬骨湯味杯麵 75GM",
          "price": "$8",
          "offer": "【2件$14.5】$14.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250327/ef17d89d-5c6f-3449-81a2-2cf9de95f479",
          "product_eng_name": "Nissin Cup Noodles Shrimp&Tonkutsu 75GM"
        }
      ],
      "name": "日清合味道鮮蝦豬骨湯味杯麵 75GM",
      "price": "$8",
      "offer": "【2件$14.5】$14.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250327/ef17d89d-5c6f-3449-81a2-2cf9de95f479",
      "product_eng_name": "Nissin Cup Noodles Shrimp&Tonkutsu 75GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E9%A4%8A%E9%A4%8A%E7%89%8C%E9%85%B8%E8%BE%A3%E8%9D%A6%E6%BF%83%E6%B9%AF%E9%BA%B5%205%20X%2070GM/i/101344095.html",
      "uid": "16b3cfaa0f74757754e083c22781439a",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "養養牌酸辣蝦濃湯麵 5 X 70GM",
          "price": "$14",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240916/16e5d427-f8ba-3d98-adc3-fe2b07bfa59b",
          "product_eng_name": "Yum Yum Tom Yum Creamy Noodles 5 X 70GM"
        },
        {
          "name": "養養牌酸辣蝦濃湯麵 5 X 70GM",
          "price": "$14",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240916/16e5d427-f8ba-3d98-adc3-fe2b07bfa59b",
          "product_eng_name": "Yum Yum Tom Yum Creamy Noodles 5 X 70GM"
        }
      ],
      "name": "養養牌酸辣蝦濃湯麵 5 X 70GM",
      "price": "$14",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240916/16e5d427-f8ba-3d98-adc3-fe2b07bfa59b",
      "product_eng_name": "Yum Yum Tom Yum Creamy Noodles 5 X 70GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%B5%B1%E4%B8%80%E6%BB%BF%E6%BC%A2%E5%A4%A7%E9%A4%90%20%E7%B4%85%E7%87%92%E8%B1%AC%E8%82%89%E5%A4%A7%E7%A2%97%E9%BA%B5%20199%20GM/i/113735136.html",
      "uid": "5c945320efac40f28026fca00463b8a0",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "統一滿漢大餐 紅燒豬肉大碗麵 199 GM",
          "price": "$32",
          "offer": "【2件$32】$32任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240316/0cf2f835-b7ac-3a03-9595-878ad5a7e1df",
          "product_eng_name": "Imperial Big Meal Braised Pork Bowl Noodles 199GM"
        },
        {
          "name": "統一滿漢大餐 紅燒豬肉大碗麵 199 GM",
          "price": "$32",
          "offer": "【2件$32】$32任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240316/0cf2f835-b7ac-3a03-9595-878ad5a7e1df",
          "product_eng_name": "Imperial Big Meal Braised Pork Bowl Noodles 199GM"
        }
      ],
      "name": "統一滿漢大餐 紅燒豬肉大碗麵 199 GM",
      "price": "$32",
      "offer": "【2件$32】$32任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240316/0cf2f835-b7ac-3a03-9595-878ad5a7e1df",
      "product_eng_name": "Imperial Big Meal Braised Pork Bowl Noodles 199GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%85%AC%E4%BB%94%E9%81%BF%E9%A2%A8%E5%A1%98%E5%8F%A3%E5%91%B3%E7%82%92%E9%BA%B5%E7%8E%8B%20112GM/i/101361516.html",
      "uid": "f8a0e352da5b6adb92bedd6bca2912ae",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "公仔避風塘口味炒麵王 112GM",
          "price": "$6",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250320/969bdb14-89e0-3b0d-a86d-752bdb42de83",
          "product_eng_name": "Doll Strong Deep Fried Garlic And Chilli Flavour 112GM"
        },
        {
          "name": "公仔避風塘口味炒麵王 112GM",
          "price": "$6",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250320/969bdb14-89e0-3b0d-a86d-752bdb42de83",
          "product_eng_name": "Doll Strong Deep Fried Garlic And Chilli Flavour 112GM"
        }
      ],
      "name": "公仔避風塘口味炒麵王 112GM",
      "price": "$6",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250320/969bdb14-89e0-3b0d-a86d-752bdb42de83",
      "product_eng_name": "Doll Strong Deep Fried Garlic And Chilli Flavour 112GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1Vifon%20%E8%B6%8A%E5%8D%97%E8%9F%B9%E8%82%89%E5%91%B3%E7%B2%97%E7%B2%89%E6%A2%9D%20%2030%20X%2060GM/i/113267704.html",
      "uid": "bf4cb565d67edb2b406ddd8369220a64",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱Vifon 越南蟹肉味粗粉條 30 X 60GM",
          "price": "$105",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20221125/09038128-da7d-48e9-a747-2b9eaf2b1bac",
          "product_eng_name": "Vifon Crab Rice Noodles Case 30 X 60GM"
        },
        {
          "name": "原箱Vifon 越南蟹肉味粗粉條 30 X 60GM",
          "price": "$105",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20221125/09038128-da7d-48e9-a747-2b9eaf2b1bac",
          "product_eng_name": "Vifon Crab Rice Noodles Case 30 X 60GM"
        }
      ],
      "name": "原箱Vifon 越南蟹肉味粗粉條 30 X 60GM",
      "price": "$105",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20221125/09038128-da7d-48e9-a747-2b9eaf2b1bac",
      "product_eng_name": "Vifon Crab Rice Noodles Case 30 X 60GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/Kiki%E9%A3%9F%E5%93%81%E8%94%A5%E6%B2%B9%E6%8B%8C%E9%BA%B5%205%20X%2090GM/i/101362829.html",
      "uid": "1c11f9a8371c5430920d8ea5e0a1133d",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "Kiki食品蔥油拌麵 5 X 90GM",
          "price": "$68",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20200430/9c9eb3d8-7280-4a92-bbe2-f1dcd7b85aa7",
          "product_eng_name": "KiKi Scallion Oil Dry-Stirred Noodles 5 x 90GM"
        },
        {
          "name": "Kiki食品蔥油拌麵 5 X 90GM",
          "price": "$68",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20200430/9c9eb3d8-7280-4a92-bbe2-f1dcd7b85aa7",
          "product_eng_name": "KiKi Scallion Oil Dry-Stirred Noodles 5 x 90GM"
        }
      ],
      "name": "Kiki食品蔥油拌麵 5 X 90GM",
      "price": "$68",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20200430/9c9eb3d8-7280-4a92-bbe2-f1dcd7b85aa7",
      "product_eng_name": "KiKi Scallion Oil Dry-Stirred Noodles 5 x 90GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%85%AC%E4%BB%94%E5%87%B1%E8%92%82%E9%BB%9E%E5%BF%83%E9%BA%B5%2033GM/i/101358953.html",
      "uid": "6bcd9565dca7b2646a385a30dc31c7ac",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "公仔凱蒂點心麵 33GM",
          "price": "$4",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210621/7edc571e-2656-43b4-913e-3ee861ce4463",
          "product_eng_name": "Doll Hello Kitty Dim Sum Noodle 33GM"
        },
        {
          "name": "公仔凱蒂點心麵 33GM",
          "price": "$4",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210621/7edc571e-2656-43b4-913e-3ee861ce4463",
          "product_eng_name": "Doll Hello Kitty Dim Sum Noodle 33GM"
        }
      ],
      "name": "公仔凱蒂點心麵 33GM",
      "price": "$4",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210621/7edc571e-2656-43b4-913e-3ee861ce4463",
      "product_eng_name": "Doll Hello Kitty Dim Sum Noodle 33GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%98%8C%E4%B8%96%E7%89%8C%20%E9%BE%8D%E5%8F%A3%E7%B2%89%E7%B5%B2%20100%20GM/i/113520974.html",
      "uid": "19918a48472b518cfbb76ac507edf546",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "昌世牌 龍口粉絲 100 GM",
          "price": "$8",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230905/978e98ff-e1d5-30ff-b317-394524da0714",
          "product_eng_name": "Chance Longkou Vermicelli 100GM"
        },
        {
          "name": "昌世牌 龍口粉絲 100 GM",
          "price": "$8",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230905/978e98ff-e1d5-30ff-b317-394524da0714",
          "product_eng_name": "Chance Longkou Vermicelli 100GM"
        }
      ],
      "name": "昌世牌 龍口粉絲 100 GM",
      "price": "$8",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230905/978e98ff-e1d5-30ff-b317-394524da0714",
      "product_eng_name": "Chance Longkou Vermicelli 100GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%99%BE%E7%9B%8A%E6%B8%85%E6%B7%A1%E6%A9%84%E6%AC%96%E6%B2%B9%201LT/i/113318808.html",
      "uid": "7914925f84a5b5e0ef45097f45816744",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "百益清淡橄欖油 1LT",
          "price": "$169",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240425/7ccdcb4d-31a8-35eb-b718-d79f64aaf389",
          "product_eng_name": "Filippo Berio Extra Light Olive Oil 1LT"
        },
        {
          "name": "百益清淡橄欖油 1LT",
          "price": "$169",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240425/7ccdcb4d-31a8-35eb-b718-d79f64aaf389",
          "product_eng_name": "Filippo Berio Extra Light Olive Oil 1LT"
        }
      ],
      "name": "百益清淡橄欖油 1LT",
      "price": "$169",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240425/7ccdcb4d-31a8-35eb-b718-d79f64aaf389",
      "product_eng_name": "Filippo Berio Extra Light Olive Oil 1LT"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%97%A5%E6%B8%85%E5%87%BA%E5%89%8D%E4%B8%80%E4%B8%81%E5%B0%8F%E9%BA%A5%E7%B2%89%E9%BA%BB%E6%B2%B9%E9%BA%B5%2091GM/i/101381820.html",
      "uid": "8468d768d3c398b0fd59c669926aa4c0",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "日清出前一丁小麥粉麻油麵 91GM",
          "price": "$21",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240902/a0a274ff-8300-3faf-bac1-2d2455a78a60",
          "product_eng_name": "Nissin Demae Iccho Hokkaido Wheat Flour Sesame Oil Noodles 5 x 91GM"
        },
        {
          "name": "日清出前一丁小麥粉麻油麵 91GM",
          "price": "$21",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240902/a0a274ff-8300-3faf-bac1-2d2455a78a60",
          "product_eng_name": "Nissin Demae Iccho Hokkaido Wheat Flour Sesame Oil Noodles 5 x 91GM"
        }
      ],
      "name": "日清出前一丁小麥粉麻油麵 91GM",
      "price": "$21",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240902/a0a274ff-8300-3faf-bac1-2d2455a78a60",
      "product_eng_name": "Nissin Demae Iccho Hokkaido Wheat Flour Sesame Oil Noodles 5 x 91GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E8%9E%BA%E9%9C%B8%E7%8E%8B%20%E9%BA%BB%E8%BE%A3%E8%9E%BA%E8%9E%84%E7%B2%89%E6%9D%AF%E8%A3%9D%20210%20GM/i/113675701.html",
      "uid": "c86570815f58f771e632ddc1114e3681",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "螺霸王 麻辣螺螄粉杯裝 210 GM",
          "price": "$11",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240129/91f58bf9-1440-34bc-b0ae-bbfe5f186885",
          "product_eng_name": "NO WANG SPICY LUOSI NDL CUP 210 GM"
        },
        {
          "name": "螺霸王 麻辣螺螄粉杯裝 210 GM",
          "price": "$11",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240129/91f58bf9-1440-34bc-b0ae-bbfe5f186885",
          "product_eng_name": "NO WANG SPICY LUOSI NDL CUP 210 GM"
        }
      ],
      "name": "螺霸王 麻辣螺螄粉杯裝 210 GM",
      "price": "$11",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240129/91f58bf9-1440-34bc-b0ae-bbfe5f186885",
      "product_eng_name": "NO WANG SPICY LUOSI NDL CUP 210 GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%B6%AD%E5%8A%9B%E7%82%B8%E9%86%AC%E9%BA%B5%20450%E5%85%8B/i/101355012.html",
      "uid": "e5e81232e04fb372d0172014f64c9365",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "維力炸醬麵 450克",
          "price": "$23",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240321/79d23d62-1769-3a82-b20c-c06478f4762c",
          "product_eng_name": "Weilih Noodle Jah Jan Falvor 450GM"
        },
        {
          "name": "維力炸醬麵 450克",
          "price": "$23",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240321/79d23d62-1769-3a82-b20c-c06478f4762c",
          "product_eng_name": "Weilih Noodle Jah Jan Falvor 450GM"
        }
      ],
      "name": "維力炸醬麵 450克",
      "price": "$23",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240321/79d23d62-1769-3a82-b20c-c06478f4762c",
      "product_eng_name": "Weilih Noodle Jah Jan Falvor 450GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E5%87%BA%E5%89%8D%E4%B8%80%E4%B8%81%20%E6%B5%B7%E9%AE%AE%E5%8D%B3%E9%A3%9F%E9%BA%B5%20%2030%20X%20100GM/i/101334341.html",
      "uid": "8500c4668e0618606b69c625bfae6707",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱出前一丁 海鮮即食麵 30 X 100GM",
          "price": "$105",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231013/1fd567d3-540e-3493-a63a-b7d7b56edec0",
          "product_eng_name": "Nissin Demae Iccho Seafood Instant Noodle case 30 x 100GM"
        },
        {
          "name": "原箱出前一丁 海鮮即食麵 30 X 100GM",
          "price": "$105",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231013/1fd567d3-540e-3493-a63a-b7d7b56edec0",
          "product_eng_name": "Nissin Demae Iccho Seafood Instant Noodle case 30 x 100GM"
        }
      ],
      "name": "原箱出前一丁 海鮮即食麵 30 X 100GM",
      "price": "$105",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20231013/1fd567d3-540e-3493-a63a-b7d7b56edec0",
      "product_eng_name": "Nissin Demae Iccho Seafood Instant Noodle case 30 x 100GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E9%A7%B1%E9%A7%9D%E5%98%9C%E8%8A%B1%E7%94%9F%E6%B2%B9900%E6%AF%AB%E5%8D%87X3/i/101380336.html",
      "uid": "765e593469afa2c32a3c024066aca8f1",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "駱駝嘜花生油900毫升X3",
          "price": "$89",
          "offer": "【買1件送1件贈品】購買每1件，即送1件人氣贈品；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240813/61299b9b-a7b1-309c-a23d-fb436cc843a7",
          "product_eng_name": "Camel Peanut Oil 3 x 900ML"
        },
        {
          "name": "駱駝嘜花生油900毫升X3",
          "price": "$89",
          "offer": "【買1件送1件贈品】購買每1件，即送1件人氣贈品；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240813/61299b9b-a7b1-309c-a23d-fb436cc843a7",
          "product_eng_name": "Camel Peanut Oil 3 x 900ML"
        }
      ],
      "name": "駱駝嘜花生油900毫升X3",
      "price": "$89",
      "offer": "【買1件送1件贈品】購買每1件，即送1件人氣贈品；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240813/61299b9b-a7b1-309c-a23d-fb436cc843a7",
      "product_eng_name": "Camel Peanut Oil 3 x 900ML"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%97%A5%E6%B8%85%E5%90%88%E5%91%B3%E9%81%93%20XO%E9%86%AC%E6%B5%B7%E9%AE%AE%E5%A4%A7%E6%9D%AF%E9%BA%B5%20105%20GM/i/102127686.html",
      "uid": "95384368879994c6d38d60b8ca3554b9",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "日清合味道 XO醬海鮮大杯麵 105 GM",
          "price": "$11",
          "offer": "【2件$18】$18任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240711/b4d8add2-fe84-37c1-aa94-e110f384be57",
          "product_eng_name": "Nissin Big Cup XO Seafood Noodles 105GM"
        },
        {
          "name": "日清合味道 XO醬海鮮大杯麵 105 GM",
          "price": "$11",
          "offer": "【2件$18】$18任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240711/b4d8add2-fe84-37c1-aa94-e110f384be57",
          "product_eng_name": "Nissin Big Cup XO Seafood Noodles 105GM"
        }
      ],
      "name": "日清合味道 XO醬海鮮大杯麵 105 GM",
      "price": "$11",
      "offer": "【2件$18】$18任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240711/b4d8add2-fe84-37c1-aa94-e110f384be57",
      "product_eng_name": "Nissin Big Cup XO Seafood Noodles 105GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/Macro%20%E6%9C%89%E6%A9%9F%E5%85%A8%E9%BA%A5%E6%84%8F%E5%A4%A7%E5%88%A9%E7%B2%89%20500%E5%85%8B/i/101362680.html",
      "uid": "430e596fb1d213792ba0f29b295c13fb",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "Macro 有機全麥意大利粉 500克",
          "price": "$28",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250219/bf9b7a02-32cc-3fb9-af71-6a755b3873fa",
          "product_eng_name": "Macro Organic Wholemeal Pasta Spaghetti 500GM"
        },
        {
          "name": "Macro 有機全麥意大利粉 500克",
          "price": "$28",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250219/bf9b7a02-32cc-3fb9-af71-6a755b3873fa",
          "product_eng_name": "Macro Organic Wholemeal Pasta Spaghetti 500GM"
        }
      ],
      "name": "Macro 有機全麥意大利粉 500克",
      "price": "$28",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250219/bf9b7a02-32cc-3fb9-af71-6a755b3873fa",
      "product_eng_name": "Macro Organic Wholemeal Pasta Spaghetti 500GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%97%A5%E6%9C%AC%E7%94%A2%E7%9B%B4%E7%B1%B3%20%E8%BF%91%E6%B1%9F%E7%B1%B3%202KG/i/113493199.html",
      "uid": "68e5a3a14f4961387ccda9c70b512b22",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "日本產直米 近江米 2KG",
          "price": "$69",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240510/7081d928-3936-3e0c-b7c8-bb23b5e9be0a",
          "product_eng_name": "Omi Shiga Rice 2KG"
        }
      ],
      "name": "日本產直米 近江米 2KG",
      "price": "$69",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240510/7081d928-3936-3e0c-b7c8-bb23b5e9be0a",
      "product_eng_name": "Omi Shiga Rice 2KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E8%BE%B2%E5%BF%83%E8%BE%9B%E8%BE%A3%E7%82%92%E9%BA%B5%20131GM/i/101859224.html",
      "uid": "ab4f914612486e392ea8d4f2c571e450",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "農心辛辣炒麵 131GM",
          "price": "$32",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220615/89c2c7da-6f31-4aba-9393-49c575d1f20b",
          "product_eng_name": "Nong Shim Shin Stir Fry Noodle 131GM"
        },
        {
          "name": "農心辛辣炒麵 131GM",
          "price": "$32",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220615/89c2c7da-6f31-4aba-9393-49c575d1f20b",
          "product_eng_name": "Nong Shim Shin Stir Fry Noodle 131GM"
        }
      ],
      "name": "農心辛辣炒麵 131GM",
      "price": "$32",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20220615/89c2c7da-6f31-4aba-9393-49c575d1f20b",
      "product_eng_name": "Nong Shim Shin Stir Fry Noodle 131GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E8%9E%BA%E9%9C%B8%E7%8E%8B%20%E7%B4%AB%E8%98%87%E5%91%B3%20%E8%9E%BA%E8%9E%84%E7%B2%89%20360%E5%85%8B/i/102098776.html",
      "uid": "29f9404425bb2a7712129587bc19089c",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "螺霸王 紫蘇味 螺螄粉 360克",
          "price": "$40",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230330/7e81248f-60f0-4832-be27-2f8af2da7a3d",
          "product_eng_name": "No Wang Perilla Flaours Rice Noodles 360G"
        },
        {
          "name": "螺霸王 紫蘇味 螺螄粉 360克",
          "price": "$40",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230330/7e81248f-60f0-4832-be27-2f8af2da7a3d",
          "product_eng_name": "No Wang Perilla Flaours Rice Noodles 360G"
        }
      ],
      "name": "螺霸王 紫蘇味 螺螄粉 360克",
      "price": "$40",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230330/7e81248f-60f0-4832-be27-2f8af2da7a3d",
      "product_eng_name": "No Wang Perilla Flaours Rice Noodles 360G"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%88%80%E5%98%9C%E7%B6%AD%E4%BB%96%E5%91%BDE%E5%81%A5%E5%BA%B7%E8%8A%B1%E7%94%9F%E9%A3%9F%E6%B2%B9%20900%E6%AF%AB%E5%8D%87X3/i/101329686.html",
      "uid": "dd23a56d925635df76992f30afef8691",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "刀嘜維他命E健康花生食油 900毫升X3",
          "price": "$85",
          "offer": "【買1件送2件贈品】購買每1件，即送2件人氣贈品；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240813/947d7dc6-be3d-38ee-b819-ee6ea0d20a22",
          "product_eng_name": "Knife Vitamin E Peanut Blended Oil 3 x 900ML"
        },
        {
          "name": "刀嘜維他命E健康花生食油 900毫升X3",
          "price": "$85",
          "offer": "【買1件送2件贈品】購買每1件，即送2件人氣贈品；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240813/947d7dc6-be3d-38ee-b819-ee6ea0d20a22",
          "product_eng_name": "Knife Vitamin E Peanut Blended Oil 3 x 900ML"
        }
      ],
      "name": "刀嘜維他命E健康花生食油 900毫升X3",
      "price": "$85",
      "offer": "【買1件送2件贈品】購買每1件，即送2件人氣贈品；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240813/947d7dc6-be3d-38ee-b819-ee6ea0d20a22",
      "product_eng_name": "Knife Vitamin E Peanut Blended Oil 3 x 900ML"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%98%A5%E7%B5%B2%20%E7%89%8C%E5%8D%97%E6%98%8C%E6%8B%8C%E7%B2%89%20209GM/i/101362454.html",
      "uid": "8c45e98d5e4953a5886fe236359d95be",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "春絲 牌南昌拌粉 209GM",
          "price": "$9",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20241028/cb4d6e38-a083-3354-b307-99f9b905cda6",
          "product_eng_name": "Chunsi Nanchang Rice Noodles 209GM"
        },
        {
          "name": "春絲 牌南昌拌粉 209GM",
          "price": "$9",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20241028/cb4d6e38-a083-3354-b307-99f9b905cda6",
          "product_eng_name": "Chunsi Nanchang Rice Noodles 209GM"
        }
      ],
      "name": "春絲 牌南昌拌粉 209GM",
      "price": "$9",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20241028/cb4d6e38-a083-3354-b307-99f9b905cda6",
      "product_eng_name": "Chunsi Nanchang Rice Noodles 209GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8F%B0%E9%85%92%E8%8A%B1%E9%9B%95%E9%85%B8%E8%8F%9C%E7%89%9B%E8%82%89%E7%A2%97%E9%BA%B5%20200GM/i/101354930.html",
      "uid": "c75190189ba2c48938ea3ccc38ecc6d6",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "台酒花雕酸菜牛肉碗麵 200GM",
          "price": "$32",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230518/a744bff4-56ad-4d9d-a96e-fa184af7d178",
          "product_eng_name": "TTL Hua Tiao Chiew Beef Noodle With Pickled Vegetables 200GM"
        },
        {
          "name": "台酒花雕酸菜牛肉碗麵 200GM",
          "price": "$32",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230518/a744bff4-56ad-4d9d-a96e-fa184af7d178",
          "product_eng_name": "TTL Hua Tiao Chiew Beef Noodle With Pickled Vegetables 200GM"
        }
      ],
      "name": "台酒花雕酸菜牛肉碗麵 200GM",
      "price": "$32",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230518/a744bff4-56ad-4d9d-a96e-fa184af7d178",
      "product_eng_name": "TTL Hua Tiao Chiew Beef Noodle With Pickled Vegetables 200GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%A3%BD%E6%A1%83%E9%AE%91%E9%AD%9A%E5%B0%8F%E6%A9%8B%E7%B1%B3%E7%B7%9A%204%20X%20215GM/i/101370595.html",
      "uid": "8f49c3a1ef7d370abc9c9a1073502ac0",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "壽桃鮑魚小橋米線 4 X 215GM",
          "price": "$14",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220505/73ab0a4e-b15c-4461-9978-cf528c9baf9d",
          "product_eng_name": "Sau Tao Abalone Rice Vermicelli 4 X 215GM"
        },
        {
          "name": "壽桃鮑魚小橋米線 4 X 215GM",
          "price": "$14",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220505/73ab0a4e-b15c-4461-9978-cf528c9baf9d",
          "product_eng_name": "Sau Tao Abalone Rice Vermicelli 4 X 215GM"
        }
      ],
      "name": "壽桃鮑魚小橋米線 4 X 215GM",
      "price": "$14",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20220505/73ab0a4e-b15c-4461-9978-cf528c9baf9d",
      "product_eng_name": "Sau Tao Abalone Rice Vermicelli 4 X 215GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E6%97%A5%E6%B8%85%E5%90%88%E5%91%B3%E9%81%93%20%E8%B1%AC%E9%AA%A8%E6%B9%AF%E5%A4%A7%E6%9D%AF%E9%BA%B5%2012%20X%20107GM/i/113465619.html",
      "uid": "12d679f2635d26d0cdf65509acebc682",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱日清合味道 豬骨湯大杯麵 12 X 107GM",
          "price": "$105",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230728/8cc45d29-84e0-3384-a1a2-eee5d2228f1a",
          "product_eng_name": "Nissin Big Cup Tonkotsu Case 12 X 107GM"
        },
        {
          "name": "原箱日清合味道 豬骨湯大杯麵 12 X 107GM",
          "price": "$105",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230728/8cc45d29-84e0-3384-a1a2-eee5d2228f1a",
          "product_eng_name": "Nissin Big Cup Tonkotsu Case 12 X 107GM"
        }
      ],
      "name": "原箱日清合味道 豬骨湯大杯麵 12 X 107GM",
      "price": "$105",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230728/8cc45d29-84e0-3384-a1a2-eee5d2228f1a",
      "product_eng_name": "Nissin Big Cup Tonkotsu Case 12 X 107GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%AE%97%E5%AE%B6%E5%BA%9C%E5%B9%B4%E7%B3%95%E6%A2%9D%20500GM/i/101577447.html",
      "uid": "e65406e9f6c8f3ab90ebfef29ca64d8b",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "宗家府年糕條 500GM",
          "price": "$18",
          "offer": "【指定分類享$25換購】每買1件，即可以$25換購1件人氣產品；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20221014/516f71c7-9eee-4eb6-834b-786038934241",
          "product_eng_name": "Jongga Rice Cake Tubular 500GM"
        }
      ],
      "name": "宗家府年糕條 500GM",
      "price": "$18",
      "offer": "【指定分類享$25換購】每買1件，即可以$25換購1件人氣產品；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20221014/516f71c7-9eee-4eb6-834b-786038934241",
      "product_eng_name": "Jongga Rice Cake Tubular 500GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/PAIKCOOK%20%E7%99%BD%E7%A8%AE%E5%85%83%E9%A6%99%E8%BE%A3%E6%8B%89%E9%BA%B5%204%20X%20115GM/i/101343944.html",
      "uid": "f0a4286723902804c71cf53c67703549",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "PAIKCOOK 白種元香辣拉麵 4 X 115GM",
          "price": "$28",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250224/3e081263-3f11-3dc4-9235-4d73400d6d92",
          "product_eng_name": "Paik Cook Paik Ramen 4 X 115GM"
        },
        {
          "name": "PAIKCOOK 白種元香辣拉麵 4 X 115GM",
          "price": "$28",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250224/3e081263-3f11-3dc4-9235-4d73400d6d92",
          "product_eng_name": "Paik Cook Paik Ramen 4 X 115GM"
        }
      ],
      "name": "PAIKCOOK 白種元香辣拉麵 4 X 115GM",
      "price": "$28",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250224/3e081263-3f11-3dc4-9235-4d73400d6d92",
      "product_eng_name": "Paik Cook Paik Ramen 4 X 115GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%99%BD%E8%B1%A1%20%E8%B6%85%E5%A4%A7%E6%A1%B6%20%E9%A6%99%E8%BE%A3%E7%89%9B%E8%82%89%E7%89%9B%E8%82%89%E9%BA%B5%20%E7%A2%97%E9%BA%B5%20147GM/i/101344888.html",
      "uid": "e0f218b1a9f2cc92d37af935872c1d07",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "白象 超大桶 香辣牛肉牛肉麵 碗麵 147GM",
          "price": "$8",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250307/2ecde8ae-5bb1-3f9a-a578-2417ee8a64d3",
          "product_eng_name": "Baixiang Spicy Beef Big Bowl Ndl 144G"
        },
        {
          "name": "白象 超大桶 香辣牛肉牛肉麵 碗麵 147GM",
          "price": "$8",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250307/2ecde8ae-5bb1-3f9a-a578-2417ee8a64d3",
          "product_eng_name": "Baixiang Spicy Beef Big Bowl Ndl 144G"
        }
      ],
      "name": "白象 超大桶 香辣牛肉牛肉麵 碗麵 147GM",
      "price": "$8",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250307/2ecde8ae-5bb1-3f9a-a578-2417ee8a64d3",
      "product_eng_name": "Baixiang Spicy Beef Big Bowl Ndl 144G"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%97%A5%E6%B8%85%E5%87%BA%E5%89%8D%E4%B8%80%E4%B8%81%E4%B9%9D%E5%B7%9E%E8%B1%AC%E9%AA%A8%E6%B9%AF%E6%A3%92%E4%B8%81%E9%BA%B5%20186GM/i/101351589.html",
      "uid": "3f99571a72a162ad371b41ec1eaf751c",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "日清出前一丁九州豬骨湯棒丁麵 186GM",
          "price": "$10",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20200413/7a6a4c70-f6ba-46b3-aad6-b183a38dd33b",
          "product_eng_name": "Nissin Demae Iccho Kyushu Tonkotsu Noodles 186GM"
        },
        {
          "name": "日清出前一丁九州豬骨湯棒丁麵 186GM",
          "price": "$10",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20200413/7a6a4c70-f6ba-46b3-aad6-b183a38dd33b",
          "product_eng_name": "Nissin Demae Iccho Kyushu Tonkotsu Noodles 186GM"
        }
      ],
      "name": "日清出前一丁九州豬骨湯棒丁麵 186GM",
      "price": "$10",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20200413/7a6a4c70-f6ba-46b3-aad6-b183a38dd33b",
      "product_eng_name": "Nissin Demae Iccho Kyushu Tonkotsu Noodles 186GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%88%80%E5%98%9C%20%E7%B4%94%E6%AD%A3%E8%8A%A5%E8%8A%B1%E7%B1%BD%E6%B2%B9%205%20LT/i/113616051.html",
      "uid": "ec6c95f15198ff278ec6b6fa9997f72d",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "刀嘜 純正芥花籽油 5 LT",
          "price": "$142",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231011/75cf2c79-8dec-3b5b-b221-4ffe3922c247",
          "product_eng_name": "Knife Pure Canola Oil 5LT"
        },
        {
          "name": "刀嘜 純正芥花籽油 5 LT",
          "price": "$142",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231011/75cf2c79-8dec-3b5b-b221-4ffe3922c247",
          "product_eng_name": "Knife Pure Canola Oil 5LT"
        }
      ],
      "name": "刀嘜 純正芥花籽油 5 LT",
      "price": "$142",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20231011/75cf2c79-8dec-3b5b-b221-4ffe3922c247",
      "product_eng_name": "Knife Pure Canola Oil 5LT"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%9D%8E%E9%8C%A6%E8%A8%98%E7%B4%94%E9%A6%99%E8%8A%9D%E9%BA%BB%E6%B2%B9%20115ML/i/101350440.html",
      "uid": "8ad084f4c5cfe31186c69da7a0c1fea8",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "李錦記純香芝麻油 115ML",
          "price": "$16",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210524/a7960950-ae81-44ef-b164-26ec402efce3",
          "product_eng_name": "Lee Kum Kee Pure Sesame Oil 115ML"
        },
        {
          "name": "李錦記純香芝麻油 115ML",
          "price": "$16",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210524/a7960950-ae81-44ef-b164-26ec402efce3",
          "product_eng_name": "Lee Kum Kee Pure Sesame Oil 115ML"
        }
      ],
      "name": "李錦記純香芝麻油 115ML",
      "price": "$16",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210524/a7960950-ae81-44ef-b164-26ec402efce3",
      "product_eng_name": "Lee Kum Kee Pure Sesame Oil 115ML"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/Meadows%E6%B8%85%E6%B7%A1%E6%A9%84%E6%AC%96%E6%B2%B9%201LT/i/101837275.html",
      "uid": "4029451d993c985891d2fcfa6458f85b",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "Meadows清淡橄欖油 1LT",
          "price": "$190",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231204/3d999ef4-8a79-318e-a567-de1b7420cb8b",
          "product_eng_name": "Meadows Extra Light Olive Oil 1LT"
        },
        {
          "name": "Meadows清淡橄欖油 1LT",
          "price": "$190",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231204/3d999ef4-8a79-318e-a567-de1b7420cb8b",
          "product_eng_name": "Meadows Extra Light Olive Oil 1LT"
        }
      ],
      "name": "Meadows清淡橄欖油 1LT",
      "price": "$190",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20231204/3d999ef4-8a79-318e-a567-de1b7420cb8b",
      "product_eng_name": "Meadows Extra Light Olive Oil 1LT"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E4%BF%9D%E5%BE%97%20%E8%91%A1%E8%90%84%E7%B1%BD%E6%B2%B9%201LT/i/113267969.html",
      "uid": "47aff0fd5d9d3d7f5751334a4136f50f",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "保得 葡萄籽油 1LT",
          "price": "$89",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230209/01f6013a-7291-47fa-bebf-5cead1787ae5",
          "product_eng_name": "Bontaste Grapeseed Oil 1LT"
        },
        {
          "name": "保得 葡萄籽油 1LT",
          "price": "$89",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230209/01f6013a-7291-47fa-bebf-5cead1787ae5",
          "product_eng_name": "Bontaste Grapeseed Oil 1LT"
        }
      ],
      "name": "保得 葡萄籽油 1LT",
      "price": "$89",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230209/01f6013a-7291-47fa-bebf-5cead1787ae5",
      "product_eng_name": "Bontaste Grapeseed Oil 1LT"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E9%87%91%E6%9A%B9%E9%A0%82%E7%B4%9A%E6%B3%B0%E5%9C%8B%E9%A6%99%E7%B1%B3%2010KG/i/101344236.html",
      "uid": "e93928190997427a41a4b06b0293c0ed",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "金暹頂級泰國香米 10KG",
          "price": "$99",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230317/7046892f-a6af-4b39-89ac-0b39f06ec4b5",
          "product_eng_name": "Golden Thai Premium Fragrant Rice 10KG"
        }
      ],
      "name": "金暹頂級泰國香米 10KG",
      "price": "$99",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230317/7046892f-a6af-4b39-89ac-0b39f06ec4b5",
      "product_eng_name": "Golden Thai Premium Fragrant Rice 10KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/Meadows%E5%88%9D%E6%A6%A8%E6%A9%84%E6%AC%96%E6%B2%B9%20500ML/i/101837289.html",
      "uid": "2ee43e88131e348ac656e1d49d5bb8cf",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "Meadows初榨橄欖油 500ML",
          "price": "$89",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231204/87deeab5-3e82-3583-9228-17af3d9d8d8b",
          "product_eng_name": "Meadows Extra Virgin Olive Oil 500ML"
        },
        {
          "name": "Meadows初榨橄欖油 500ML",
          "price": "$89",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231204/87deeab5-3e82-3583-9228-17af3d9d8d8b",
          "product_eng_name": "Meadows Extra Virgin Olive Oil 500ML"
        }
      ],
      "name": "Meadows初榨橄欖油 500ML",
      "price": "$89",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20231204/87deeab5-3e82-3583-9228-17af3d9d8d8b",
      "product_eng_name": "Meadows Extra Virgin Olive Oil 500ML"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E8%B6%85%E5%8A%9B%20%E5%8D%B3%E9%A3%9F%E9%8A%80%E7%B5%B2%E7%B1%B3%E7%B2%89%2030%20X%2065GM/i/101334419.html",
      "uid": "6e3ae6f4a5b80f1e86b3e6bd3bcb691f",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱超力 即食銀絲米粉 30 X 65GM",
          "price": "$105",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230202/bfaf46a9-8e0e-4bf5-bcde-d60775a9886b",
          "product_eng_name": "Chewy Instant Mei Fun Case 30 X 65GM"
        },
        {
          "name": "原箱超力 即食銀絲米粉 30 X 65GM",
          "price": "$105",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230202/bfaf46a9-8e0e-4bf5-bcde-d60775a9886b",
          "product_eng_name": "Chewy Instant Mei Fun Case 30 X 65GM"
        }
      ],
      "name": "原箱超力 即食銀絲米粉 30 X 65GM",
      "price": "$105",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230202/bfaf46a9-8e0e-4bf5-bcde-d60775a9886b",
      "product_eng_name": "Chewy Instant Mei Fun Case 30 X 65GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%9C%88%E7%A8%BB%E9%AB%98%E7%B4%9A%E6%B3%B0%E5%9C%8B%E9%A6%99%E7%B1%B3%208KG/i/101356052.html",
      "uid": "5857428e163219920e341acd2f2aa4dd",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "月稻高級泰國香米 8KG",
          "price": "$122",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250327/20353822-1d2b-33d7-b4b6-e2b0706b6b3a",
          "product_eng_name": "Moon Seed Thai Fragant Rice 8KG"
        }
      ],
      "name": "月稻高級泰國香米 8KG",
      "price": "$122",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250327/20353822-1d2b-33d7-b4b6-e2b0706b6b3a",
      "product_eng_name": "Moon Seed Thai Fragant Rice 8KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%99%BD%E8%B1%A1%20%E8%80%81%E5%A3%87%E9%85%B8%E8%8F%9C%E7%89%9B%E8%82%89%E9%BA%B5%E7%A2%97%E9%BA%B5%20163%20GM/i/115054364.html",
      "uid": "4d5d8fdfb82dfc51fa5bbf2e56d2d290",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "白象 老壇酸菜牛肉麵碗麵 163 GM",
          "price": "$8",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250307/4bf61a31-d86a-3569-9a74-571a3bd294ce",
          "product_eng_name": "Baixiang Sauerkrut Beef Bowl Noodles 163GM"
        },
        {
          "name": "白象 老壇酸菜牛肉麵碗麵 163 GM",
          "price": "$8",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250307/4bf61a31-d86a-3569-9a74-571a3bd294ce",
          "product_eng_name": "Baixiang Sauerkrut Beef Bowl Noodles 163GM"
        }
      ],
      "name": "白象 老壇酸菜牛肉麵碗麵 163 GM",
      "price": "$8",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250307/4bf61a31-d86a-3569-9a74-571a3bd294ce",
      "product_eng_name": "Baixiang Sauerkrut Beef Bowl Noodles 163GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E5%BE%A1%E5%93%81%E7%9A%87%20%E8%80%81%E6%AF%8D%E9%9B%9E%E5%91%B3%E6%B9%AF%E9%BA%B5%20103%20GM/i/113612071.html",
      "uid": "b10aaab705531e6e021dbb97ea9ad8e2",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱御品皇 老母雞味湯麵 103 GM",
          "price": "$120",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230926/724c134c-7a17-3001-b8c4-4e46ec4d6f0c",
          "product_eng_name": "Yu Pin King Chicken Flavour Soup Noodles 30 x 103GM"
        },
        {
          "name": "原箱御品皇 老母雞味湯麵 103 GM",
          "price": "$120",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230926/724c134c-7a17-3001-b8c4-4e46ec4d6f0c",
          "product_eng_name": "Yu Pin King Chicken Flavour Soup Noodles 30 x 103GM"
        }
      ],
      "name": "原箱御品皇 老母雞味湯麵 103 GM",
      "price": "$120",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230926/724c134c-7a17-3001-b8c4-4e46ec4d6f0c",
      "product_eng_name": "Yu Pin King Chicken Flavour Soup Noodles 30 x 103GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%A3%BD%E6%A1%83%E7%89%8C%E5%8C%97%E4%BA%AC%E6%8B%89%E9%BA%B5%20375GM/i/101349378.html",
      "uid": "6c2a4edcc94133ed470033e55c537b1d",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "壽桃牌北京拉麵 375GM",
          "price": "$7",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220505/1c11cb7b-ac17-4513-8159-5ca15260d972",
          "product_eng_name": "Sau Tao Beijing Noodle 375GM"
        },
        {
          "name": "壽桃牌北京拉麵 375GM",
          "price": "$7",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220505/1c11cb7b-ac17-4513-8159-5ca15260d972",
          "product_eng_name": "Sau Tao Beijing Noodle 375GM"
        }
      ],
      "name": "壽桃牌北京拉麵 375GM",
      "price": "$7",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20220505/1c11cb7b-ac17-4513-8159-5ca15260d972",
      "product_eng_name": "Sau Tao Beijing Noodle 375GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%86%8A%E4%BA%95%E7%8F%8D%E7%8F%A0%E7%B1%B3%208KG/i/101330223.html",
      "uid": "f78ea745a175b8729ae368b1fc39816b",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "熊井珍珠米 8KG",
          "price": "$109",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250313/5872e422-76e1-3039-93e0-19452b1689bb",
          "product_eng_name": "Kumai American Pearl Rice 8KG"
        }
      ],
      "name": "熊井珍珠米 8KG",
      "price": "$109",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250313/5872e422-76e1-3039-93e0-19452b1689bb",
      "product_eng_name": "Kumai American Pearl Rice 8KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%97%A5%E6%B8%85%E5%87%BA%E5%89%8D%E4%B8%80%E4%B8%81%E4%B9%9D%E5%B7%9E%E8%B1%AC%E9%AA%A8%E6%BF%83%E6%B9%AF%E9%BA%B5%20100GM/i/101354717.html",
      "uid": "902b11b7e9e6a95a441db0b322bd8ab9",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "日清出前一丁九州豬骨濃湯麵 100GM",
          "price": "$5",
          "offer": "【8件$28.5】$28.5任揀8件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250407/4a8d8d01-b2f5-3ffc-a711-a2f2a60bbb0c",
          "product_eng_name": "Nissin Demae Iccho Tonkotsu Noodle 100GM"
        },
        {
          "name": "日清出前一丁九州豬骨濃湯麵 100GM",
          "price": "$5",
          "offer": "【8件$28.5】$28.5任揀8件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250407/4a8d8d01-b2f5-3ffc-a711-a2f2a60bbb0c",
          "product_eng_name": "Nissin Demae Iccho Tonkotsu Noodle 100GM"
        }
      ],
      "name": "日清出前一丁九州豬骨濃湯麵 100GM",
      "price": "$5",
      "offer": "【8件$28.5】$28.5任揀8件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250407/4a8d8d01-b2f5-3ffc-a711-a2f2a60bbb0c",
      "product_eng_name": "Nissin Demae Iccho Tonkotsu Noodle 100GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%85%AC%E4%BB%94%E5%85%AC%E4%BB%94%E7%82%92%E9%BA%B5%E7%8E%8B%E9%BA%BB%E8%BE%A3%E5%91%B3%E5%8D%B3%E9%A3%9F%E9%BA%B5%20112GM/i/101381802.html",
      "uid": "3e748f189fe6fa9135b60758753d137f",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "公仔公仔炒麵王麻辣味即食麵 112GM",
          "price": "$7",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250320/9c85423f-4134-3b45-9e78-a4ee800de759",
          "product_eng_name": "Doll Fried Noodle Mala Flavour 112GM"
        },
        {
          "name": "公仔公仔炒麵王麻辣味即食麵 112GM",
          "price": "$7",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250320/9c85423f-4134-3b45-9e78-a4ee800de759",
          "product_eng_name": "Doll Fried Noodle Mala Flavour 112GM"
        }
      ],
      "name": "公仔公仔炒麵王麻辣味即食麵 112GM",
      "price": "$7",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250320/9c85423f-4134-3b45-9e78-a4ee800de759",
      "product_eng_name": "Doll Fried Noodle Mala Flavour 112GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%85%AB%E9%81%93%20%E6%B5%B7%E9%AE%AE%E9%86%AC%E6%B2%B9%E6%92%88%E9%BA%B5%20130%20GM/i/114910516.html",
      "uid": "616e60de3b5010971a9de8daec838220",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "八道 海鮮醬油撈麵 130 GM",
          "price": "$27",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20241017/26f70f65-235f-35a6-a3ec-0fd9194d2373",
          "product_eng_name": "Paldo Seafood Bibimmen II Noodles 4 x 130GM"
        },
        {
          "name": "八道 海鮮醬油撈麵 130 GM",
          "price": "$27",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20241017/26f70f65-235f-35a6-a3ec-0fd9194d2373",
          "product_eng_name": "Paldo Seafood Bibimmen II Noodles 4 x 130GM"
        }
      ],
      "name": "八道 海鮮醬油撈麵 130 GM",
      "price": "$27",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20241017/26f70f65-235f-35a6-a3ec-0fd9194d2373",
      "product_eng_name": "Paldo Seafood Bibimmen II Noodles 4 x 130GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E9%87%91%E9%B3%B3%20%E6%B3%B0%E5%9C%8B%E9%A0%82%E7%B4%9A%E9%A6%99%E7%B3%99%E7%B1%B3%201.5%20KGM/i/115044821.html",
      "uid": "b02e083382f4e5cf89525995df8ce6ab",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "金鳳 泰國頂級香糙米 1.5 KGM",
          "price": "$40",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250307/1a44e41d-5e6c-3d21-a129-10235a07aefb",
          "product_eng_name": "GOLDEN PHOENIX THAI BROWN RICE 1.5 KG"
        }
      ],
      "name": "金鳳 泰國頂級香糙米 1.5 KGM",
      "price": "$40",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250307/1a44e41d-5e6c-3d21-a129-10235a07aefb",
      "product_eng_name": "GOLDEN PHOENIX THAI BROWN RICE 1.5 KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E8%A2%8B%E9%BC%A0%E7%89%8C%E7%B2%BE%E9%81%B8%E7%B5%B2%E8%8B%97%208KG/i/101345455.html",
      "uid": "1d7cbe1f14ee5b78b88dc93b11745c51",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "袋鼠牌精選絲苗 8KG",
          "price": "$86",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230726/5f16ac12-97f0-49e6-bcb9-ccd550770ee0",
          "product_eng_name": "Kangaroo Seemew Rice 8KG"
        }
      ],
      "name": "袋鼠牌精選絲苗 8KG",
      "price": "$86",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230726/5f16ac12-97f0-49e6-bcb9-ccd550770ee0",
      "product_eng_name": "Kangaroo Seemew Rice 8KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E4%B8%89%E9%A4%8A%20%E5%A5%B6%E6%B2%B9%E7%8E%AB%E7%91%B0%E8%BE%A3%E9%9B%9E%E6%92%88%E9%BA%B5%20105%20GM/i/114326946.html",
      "uid": "caf03b1601293b33169b825772b5263c",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "三養 奶油玫瑰辣雞撈麵 105 GM",
          "price": "$11",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240826/b5cb37e4-0908-3558-97a4-8dc634e21459",
          "product_eng_name": "Samyang Rosé Buldak Hot Chicken Ramen Bowl 105GM"
        },
        {
          "name": "三養 奶油玫瑰辣雞撈麵 105 GM",
          "price": "$11",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240826/b5cb37e4-0908-3558-97a4-8dc634e21459",
          "product_eng_name": "Samyang Rosé Buldak Hot Chicken Ramen Bowl 105GM"
        }
      ],
      "name": "三養 奶油玫瑰辣雞撈麵 105 GM",
      "price": "$11",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240826/b5cb37e4-0908-3558-97a4-8dc634e21459",
      "product_eng_name": "Samyang Rosé Buldak Hot Chicken Ramen Bowl 105GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%B0%B8%E6%A8%82%E7%B2%89%E9%BA%B5%E5%BB%A0%E6%BF%83%E9%A6%99%E6%BC%81%E6%B9%AF%E8%8A%AB%E8%8D%BD%E9%BA%B5%2012PC/i/113323268.html",
      "uid": "51105f33cdc2455330119cc2f6ecf3e7",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "永樂粉麵廠濃香漁湯芫荽麵 12PC",
          "price": "$85",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230411/8f603fc9-94aa-4faa-bc42-c6c8856648f2",
          "product_eng_name": "Wing Lok Coriander Fish Soup Noodle 12PC"
        },
        {
          "name": "永樂粉麵廠濃香漁湯芫荽麵 12PC",
          "price": "$85",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230411/8f603fc9-94aa-4faa-bc42-c6c8856648f2",
          "product_eng_name": "Wing Lok Coriander Fish Soup Noodle 12PC"
        }
      ],
      "name": "永樂粉麵廠濃香漁湯芫荽麵 12PC",
      "price": "$85",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230411/8f603fc9-94aa-4faa-bc42-c6c8856648f2",
      "product_eng_name": "Wing Lok Coriander Fish Soup Noodle 12PC"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%A6%8F%E5%AD%97%E9%9B%9E%E6%B9%AF%E5%91%B3%E7%B1%B3%E7%B2%89%205%20X%2055GM/i/101578495.html",
      "uid": "6988d4a128a1eb1dcb10b295345e327a",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "福字雞湯味米粉 5 X 55GM",
          "price": "$16",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210920/668dce5c-5678-4cf6-9f89-c4b9a79e9eb3",
          "product_eng_name": "Fuku Bi Hun Soto Mifun 5 X 55GM"
        },
        {
          "name": "福字雞湯味米粉 5 X 55GM",
          "price": "$16",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210920/668dce5c-5678-4cf6-9f89-c4b9a79e9eb3",
          "product_eng_name": "Fuku Bi Hun Soto Mifun 5 X 55GM"
        }
      ],
      "name": "福字雞湯味米粉 5 X 55GM",
      "price": "$16",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210920/668dce5c-5678-4cf6-9f89-c4b9a79e9eb3",
      "product_eng_name": "Fuku Bi Hun Soto Mifun 5 X 55GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E4%B8%8D%E5%80%92%E7%BF%81%E9%87%91%E6%8B%89%E9%BA%B5%205%20X%20120GM/i/101342808.html",
      "uid": "dd2e8a36835551b26670fd37badf56c7",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "不倒翁金拉麵 5 X 120GM",
          "price": "$28",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231011/f5058885-27bc-3284-8977-dc52377febb7",
          "product_eng_name": "Ottogi Jin Ramen (Mild) 5 x 120GM"
        },
        {
          "name": "不倒翁金拉麵 5 X 120GM",
          "price": "$28",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231011/f5058885-27bc-3284-8977-dc52377febb7",
          "product_eng_name": "Ottogi Jin Ramen (Mild) 5 x 120GM"
        }
      ],
      "name": "不倒翁金拉麵 5 X 120GM",
      "price": "$28",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20231011/f5058885-27bc-3284-8977-dc52377febb7",
      "product_eng_name": "Ottogi Jin Ramen (Mild) 5 x 120GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%99%BD%E8%B1%A1%20%E6%B9%AF%E5%A5%BD%E5%96%9D%E8%BE%A3%E7%89%9B%E8%82%89%E6%B9%AF%E5%91%B3%E9%BA%B55%E9%80%A3%E5%8C%85%20111%20GM/i/102098801.html",
      "uid": "c3108835bb8c416c2252b52333134d24",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "白象 湯好喝辣牛肉湯味麵5連包 111 GM",
          "price": "$40",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230330/20545f84-0525-4aa8-8c91-f392c0233715",
          "product_eng_name": "BAI XIANG SPICY BEEF SOUP FLV INST NOODLE 5S PACK 111 GM"
        },
        {
          "name": "白象 湯好喝辣牛肉湯味麵5連包 111 GM",
          "price": "$40",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230330/20545f84-0525-4aa8-8c91-f392c0233715",
          "product_eng_name": "BAI XIANG SPICY BEEF SOUP FLV INST NOODLE 5S PACK 111 GM"
        }
      ],
      "name": "白象 湯好喝辣牛肉湯味麵5連包 111 GM",
      "price": "$40",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230330/20545f84-0525-4aa8-8c91-f392c0233715",
      "product_eng_name": "BAI XIANG SPICY BEEF SOUP FLV INST NOODLE 5S PACK 111 GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E8%BE%B2%E5%BF%83%E8%A3%9D%E8%BE%9B%E6%8B%89%E9%BA%B5%205%20X%20120GM/i/101344977.html",
      "uid": "80545aa17a291fd847c2986b3adf3eba",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "農心裝辛拉麵 5 X 120GM",
          "price": "$20",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210325/ae790a06-b482-4368-98de-2e44769d67c9",
          "product_eng_name": "Nong Shim Shin Ramyun 5 X 120GM"
        },
        {
          "name": "農心裝辛拉麵 5 X 120GM",
          "price": "$20",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210325/ae790a06-b482-4368-98de-2e44769d67c9",
          "product_eng_name": "Nong Shim Shin Ramyun 5 X 120GM"
        }
      ],
      "name": "農心裝辛拉麵 5 X 120GM",
      "price": "$20",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210325/ae790a06-b482-4368-98de-2e44769d67c9",
      "product_eng_name": "Nong Shim Shin Ramyun 5 X 120GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%A6%8F%E5%AD%97%E4%B8%8A%E6%B9%AF%E4%BC%8A%E9%BA%B5%2090GM/i/101343615.html",
      "uid": "1b3a9d24016ad748c286bfba282ce7d1",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "福字上湯伊麵 90GM",
          "price": "$5",
          "offer": "【3件$9.5】$9.5任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210513/1a17f615-78f5-4ff2-82c0-daace21ecc1f",
          "product_eng_name": "Fuku Instant Noodle 90GM"
        },
        {
          "name": "福字上湯伊麵 90GM",
          "price": "$5",
          "offer": "【3件$9.5】$9.5任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210513/1a17f615-78f5-4ff2-82c0-daace21ecc1f",
          "product_eng_name": "Fuku Instant Noodle 90GM"
        }
      ],
      "name": "福字上湯伊麵 90GM",
      "price": "$5",
      "offer": "【3件$9.5】$9.5任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210513/1a17f615-78f5-4ff2-82c0-daace21ecc1f",
      "product_eng_name": "Fuku Instant Noodle 90GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E8%B1%A1%E7%9A%87%20%E6%B3%B0%E5%9C%8B%E6%A5%B5%E4%B8%8A%E8%8C%89%E8%8E%89%E9%A6%99%E7%B1%B3%205%20KG/i/113632936.html",
      "uid": "1af596b0aa2ba9963f49f151e2626838",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "象皇 泰國極上茉莉香米 5 KG",
          "price": "$89",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240425/3d95a007-2ef9-382f-b23f-9d056245ddd9",
          "product_eng_name": "Royal Elephant Premium Thai Hom Mali Rice 5KG"
        }
      ],
      "name": "象皇 泰國極上茉莉香米 5 KG",
      "price": "$89",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240425/3d95a007-2ef9-382f-b23f-9d056245ddd9",
      "product_eng_name": "Royal Elephant Premium Thai Hom Mali Rice 5KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8A%9F%E5%BE%B7%E6%9E%97-%E4%B8%80%E5%93%81%E7%B4%A0%E9%BA%B5%E9%A6%99%E8%8F%87%E9%87%8E%E8%8F%9C%E9%BA%B5%205%20X%2085GM/i/101340608.html",
      "uid": "a007990038e9e11340b9649e76d85ea2",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "功德林-一品素麵香菇野菜麵 5 X 85GM",
          "price": "$8",
          "offer": "【2件$30】$30任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210125/9259c123-52ee-46e8-9a39-ae138684d678",
          "product_eng_name": "Kung Tak Lam Vegetable Mushroom Noodles 5 x 85GM"
        },
        {
          "name": "功德林-一品素麵香菇野菜麵 5 X 85GM",
          "price": "$8",
          "offer": "【2件$30】$30任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210125/9259c123-52ee-46e8-9a39-ae138684d678",
          "product_eng_name": "Kung Tak Lam Vegetable Mushroom Noodles 5 x 85GM"
        }
      ],
      "name": "功德林-一品素麵香菇野菜麵 5 X 85GM",
      "price": "$8",
      "offer": "【2件$30】$30任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210125/9259c123-52ee-46e8-9a39-ae138684d678",
      "product_eng_name": "Kung Tak Lam Vegetable Mushroom Noodles 5 x 85GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E8%9E%BA%E9%9C%B8%E7%8E%8B%20%E8%9E%BA%E8%9E%84%E7%B2%89%E6%9D%AF%E9%BA%B5%20210GM/i/101341228.html",
      "uid": "7772f905d9d90cd5581e4e42d45e7d96",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "螺霸王 螺螄粉杯麵 210GM",
          "price": "$11",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240124/05ff55a0-606e-3368-b964-ecb519094731",
          "product_eng_name": "No Wang Snail Noodles Cup 210GM"
        },
        {
          "name": "螺霸王 螺螄粉杯麵 210GM",
          "price": "$11",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240124/05ff55a0-606e-3368-b964-ecb519094731",
          "product_eng_name": "No Wang Snail Noodles Cup 210GM"
        }
      ],
      "name": "螺霸王 螺螄粉杯麵 210GM",
      "price": "$11",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240124/05ff55a0-606e-3368-b964-ecb519094731",
      "product_eng_name": "No Wang Snail Noodles Cup 210GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%99%BE%E5%BE%97%E9%98%BF%E5%A7%A8%E5%8D%83%E5%B1%A4%E9%BA%B5%20500GM/i/101350713.html",
      "uid": "b04959feb9a678825a517642e3d2f548",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "百得阿姨千層麵 500GM",
          "price": "$38",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240916/f1dfff2e-e564-33d2-ba01-6c76c334602e",
          "product_eng_name": "Barilla Lasagna Semola 500GM"
        },
        {
          "name": "百得阿姨千層麵 500GM",
          "price": "$38",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240916/f1dfff2e-e564-33d2-ba01-6c76c334602e",
          "product_eng_name": "Barilla Lasagna Semola 500GM"
        }
      ],
      "name": "百得阿姨千層麵 500GM",
      "price": "$38",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240916/f1dfff2e-e564-33d2-ba01-6c76c334602e",
      "product_eng_name": "Barilla Lasagna Semola 500GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%85%AC%E4%BB%94%E7%82%92%E9%BA%B5%E7%8E%8B%E6%B8%AF%E5%BC%8F%E6%B2%99%E5%97%B2%E7%89%9B%E8%82%89%E5%91%B3%20108GM/i/113562914.html",
      "uid": "ead7cf68385bc521c9edab615afde2a5",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "公仔炒麵王港式沙嗲牛肉味 108GM",
          "price": "$7",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20241227/75c1e5a4-1da0-3ffd-85f7-865eff709c35",
          "product_eng_name": "Doll Fried Noodle Hong Kong Style Satay Beef Flavour 108GM"
        },
        {
          "name": "公仔炒麵王港式沙嗲牛肉味 108GM",
          "price": "$7",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20241227/75c1e5a4-1da0-3ffd-85f7-865eff709c35",
          "product_eng_name": "Doll Fried Noodle Hong Kong Style Satay Beef Flavour 108GM"
        }
      ],
      "name": "公仔炒麵王港式沙嗲牛肉味 108GM",
      "price": "$7",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20241227/75c1e5a4-1da0-3ffd-85f7-865eff709c35",
      "product_eng_name": "Doll Fried Noodle Hong Kong Style Satay Beef Flavour 108GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E9%87%91%E6%BB%BF%E5%AE%B6%E9%A6%99%E7%A8%BB%E7%B5%B2%E8%8B%97%203KG/i/101350094.html",
      "uid": "deb1d6f265b80d7b151e40c00d0a864d",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "金滿家香稻絲苗 3KG",
          "price": "$57",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210511/918230f3-e6f1-466b-9993-519a8deaecc5",
          "product_eng_name": "Golden Home Long Grain White Rice 3KG"
        }
      ],
      "name": "金滿家香稻絲苗 3KG",
      "price": "$57",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210511/918230f3-e6f1-466b-9993-519a8deaecc5",
      "product_eng_name": "Golden Home Long Grain White Rice 3KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E9%9B%85%E5%8F%94%E4%B8%8A%E6%B5%B7%E8%94%A5%E6%B2%B9%E6%8B%8C%E9%BA%B5(2%E4%BA%BA%E4%BB%BD)%20270%E5%85%8B/i/101355032.html",
      "uid": "7df69770ec78e25d9e50108e30dc996d",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "雅叔上海蔥油拌麵(2人份) 270克",
          "price": "$13",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240312/eac66209-7d7f-3eb6-a0fe-9f18e6423128",
          "product_eng_name": "Ya Shu Shanghai Scallion Oil Noodles (2Bag) 270G"
        },
        {
          "name": "雅叔上海蔥油拌麵(2人份) 270克",
          "price": "$13",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240312/eac66209-7d7f-3eb6-a0fe-9f18e6423128",
          "product_eng_name": "Ya Shu Shanghai Scallion Oil Noodles (2Bag) 270G"
        }
      ],
      "name": "雅叔上海蔥油拌麵(2人份) 270克",
      "price": "$13",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240312/eac66209-7d7f-3eb6-a0fe-9f18e6423128",
      "product_eng_name": "Ya Shu Shanghai Scallion Oil Noodles (2Bag) 270G"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%A3%BD%E6%A1%83%E8%95%83%E8%8C%84%E5%B0%8F%E6%A9%8B%E7%B1%B3%E7%B7%9A%204%20X%20215GM/i/101342460.html",
      "uid": "cf0c8ace02f2fbc3f1604d0cb34b0e2b",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "壽桃蕃茄小橋米線 4 X 215GM",
          "price": "$14",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220505/a95dc129-a819-4a6d-b0a8-b60574a95e55",
          "product_eng_name": "Sau Tao Tomato Rice Vermicelli 4 X 215GM"
        },
        {
          "name": "壽桃蕃茄小橋米線 4 X 215GM",
          "price": "$14",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220505/a95dc129-a819-4a6d-b0a8-b60574a95e55",
          "product_eng_name": "Sau Tao Tomato Rice Vermicelli 4 X 215GM"
        }
      ],
      "name": "壽桃蕃茄小橋米線 4 X 215GM",
      "price": "$14",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20220505/a95dc129-a819-4a6d-b0a8-b60574a95e55",
      "product_eng_name": "Sau Tao Tomato Rice Vermicelli 4 X 215GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/ACE%E5%8C%97%E6%B5%B7%E9%81%93%E6%89%8B%E6%89%93%E9%A2%A8%E7%83%8F%E5%86%AC%20%204%20X%20200GM/i/101323956.html",
      "uid": "2a85a688f09ab6be8eecff397bc1c8f4",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "ACE北海道手打風烏冬 4 X 200GM",
          "price": "$19",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231211/20323f12-a88e-3155-8b9d-7330c76e0fb8",
          "product_eng_name": "ACE Hokkaido Udon 4 x 200GM"
        },
        {
          "name": "ACE北海道手打風烏冬 4 X 200GM",
          "price": "$19",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231211/20323f12-a88e-3155-8b9d-7330c76e0fb8",
          "product_eng_name": "ACE Hokkaido Udon 4 x 200GM"
        }
      ],
      "name": "ACE北海道手打風烏冬 4 X 200GM",
      "price": "$19",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20231211/20323f12-a88e-3155-8b9d-7330c76e0fb8",
      "product_eng_name": "ACE Hokkaido Udon 4 x 200GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%85%AC%E4%BB%94%E9%9B%AA%E8%8F%9C%E5%91%B3%E7%B1%B3%E7%B2%89%2070GM/i/101341224.html",
      "uid": "72c5f53bf6870e693e33d9f4b945537f",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "公仔雪菜味米粉 70GM",
          "price": "$4",
          "offer": "【3件$9】$9任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210621/2154dabb-626f-4cf4-9eec-6c7c329dbad5",
          "product_eng_name": "Doll Pickled Vegetable Vermicelli 70GM"
        },
        {
          "name": "公仔雪菜味米粉 70GM",
          "price": "$4",
          "offer": "【3件$9】$9任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210621/2154dabb-626f-4cf4-9eec-6c7c329dbad5",
          "product_eng_name": "Doll Pickled Vegetable Vermicelli 70GM"
        }
      ],
      "name": "公仔雪菜味米粉 70GM",
      "price": "$4",
      "offer": "【3件$9】$9任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210621/2154dabb-626f-4cf4-9eec-6c7c329dbad5",
      "product_eng_name": "Doll Pickled Vegetable Vermicelli 70GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%B7%98%E5%A4%A7%E7%B4%94%E8%8A%9D%E9%BA%BB%E6%B2%B9%20150ML/i/101345037.html",
      "uid": "7a580fd3dbac2efb4e9b6afb062d0043",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "淘大純芝麻油 150ML",
          "price": "$22",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210126/05c9dd75-9921-465d-91d0-a4bcc06f665e",
          "product_eng_name": "Amoy Pure Sesame Oil 150ML"
        },
        {
          "name": "淘大純芝麻油 150ML",
          "price": "$22",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210126/05c9dd75-9921-465d-91d0-a4bcc06f665e",
          "product_eng_name": "Amoy Pure Sesame Oil 150ML"
        }
      ],
      "name": "淘大純芝麻油 150ML",
      "price": "$22",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210126/05c9dd75-9921-465d-91d0-a4bcc06f665e",
      "product_eng_name": "Amoy Pure Sesame Oil 150ML"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%BE%A1%E5%93%81%E7%9A%87%E7%B4%94%E6%AD%A3%E8%8A%A5%E8%8A%B1%E7%B1%BD%E6%B2%B9%20700ML/i/101573379.html",
      "uid": "37b89163c2ec1836ad4591b6630b96bd",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "御品皇純正芥花籽油 700ML",
          "price": "$20",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210426/3b1489db-5921-4f9d-b3e6-74aa2a0f916e",
          "product_eng_name": "Yu Pin King Pure Canola Oil 700ML"
        },
        {
          "name": "御品皇純正芥花籽油 700ML",
          "price": "$20",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210426/3b1489db-5921-4f9d-b3e6-74aa2a0f916e",
          "product_eng_name": "Yu Pin King Pure Canola Oil 700ML"
        }
      ],
      "name": "御品皇純正芥花籽油 700ML",
      "price": "$20",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210426/3b1489db-5921-4f9d-b3e6-74aa2a0f916e",
      "product_eng_name": "Yu Pin King Pure Canola Oil 700ML"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%B7%98%E5%A4%A7%E5%B0%8F%E8%98%91%E9%BA%BB%E6%B2%B9%20150ML/i/101343821.html",
      "uid": "549054d1befaa9c4874f1134685186db",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "淘大小蘑麻油 150ML",
          "price": "$14",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250314/ffd96bc1-2993-355b-b0fc-80181b3ef1e5",
          "product_eng_name": "Amoy Oil Sesame 150ML"
        },
        {
          "name": "淘大小蘑麻油 150ML",
          "price": "$14",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250314/ffd96bc1-2993-355b-b0fc-80181b3ef1e5",
          "product_eng_name": "Amoy Oil Sesame 150ML"
        }
      ],
      "name": "淘大小蘑麻油 150ML",
      "price": "$14",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250314/ffd96bc1-2993-355b-b0fc-80181b3ef1e5",
      "product_eng_name": "Amoy Oil Sesame 150ML"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E9%8A%80%E8%8A%B1%E9%9D%9A%E7%B1%B3%208KG/i/101355336.html",
      "uid": "a9d35bd7b01e3e189f429627780a0424",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "銀花靚米 8KG",
          "price": "$73",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230321/02ed53e1-cab9-4ae2-b160-8f2a12aa4b1c",
          "product_eng_name": "Silverblossom Quality Rice 8KG"
        }
      ],
      "name": "銀花靚米 8KG",
      "price": "$73",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230321/02ed53e1-cab9-4ae2-b160-8f2a12aa4b1c",
      "product_eng_name": "Silverblossom Quality Rice 8KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E8%B6%85%E5%8A%9B%20%E5%9B%9B%E7%89%87%E8%A3%9D%E7%B1%B3%E7%B2%89%20280GM/i/101342384.html",
      "uid": "356fa6150210a3bbedf3ab487c079e8b",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱超力 四片裝米粉 280GM",
          "price": "$131",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230202/84345d6a-baba-4cb6-b1db-78b217967af1",
          "product_eng_name": "Chewy Instant Rice Vermicelli Case 12 x 280GM"
        },
        {
          "name": "原箱超力 四片裝米粉 280GM",
          "price": "$131",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230202/84345d6a-baba-4cb6-b1db-78b217967af1",
          "product_eng_name": "Chewy Instant Rice Vermicelli Case 12 x 280GM"
        }
      ],
      "name": "原箱超力 四片裝米粉 280GM",
      "price": "$131",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230202/84345d6a-baba-4cb6-b1db-78b217967af1",
      "product_eng_name": "Chewy Instant Rice Vermicelli Case 12 x 280GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%87%9F%E5%A4%9A%E6%92%88%E9%BA%B5%E6%9D%AF%2075GM/i/101352219.html",
      "uid": "0015ead65c9cb1cc0c7ff7244ee89d92",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "營多撈麵杯 75GM",
          "price": "$9",
          "offer": "【3件$25】$25任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210513/5588a8c6-a825-4d01-8d8a-762ae2657107",
          "product_eng_name": "Indomie Mi Goreng Cup Noodles 75GM"
        },
        {
          "name": "營多撈麵杯 75GM",
          "price": "$9",
          "offer": "【3件$25】$25任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210513/5588a8c6-a825-4d01-8d8a-762ae2657107",
          "product_eng_name": "Indomie Mi Goreng Cup Noodles 75GM"
        }
      ],
      "name": "營多撈麵杯 75GM",
      "price": "$9",
      "offer": "【3件$25】$25任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210513/5588a8c6-a825-4d01-8d8a-762ae2657107",
      "product_eng_name": "Indomie Mi Goreng Cup Noodles 75GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%B7%BA%E4%BA%95%E5%9F%BC%E7%8E%89%E7%B8%A3%E5%BD%A9%E4%B9%8B%E8%BC%9D%E7%B1%B3%202KG/i/101338204.html",
      "uid": "a0a6880d55fb56cd510aa7175b088d0e",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "淺井埼玉縣彩之輝米 2KG",
          "price": "$74",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210511/39d3e45f-c091-410a-9227-8d90d9107deb",
          "product_eng_name": "Azai Saitamakagayaki Rice 2KG"
        }
      ],
      "name": "淺井埼玉縣彩之輝米 2KG",
      "price": "$74",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210511/39d3e45f-c091-410a-9227-8d90d9107deb",
      "product_eng_name": "Azai Saitamakagayaki Rice 2KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%97%A5%E6%B8%85%E5%90%88%E5%91%B3%E9%81%93%E6%B5%B7%E9%AE%AE%E6%9D%AF%E9%BA%B5%2072GM/i/101339843.html",
      "uid": "921b048cd7b6912bb2d4991a4e078b2a",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "日清合味道海鮮杯麵 72GM",
          "price": "$8",
          "offer": "【2件$14.5】$14.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250327/c357cfd7-3c4a-3fe7-9134-3727db747830",
          "product_eng_name": "Nissin Cup Noodle Seafood 72GM"
        },
        {
          "name": "日清合味道海鮮杯麵 72GM",
          "price": "$8",
          "offer": "【2件$14.5】$14.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250327/c357cfd7-3c4a-3fe7-9134-3727db747830",
          "product_eng_name": "Nissin Cup Noodle Seafood 72GM"
        }
      ],
      "name": "日清合味道海鮮杯麵 72GM",
      "price": "$8",
      "offer": "【2件$14.5】$14.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250327/c357cfd7-3c4a-3fe7-9134-3727db747830",
      "product_eng_name": "Nissin Cup Noodle Seafood 72GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%AE%B6%E6%A8%82%E7%89%8C%E8%82%89%E4%B8%81%E5%91%B3%E5%BF%AB%E7%86%9F%E9%80%9A%E5%BF%83%E7%B2%89%2080GM/i/101356832.html",
      "uid": "00f958ca04de378d4b177cbd5be90997",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "家樂牌肉丁味快熟通心粉 80GM",
          "price": "$7",
          "offer": "【3件$17】$17任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220705/26861613-5b67-4a51-91ed-5b1c3126781e",
          "product_eng_name": "Knorr Quick Serve Bbq Broth Macaroni 80GM"
        },
        {
          "name": "家樂牌肉丁味快熟通心粉 80GM",
          "price": "$7",
          "offer": "【3件$17】$17任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220705/26861613-5b67-4a51-91ed-5b1c3126781e",
          "product_eng_name": "Knorr Quick Serve Bbq Broth Macaroni 80GM"
        }
      ],
      "name": "家樂牌肉丁味快熟通心粉 80GM",
      "price": "$7",
      "offer": "【3件$17】$17任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20220705/26861613-5b67-4a51-91ed-5b1c3126781e",
      "product_eng_name": "Knorr Quick Serve Bbq Broth Macaroni 80GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E8%BE%B2%E5%BF%83%E8%BE%A3%E7%99%BD%E8%8F%9C%E6%8B%89%E9%BA%B5%205%20X%20120GM/i/101326783.html",
      "uid": "9dede106c9f57fbb6e1f4caa86d89079",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "農心辣白菜拉麵 5 X 120GM",
          "price": "$20",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230913/7f9566d4-5a78-3fd0-8140-04bb9b3c085f",
          "product_eng_name": "Nong Shim Kimchi Ramyun 5 X 120GM"
        },
        {
          "name": "農心辣白菜拉麵 5 X 120GM",
          "price": "$20",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230913/7f9566d4-5a78-3fd0-8140-04bb9b3c085f",
          "product_eng_name": "Nong Shim Kimchi Ramyun 5 X 120GM"
        }
      ],
      "name": "農心辣白菜拉麵 5 X 120GM",
      "price": "$20",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230913/7f9566d4-5a78-3fd0-8140-04bb9b3c085f",
      "product_eng_name": "Nong Shim Kimchi Ramyun 5 X 120GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/Meadows%E7%B4%B0%E8%B2%9D%E6%AE%BC%E7%B2%89n28%20500GM/i/101579437.html",
      "uid": "f175bbb9691636c65fdc98606bcd324b",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "Meadows細貝殼粉n28 500GM",
          "price": "$16",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231204/3168e280-a145-36d8-8064-f424f674fa73",
          "product_eng_name": "Meadows Small Shells N28 500GM"
        },
        {
          "name": "Meadows細貝殼粉n28 500GM",
          "price": "$16",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231204/3168e280-a145-36d8-8064-f424f674fa73",
          "product_eng_name": "Meadows Small Shells N28 500GM"
        }
      ],
      "name": "Meadows細貝殼粉n28 500GM",
      "price": "$16",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20231204/3168e280-a145-36d8-8064-f424f674fa73",
      "product_eng_name": "Meadows Small Shells N28 500GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%A3%BD%E6%A1%83%E5%A5%B6%E6%B2%B9%E9%BA%B5%20340GM/i/101336228.html",
      "uid": "b2d0f829d95a45ca59221f2a197569dc",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "壽桃奶油麵 340GM",
          "price": "$9",
          "offer": "【2件$11】$11任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220505/8c216874-1a14-4f2c-adee-fe20a8622b23",
          "product_eng_name": "Sau Tao Cream Noodle 340GM"
        },
        {
          "name": "壽桃奶油麵 340GM",
          "price": "$9",
          "offer": "【2件$11】$11任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220505/8c216874-1a14-4f2c-adee-fe20a8622b23",
          "product_eng_name": "Sau Tao Cream Noodle 340GM"
        }
      ],
      "name": "壽桃奶油麵 340GM",
      "price": "$9",
      "offer": "【2件$11】$11任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20220505/8c216874-1a14-4f2c-adee-fe20a8622b23",
      "product_eng_name": "Sau Tao Cream Noodle 340GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E4%BA%94%E6%9C%A8%E8%85%90%E7%9A%AE%E7%83%8F%E5%86%AC%E7%A2%97%E9%BA%B5%20166GM/i/101350570.html",
      "uid": "32a7b9cebe4dc28ec1d6702196b0cc80",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "五木腐皮烏冬碗麵 166GM",
          "price": "$10",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20200501/04d2928c-0269-43f4-afcf-1b658b5fb395",
          "product_eng_name": "Itsuki Cup Kitsune Udon 166GM"
        },
        {
          "name": "五木腐皮烏冬碗麵 166GM",
          "price": "$10",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20200501/04d2928c-0269-43f4-afcf-1b658b5fb395",
          "product_eng_name": "Itsuki Cup Kitsune Udon 166GM"
        }
      ],
      "name": "五木腐皮烏冬碗麵 166GM",
      "price": "$10",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20200501/04d2928c-0269-43f4-afcf-1b658b5fb395",
      "product_eng_name": "Itsuki Cup Kitsune Udon 166GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%9C%88%E7%A8%BB%E9%AB%98%E7%B4%9A%E9%A6%99%E7%B1%B3%203KG/i/101338230.html",
      "uid": "8ac204dfef7b1732a78cf565d6e75e18",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "月稻高級香米 3KG",
          "price": "$49",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210126/078e6699-45c8-4431-85df-cace7485df4c",
          "product_eng_name": "Moon Seed Fragrant Rice 3KG"
        }
      ],
      "name": "月稻高級香米 3KG",
      "price": "$49",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210126/078e6699-45c8-4431-85df-cace7485df4c",
      "product_eng_name": "Moon Seed Fragrant Rice 3KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%A5%BD%E9%81%8B%E7%89%8C%E7%89%B9%E9%81%B8%E5%84%AA%E8%B3%AA%E9%A6%99%E7%B1%B3%208KG/i/101343828.html",
      "uid": "36e9d46617a9b34e75a3595f17557963",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "好運牌特選優質香米 8KG",
          "price": "$86",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250320/77c49775-c737-3d01-a353-95229df75bc8",
          "product_eng_name": "Lucky Brand Premium Fragrant Rice 8KG"
        }
      ],
      "name": "好運牌特選優質香米 8KG",
      "price": "$86",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250320/77c49775-c737-3d01-a353-95229df75bc8",
      "product_eng_name": "Lucky Brand Premium Fragrant Rice 8KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E9%A7%B1%E9%A7%9D%E5%98%9C%E8%8A%B1%E7%94%9F%E7%89%B9%E7%B4%9A%E9%A3%9F%E6%B2%B9%205LT/i/101326099.html",
      "uid": "50ba81e5e530ebeadf444211078b80eb",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "駱駝嘜花生特級食油 5LT",
          "price": "$129",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230428/a3af2d94-886a-46b7-926e-e1f48814d226",
          "product_eng_name": "Camel Peanut Aroma Cooking Oil 5LT"
        },
        {
          "name": "駱駝嘜花生特級食油 5LT",
          "price": "$129",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230428/a3af2d94-886a-46b7-926e-e1f48814d226",
          "product_eng_name": "Camel Peanut Aroma Cooking Oil 5LT"
        }
      ],
      "name": "駱駝嘜花生特級食油 5LT",
      "price": "$129",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230428/a3af2d94-886a-46b7-926e-e1f48814d226",
      "product_eng_name": "Camel Peanut Aroma Cooking Oil 5LT"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%A3%BD%E6%A1%83%E7%89%8C%E9%AE%91%E9%AD%9A%E9%9B%9E%E6%B9%AF%E9%9B%B2%E5%8D%97%E7%B1%B3%E7%B7%9A%20180GM/i/101335867.html",
      "uid": "725aa5b154f283d111cd08159dd6c805",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "壽桃牌鮑魚雞湯雲南米線 180GM",
          "price": "$6",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220505/89ec3e20-8d68-474e-9c06-969bea957b12",
          "product_eng_name": "Sau Tao Rice Vermicelli Abalone Chicken Soup Flavour 180GM"
        },
        {
          "name": "壽桃牌鮑魚雞湯雲南米線 180GM",
          "price": "$6",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220505/89ec3e20-8d68-474e-9c06-969bea957b12",
          "product_eng_name": "Sau Tao Rice Vermicelli Abalone Chicken Soup Flavour 180GM"
        }
      ],
      "name": "壽桃牌鮑魚雞湯雲南米線 180GM",
      "price": "$6",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20220505/89ec3e20-8d68-474e-9c06-969bea957b12",
      "product_eng_name": "Sau Tao Rice Vermicelli Abalone Chicken Soup Flavour 180GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%8D%85%E7%90%83%E5%98%9C%E5%88%9D%E6%90%BE%E6%A9%84%E6%AC%96%E8%8A%A5%E8%8A%B1%E7%B1%BD%E6%B2%B9%203%20X%20900ML/i/101341067.html",
      "uid": "5e9bf86b6593ef7d0528431ed92a00df",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "獅球嘜初搾橄欖芥花籽油 3 X 900ML",
          "price": "$99",
          "offer": "【買1件送1件贈品】購買每1件，即送1件人氣贈品；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250331/cbdbd52b-c588-3663-84d3-7fa8daa57091",
          "product_eng_name": "Lion & Globe Extra Virgin Olive Oil with Canola Oil 3 x 900ML"
        },
        {
          "name": "獅球嘜初搾橄欖芥花籽油 3 X 900ML",
          "price": "$99",
          "offer": "【買1件送1件贈品】購買每1件，即送1件人氣贈品；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250331/cbdbd52b-c588-3663-84d3-7fa8daa57091",
          "product_eng_name": "Lion & Globe Extra Virgin Olive Oil with Canola Oil 3 x 900ML"
        }
      ],
      "name": "獅球嘜初搾橄欖芥花籽油 3 X 900ML",
      "price": "$99",
      "offer": "【買1件送1件贈品】購買每1件，即送1件人氣贈品；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250331/cbdbd52b-c588-3663-84d3-7fa8daa57091",
      "product_eng_name": "Lion & Globe Extra Virgin Olive Oil with Canola Oil 3 x 900ML"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/Macro%20%E6%9C%89%E6%A9%9F%E5%85%A8%E9%BA%A5%E8%9E%BA%E6%97%8B%E9%BA%B5%20500%20%E5%85%8B/i/101362671.html",
      "uid": "9c82d06c107282a153c356d6f2988abe",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "Macro 有機全麥螺旋麵 500 克",
          "price": "$28",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250219/ec69c273-ca9e-397f-a754-fd76b5b3b92d",
          "product_eng_name": "Macro Organic Wholemeal Pasta Spirals 500GM"
        },
        {
          "name": "Macro 有機全麥螺旋麵 500 克",
          "price": "$28",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250219/ec69c273-ca9e-397f-a754-fd76b5b3b92d",
          "product_eng_name": "Macro Organic Wholemeal Pasta Spirals 500GM"
        }
      ],
      "name": "Macro 有機全麥螺旋麵 500 克",
      "price": "$28",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250219/ec69c273-ca9e-397f-a754-fd76b5b3b92d",
      "product_eng_name": "Macro Organic Wholemeal Pasta Spirals 500GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E5%87%BA%E5%89%8D%E4%B8%80%E4%B8%81%20%E9%9B%9E%E8%93%89%E5%8D%B3%E9%A3%9F%E9%BA%B5%20100%20GM/i/101363782.html",
      "uid": "c4917183e99d371eda84f46db3b2fe11",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱出前一丁 雞蓉即食麵 100 GM",
          "price": "$105",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231013/13cdd11a-4217-3474-86af-67a8317d17f0",
          "product_eng_name": "Nissin Demae Iccho Chicken Noodle Case 30 x 100GM"
        },
        {
          "name": "原箱出前一丁 雞蓉即食麵 100 GM",
          "price": "$105",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231013/13cdd11a-4217-3474-86af-67a8317d17f0",
          "product_eng_name": "Nissin Demae Iccho Chicken Noodle Case 30 x 100GM"
        }
      ],
      "name": "原箱出前一丁 雞蓉即食麵 100 GM",
      "price": "$105",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20231013/13cdd11a-4217-3474-86af-67a8317d17f0",
      "product_eng_name": "Nissin Demae Iccho Chicken Noodle Case 30 x 100GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%97%A5%E6%B8%85%E5%87%BA%E5%89%8D%E4%B8%80%E4%B8%81%E7%89%9B%E8%82%89%E5%8D%B3%E9%A3%9F%E9%BA%B5%20100GM/i/101322581.html",
      "uid": "48cdea9ff2427f5e7b78a317a02f19f2",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "日清出前一丁牛肉即食麵 100GM",
          "price": "$5",
          "offer": "【8件$28.5】$28.5任揀8件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250407/3adbacfa-ae26-3b75-ac16-e0b1320d180a",
          "product_eng_name": "Nissin Demae Iccho Beef Instant Noodle 100GM"
        },
        {
          "name": "日清出前一丁牛肉即食麵 100GM",
          "price": "$5",
          "offer": "【8件$28.5】$28.5任揀8件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250407/3adbacfa-ae26-3b75-ac16-e0b1320d180a",
          "product_eng_name": "Nissin Demae Iccho Beef Instant Noodle 100GM"
        }
      ],
      "name": "日清出前一丁牛肉即食麵 100GM",
      "price": "$5",
      "offer": "【8件$28.5】$28.5任揀8件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250407/3adbacfa-ae26-3b75-ac16-e0b1320d180a",
      "product_eng_name": "Nissin Demae Iccho Beef Instant Noodle 100GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/GROVE%20%E7%89%9B%E6%B2%B9%E6%9E%9C%E6%B2%B9-%E8%92%9C%E9%A6%99%E5%91%B3%20250ML/i/101359755.html",
      "uid": "7cc4258e58bacac501facce9322697d0",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "GROVE 牛油果油-蒜香味 250ML",
          "price": "$119",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240510/fe912a1f-7236-32f9-b150-a9e238a9644e",
          "product_eng_name": "(無法擷取英文名稱)"
        },
        {
          "name": "GROVE 牛油果油-蒜香味 250ML",
          "price": "$119",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240510/fe912a1f-7236-32f9-b150-a9e238a9644e",
          "product_eng_name": "Grove Cold Pressed Avocado Oil Garlic 250ML"
        }
      ],
      "name": "GROVE 牛油果油-蒜香味 250ML",
      "price": "$119",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240510/fe912a1f-7236-32f9-b150-a9e238a9644e",
      "product_eng_name": "Grove Cold Pressed Avocado Oil Garlic 250ML"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%BA%A6%E5%B0%8F%E6%9C%88%E8%95%8E%E9%BA%A5%E9%A4%8A%E7%94%9F%E9%BA%B5%20500GM/i/101348026.html",
      "uid": "4e046cdd3040bb29cd1c29e8f5bf15b8",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "度小月蕎麥養生麵 500GM",
          "price": "$22",
          "offer": "【2件$50】$50任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210513/1c99ac3a-7a8a-48c0-80e7-2f40a5f45b06",
          "product_eng_name": "Doshee Buckwheat Noodle 500GM"
        },
        {
          "name": "度小月蕎麥養生麵 500GM",
          "price": "$22",
          "offer": "【2件$50】$50任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210513/1c99ac3a-7a8a-48c0-80e7-2f40a5f45b06",
          "product_eng_name": "Doshee Buckwheat Noodle 500GM"
        }
      ],
      "name": "度小月蕎麥養生麵 500GM",
      "price": "$22",
      "offer": "【2件$50】$50任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210513/1c99ac3a-7a8a-48c0-80e7-2f40a5f45b06",
      "product_eng_name": "Doshee Buckwheat Noodle 500GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%B5%B1%E4%B8%80%E8%8C%84%E7%9A%87%20%E7%95%AA%E8%8C%84%E7%89%9B%E8%82%89%E9%9D%A2%20630GM/i/101346844.html",
      "uid": "709514661356ae4105b94958f6820e8c",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "統一茄皇 番茄牛肉面 630GM",
          "price": "$27",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240124/f245561c-2fc7-338b-98a9-fb94d0572c0b",
          "product_eng_name": "Uni President Tomato Beef Noodles 630GM"
        },
        {
          "name": "統一茄皇 番茄牛肉面 630GM",
          "price": "$27",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240124/f245561c-2fc7-338b-98a9-fb94d0572c0b",
          "product_eng_name": "Uni President Tomato Beef Noodles 630GM"
        }
      ],
      "name": "統一茄皇 番茄牛肉面 630GM",
      "price": "$27",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240124/f245561c-2fc7-338b-98a9-fb94d0572c0b",
      "product_eng_name": "Uni President Tomato Beef Noodles 630GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%97%A5%E6%B8%85%E5%87%BA%E5%89%8D%E4%B8%80%E4%B8%81%E9%9F%93%E5%BC%8F%E7%89%9B%E9%AA%A8%E6%B9%AF%E5%91%B3%E7%A2%97%E9%BA%B5%20105GM/i/101573956.html",
      "uid": "c8dc7407b3d7ba437258093c6c222ec0",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "日清出前一丁韓式牛骨湯味碗麵 105GM",
          "price": "$10",
          "offer": "【2件$18】$18任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210624/9dc14c35-6df0-40e6-b89f-b378557d2ea1",
          "product_eng_name": "Nissin Demae Iccho Korean Beef Bowl Noodle 105GM"
        },
        {
          "name": "日清出前一丁韓式牛骨湯味碗麵 105GM",
          "price": "$10",
          "offer": "【2件$18】$18任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210624/9dc14c35-6df0-40e6-b89f-b378557d2ea1",
          "product_eng_name": "Nissin Demae Iccho Korean Beef Bowl Noodle 105GM"
        }
      ],
      "name": "日清出前一丁韓式牛骨湯味碗麵 105GM",
      "price": "$10",
      "offer": "【2件$18】$18任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210624/9dc14c35-6df0-40e6-b89f-b378557d2ea1",
      "product_eng_name": "Nissin Demae Iccho Korean Beef Bowl Noodle 105GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%8D%85%E7%90%83%E5%98%9C%E8%8A%A5%E8%8A%B1%E7%B1%BD%E6%B2%B9%203LT/i/101326098.html",
      "uid": "7a71a09014c6aa42d94fad6852485b2e",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "獅球嘜芥花籽油 3LT",
          "price": "$87",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240507/bbd038c1-0554-3840-9c40-90eef5d74964",
          "product_eng_name": "Lion & Globe Canola Oil 3LT"
        },
        {
          "name": "獅球嘜芥花籽油 3LT",
          "price": "$87",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240507/bbd038c1-0554-3840-9c40-90eef5d74964",
          "product_eng_name": "Lion & Globe Canola Oil 3LT"
        }
      ],
      "name": "獅球嘜芥花籽油 3LT",
      "price": "$87",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240507/bbd038c1-0554-3840-9c40-90eef5d74964",
      "product_eng_name": "Lion & Globe Canola Oil 3LT"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%97%A5%E6%B8%85%20%E5%92%9A%E5%85%B5%E8%A1%9B%E5%A4%A9%E5%A9%A6%E7%BE%85%E6%89%8B%E6%89%93%E9%A2%A8%E7%83%8F%E5%86%AC%E7%A2%97%20219%20GM/i/113340663.html",
      "uid": "7d549f05d10e640b777f4b5479054397",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "日清 咚兵衛天婦羅手打風烏冬碗 219 GM",
          "price": "$16",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240823/44effe9b-641b-3f36-bbf1-c9c5a2118e0a",
          "product_eng_name": "Nissin Donbei Tempura Handmade Style Udon 219GM"
        },
        {
          "name": "日清 咚兵衛天婦羅手打風烏冬碗 219 GM",
          "price": "$16",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240823/44effe9b-641b-3f36-bbf1-c9c5a2118e0a",
          "product_eng_name": "Nissin Donbei Tempura Handmade Style Udon 219GM"
        }
      ],
      "name": "日清 咚兵衛天婦羅手打風烏冬碗 219 GM",
      "price": "$16",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240823/44effe9b-641b-3f36-bbf1-c9c5a2118e0a",
      "product_eng_name": "Nissin Donbei Tempura Handmade Style Udon 219GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/La%20Molisana%E9%95%B7%E7%9B%B4%E9%80%9A%E7%B2%89%2320%20500GM/i/101381097.html",
      "uid": "a54d05dec7ee257f2db44ee341149afb",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "La Molisana長直通粉#20 500GM",
          "price": "$23",
          "offer": "【2件$30】$30任揀2件；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230714/6477e963-e03a-4c36-a388-f596131d913c",
          "product_eng_name": "La Molisana Penne Rigate #20 500GM"
        },
        {
          "name": "La Molisana長直通粉#20 500GM",
          "price": "$23",
          "offer": "【2件$30】$30任揀2件；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230714/6477e963-e03a-4c36-a388-f596131d913c",
          "product_eng_name": "La Molisana Penne Rigate #20 500GM"
        }
      ],
      "name": "La Molisana長直通粉#20 500GM",
      "price": "$23",
      "offer": "【2件$30】$30任揀2件；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230714/6477e963-e03a-4c36-a388-f596131d913c",
      "product_eng_name": "La Molisana Penne Rigate #20 500GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E8%BE%B2%E5%BF%83%E8%BE%A3%E7%99%BD%E8%8F%9C%E6%9D%AF%E9%BA%B5%2070GM/i/101331702.html",
      "uid": "68fd49f094c28b46c5d88cb751e01cbc",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "農心辣白菜杯麵 70GM",
          "price": "$8",
          "offer": "【3件$18】$18任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20201016/8649a92c-1905-413e-b14f-4e53980f9995",
          "product_eng_name": "Nong Shim Kimchi Cup Noodle 70GM"
        },
        {
          "name": "農心辣白菜杯麵 70GM",
          "price": "$8",
          "offer": "【3件$18】$18任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20201016/8649a92c-1905-413e-b14f-4e53980f9995",
          "product_eng_name": "Nong Shim Kimchi Cup Noodle 70GM"
        }
      ],
      "name": "農心辣白菜杯麵 70GM",
      "price": "$8",
      "offer": "【3件$18】$18任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20201016/8649a92c-1905-413e-b14f-4e53980f9995",
      "product_eng_name": "Nong Shim Kimchi Cup Noodle 70GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%97%A5%E6%B8%85%E5%92%9A%E5%85%B5%E8%A1%9B%E6%97%A5%E5%BC%8F%E8%85%90%E7%9A%AE%E6%9D%AF%E7%83%8F%E5%86%AC%20(%E5%8D%B3%E9%A3%9F%E9%BA%B5)/i/101385275.html",
      "uid": "997cf80ed1f7b72a1ecef60ed1ddbc07",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "日清咚兵衛日式腐皮杯烏冬 (即食麵)",
          "price": "$10",
          "offer": "【2件$18】$18任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20241028/fef2f37a-f893-3ca3-8558-7e7a4fffa364",
          "product_eng_name": "Nissin Donbei Kitsune Cup Udon (Instant Noodle)"
        },
        {
          "name": "日清咚兵衛日式腐皮杯烏冬 (即食麵)",
          "price": "$10",
          "offer": "【2件$18】$18任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20241028/fef2f37a-f893-3ca3-8558-7e7a4fffa364",
          "product_eng_name": "Nissin Donbei Kitsune Cup Udon (Instant Noodle)"
        }
      ],
      "name": "日清咚兵衛日式腐皮杯烏冬 (即食麵)",
      "price": "$10",
      "offer": "【2件$18】$18任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20241028/fef2f37a-f893-3ca3-8558-7e7a4fffa364",
      "product_eng_name": "Nissin Donbei Kitsune Cup Udon (Instant Noodle)"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E4%BA%94%E8%B1%90100%25%E7%B4%94%E8%95%8E%E9%BA%A5%E9%BA%B5%20300GM/i/101346328.html",
      "uid": "e6f70e74cd53d99f585b417cacf41248",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "五豐100%純蕎麥麵 300GM",
          "price": "$9",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210125/715fcce2-26ce-4894-9b64-04bbce2f4cb9",
          "product_eng_name": "Ng Fung 100% Buckwheat Noodle 300GM"
        },
        {
          "name": "五豐100%純蕎麥麵 300GM",
          "price": "$9",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210125/715fcce2-26ce-4894-9b64-04bbce2f4cb9",
          "product_eng_name": "Ng Fung 100% Buckwheat Noodle 300GM"
        }
      ],
      "name": "五豐100%純蕎麥麵 300GM",
      "price": "$9",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210125/715fcce2-26ce-4894-9b64-04bbce2f4cb9",
      "product_eng_name": "Ng Fung 100% Buckwheat Noodle 300GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E8%B6%85%E5%8A%9B%E6%96%B0%E7%AB%B9%E7%B1%B3%E7%B2%89%20400GM/i/101384639.html",
      "uid": "578d6e8cd87810862118e123d57682d9",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "超力新竹米粉 400GM",
          "price": "$20",
          "offer": "【2件$21】$21任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240916/8267a822-192e-34de-bffb-aa6655456a4a",
          "product_eng_name": "Chewy Hsin Chu Rice Stick 400GM"
        },
        {
          "name": "超力新竹米粉 400GM",
          "price": "$20",
          "offer": "【2件$21】$21任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240916/8267a822-192e-34de-bffb-aa6655456a4a",
          "product_eng_name": "Chewy Hsin Chu Rice Stick 400GM"
        }
      ],
      "name": "超力新竹米粉 400GM",
      "price": "$20",
      "offer": "【2件$21】$21任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240916/8267a822-192e-34de-bffb-aa6655456a4a",
      "product_eng_name": "Chewy Hsin Chu Rice Stick 400GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%99%BE%E5%BE%97%E9%98%BF%E5%A7%A8%E6%84%8F%E5%A4%A7%E5%88%A9%E7%B2%89%235%20500GM/i/101326062.html",
      "uid": "0c885b3c4c0b3213074e15648b100078",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "百得阿姨意大利粉#5 500GM",
          "price": "$22",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240916/9a421fe1-3007-3fe5-826c-9505631ed4d4",
          "product_eng_name": "Barilla Spaghetti #5 500GM"
        },
        {
          "name": "百得阿姨意大利粉#5 500GM",
          "price": "$22",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240916/9a421fe1-3007-3fe5-826c-9505631ed4d4",
          "product_eng_name": "Barilla Spaghetti #5 500GM"
        }
      ],
      "name": "百得阿姨意大利粉#5 500GM",
      "price": "$22",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240916/9a421fe1-3007-3fe5-826c-9505631ed4d4",
      "product_eng_name": "Barilla Spaghetti #5 500GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E6%97%A5%E6%B8%85%E5%92%9A%E5%85%B5%E8%A1%9B%E8%85%90%E7%9A%AE%E7%83%8F%E5%86%AC%2012%20X%2095GM/i/113268814.html",
      "uid": "7a3b8b9a32c290709026f7969f5fd7b3",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱日清咚兵衛腐皮烏冬 12 X 95GM",
          "price": "$120",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20241029/9b087f49-8bf9-378e-8bcd-d00f7b29cd16",
          "product_eng_name": "Nissin Donbei Kitsune Udon Case 12 X 95GM"
        },
        {
          "name": "原箱日清咚兵衛腐皮烏冬 12 X 95GM",
          "price": "$120",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20241029/9b087f49-8bf9-378e-8bcd-d00f7b29cd16",
          "product_eng_name": "Nissin Donbei Kitsune Udon Case 12 X 95GM"
        }
      ],
      "name": "原箱日清咚兵衛腐皮烏冬 12 X 95GM",
      "price": "$120",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20241029/9b087f49-8bf9-378e-8bcd-d00f7b29cd16",
      "product_eng_name": "Nissin Donbei Kitsune Udon Case 12 X 95GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E8%BE%B2%E5%BF%83%20%E7%89%B9%E8%BE%A3%E5%A4%A7%E7%A2%97%E9%BA%B5%20114%20GM/i/113559394.html",
      "uid": "67a6850afdf35770eb00e33718015918",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱農心 特辣大碗麵 114 GM",
          "price": "$92",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231013/f65751b2-c346-335e-b82c-b8d367002573",
          "product_eng_name": "Nong Shim Shin Bowl Noodle Case 16 x 114GM"
        },
        {
          "name": "原箱農心 特辣大碗麵 114 GM",
          "price": "$92",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231013/f65751b2-c346-335e-b82c-b8d367002573",
          "product_eng_name": "Nong Shim Shin Bowl Noodle Case 16 x 114GM"
        }
      ],
      "name": "原箱農心 特辣大碗麵 114 GM",
      "price": "$92",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20231013/f65751b2-c346-335e-b82c-b8d367002573",
      "product_eng_name": "Nong Shim Shin Bowl Noodle Case 16 x 114GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E9%87%91%E8%B1%A1%E7%89%8C%E9%A0%82%E4%B8%8A%E8%8C%89%E8%8E%89%E9%A6%99%E7%B1%B3%205KG/i/101322993.html",
      "uid": "c660e58baf0dd30c4c2bdc1445bd3467",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "金象牌頂上茉莉香米 5KG",
          "price": "$72",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250407/76fc92b5-52da-3f08-b02f-f39c3d0fbbd6",
          "product_eng_name": "Golden Elephant Premium Jasmine Rice 5KG"
        }
      ],
      "name": "金象牌頂上茉莉香米 5KG",
      "price": "$72",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250407/76fc92b5-52da-3f08-b02f-f39c3d0fbbd6",
      "product_eng_name": "Golden Elephant Premium Jasmine Rice 5KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%97%A5%E6%9C%AC%E8%A3%BD%E7%B2%89%20HELLO%20KITTY%E9%80%9A%E5%BF%83%E7%B2%89%20120%20GM/i/113551539.html",
      "uid": "fb0bd6e9086c46ab54d09cb3ce8efd4c",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "日本製粉 HELLO KITTY通心粉 120 GM",
          "price": "$19",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250218/a2941e89-b38b-39fe-9974-e9a742acd800",
          "product_eng_name": "Nippn Hello Kitty Macaroni 120GM"
        },
        {
          "name": "日本製粉 HELLO KITTY通心粉 120 GM",
          "price": "$19",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250218/a2941e89-b38b-39fe-9974-e9a742acd800",
          "product_eng_name": "Nippn Hello Kitty Macaroni 120GM"
        }
      ],
      "name": "日本製粉 HELLO KITTY通心粉 120 GM",
      "price": "$19",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250218/a2941e89-b38b-39fe-9974-e9a742acd800",
      "product_eng_name": "Nippn Hello Kitty Macaroni 120GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E6%97%A5%E6%B8%85%E5%90%88%E5%91%B3%E9%81%93%20%E5%92%96%E5%96%B1%E5%A4%A7%E6%9D%AF%E9%BA%B5%2012%20X%20101GM/i/113465599.html",
      "uid": "504dc4dc7be91db92e9fdb6d86a3a4af",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱日清合味道 咖喱大杯麵 12 X 101GM",
          "price": "$105",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230728/db7a56ff-0bf4-324a-b30e-93e7f96ccc1d",
          "product_eng_name": "Nissin Big Cup Curry Seafood Case 12 X 101GM"
        },
        {
          "name": "原箱日清合味道 咖喱大杯麵 12 X 101GM",
          "price": "$105",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230728/db7a56ff-0bf4-324a-b30e-93e7f96ccc1d",
          "product_eng_name": "Nissin Big Cup Curry Seafood Case 12 X 101GM"
        }
      ],
      "name": "原箱日清合味道 咖喱大杯麵 12 X 101GM",
      "price": "$105",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230728/db7a56ff-0bf4-324a-b30e-93e7f96ccc1d",
      "product_eng_name": "Nissin Big Cup Curry Seafood Case 12 X 101GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%B6%AD%E5%8A%9B%E4%B8%80%E5%BA%A6%E8%B4%8A%20%E7%88%8C%E8%82%89%E7%A2%97%E9%BA%B5%20200%20GM/i/113737621.html",
      "uid": "71be4bd27f576ab716794add3b5190a2",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "維力一度贊 爌肉碗麵 200 GM",
          "price": "$15",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240321/b4ec99a0-0378-38d1-a638-62fbb67bb735",
          "product_eng_name": "Wei Lih Ichiban Delicious Roast Pork Flavour Noodles 200GM"
        },
        {
          "name": "維力一度贊 爌肉碗麵 200 GM",
          "price": "$15",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240321/b4ec99a0-0378-38d1-a638-62fbb67bb735",
          "product_eng_name": "Wei Lih Ichiban Delicious Roast Pork Flavour Noodles 200GM"
        }
      ],
      "name": "維力一度贊 爌肉碗麵 200 GM",
      "price": "$15",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240321/b4ec99a0-0378-38d1-a638-62fbb67bb735",
      "product_eng_name": "Wei Lih Ichiban Delicious Roast Pork Flavour Noodles 200GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%A4%A7%E5%B8%AB%E5%A7%90%20%E5%85%A8%E8%9B%8B%E9%BA%B5(%E5%B9%BC)%206%E5%80%8B%E8%A3%9D/i/101341765.html",
      "uid": "55fbcdf5c110e38909fd6b0e4e55e739",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "大師姐 全蛋麵(幼) 6個裝",
          "price": "$78",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250122/83e00365-902b-3416-a1f9-473f84ce23bf",
          "product_eng_name": "Dashijie Egg Noodle (Fine)"
        },
        {
          "name": "大師姐 全蛋麵(幼) 6個裝",
          "price": "$78",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250122/83e00365-902b-3416-a1f9-473f84ce23bf",
          "product_eng_name": "Dashijie Egg Noodle (Fine)"
        }
      ],
      "name": "大師姐 全蛋麵(幼) 6個裝",
      "price": "$78",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250122/83e00365-902b-3416-a1f9-473f84ce23bf",
      "product_eng_name": "Dashijie Egg Noodle (Fine)"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/GROVE%20%E7%89%9B%E6%B2%B9%E6%9E%9C%E6%B2%B9-%E9%9D%92%E6%AA%B8%E5%91%B3%20250%20ML/i/114228296.html",
      "uid": "7c4fce9a71aef763c1df09a347389d56",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "GROVE 牛油果油-青檸味 250 ML",
          "price": "$119",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240529/9fd3879f-36a5-3e17-89ca-8ec61eabf834",
          "product_eng_name": "Grove Cold Pressed Avocado Oil Lime 250ML"
        },
        {
          "name": "GROVE 牛油果油-青檸味 250 ML",
          "price": "$119",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240529/9fd3879f-36a5-3e17-89ca-8ec61eabf834",
          "product_eng_name": "Grove Cold Pressed Avocado Oil Lime 250ML"
        }
      ],
      "name": "GROVE 牛油果油-青檸味 250 ML",
      "price": "$119",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240529/9fd3879f-36a5-3e17-89ca-8ec61eabf834",
      "product_eng_name": "Grove Cold Pressed Avocado Oil Lime 250ML"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%A3%BD%E6%A1%83%E5%B9%BC%E6%BB%91%E4%B8%8A%E6%B5%B7%E9%BA%B5%E5%84%AA%E6%83%A0%E8%A3%9D4%E5%8C%85%E8%A3%9D/i/101684187.html",
      "uid": "b6b4ee61349323083ce08199acb45cdc",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "壽桃幼滑上海麵優惠裝4包裝",
          "price": "$17",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240913/4c7c8085-3f90-3683-97ff-abc7efef5364",
          "product_eng_name": "(無法擷取英文名稱)"
        },
        {
          "name": "壽桃幼滑上海麵優惠裝4包裝",
          "price": "$17",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240913/4c7c8085-3f90-3683-97ff-abc7efef5364",
          "product_eng_name": "Sau Tao Shanghai Noodle (4 packs)"
        }
      ],
      "name": "壽桃幼滑上海麵優惠裝4包裝",
      "price": "$17",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240913/4c7c8085-3f90-3683-97ff-abc7efef5364",
      "product_eng_name": "Sau Tao Shanghai Noodle (4 packs)"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E8%BE%B2%E5%BF%83%E7%89%B9%E8%BE%A3%E6%9D%AF%E9%BA%B5%2065GM/i/101357191.html",
      "uid": "3ccfc344bf9f4ce33d268ece4cc37189",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "農心特辣杯麵 65GM",
          "price": "$8",
          "offer": "【3件$18】$18任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20201016/fcaabc59-b3e1-4183-9ddc-0f68fe0e9547",
          "product_eng_name": "Nong Shim Shin Cup Noodles 65GM"
        },
        {
          "name": "農心特辣杯麵 65GM",
          "price": "$8",
          "offer": "【3件$18】$18任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20201016/fcaabc59-b3e1-4183-9ddc-0f68fe0e9547",
          "product_eng_name": "(無法擷取英文名稱)"
        }
      ],
      "name": "農心特辣杯麵 65GM",
      "price": "$8",
      "offer": "【3件$18】$18任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20201016/fcaabc59-b3e1-4183-9ddc-0f68fe0e9547",
      "product_eng_name": "(無法擷取英文名稱)"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%99%BE%E5%BE%97%E9%98%BF%E5%A7%A8%E7%B2%97%E7%B2%92%E6%84%8F%E5%A4%A7%E5%88%A9%E7%B2%897%E8%99%9F%20500GM/i/101343444.html",
      "uid": "27d33cb70e862a1124fdbbde1bc9e18d",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "百得阿姨粗粒意大利粉7號 500GM",
          "price": "$19",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240916/ba5a3162-6669-3156-862a-b8fb34f4c2d2",
          "product_eng_name": "Barilla Spaghettoni N7 500GM"
        },
        {
          "name": "百得阿姨粗粒意大利粉7號 500GM",
          "price": "$19",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240916/ba5a3162-6669-3156-862a-b8fb34f4c2d2",
          "product_eng_name": "Barilla Spaghettoni N7 500GM"
        }
      ],
      "name": "百得阿姨粗粒意大利粉7號 500GM",
      "price": "$19",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240916/ba5a3162-6669-3156-862a-b8fb34f4c2d2",
      "product_eng_name": "Barilla Spaghettoni N7 500GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E6%97%A5%E6%B8%85%E5%90%88%E5%91%B3%E9%81%93%E9%A6%99%E8%BE%A3%E6%B5%B7%E9%AE%AE%E6%9D%AF%E9%BA%B5%2024%20X%2075GM/i/101363773.html",
      "uid": "7ec43f6de568dce7e1cea8720995e3df",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱日清合味道香辣海鮮杯麵 24 X 75GM",
          "price": "$170",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230202/84424668-3d40-401d-bd28-4744ba63d053",
          "product_eng_name": "Nissin Cup Noodles Spicy Seafood 24 X 75GM"
        },
        {
          "name": "原箱日清合味道香辣海鮮杯麵 24 X 75GM",
          "price": "$170",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230202/84424668-3d40-401d-bd28-4744ba63d053",
          "product_eng_name": "Nissin Cup Noodles Spicy Seafood 24 X 75GM"
        }
      ],
      "name": "原箱日清合味道香辣海鮮杯麵 24 X 75GM",
      "price": "$170",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230202/84424668-3d40-401d-bd28-4744ba63d053",
      "product_eng_name": "Nissin Cup Noodles Spicy Seafood 24 X 75GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E9%A7%B1%E9%A7%9D%E5%98%9C%E8%8A%B1%E7%94%9F%E7%89%B9%E7%B4%9A%E9%A3%9F%E6%B2%B9900%E6%AF%AB%E5%8D%87X3/i/101344103.html",
      "uid": "71522dcc87b5287828d769f5aefe8b5f",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "駱駝嘜花生特級食油900毫升X3",
          "price": "$72",
          "offer": "【買1件送1件贈品】購買每1件，即送1件人氣贈品；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240813/06e320cc-517e-3d75-ba1a-4fc6ffb8c818",
          "product_eng_name": "Camel Peanut Aroma Cooking Oil 3 x 900ML"
        },
        {
          "name": "駱駝嘜花生特級食油900毫升X3",
          "price": "$72",
          "offer": "【買1件送1件贈品】購買每1件，即送1件人氣贈品；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240813/06e320cc-517e-3d75-ba1a-4fc6ffb8c818",
          "product_eng_name": "Camel Peanut Aroma Cooking Oil 3 x 900ML"
        }
      ],
      "name": "駱駝嘜花生特級食油900毫升X3",
      "price": "$72",
      "offer": "【買1件送1件贈品】購買每1件，即送1件人氣贈品；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240813/06e320cc-517e-3d75-ba1a-4fc6ffb8c818",
      "product_eng_name": "Camel Peanut Aroma Cooking Oil 3 x 900ML"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%A8%82%E5%AE%B6%E7%B4%94%E6%A9%84%E6%AC%96%E6%B2%B9%20750%E6%AF%AB%E5%8D%87/i/101335010.html",
      "uid": "0d71525185b543b54db1022b4413ac70",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "樂家純橄欖油 750毫升",
          "price": "$167",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20241007/2269bba1-8711-3780-be94-1aa262ecef4b",
          "product_eng_name": "Colavita Pure Olive Oil 750ml"
        },
        {
          "name": "樂家純橄欖油 750毫升",
          "price": "$167",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20241007/2269bba1-8711-3780-be94-1aa262ecef4b",
          "product_eng_name": "Colavita Pure Olive Oil 750ml"
        }
      ],
      "name": "樂家純橄欖油 750毫升",
      "price": "$167",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20241007/2269bba1-8711-3780-be94-1aa262ecef4b",
      "product_eng_name": "Colavita Pure Olive Oil 750ml"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%97%A5%E6%B8%85%E5%90%88%E5%91%B3%E9%81%93%E9%A6%99%E8%BE%A3%E6%B5%B7%E9%AE%AE%E6%9D%AF%E9%BA%B5%2075GM/i/101350005.html",
      "uid": "0ab7d3647aa1fa282e0e0af18533a397",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "日清合味道香辣海鮮杯麵 75GM",
          "price": "$8",
          "offer": "【2件$14.5】$14.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250327/f463aad5-ab8a-3025-9667-017a20120e21",
          "product_eng_name": "Nissin Cup Noodle Spicy Seafood 75GM"
        },
        {
          "name": "日清合味道香辣海鮮杯麵 75GM",
          "price": "$8",
          "offer": "【2件$14.5】$14.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250327/f463aad5-ab8a-3025-9667-017a20120e21",
          "product_eng_name": "Nissin Cup Noodle Spicy Seafood 75GM"
        }
      ],
      "name": "日清合味道香辣海鮮杯麵 75GM",
      "price": "$8",
      "offer": "【2件$14.5】$14.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250327/f463aad5-ab8a-3025-9667-017a20120e21",
      "product_eng_name": "Nissin Cup Noodle Spicy Seafood 75GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%97%A5%E6%B8%85%E5%90%88%E5%91%B3%E9%81%93%E9%AE%AE%E8%9D%A6%E6%9D%AF%E9%BA%B5%2074GM/i/101327559.html",
      "uid": "e347ae4f6979310fa8aea8794369aa4e",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "日清合味道鮮蝦杯麵 74GM",
          "price": "$8",
          "offer": "【2件$14.5】$14.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250327/b064d475-7ad1-3c31-9493-3f20aa1be425",
          "product_eng_name": "Nissin Prawn Cup Noodle 74GM"
        },
        {
          "name": "日清合味道鮮蝦杯麵 74GM",
          "price": "$8",
          "offer": "【2件$14.5】$14.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250327/b064d475-7ad1-3c31-9493-3f20aa1be425",
          "product_eng_name": "Nissin Prawn Cup Noodle 74GM"
        }
      ],
      "name": "日清合味道鮮蝦杯麵 74GM",
      "price": "$8",
      "offer": "【2件$14.5】$14.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250327/b064d475-7ad1-3c31-9493-3f20aa1be425",
      "product_eng_name": "Nissin Prawn Cup Noodle 74GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E8%B6%85%E5%8A%9B%20%E9%86%AC%E7%88%86%E7%B3%BB%E5%88%97-%E8%80%81%E5%A3%87%E9%85%B8%E8%8F%9C%E7%B1%B3%E7%B2%894%E5%8C%85%E8%A3%9D%20105%20GM/i/113401198.html",
      "uid": "8ba365b15a7ea146cc89e3df8a7dd788",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "超力 醬爆系列-老壇酸菜米粉4包裝 105 GM",
          "price": "$20",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230606/7689b5b0-3d1f-4a05-a427-fa78f0aee637",
          "product_eng_name": "Chewy Instant Rice Vermicelli - Laotan Pickled Flavour 4 X 105GM"
        },
        {
          "name": "超力 醬爆系列-老壇酸菜米粉4包裝 105 GM",
          "price": "$20",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230606/7689b5b0-3d1f-4a05-a427-fa78f0aee637",
          "product_eng_name": "Chewy Instant Rice Vermicelli - Laotan Pickled Flavour 4 X 105GM"
        }
      ],
      "name": "超力 醬爆系列-老壇酸菜米粉4包裝 105 GM",
      "price": "$20",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230606/7689b5b0-3d1f-4a05-a427-fa78f0aee637",
      "product_eng_name": "Chewy Instant Rice Vermicelli - Laotan Pickled Flavour 4 X 105GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%AE%97%E5%AE%B6%E5%BA%9C%E5%B9%B4%E7%B3%95%E7%89%87%20500GM/i/101576937.html",
      "uid": "e48396bd777e56b8f5574b4128c556a1",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "宗家府年糕片 500GM",
          "price": "$18",
          "offer": "【指定分類享$25換購】每買1件，即可以$25換購1件人氣產品；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210524/d41e7368-bd6a-4815-9f9b-0afd3b79c3e7",
          "product_eng_name": "Jongga Rice Cake Sliced 500GM"
        }
      ],
      "name": "宗家府年糕片 500GM",
      "price": "$18",
      "offer": "【指定分類享$25換購】每買1件，即可以$25換購1件人氣產品；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210524/d41e7368-bd6a-4815-9f9b-0afd3b79c3e7",
      "product_eng_name": "Jongga Rice Cake Sliced 500GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%88%80%E5%98%9C%20%E7%B4%94%E6%AD%A3%E7%B2%9F%E7%B1%B3%E6%B2%B93%E6%94%AF%E8%A3%9D%20900%20ML/i/113551959.html",
      "uid": "ef3076995972ff3ad528b4c2696d1c63",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "刀嘜 純正粟米油3支裝 900 ML",
          "price": "$85",
          "offer": "【買1件送2件贈品】購買每1件，即送2件人氣贈品；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231011/f7f907b0-bcb0-39c6-b246-e576a7d7286c",
          "product_eng_name": "Knife Pure Corn Oil 3 x 900ML"
        },
        {
          "name": "刀嘜 純正粟米油3支裝 900 ML",
          "price": "$85",
          "offer": "【買1件送2件贈品】購買每1件，即送2件人氣贈品；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231011/f7f907b0-bcb0-39c6-b246-e576a7d7286c",
          "product_eng_name": "Knife Pure Corn Oil 3 x 900ML"
        }
      ],
      "name": "刀嘜 純正粟米油3支裝 900 ML",
      "price": "$85",
      "offer": "【買1件送2件贈品】購買每1件，即送2件人氣贈品；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20231011/f7f907b0-bcb0-39c6-b246-e576a7d7286c",
      "product_eng_name": "Knife Pure Corn Oil 3 x 900ML"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%A5%BD%E9%81%8B%E7%89%8C%E7%89%B9%E9%81%B8%E5%84%AA%E8%B3%AA%E9%A6%99%E7%B1%B3%205KG/i/101358954.html",
      "uid": "1e749a90d4bdd87a32ebe3e8fbf61b59",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "好運牌特選優質香米 5KG",
          "price": "$59",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230321/bd104525-d35e-4b8d-81e7-db16d7727037",
          "product_eng_name": "Lucky Brand Premium Fragrant Rice 5KG"
        }
      ],
      "name": "好運牌特選優質香米 5KG",
      "price": "$59",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230321/bd104525-d35e-4b8d-81e7-db16d7727037",
      "product_eng_name": "Lucky Brand Premium Fragrant Rice 5KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%99%BE%E7%9B%8A%E6%B8%85%E6%B7%A1%E6%A9%84%E6%AC%96%E6%B2%B9%E5%99%B4%E9%9C%A7%E8%A3%9D%20200ML/i/101336914.html",
      "uid": "ff507238e96e3f90983e52561fe86569",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "百益清淡橄欖油噴霧裝 200ML",
          "price": "$59",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20241120/5046228e-6448-3d9a-8c16-994b57e12d52",
          "product_eng_name": "Filippo Berio Mild & Light Olive Oil Spray 200ML"
        },
        {
          "name": "百益清淡橄欖油噴霧裝 200ML",
          "price": "$59",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20241120/5046228e-6448-3d9a-8c16-994b57e12d52",
          "product_eng_name": "Filippo Berio Mild & Light Olive Oil Spray 200ML"
        }
      ],
      "name": "百益清淡橄欖油噴霧裝 200ML",
      "price": "$59",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20241120/5046228e-6448-3d9a-8c16-994b57e12d52",
      "product_eng_name": "Filippo Berio Mild & Light Olive Oil Spray 200ML"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%A3%BD%E6%A1%83%E6%B3%B0%E5%9C%8B%E9%87%91%E9%82%8A%E7%B2%89%20300GM/i/102992291.html",
      "uid": "e387e6f114f035d2d100178555b2331b",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "壽桃泰國金邊粉 300GM",
          "price": "$7",
          "offer": "【2件$16.5】$16.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20221108/1f8023eb-54bc-4e70-9e06-355cdeb4000a",
          "product_eng_name": "Sau Tao Pad Thai Rice Noodles 300GM"
        },
        {
          "name": "壽桃泰國金邊粉 300GM",
          "price": "$7",
          "offer": "【2件$16.5】$16.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20221108/1f8023eb-54bc-4e70-9e06-355cdeb4000a",
          "product_eng_name": "Sau Tao Pad Thai Rice Noodles 300GM"
        }
      ],
      "name": "壽桃泰國金邊粉 300GM",
      "price": "$7",
      "offer": "【2件$16.5】$16.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20221108/1f8023eb-54bc-4e70-9e06-355cdeb4000a",
      "product_eng_name": "Sau Tao Pad Thai Rice Noodles 300GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E4%B8%89%E9%A4%8A%E8%BE%A3%E9%9B%9E%E5%8D%A1%E9%82%A6%E5%B0%BC%E5%91%B3%E6%92%88%E9%BA%B5%205%20X%20130GM/i/101323067.html",
      "uid": "44f32575c0fc39a250e45aaa11136924",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "三養辣雞卡邦尼味撈麵 5 X 130GM",
          "price": "$40",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20200821/4d6ded8e-23f0-4461-b8a7-1a9267321c48",
          "product_eng_name": "Samyang Hot Chicken Caronara 5 X 130GM"
        },
        {
          "name": "三養辣雞卡邦尼味撈麵 5 X 130GM",
          "price": "$40",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20200821/4d6ded8e-23f0-4461-b8a7-1a9267321c48",
          "product_eng_name": "Samyang Hot Chicken Caronara 5 X 130GM"
        }
      ],
      "name": "三養辣雞卡邦尼味撈麵 5 X 130GM",
      "price": "$40",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20200821/4d6ded8e-23f0-4461-b8a7-1a9267321c48",
      "product_eng_name": "Samyang Hot Chicken Caronara 5 X 130GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%97%A5%E6%9C%AC%E4%B9%8B%E8%AD%BD%E8%B6%8A%E5%85%89%E7%B1%B3%202KG/i/101346900.html",
      "uid": "720087b2bb810dfaee2026a848b59323",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "日本之譽越光米 2KG",
          "price": "$108",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240529/04ad8901-37c9-3382-a6dd-4fdfb7e6cdc4",
          "product_eng_name": "Nihon no Homare Koshihikari Rice 2KG"
        }
      ],
      "name": "日本之譽越光米 2KG",
      "price": "$108",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240529/04ad8901-37c9-3382-a6dd-4fdfb7e6cdc4",
      "product_eng_name": "Nihon no Homare Koshihikari Rice 2KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E8%B6%85%E5%8A%9B%20%E5%8D%B3%E9%A3%9F%E9%8A%80%E7%B5%B2%E7%B1%B3%E7%B2%89%2065GM/i/101322586.html",
      "uid": "65cbe1e7e93759b35789b1892ded3b94",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "超力 即食銀絲米粉 65GM",
          "price": "$5",
          "offer": "【3件$10.5】$10.5任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210429/d4ceb33a-5f79-46e3-a194-82052017e75e",
          "product_eng_name": "Chewy Instant Mei Fun 65GM"
        },
        {
          "name": "超力 即食銀絲米粉 65GM",
          "price": "$5",
          "offer": "【3件$10.5】$10.5任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210429/d4ceb33a-5f79-46e3-a194-82052017e75e",
          "product_eng_name": "Chewy Instant Mei Fun 65GM"
        }
      ],
      "name": "超力 即食銀絲米粉 65GM",
      "price": "$5",
      "offer": "【3件$10.5】$10.5任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210429/d4ceb33a-5f79-46e3-a194-82052017e75e",
      "product_eng_name": "Chewy Instant Mei Fun 65GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%87%BA%E5%89%8D%E4%B8%80%E4%B8%81%20%E6%A4%92%E9%BA%BB%E9%BA%BB%E6%B2%B9%E5%91%B3%E5%8D%B3%E9%A3%9F%E9%BA%B5%2096GM/i/101351388.html",
      "uid": "4b7cb538c6f577fad146e272104f6eef",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "出前一丁 椒麻麻油味即食麵 96GM",
          "price": "$5",
          "offer": "【8件$28.5】$28.5任揀8件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250407/43fac1a7-b21a-3ace-a142-f6fdfaab8946",
          "product_eng_name": "Demae Peppercorn Sesame Noodles 96GM"
        },
        {
          "name": "出前一丁 椒麻麻油味即食麵 96GM",
          "price": "$5",
          "offer": "【8件$28.5】$28.5任揀8件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250407/43fac1a7-b21a-3ace-a142-f6fdfaab8946",
          "product_eng_name": "Demae Peppercorn Sesame Noodles 96GM"
        }
      ],
      "name": "出前一丁 椒麻麻油味即食麵 96GM",
      "price": "$5",
      "offer": "【8件$28.5】$28.5任揀8件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250407/43fac1a7-b21a-3ace-a142-f6fdfaab8946",
      "product_eng_name": "Demae Peppercorn Sesame Noodles 96GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/La%20Molisana%E8%9D%B4%E8%9D%B6%E7%B2%89%2366%20500GM/i/101381098.html",
      "uid": "9656a65d67a20590bc6a3c02cc0d0c86",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "La Molisana蝴蝶粉#66 500GM",
          "price": "$23",
          "offer": "【2件$30】$30任揀2件；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230714/8c58e05f-895e-4273-90f9-19101c75a059",
          "product_eng_name": "La Molisana Farfalle Rigate #66 500GM"
        },
        {
          "name": "La Molisana蝴蝶粉#66 500GM",
          "price": "$23",
          "offer": "【2件$30】$30任揀2件；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230714/8c58e05f-895e-4273-90f9-19101c75a059",
          "product_eng_name": "La Molisana Farfalle Rigate #66 500GM"
        }
      ],
      "name": "La Molisana蝴蝶粉#66 500GM",
      "price": "$23",
      "offer": "【2件$30】$30任揀2件；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230714/8c58e05f-895e-4273-90f9-19101c75a059",
      "product_eng_name": "La Molisana Farfalle Rigate #66 500GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%A4%A7%E5%B8%AB%E5%A7%90%20%E9%A0%82%E7%B4%9A%E7%91%A4%E6%9F%B1%E8%9D%A6%E5%AD%90%E9%BA%B5(%E5%B9%BC)%206%E5%80%8B%E8%A3%9D/i/101341722.html",
      "uid": "5495479f99c31b3e51564f7fbfa6ccb3",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "大師姐 頂級瑤柱蝦子麵(幼) 6個裝",
          "price": "$98",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250122/b6e799fb-d564-3602-bff2-0bef4d42bf60",
          "product_eng_name": "Dashijie Dried Scallop & Dried Shrimp Roe Noodles (Fine)"
        },
        {
          "name": "大師姐 頂級瑤柱蝦子麵(幼) 6個裝",
          "price": "$98",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250122/b6e799fb-d564-3602-bff2-0bef4d42bf60",
          "product_eng_name": "Dashijie Dried Scallop & Dried Shrimp Roe Noodles (Fine)"
        }
      ],
      "name": "大師姐 頂級瑤柱蝦子麵(幼) 6個裝",
      "price": "$98",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250122/b6e799fb-d564-3602-bff2-0bef4d42bf60",
      "product_eng_name": "Dashijie Dried Scallop & Dried Shrimp Roe Noodles (Fine)"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%88%80%E5%98%9C%20%E7%B4%94%E6%AD%A3%E8%8A%A5%E8%8A%B1%E7%B1%BD%E6%B2%B93%E6%94%AF%E8%A3%9D%20900%20ML/i/101340710.html",
      "uid": "b68fe77f55f975279183560395ae654e",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "刀嘜 純正芥花籽油3支裝 900 ML",
          "price": "$79",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240516/dc11d873-9e28-3dac-be63-e14068ca6d5d",
          "product_eng_name": "Knife Pure Canola Oil 3 x 900ML"
        },
        {
          "name": "刀嘜 純正芥花籽油3支裝 900 ML",
          "price": "$79",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240516/dc11d873-9e28-3dac-be63-e14068ca6d5d",
          "product_eng_name": "Knife Pure Canola Oil 3 x 900ML"
        }
      ],
      "name": "刀嘜 純正芥花籽油3支裝 900 ML",
      "price": "$79",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240516/dc11d873-9e28-3dac-be63-e14068ca6d5d",
      "product_eng_name": "Knife Pure Canola Oil 3 x 900ML"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%A3%BD%E6%A1%83%E5%B9%BC%E7%99%BD%E7%B4%A0%E9%BA%B5%20284GM/i/101335991.html",
      "uid": "0bcfed5ec2eb3359bf3b1295755bfe7c",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "壽桃幼白素麵 284GM",
          "price": "$8",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220505/24794081-9668-4af4-9bfd-ed48d01e566e",
          "product_eng_name": "Sau Tao White Plain Noodles 284GM"
        },
        {
          "name": "壽桃幼白素麵 284GM",
          "price": "$8",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220505/24794081-9668-4af4-9bfd-ed48d01e566e",
          "product_eng_name": "Sau Tao White Plain Noodles 284GM"
        }
      ],
      "name": "壽桃幼白素麵 284GM",
      "price": "$8",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20220505/24794081-9668-4af4-9bfd-ed48d01e566e",
      "product_eng_name": "Sau Tao White Plain Noodles 284GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%A3%BD%E6%A1%83%E7%88%BD%E6%BB%91%E5%A5%B6%E6%B2%B9%E9%BA%B5%E5%84%AA%E6%83%A0%E8%A3%9D4%E5%8C%85%E8%A3%9D/i/101330292.html",
      "uid": "b34b9236ee23393cd2503e10d3a39c4c",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "壽桃爽滑奶油麵優惠裝4包裝",
          "price": "$17",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240913/a3cc7d3b-a9be-3139-b452-eb86edbe32d1",
          "product_eng_name": "(無法擷取英文名稱)"
        },
        {
          "name": "壽桃爽滑奶油麵優惠裝4包裝",
          "price": "$17",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240913/a3cc7d3b-a9be-3139-b452-eb86edbe32d1",
          "product_eng_name": "Sau Tao Crème Noodle (4 packs)"
        }
      ],
      "name": "壽桃爽滑奶油麵優惠裝4包裝",
      "price": "$17",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240913/a3cc7d3b-a9be-3139-b452-eb86edbe32d1",
      "product_eng_name": "Sau Tao Crème Noodle (4 packs)"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%A5%A7%E5%88%A9%E7%89%8C%20%E5%88%9D%E6%A6%A8%E6%A9%84%E6%AC%96%E6%B2%B9%201%20LT/i/113734406.html",
      "uid": "3f754c9f3ed10142165e92bd1b08e397",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "奧利牌 初榨橄欖油 1 LT",
          "price": "$184",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240306/e103428c-4874-3b58-ac2d-8851f6a5b65a",
          "product_eng_name": "Olitalia Extra Virgin Olive Oil 1LT"
        },
        {
          "name": "奧利牌 初榨橄欖油 1 LT",
          "price": "$184",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240306/e103428c-4874-3b58-ac2d-8851f6a5b65a",
          "product_eng_name": "Olitalia Extra Virgin Olive Oil 1LT"
        }
      ],
      "name": "奧利牌 初榨橄欖油 1 LT",
      "price": "$184",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240306/e103428c-4874-3b58-ac2d-8851f6a5b65a",
      "product_eng_name": "Olitalia Extra Virgin Olive Oil 1LT"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E8%BE%9B%E8%BE%A3%E8%BE%A3%E9%9B%9E%E5%91%B3%E5%A4%A7%E7%A2%97%E9%BA%B5/i/114326966.html",
      "uid": "c1429283b45adc150489f593a375ca80",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "辛辣辣雞味大碗麵",
          "price": "$20",
          "offer": "【2件$26】$26任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240923/3ddffa86-b53e-32b1-aab2-02a836716afd",
          "product_eng_name": "Shin Ramyun Chicken Bowl 114GM"
        },
        {
          "name": "辛辣辣雞味大碗麵",
          "price": "$20",
          "offer": "【2件$26】$26任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240923/3ddffa86-b53e-32b1-aab2-02a836716afd",
          "product_eng_name": "Shin Ramyun Chicken Bowl 114GM"
        }
      ],
      "name": "辛辣辣雞味大碗麵",
      "price": "$20",
      "offer": "【2件$26】$26任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240923/3ddffa86-b53e-32b1-aab2-02a836716afd",
      "product_eng_name": "Shin Ramyun Chicken Bowl 114GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%91%B3%E5%91%B3%E4%B8%80%E5%93%81%E7%8F%8D%E5%91%B3%E7%88%8C%E8%82%89%E9%BA%B5%E5%A4%A7%E7%A2%97%E9%BA%B5%20190GM/i/101346680.html",
      "uid": "c611bd7ee2708b044cf885618cb5c9ca",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "味味一品珍味爌肉麵大碗麵 190GM",
          "price": "$21",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210125/fcc36ceb-71fa-4f7b-b438-8819d9bd76e7",
          "product_eng_name": "Weiwei Premium Premium Pork Bowl Noodle 190GM"
        },
        {
          "name": "味味一品珍味爌肉麵大碗麵 190GM",
          "price": "$21",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210125/fcc36ceb-71fa-4f7b-b438-8819d9bd76e7",
          "product_eng_name": "Weiwei Premium Premium Pork Bowl Noodle 190GM"
        }
      ],
      "name": "味味一品珍味爌肉麵大碗麵 190GM",
      "price": "$21",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210125/fcc36ceb-71fa-4f7b-b438-8819d9bd76e7",
      "product_eng_name": "Weiwei Premium Premium Pork Bowl Noodle 190GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E8%BE%B2%E5%BF%83%E7%89%B9%E8%BE%A3%E9%A6%99%E8%8F%87%E6%8B%89%E9%BA%B5%20120GM/i/101350737.html",
      "uid": "720a4b12e19163b5ce045062c458d47c",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "農心特辣香菇拉麵 120GM",
          "price": "$6",
          "offer": "【3件$15】$15任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210520/b1b6cba0-86f1-43ca-978d-745ec37b8653",
          "product_eng_name": "Nong Shim Shin Ramyun 120GM"
        },
        {
          "name": "農心特辣香菇拉麵 120GM",
          "price": "$6",
          "offer": "【3件$15】$15任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210520/b1b6cba0-86f1-43ca-978d-745ec37b8653",
          "product_eng_name": "Nong Shim Shin Ramyun 120GM"
        }
      ],
      "name": "農心特辣香菇拉麵 120GM",
      "price": "$6",
      "offer": "【3件$15】$15任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210520/b1b6cba0-86f1-43ca-978d-745ec37b8653",
      "product_eng_name": "Nong Shim Shin Ramyun 120GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%B6%AD%E5%8A%9B%E4%B8%80%E5%BA%A6%E8%B4%8A%20%E7%B4%85%E7%87%92%E7%89%9B%E8%82%89%E7%A2%97%E9%BA%B5%20200%20GM/i/113737631.html",
      "uid": "62b9439abb76a4dbe458565525c31b0d",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "維力一度贊 紅燒牛肉碗麵 200 GM",
          "price": "$15",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240916/031d7890-1877-3285-945e-669566310e7e",
          "product_eng_name": "Wei Lih Ichiban Delicious Roast Beef Flavour Noodles 200Gm"
        },
        {
          "name": "維力一度贊 紅燒牛肉碗麵 200 GM",
          "price": "$15",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240916/031d7890-1877-3285-945e-669566310e7e",
          "product_eng_name": "Wei Lih Ichiban Delicious Roast Beef Flavour Noodles 200Gm"
        }
      ],
      "name": "維力一度贊 紅燒牛肉碗麵 200 GM",
      "price": "$15",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240916/031d7890-1877-3285-945e-669566310e7e",
      "product_eng_name": "Wei Lih Ichiban Delicious Roast Beef Flavour Noodles 200Gm"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%88%80%E5%98%9C%E9%87%91%E8%A3%9D%E6%BF%83%E9%A6%99%E8%8A%B1%E7%94%9F%E6%B2%B9%203%20X%20900ML/i/101360254.html",
      "uid": "e880e54daa9e45c7099b02e6098a3606",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "刀嘜金裝濃香花生油 3 X 900ML",
          "price": "$107",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240925/acaa28f7-1815-3d8c-8b8e-301a7ec50f35",
          "product_eng_name": "Knife Supreme Peanut Oil 3 X 900ML"
        },
        {
          "name": "刀嘜金裝濃香花生油 3 X 900ML",
          "price": "$107",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240925/acaa28f7-1815-3d8c-8b8e-301a7ec50f35",
          "product_eng_name": "Knife Supreme Peanut Oil 3 X 900ML"
        }
      ],
      "name": "刀嘜金裝濃香花生油 3 X 900ML",
      "price": "$107",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240925/acaa28f7-1815-3d8c-8b8e-301a7ec50f35",
      "product_eng_name": "Knife Supreme Peanut Oil 3 X 900ML"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%BE%8E%E6%8B%BE%E6%B4%BE%20%E9%AE%91%E9%AD%9A%E4%B9%BE%E8%B2%9D%E8%9D%A6%E4%BB%81%E7%B2%A5%E6%96%99%201.4%20KG/i/113660171.html",
      "uid": "8f9ff134595efe1099845c872d9bd599",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "美拾派 鮑魚乾貝蝦仁粥料 1.4 KG",
          "price": "$108",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240105/8a1bcaf7-c0aa-3bfa-a537-2afe2fe3fd65",
          "product_eng_name": "Meysypal Abalone & Shrimp Porridge 1.4KG"
        },
        {
          "name": "美拾派 鮑魚乾貝蝦仁粥料 1.4 KG",
          "price": "$108",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240105/8a1bcaf7-c0aa-3bfa-a537-2afe2fe3fd65",
          "product_eng_name": "Meysypal Abalone & Shrimp Porridge 1.4KG"
        }
      ],
      "name": "美拾派 鮑魚乾貝蝦仁粥料 1.4 KG",
      "price": "$108",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240105/8a1bcaf7-c0aa-3bfa-a537-2afe2fe3fd65",
      "product_eng_name": "Meysypal Abalone & Shrimp Porridge 1.4KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%AE%B6%E6%A8%82%E7%89%8C%E9%9B%B2%E5%90%9E%E5%BF%AB%E7%86%9F%E9%80%9A%E5%BF%83%E7%B2%89%2080GM/i/101356768.html",
      "uid": "f1e50a39d28f21bef17a58356ae06fe2",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "家樂牌雲吞快熟通心粉 80GM",
          "price": "$7",
          "offer": "【3件$17】$17任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220705/23f844d9-3a59-4363-840a-c792ddf7986a",
          "product_eng_name": "Knorr Quick Serve Wonton Macaron 80GM"
        },
        {
          "name": "家樂牌雲吞快熟通心粉 80GM",
          "price": "$7",
          "offer": "【3件$17】$17任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220705/23f844d9-3a59-4363-840a-c792ddf7986a",
          "product_eng_name": "Knorr Quick Serve Wonton Macaron 80GM"
        }
      ],
      "name": "家樂牌雲吞快熟通心粉 80GM",
      "price": "$7",
      "offer": "【3件$17】$17任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20220705/23f844d9-3a59-4363-840a-c792ddf7986a",
      "product_eng_name": "Knorr Quick Serve Wonton Macaron 80GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E9%BB%9E%E9%BB%9E%E7%B6%A0%E5%8D%81%E4%BA%94%E7%A9%80%E7%B1%B3%201KG/i/101839581.html",
      "uid": "999e501ddb386ee5d7bb56d9450c967e",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "點點綠十五穀米 1KG",
          "price": "$62",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250320/1bbe9af8-07f0-326a-9ad8-7f58113c08e9",
          "product_eng_name": "Green Dot Dot 15 Grains Rice 1KG"
        }
      ],
      "name": "點點綠十五穀米 1KG",
      "price": "$62",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250320/1bbe9af8-07f0-326a-9ad8-7f58113c08e9",
      "product_eng_name": "Green Dot Dot 15 Grains Rice 1KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%9D%B1%E9%81%A0%E4%B8%80%E5%93%81%E7%94%9C%E8%96%AF%E7%B2%89%E7%B5%B2%20300GM/i/101340785.html",
      "uid": "8c6673e341ce7dc527e456174182ce80",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "東遠一品甜薯粉絲 300GM",
          "price": "$14",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210517/4d1d22ec-436d-4252-8909-a1b800d31402",
          "product_eng_name": "Dongwon Sweet Potato Vermicelli 300GM"
        },
        {
          "name": "東遠一品甜薯粉絲 300GM",
          "price": "$14",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210517/4d1d22ec-436d-4252-8909-a1b800d31402",
          "product_eng_name": "Dongwon Sweet Potato Vermicelli 300GM"
        }
      ],
      "name": "東遠一品甜薯粉絲 300GM",
      "price": "$14",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210517/4d1d22ec-436d-4252-8909-a1b800d31402",
      "product_eng_name": "Dongwon Sweet Potato Vermicelli 300GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/La%20Molisana%E8%9E%BA%E7%B5%B2%E7%B2%89%2328%20500GM/i/101381096.html",
      "uid": "22d714d7da153e76803c506c9b37db78",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "La Molisana螺絲粉#28 500GM",
          "price": "$23",
          "offer": "【2件$30】$30任揀2件；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230714/76c4de09-f8dc-4c32-9235-c1b97c149a89",
          "product_eng_name": "La Molisana Fusilli #28 500GM"
        },
        {
          "name": "La Molisana螺絲粉#28 500GM",
          "price": "$23",
          "offer": "【2件$30】$30任揀2件；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230714/76c4de09-f8dc-4c32-9235-c1b97c149a89",
          "product_eng_name": "La Molisana Fusilli #28 500GM"
        }
      ],
      "name": "La Molisana螺絲粉#28 500GM",
      "price": "$23",
      "offer": "【2件$30】$30任揀2件；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230714/76c4de09-f8dc-4c32-9235-c1b97c149a89",
      "product_eng_name": "La Molisana Fusilli #28 500GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E7%A6%8F%E5%AD%97%20%E4%B8%8A%E6%B9%AF%E4%BC%8A%E9%BA%B5%E4%BA%94%E5%8C%85%E8%A3%9D6%20X%2090%20GM/i/101335723.html",
      "uid": "9b109aec28305c9d683747eeaeca6f8a",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱福字 上湯伊麵五包裝6 X 90 GM",
          "price": "$150",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231229/18ab3afd-88b3-3eda-8092-5945f7d419fc",
          "product_eng_name": "Fuku* Instant Noodle\\5 Case 6 X 90 GM"
        },
        {
          "name": "原箱福字 上湯伊麵五包裝6 X 90 GM",
          "price": "$150",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231229/18ab3afd-88b3-3eda-8092-5945f7d419fc",
          "product_eng_name": "Fuku* Instant Noodle\\5 Case 6 X 90 GM"
        }
      ],
      "name": "原箱福字 上湯伊麵五包裝6 X 90 GM",
      "price": "$150",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20231229/18ab3afd-88b3-3eda-8092-5945f7d419fc",
      "product_eng_name": "Fuku* Instant Noodle\\5 Case 6 X 90 GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/DEMAE%20ICCHO%20%E6%BF%80%E8%BE%A3%E7%81%AB%E5%B1%B1%E5%91%B3%20100%20GM/i/101328377.html",
      "uid": "08ab0d0b491601ee7fe149c08dabae8b",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "DEMAE ICCHO 激辣火山味 100 GM",
          "price": "$5",
          "offer": "【8件$28.5】$28.5任揀8件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250407/8e73576d-64ea-36fd-b98b-810e6e7df5cb",
          "product_eng_name": "Nissin Demae Iccho Chilli Volcano Noodle 100 GM"
        },
        {
          "name": "DEMAE ICCHO 激辣火山味 100 GM",
          "price": "$5",
          "offer": "【8件$28.5】$28.5任揀8件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250407/8e73576d-64ea-36fd-b98b-810e6e7df5cb",
          "product_eng_name": "Nissin Demae Iccho Chilli Volcano Noodle 100 GM"
        }
      ],
      "name": "DEMAE ICCHO 激辣火山味 100 GM",
      "price": "$5",
      "offer": "【8件$28.5】$28.5任揀8件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250407/8e73576d-64ea-36fd-b98b-810e6e7df5cb",
      "product_eng_name": "Nissin Demae Iccho Chilli Volcano Noodle 100 GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E8%BE%B2%E5%BF%83%20%E9%9F%93%E5%9C%8B%E7%89%88%E8%BE%9B%E8%BE%A3%E9%BA%B5%20600%20GM/i/113559429.html",
      "uid": "d0fcbe2c075e48e142a3b0cb928ea9be",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱農心 韓國版辛辣麵 600 GM",
          "price": "$190",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231013/f2048fbc-788b-3621-93bd-5bd6cbc329dd",
          "product_eng_name": "Nong Shim Korean Shin Ramyun Case 40 x 120GM"
        },
        {
          "name": "原箱農心 韓國版辛辣麵 600 GM",
          "price": "$190",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231013/f2048fbc-788b-3621-93bd-5bd6cbc329dd",
          "product_eng_name": "Nong Shim Korean Shin Ramyun Case 40 x 120GM"
        }
      ],
      "name": "原箱農心 韓國版辛辣麵 600 GM",
      "price": "$190",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20231013/f2048fbc-788b-3621-93bd-5bd6cbc329dd",
      "product_eng_name": "Nong Shim Korean Shin Ramyun Case 40 x 120GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%A5%BD%E6%AD%A1%E8%9E%BA%E8%9E%BA%E8%9E%84%E7%B2%89%20400GM/i/101348254.html",
      "uid": "e09f907d588e0216aa6c041a73bdd141",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "好歡螺螺螄粉 400GM",
          "price": "$18",
          "offer": "【3件$50】$50任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20241014/5a0a2d18-4606-3ceb-94c1-51d1cfbd97e9",
          "product_eng_name": "Haohuanluo Rice Noodle With Snail 400GM"
        },
        {
          "name": "好歡螺螺螄粉 400GM",
          "price": "$18",
          "offer": "【3件$50】$50任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20241014/5a0a2d18-4606-3ceb-94c1-51d1cfbd97e9",
          "product_eng_name": "Haohuanluo Rice Noodle With Snail 400GM"
        }
      ],
      "name": "好歡螺螺螄粉 400GM",
      "price": "$18",
      "offer": "【3件$50】$50任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20241014/5a0a2d18-4606-3ceb-94c1-51d1cfbd97e9",
      "product_eng_name": "Haohuanluo Rice Noodle With Snail 400GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%97%A5%E6%B8%85%E5%87%BA%E5%89%8D%E4%B8%80%E4%B8%81%E6%B5%B7%E9%AE%AE%E5%8D%B3%E9%A3%9F%E9%BA%B5%20100GM/i/101335315.html",
      "uid": "9754914832bbd504142b1b88d165f87d",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "日清出前一丁海鮮即食麵 100GM",
          "price": "$5",
          "offer": "【8件$28.5】$28.5任揀8件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250407/6e15030b-712b-3ab9-a8d4-a24d75bcb4cd",
          "product_eng_name": "Nissin Demae Iccho Seafood Instant Noodle 100GM"
        },
        {
          "name": "日清出前一丁海鮮即食麵 100GM",
          "price": "$5",
          "offer": "【8件$28.5】$28.5任揀8件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250407/6e15030b-712b-3ab9-a8d4-a24d75bcb4cd",
          "product_eng_name": "Nissin Demae Iccho Seafood Instant Noodle 100GM"
        }
      ],
      "name": "日清出前一丁海鮮即食麵 100GM",
      "price": "$5",
      "offer": "【8件$28.5】$28.5任揀8件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250407/6e15030b-712b-3ab9-a8d4-a24d75bcb4cd",
      "product_eng_name": "Nissin Demae Iccho Seafood Instant Noodle 100GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E6%97%A5%E6%B8%85%E5%87%BA%E5%89%8D%E4%B8%80%E4%B8%81%20%E4%B9%9D%E5%B7%9E%E8%B1%AC%E9%AA%A8%E6%BF%83%E6%B9%AF%2030%20X%20100GM/i/101334562.html",
      "uid": "e147a5ab96a5dcbafb7831c95a82b611",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱日清出前一丁 九州豬骨濃湯 30 X 100GM",
          "price": "$105",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230202/3f201336-6c3e-4da6-9003-0fe62ac4021f",
          "product_eng_name": "Nissin Demae Iccho Tonkotsu Noodle Case 30 X 100GM"
        },
        {
          "name": "原箱日清出前一丁 九州豬骨濃湯 30 X 100GM",
          "price": "$105",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230202/3f201336-6c3e-4da6-9003-0fe62ac4021f",
          "product_eng_name": "Nissin Demae Iccho Tonkotsu Noodle Case 30 X 100GM"
        }
      ],
      "name": "原箱日清出前一丁 九州豬骨濃湯 30 X 100GM",
      "price": "$105",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230202/3f201336-6c3e-4da6-9003-0fe62ac4021f",
      "product_eng_name": "Nissin Demae Iccho Tonkotsu Noodle Case 30 X 100GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%85%AC%E4%BB%94%E5%86%AC%E8%8F%9C%E5%8D%B3%E9%A3%9F%E9%BA%B5%205%20X%20103GM/i/101352102.html",
      "uid": "0a8a1204b6bae34ae83738eeef943d77",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "公仔冬菜即食麵 5 X 103GM",
          "price": "$18",
          "offer": "【2件$28】$28任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231011/8a37bb7b-f2a7-3f0f-99c7-420412b9fe9b",
          "product_eng_name": "Doll Pickled Vegetable Noodle 5 X 103GM"
        },
        {
          "name": "公仔冬菜即食麵 5 X 103GM",
          "price": "$18",
          "offer": "【2件$28】$28任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231011/8a37bb7b-f2a7-3f0f-99c7-420412b9fe9b",
          "product_eng_name": "Doll Pickled Vegetable Noodle 5 X 103GM"
        }
      ],
      "name": "公仔冬菜即食麵 5 X 103GM",
      "price": "$18",
      "offer": "【2件$28】$28任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20231011/8a37bb7b-f2a7-3f0f-99c7-420412b9fe9b",
      "product_eng_name": "Doll Pickled Vegetable Noodle 5 X 103GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%A3%BD%E6%A1%83%20%E7%91%A4%E6%9F%B1%E6%B5%B7%E9%AE%AE%E5%91%B3%E6%B7%AE%E5%B1%B1%E9%BA%B5%20180%20GM/i/101328392.html",
      "uid": "b7455d23dd19cb005a3765440c5527a1",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "壽桃 瑤柱海鮮味淮山麵 180 GM",
          "price": "$9",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240823/9985b619-a2c8-3294-8bce-4346edb902e8",
          "product_eng_name": "Sau Tao Dried Scallop and Seafood Flavour Yam Noodles 180GM"
        },
        {
          "name": "壽桃 瑤柱海鮮味淮山麵 180 GM",
          "price": "$9",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240823/9985b619-a2c8-3294-8bce-4346edb902e8",
          "product_eng_name": "Sau Tao Dried Scallop and Seafood Flavour Yam Noodles 180GM"
        }
      ],
      "name": "壽桃 瑤柱海鮮味淮山麵 180 GM",
      "price": "$9",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240823/9985b619-a2c8-3294-8bce-4346edb902e8",
      "product_eng_name": "Sau Tao Dried Scallop and Seafood Flavour Yam Noodles 180GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E9%87%91%E9%A6%99%E8%8C%89%E8%8E%89%E9%A6%99%E7%B1%B3%E7%8E%8B%208KG/i/101352941.html",
      "uid": "aff6963c662a703abdce40a7cf73bcde",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "金香茉莉香米王 8KG",
          "price": "$89",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230726/47597b39-cb80-4fe5-aa3b-3eac513ab66f",
          "product_eng_name": "Kam Heung Premium Jasmine Rice 8KG"
        }
      ],
      "name": "金香茉莉香米王 8KG",
      "price": "$89",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230726/47597b39-cb80-4fe5-aa3b-3eac513ab66f",
      "product_eng_name": "Kam Heung Premium Jasmine Rice 8KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%88%80%E5%98%9C%20%E7%B4%94%E6%AD%A3%E8%8A%B1%E7%94%9F%E6%B2%B9%20750%20ML/i/113467274.html",
      "uid": "fd62d32b32ed144dc7235224616ced02",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "刀嘜 純正花生油 750 ML",
          "price": "$42",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230711/6d3cc3a6-da47-4b24-8255-c74e30a386fe",
          "product_eng_name": "Knife Pure Peanut Oil 750ML"
        },
        {
          "name": "刀嘜 純正花生油 750 ML",
          "price": "$42",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230711/6d3cc3a6-da47-4b24-8255-c74e30a386fe",
          "product_eng_name": "Knife Pure Peanut Oil 750ML"
        }
      ],
      "name": "刀嘜 純正花生油 750 ML",
      "price": "$42",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230711/6d3cc3a6-da47-4b24-8255-c74e30a386fe",
      "product_eng_name": "Knife Pure Peanut Oil 750ML"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%97%A5%E6%B8%85%E5%90%88%E5%91%B3%E9%81%93%E6%B3%95%E5%BC%8F%E9%BE%8D%E8%9D%A6%E6%B9%AF%E5%91%B3%E6%9D%AF%E9%BA%B5%2075GM/i/101337689.html",
      "uid": "0d26f483fade61352b0ec50e42811d13",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "日清合味道法式龍蝦湯味杯麵 75GM",
          "price": "$8",
          "offer": "【2件$14.5】$14.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250327/0aae0170-9ab3-3356-bf04-392d3b7e358c",
          "product_eng_name": "Nissin Lobster Bisque Cup 75GM"
        },
        {
          "name": "日清合味道法式龍蝦湯味杯麵 75GM",
          "price": "$8",
          "offer": "【2件$14.5】$14.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250327/0aae0170-9ab3-3356-bf04-392d3b7e358c",
          "product_eng_name": "Nissin Lobster Bisque Cup 75GM"
        }
      ],
      "name": "日清合味道法式龍蝦湯味杯麵 75GM",
      "price": "$8",
      "offer": "【2件$14.5】$14.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250327/0aae0170-9ab3-3356-bf04-392d3b7e358c",
      "product_eng_name": "Nissin Lobster Bisque Cup 75GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%87%BA%E5%89%8D%E4%B8%80%E4%B8%81%20%E9%BA%BB%E8%BE%A3XO%E9%86%AC%E6%B5%B7%E9%AE%AE%E9%BA%B5%20100%20GM/i/101328378.html",
      "uid": "943871f5b3fc56fbbcca23e1632266b6",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "出前一丁 麻辣XO醬海鮮麵 100 GM",
          "price": "$5",
          "offer": "【8件$28.5】$28.5任揀8件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250407/6c39a311-b84d-3898-aa1b-60c6c59ea91c",
          "product_eng_name": "Nissin Demae Iccho Mala XO Sauce Seafood Noodle 100GM"
        },
        {
          "name": "出前一丁 麻辣XO醬海鮮麵 100 GM",
          "price": "$5",
          "offer": "【8件$28.5】$28.5任揀8件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250407/6c39a311-b84d-3898-aa1b-60c6c59ea91c",
          "product_eng_name": "Nissin Demae Iccho Mala XO Sauce Seafood Noodle 100GM"
        }
      ],
      "name": "出前一丁 麻辣XO醬海鮮麵 100 GM",
      "price": "$5",
      "offer": "【8件$28.5】$28.5任揀8件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250407/6c39a311-b84d-3898-aa1b-60c6c59ea91c",
      "product_eng_name": "Nissin Demae Iccho Mala XO Sauce Seafood Noodle 100GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E9%BB%9E%E9%BB%9E%E7%B6%A0%E6%9C%89%E6%A9%9F%E5%8D%8A%E7%B3%99%E7%B1%B3%201KG/i/101326218.html",
      "uid": "340a8bb0791085ba769cea7e4eacaf07",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "點點綠有機半糙米 1KG",
          "price": "$41",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250320/ca1f08c2-d2b4-3424-83de-b7d8240e6d5c",
          "product_eng_name": "Green Dot Dot Organic Brown Rice Semi 1KG"
        }
      ],
      "name": "點點綠有機半糙米 1KG",
      "price": "$41",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250320/ca1f08c2-d2b4-3424-83de-b7d8240e6d5c",
      "product_eng_name": "Green Dot Dot Organic Brown Rice Semi 1KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/SANUKIHONP%20%E8%AE%9A%E5%B2%90%E7%83%8F%E5%86%AC%20500GM/i/101322697.html",
      "uid": "a52a5653b262c72e98c29c1bc55c7ab3",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "SANUKIHONP 讚岐烏冬 500GM",
          "price": "$20",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240426/481bfca4-c7fd-3f0b-8ccc-9cc6e10ab78e",
          "product_eng_name": "Sanuki Honpo Sanuki Udon 500GM"
        },
        {
          "name": "SANUKIHONP 讚岐烏冬 500GM",
          "price": "$20",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240426/481bfca4-c7fd-3f0b-8ccc-9cc6e10ab78e",
          "product_eng_name": "Sanuki Honpo Sanuki Udon 500GM"
        }
      ],
      "name": "SANUKIHONP 讚岐烏冬 500GM",
      "price": "$20",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240426/481bfca4-c7fd-3f0b-8ccc-9cc6e10ab78e",
      "product_eng_name": "Sanuki Honpo Sanuki Udon 500GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%87%9F%E5%A4%9A%E5%8D%B0%E5%B0%BC%E6%92%88%E9%BA%B5%205%20X%2085GM/i/101843334.html",
      "uid": "079a9a5cd3d48ede86e19371b04d2101",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "營多印尼撈麵 5 X 85GM",
          "price": "$22",
          "offer": "【2件$23】$23任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240726/4cefe665-bdd6-34e2-af9e-444bf1b424ee",
          "product_eng_name": "Indomie Mi Goreng Fried Noodles 5 x 85GM (Parallel Import)"
        },
        {
          "name": "營多印尼撈麵 5 X 85GM",
          "price": "$22",
          "offer": "【2件$23】$23任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240726/4cefe665-bdd6-34e2-af9e-444bf1b424ee",
          "product_eng_name": "Indomie Mi Goreng Fried Noodles 5 x 85GM (Parallel Import)"
        }
      ],
      "name": "營多印尼撈麵 5 X 85GM",
      "price": "$22",
      "offer": "【2件$23】$23任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240726/4cefe665-bdd6-34e2-af9e-444bf1b424ee",
      "product_eng_name": "Indomie Mi Goreng Fried Noodles 5 x 85GM (Parallel Import)"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%BB%BF%E5%B0%8F%E9%A3%BD%20%E8%82%A5%E6%B1%81%E7%B1%B3%E7%B7%9A%E6%9D%AF%E9%9D%A2%20112.6G/i/101341183.html",
      "uid": "8dafe865b3af5e0574648a13dbac0497",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "滿小飽 肥汁米線杯面 112.6G",
          "price": "$9",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240124/42ed936a-c11d-3c1b-bd15-e80ce4146278",
          "product_eng_name": "Man Xiao Bao Rice Noodle And Rich Sauce Cup 112.6G"
        },
        {
          "name": "滿小飽 肥汁米線杯面 112.6G",
          "price": "$9",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240124/42ed936a-c11d-3c1b-bd15-e80ce4146278",
          "product_eng_name": "Man Xiao Bao Rice Noodle And Rich Sauce Cup 112.6G"
        }
      ],
      "name": "滿小飽 肥汁米線杯面 112.6G",
      "price": "$9",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240124/42ed936a-c11d-3c1b-bd15-e80ce4146278",
      "product_eng_name": "Man Xiao Bao Rice Noodle And Rich Sauce Cup 112.6G"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%8D%85%E7%90%83%E5%98%9C%E5%81%A5%E5%BA%B7%E9%AB%98%E6%B2%B9%E9%85%B8%E8%91%B5%E8%8A%B1%E7%B1%BD%E6%B2%B9(%E9%9B%B6%E5%8F%8D%E5%BC%8F%E8%84%82%E8%82%AA)%203%20X%20900ML/i/102697421.html",
      "uid": "dfb52279f95457b10eeb78696e91e865",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "獅球嘜健康高油酸葵花籽油(零反式脂肪) 3 X 900ML",
          "price": "$109",
          "offer": "【買1件送1件贈品】購買每1件，即送1件人氣贈品；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220613/72f0afdf-bc1a-4c59-8883-54add6dd0318",
          "product_eng_name": "Lion & Globe High Oleic Sunflower Seed Oil (Zero Trans Fat) 3 X 900ML"
        },
        {
          "name": "獅球嘜健康高油酸葵花籽油(零反式脂肪) 3 X 900ML",
          "price": "$109",
          "offer": "【買1件送1件贈品】購買每1件，即送1件人氣贈品；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220613/72f0afdf-bc1a-4c59-8883-54add6dd0318",
          "product_eng_name": "Lion & Globe High Oleic Sunflower Seed Oil (Zero Trans Fat) 3 X 900ML"
        }
      ],
      "name": "獅球嘜健康高油酸葵花籽油(零反式脂肪) 3 X 900ML",
      "price": "$109",
      "offer": "【買1件送1件贈品】購買每1件，即送1件人氣贈品；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20220613/72f0afdf-bc1a-4c59-8883-54add6dd0318",
      "product_eng_name": "Lion & Globe High Oleic Sunflower Seed Oil (Zero Trans Fat) 3 X 900ML"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E8%B6%85%E5%8A%9B%E7%89%B9%E7%B4%9A%E9%8A%80%E7%B5%B2%E7%82%92%E7%B1%B3%E7%B2%89%20280GM/i/101341227.html",
      "uid": "f9aca52f7efac4f7fe2362143b084699",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "超力特級銀絲炒米粉 280GM",
          "price": "$16",
          "offer": "【2件$18】$18任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240916/593a7c44-c6d8-3b91-93d2-a66a59d23720",
          "product_eng_name": "Chewy Dried Rice Stick 280GM"
        },
        {
          "name": "超力特級銀絲炒米粉 280GM",
          "price": "$16",
          "offer": "【2件$18】$18任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240916/593a7c44-c6d8-3b91-93d2-a66a59d23720",
          "product_eng_name": "Chewy Dried Rice Stick 280GM"
        }
      ],
      "name": "超力特級銀絲炒米粉 280GM",
      "price": "$16",
      "offer": "【2件$18】$18任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240916/593a7c44-c6d8-3b91-93d2-a66a59d23720",
      "product_eng_name": "Chewy Dried Rice Stick 280GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%85%AC%E4%BB%94%E9%BB%9E%E5%BF%83%E9%BA%B5%E6%97%A5%E5%BC%8F%E6%B5%B7%E8%80%81%E5%91%B3%E5%8D%B3%E9%A3%9F%E9%BA%B5%2037GM/i/113251509.html",
      "uid": "fa194c344bacf711840e308a8297b304",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "公仔點心麵日式海老味即食麵 37GM",
          "price": "$4",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240926/cb806e03-c77e-30bf-bece-b56708d6d71b",
          "product_eng_name": "Doll Dim Sum Noodle Japanese Shrimp Flavour 37GM"
        },
        {
          "name": "公仔點心麵日式海老味即食麵 37GM",
          "price": "$4",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240926/cb806e03-c77e-30bf-bece-b56708d6d71b",
          "product_eng_name": "Doll Dim Sum Noodle Japanese Shrimp Flavour 37GM"
        }
      ],
      "name": "公仔點心麵日式海老味即食麵 37GM",
      "price": "$4",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240926/cb806e03-c77e-30bf-bece-b56708d6d71b",
      "product_eng_name": "Doll Dim Sum Noodle Japanese Shrimp Flavour 37GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/Ja-Rice%E6%97%A5%E6%9C%AC%E8%B6%8A%E5%85%89%E7%B1%B3%202KG/i/101323917.html",
      "uid": "fe5d093547bd3f25bf0022568e7e98b9",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "Ja-Rice日本越光米 2KG",
          "price": "$69",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210430/e61b3457-c737-4ecf-abe1-bf14d96dcc76",
          "product_eng_name": "Ja-Rice Koshihikari Rice 2KG"
        }
      ],
      "name": "Ja-Rice日本越光米 2KG",
      "price": "$69",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210430/e61b3457-c737-4ecf-abe1-bf14d96dcc76",
      "product_eng_name": "Ja-Rice Koshihikari Rice 2KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E8%BE%B2%E5%BF%83%E7%9F%B3%E7%A2%A2%E7%A2%97%E9%BA%B5%20117GM/i/101353940.html",
      "uid": "6bdbf35770bc9bb653dc0ea6f3aac57a",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "農心石碢碗麵 117GM",
          "price": "$9",
          "offer": "【2件$12】$12任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20201016/4d1e3309-eca5-426a-8375-b7d30c9141f4",
          "product_eng_name": "Nong Shim Clay Pot Bowl Noodles 117GM"
        },
        {
          "name": "農心石碢碗麵 117GM",
          "price": "$9",
          "offer": "【2件$12】$12任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20201016/4d1e3309-eca5-426a-8375-b7d30c9141f4",
          "product_eng_name": "Nong Shim Clay Pot Bowl Noodles 117GM"
        }
      ],
      "name": "農心石碢碗麵 117GM",
      "price": "$9",
      "offer": "【2件$12】$12任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20201016/4d1e3309-eca5-426a-8375-b7d30c9141f4",
      "product_eng_name": "Nong Shim Clay Pot Bowl Noodles 117GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%97%A5%E6%9C%AC%E7%83%8F%E5%86%AC%E9%BA%B5%20600GM/i/101359754.html",
      "uid": "87efffc301dcabe2057cf08c202c8c77",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "日本烏冬麵 600GM",
          "price": "$15",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240916/a99990dc-3c2b-38ac-94b4-5105be218324",
          "product_eng_name": "Yoshiya Udon Noodles 600GM"
        },
        {
          "name": "日本烏冬麵 600GM",
          "price": "$15",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240916/a99990dc-3c2b-38ac-94b4-5105be218324",
          "product_eng_name": "Yoshiya Udon Noodles 600GM"
        }
      ],
      "name": "日本烏冬麵 600GM",
      "price": "$15",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240916/a99990dc-3c2b-38ac-94b4-5105be218324",
      "product_eng_name": "Yoshiya Udon Noodles 600GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%BE%A1%E5%93%81%E7%9A%87%E5%84%AA%E8%B3%AA%E6%B3%B0%E5%9C%8B%E8%8C%89%E8%8E%89%E9%A6%99%E7%B1%B3%202KG/i/101381362.html",
      "uid": "40d33c1e382bfc25b2b31d4604ebc661",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "御品皇優質泰國茉莉香米 2KG",
          "price": "$30",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250306/ad5b0923-853f-3f30-9036-6912ad2076c3",
          "product_eng_name": "Yu Pin King Thai Jasmine Fragrant Rice 2KG"
        }
      ],
      "name": "御品皇優質泰國茉莉香米 2KG",
      "price": "$30",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250306/ad5b0923-853f-3f30-9036-6912ad2076c3",
      "product_eng_name": "Yu Pin King Thai Jasmine Fragrant Rice 2KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1INDOMIE%20%E5%8D%B0%E5%B0%BC%E7%89%88-%E6%92%88%E9%BA%B5%20425%20GM/i/113559399.html",
      "uid": "dcb77315b3236ede83abc565d777a100",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱INDOMIE 印尼版-撈麵 425 GM",
          "price": "$84",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231013/b6c6f020-33e0-3413-90dd-d485033d7433",
          "product_eng_name": "Indomie Mi Goreng Fried Noodles Case 40 x 85GM (Parallel Import)"
        },
        {
          "name": "原箱INDOMIE 印尼版-撈麵 425 GM",
          "price": "$84",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231013/b6c6f020-33e0-3413-90dd-d485033d7433",
          "product_eng_name": "Indomie Mi Goreng Fried Noodles Case 40 x 85GM (Parallel Import)"
        }
      ],
      "name": "原箱INDOMIE 印尼版-撈麵 425 GM",
      "price": "$84",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20231013/b6c6f020-33e0-3413-90dd-d485033d7433",
      "product_eng_name": "Indomie Mi Goreng Fried Noodles Case 40 x 85GM (Parallel Import)"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E9%BB%9E%E9%BB%9E%E7%B6%A0%E6%9C%89%E6%A9%9F%E5%8D%81%E7%A9%80%E7%B1%B3%201KG/i/101326321.html",
      "uid": "f59fcd8cae648304a1d051ca2ae78fbf",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "點點綠有機十穀米 1KG",
          "price": "$74",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250320/c62df315-abd0-3c7a-a88b-6023f8b5bc00",
          "product_eng_name": "Green Dot Dot Organic Ten Grains Rice 1KG"
        }
      ],
      "name": "點點綠有機十穀米 1KG",
      "price": "$74",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250320/c62df315-abd0-3c7a-a88b-6023f8b5bc00",
      "product_eng_name": "Green Dot Dot Organic Ten Grains Rice 1KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E5%BE%A1%E5%93%81%E7%9A%87%20%E7%B4%85%E6%B2%B9%E9%A6%99%E8%BE%A3%E6%8B%8C%E9%BA%B5%2098%20GM/i/113612026.html",
      "uid": "f820b43b22c4d4ed6e9239b8a34b67f2",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱御品皇 紅油香辣拌麵 98 GM",
          "price": "$120",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230926/791e05ab-ac39-3191-b6d3-f170deb859bf",
          "product_eng_name": "Yu Pin King Chili Oil Dry-Stirred Noodles Case 30 x 98GM"
        },
        {
          "name": "原箱御品皇 紅油香辣拌麵 98 GM",
          "price": "$120",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230926/791e05ab-ac39-3191-b6d3-f170deb859bf",
          "product_eng_name": "(無法擷取英文名稱)"
        }
      ],
      "name": "原箱御品皇 紅油香辣拌麵 98 GM",
      "price": "$120",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230926/791e05ab-ac39-3191-b6d3-f170deb859bf",
      "product_eng_name": "(無法擷取英文名稱)"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%85%AC%E4%BB%94%E6%B2%99%E5%97%B2%E9%9B%9E%E8%82%89%E4%B8%B2%E7%87%92%E5%91%B3%E7%82%92%E9%BA%B5%E7%8E%8B%20112GM/i/102689381.html",
      "uid": "11075bd98cc0e21022ba9f0e34695084",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "公仔沙嗲雞肉串燒味炒麵王 112GM",
          "price": "$7",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250320/088c585e-be06-3a95-a179-687c1fc281e1",
          "product_eng_name": "Doll Satay Chicken Skewer Flavour 112GM"
        }
      ],
      "name": "公仔沙嗲雞肉串燒味炒麵王 112GM",
      "price": "$7",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250320/088c585e-be06-3a95-a179-687c1fc281e1",
      "product_eng_name": "Doll Satay Chicken Skewer Flavour 112GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E4%B8%8D%E5%80%92%E7%BF%81%E8%8A%9D%E5%A3%AB%E6%92%88%E7%A2%97%E9%BA%B5%2095GM/i/101349290.html",
      "uid": "bd0ff3f115ec33459134a552800eb2cf",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "不倒翁芝士撈碗麵 95GM",
          "price": "$16",
          "offer": "【2件$21】$21任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240917/35bb925b-fa1c-340a-846c-ac9d54d13702",
          "product_eng_name": "Ottogi Cheese Bokki Bowl 95GM"
        },
        {
          "name": "不倒翁芝士撈碗麵 95GM",
          "price": "$16",
          "offer": "【2件$21】$21任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240917/35bb925b-fa1c-340a-846c-ac9d54d13702",
          "product_eng_name": "Ottogi Cheese Bokki Bowl 95GM"
        }
      ],
      "name": "不倒翁芝士撈碗麵 95GM",
      "price": "$16",
      "offer": "【2件$21】$21任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240917/35bb925b-fa1c-340a-846c-ac9d54d13702",
      "product_eng_name": "Ottogi Cheese Bokki Bowl 95GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%A3%BD%E6%A1%83%E5%B9%BC%E5%85%A8%E8%9B%8B%E9%BA%B5%20454GM/i/101342538.html",
      "uid": "8bf85d27931a396c35f5b1cb71bdba9e",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "壽桃幼全蛋麵 454GM",
          "price": "$13",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220505/808c8eef-0767-453a-a88b-94cd8e381922",
          "product_eng_name": "Sau Tao Thin Egg Noodle 454GM"
        },
        {
          "name": "壽桃幼全蛋麵 454GM",
          "price": "$13",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220505/808c8eef-0767-453a-a88b-94cd8e381922",
          "product_eng_name": "Sau Tao Thin Egg Noodle 454GM"
        }
      ],
      "name": "壽桃幼全蛋麵 454GM",
      "price": "$13",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20220505/808c8eef-0767-453a-a88b-94cd8e381922",
      "product_eng_name": "Sau Tao Thin Egg Noodle 454GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%8D%85%E7%90%83%E5%98%9C%E5%88%9D%E6%90%BE%E6%A9%84%E6%AC%96%E8%8A%A5%E8%8A%B1%E7%B1%BD%E6%B2%B9%203LT/i/101343747.html",
      "uid": "e97fb579106fa17637164a78f8d4841e",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "獅球嘜初搾橄欖芥花籽油 3LT",
          "price": "$106",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230324/9cc8043e-b6b8-4b15-a2ae-a73f861680f1",
          "product_eng_name": "Lion & Globe Extra Virgin Oil + Canola Oil 3LT"
        },
        {
          "name": "獅球嘜初搾橄欖芥花籽油 3LT",
          "price": "$106",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230324/9cc8043e-b6b8-4b15-a2ae-a73f861680f1",
          "product_eng_name": "Lion & Globe Extra Virgin Oil + Canola Oil 3LT"
        }
      ],
      "name": "獅球嘜初搾橄欖芥花籽油 3LT",
      "price": "$106",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230324/9cc8043e-b6b8-4b15-a2ae-a73f861680f1",
      "product_eng_name": "Lion & Globe Extra Virgin Oil + Canola Oil 3LT"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%97%A5%E6%B8%85%E5%87%BA%E5%89%8D%E4%B8%80%E4%B8%81%E5%8C%97%E6%B5%B7%E9%81%93%E5%B0%8F%E9%BA%A5%E7%B2%89%E9%BB%91%E8%92%9C%E8%B1%AC%E9%AA%A8%E9%BA%B5%205%20X%20100GM/i/101843840.html",
      "uid": "05a821b450d14d29b022ce9a22f29fbe",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "日清出前一丁北海道小麥粉黑蒜豬骨麵 5 X 100GM",
          "price": "$21",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240920/44e88b4c-197a-3228-a9a8-541c427ea113",
          "product_eng_name": "Nissin Demae Iccho Hokkaido Wheat Flour Black Garlic Oil Tonkotsu Flavour 5 X 100GM"
        },
        {
          "name": "日清出前一丁北海道小麥粉黑蒜豬骨麵 5 X 100GM",
          "price": "$21",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240920/44e88b4c-197a-3228-a9a8-541c427ea113",
          "product_eng_name": "Nissin Demae Iccho Hokkaido Wheat Flour Black Garlic Oil Tonkotsu Flavour 5 X 100GM"
        }
      ],
      "name": "日清出前一丁北海道小麥粉黑蒜豬骨麵 5 X 100GM",
      "price": "$21",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240920/44e88b4c-197a-3228-a9a8-541c427ea113",
      "product_eng_name": "Nissin Demae Iccho Hokkaido Wheat Flour Black Garlic Oil Tonkotsu Flavour 5 X 100GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E8%BE%B2%E5%BF%83%E9%9D%9E%E6%B2%B9%E7%82%B8%E8%BE%9B%E6%8B%89%E9%BA%B5%204%20X%2097GM/i/101359960.html",
      "uid": "522a47b3cbcc44d7cb6dc6f94d484e19",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "農心非油炸辛拉麵 4 X 97GM",
          "price": "$32",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210520/15b66051-ddd6-40c9-8bea-a838d1c09ad1",
          "product_eng_name": "Nong Shim Non-Frying Noodle 4 X 97GM"
        },
        {
          "name": "農心非油炸辛拉麵 4 X 97GM",
          "price": "$32",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210520/15b66051-ddd6-40c9-8bea-a838d1c09ad1",
          "product_eng_name": "Nong Shim Non-Frying Noodle 4 X 97GM"
        }
      ],
      "name": "農心非油炸辛拉麵 4 X 97GM",
      "price": "$32",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210520/15b66051-ddd6-40c9-8bea-a838d1c09ad1",
      "product_eng_name": "Nong Shim Non-Frying Noodle 4 X 97GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E9%9D%92%E7%9A%84%E8%BE%B2%E5%A0%B4%E5%8D%81%E5%85%AB%E7%A9%80%201.2KG/i/102105951.html",
      "uid": "1629306a83de46b337c5226764286835",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "青的農場十八穀 1.2KG",
          "price": "$68",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220322/eb6ecfc5-552f-4669-a399-5db0086b0e9b",
          "product_eng_name": "Green Farm Mixed Grains 1.2KG"
        }
      ],
      "name": "青的農場十八穀 1.2KG",
      "price": "$68",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20220322/eb6ecfc5-552f-4669-a399-5db0086b0e9b",
      "product_eng_name": "Green Farm Mixed Grains 1.2KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E7%A6%8F%E5%AD%97%20%E4%B8%8A%E6%B9%AF%E4%BC%8A%E9%BA%B5%2030X90GM/i/101346472.html",
      "uid": "09146365f5e513bebdbe632de3d8b09c",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱福字 上湯伊麵 30X90GM",
          "price": "$93",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230202/cddd1217-7b49-497b-b72f-1cd75005dd87",
          "product_eng_name": "Fuku Noodle 30X90GM"
        },
        {
          "name": "原箱福字 上湯伊麵 30X90GM",
          "price": "$93",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230202/cddd1217-7b49-497b-b72f-1cd75005dd87",
          "product_eng_name": "Fuku Noodle 30X90GM"
        }
      ],
      "name": "原箱福字 上湯伊麵 30X90GM",
      "price": "$93",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230202/cddd1217-7b49-497b-b72f-1cd75005dd87",
      "product_eng_name": "Fuku Noodle 30X90GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%A4%A7%E6%8B%99%E5%8C%A0%E4%BA%BA%20%E9%B5%9D%E6%B2%B9%E5%85%88%E7%94%9F%E9%B5%9D%E6%B2%B9%E9%A6%99%E8%92%9C%20111%20GM/i/101326134.html",
      "uid": "a02a64d1829fc8040aead4f7921fa087",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "大拙匠人 鵝油先生鵝油香蒜 111 GM",
          "price": "$60",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240823/daa0d167-87c6-34d2-83a2-625eae10730b",
          "product_eng_name": "Kungfood Mr. Goose Premium Goose Oil Scallion Noodles 3 x 111GM"
        },
        {
          "name": "大拙匠人 鵝油先生鵝油香蒜 111 GM",
          "price": "$60",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240823/daa0d167-87c6-34d2-83a2-625eae10730b",
          "product_eng_name": "Kungfood Mr. Goose Premium Goose Oil Scallion Noodles 3 x 111GM"
        }
      ],
      "name": "大拙匠人 鵝油先生鵝油香蒜 111 GM",
      "price": "$60",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240823/daa0d167-87c6-34d2-83a2-625eae10730b",
      "product_eng_name": "Kungfood Mr. Goose Premium Goose Oil Scallion Noodles 3 x 111GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E8%BE%B2%E5%BF%83%E9%A6%AC%E7%8E%B2%E8%96%AF%E6%8E%92%E9%AA%A8%205%20X%20120GM/i/101344732.html",
      "uid": "7e855373de5b9ddf6576607a1a60132a",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "農心馬玲薯排骨 5 X 120GM",
          "price": "$20",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240916/212cbb57-65f8-392d-ae3a-61ef55751d0f",
          "product_eng_name": "Nong Shim Potato Pork Noodle 5 X 120GM"
        },
        {
          "name": "農心馬玲薯排骨 5 X 120GM",
          "price": "$20",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240916/212cbb57-65f8-392d-ae3a-61ef55751d0f",
          "product_eng_name": "Nong Shim Potato Pork Noodle 5 X 120GM"
        }
      ],
      "name": "農心馬玲薯排骨 5 X 120GM",
      "price": "$20",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240916/212cbb57-65f8-392d-ae3a-61ef55751d0f",
      "product_eng_name": "Nong Shim Potato Pork Noodle 5 X 120GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%BE%A1%E5%93%81%E7%9A%87%20%E5%AE%85%E6%AF%8D%E9%9B%9E%E5%91%B3%E6%B9%AF%E9%BA%B5%20103%20GM/i/113464009.html",
      "uid": "07d2a0ff42d2a79587484c2b6c7110cd",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "御品皇 宅母雞味湯麵 103 GM",
          "price": "$4",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240925/b64e0862-f10b-31a3-b949-dab7e1d85509",
          "product_eng_name": "Yu Pin King Chicken Flavour Soup Noodles 103GM"
        },
        {
          "name": "御品皇 宅母雞味湯麵 103 GM",
          "price": "$4",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240925/b64e0862-f10b-31a3-b949-dab7e1d85509",
          "product_eng_name": "Yu Pin King Chicken Flavour Soup Noodles 103GM"
        }
      ],
      "name": "御品皇 宅母雞味湯麵 103 GM",
      "price": "$4",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240925/b64e0862-f10b-31a3-b949-dab7e1d85509",
      "product_eng_name": "Yu Pin King Chicken Flavour Soup Noodles 103GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%BE%A1%E5%93%81%E7%9A%87%E7%B4%85%E7%B1%B3%202KG/i/101572853.html",
      "uid": "edad45733641a3d889c7bcdfc9f24936",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "御品皇紅米 2KG",
          "price": "$64",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250306/95d22901-2657-30c3-bf18-a73f20dc120e",
          "product_eng_name": "Yu Pin King Pure Red Rice 2KG"
        }
      ],
      "name": "御品皇紅米 2KG",
      "price": "$64",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250306/95d22901-2657-30c3-bf18-a73f20dc120e",
      "product_eng_name": "Yu Pin King Pure Red Rice 2KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%BE%A1%E5%93%81%E7%9A%87%20%E9%A0%82%E7%B4%9A%E6%B3%B0%E5%9C%8B%E8%8C%89%E8%8E%89%E9%A6%99%E7%B1%B3%202KG/i/113248014.html",
      "uid": "c4eaa20ee972be5172adc54e76a4d665",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "御品皇 頂級泰國茉莉香米 2KG",
          "price": "$33",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250306/8b79f2e9-f8fb-3462-a76e-224071349c5f",
          "product_eng_name": "Yu Pin King Thai Hom Mali Rice 2KG"
        }
      ],
      "name": "御品皇 頂級泰國茉莉香米 2KG",
      "price": "$33",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250306/8b79f2e9-f8fb-3462-a76e-224071349c5f",
      "product_eng_name": "Yu Pin King Thai Hom Mali Rice 2KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%20%E5%BE%A1%E5%93%81%E7%9A%87%E8%92%9C%E9%A6%99%E9%BA%BB%E9%86%AC%E6%8B%8C%E9%BA%B5%2030x115GM/i/101362431.html",
      "uid": "9f2f3933a5ce60cfa8770aa736390377",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱 御品皇蒜香麻醬拌麵 30x115GM",
          "price": "$120",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250206/d4105a4d-e92d-31ff-9620-cef272b53a62",
          "product_eng_name": "Yu Pin King Garlic Sesame Sauce Case 30X115GM"
        },
        {
          "name": "原箱 御品皇蒜香麻醬拌麵 30x115GM",
          "price": "$120",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250206/d4105a4d-e92d-31ff-9620-cef272b53a62",
          "product_eng_name": "Yu Pin King Garlic Sesame Sauce Case 30X115GM"
        }
      ],
      "name": "原箱 御品皇蒜香麻醬拌麵 30x115GM",
      "price": "$120",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250206/d4105a4d-e92d-31ff-9620-cef272b53a62",
      "product_eng_name": "Yu Pin King Garlic Sesame Sauce Case 30X115GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E5%87%BA%E5%89%8D%E4%B8%80%E4%B8%81%20%E9%BA%BB%E6%B2%B9%E5%91%B3%E7%A2%97%E9%BA%B5%2099%20GM/i/113559504.html",
      "uid": "415f9e666629979c828f8297136716f4",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱出前一丁 麻油味碗麵 99 GM",
          "price": "$95",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231013/8b41989f-5cd4-3521-8a71-9ee28d76d14f",
          "product_eng_name": "Nissin Demae Iccho Sesame Oil Bowl Noodles Case 12 x 99GM"
        },
        {
          "name": "原箱出前一丁 麻油味碗麵 99 GM",
          "price": "$95",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231013/8b41989f-5cd4-3521-8a71-9ee28d76d14f",
          "product_eng_name": "Nissin Demae Iccho Sesame Oil Bowl Noodles Case 12 x 99GM"
        }
      ],
      "name": "原箱出前一丁 麻油味碗麵 99 GM",
      "price": "$95",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20231013/8b41989f-5cd4-3521-8a71-9ee28d76d14f",
      "product_eng_name": "Nissin Demae Iccho Sesame Oil Bowl Noodles Case 12 x 99GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%A3%BD%E6%A1%83%E6%B7%AE%E5%B1%B1%E9%BA%B5%20143GM/i/102126396.html",
      "uid": "68c82402df42e4fefb24d7396d4a5279",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "壽桃淮山麵 143GM",
          "price": "$3",
          "offer": "【2件$9】$9任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220615/caa2fd99-6c10-45ee-a609-92b04dcc1ebe",
          "product_eng_name": "Sau Tao Yam Noodles 143GM"
        },
        {
          "name": "壽桃淮山麵 143GM",
          "price": "$3",
          "offer": "【2件$9】$9任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220615/caa2fd99-6c10-45ee-a609-92b04dcc1ebe",
          "product_eng_name": "Sau Tao Yam Noodles 143GM"
        }
      ],
      "name": "壽桃淮山麵 143GM",
      "price": "$3",
      "offer": "【2件$9】$9任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20220615/caa2fd99-6c10-45ee-a609-92b04dcc1ebe",
      "product_eng_name": "Sau Tao Yam Noodles 143GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%97%A5%E6%B8%85%E5%90%88%E5%91%B3%E9%81%93%20%E8%B1%AC%E9%AA%A8%E6%BF%83%E6%B9%AF%E5%91%B3%2075%20GM/i/101328243.html",
      "uid": "82b8974e7a0bd5cab15647360ba9b7c4",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "日清合味道 豬骨濃湯味 75 GM",
          "price": "$8",
          "offer": "【2件$14.5】$14.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250327/232439ba-b7a9-336b-9efb-2fc9b79e7ca2",
          "product_eng_name": "Nissin Tonkotsu Cup Noodle 75GM"
        },
        {
          "name": "日清合味道 豬骨濃湯味 75 GM",
          "price": "$8",
          "offer": "【2件$14.5】$14.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250327/232439ba-b7a9-336b-9efb-2fc9b79e7ca2",
          "product_eng_name": "Nissin Tonkotsu Cup Noodle 75GM"
        }
      ],
      "name": "日清合味道 豬骨濃湯味 75 GM",
      "price": "$8",
      "offer": "【2件$14.5】$14.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250327/232439ba-b7a9-336b-9efb-2fc9b79e7ca2",
      "product_eng_name": "Nissin Tonkotsu Cup Noodle 75GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%B2%A9%E7%94%B0%E8%A3%BD%E9%BA%B5%E6%89%80%20%E7%84%A1%E9%B9%BD%E8%A3%BD%E9%BA%B5%E8%95%8E%E9%BA%A5%E9%BA%B5%20250%20GM/i/114215806.html",
      "uid": "4c0189e909353e1d152746bf6ed8f21b",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "岩田製麵所 無鹽製麵蕎麥麵 250 GM",
          "price": "$18",
          "offer": "【4件$50】$50任揀4件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240429/2025e5a2-c676-3c51-84bd-5eb0a279d97d",
          "product_eng_name": "Aoi Foods Muenseiho Soba 250GM"
        },
        {
          "name": "岩田製麵所 無鹽製麵蕎麥麵 250 GM",
          "price": "$18",
          "offer": "【4件$50】$50任揀4件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240429/2025e5a2-c676-3c51-84bd-5eb0a279d97d",
          "product_eng_name": "Aoi Foods Muenseiho Soba 250GM"
        }
      ],
      "name": "岩田製麵所 無鹽製麵蕎麥麵 250 GM",
      "price": "$18",
      "offer": "【4件$50】$50任揀4件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240429/2025e5a2-c676-3c51-84bd-5eb0a279d97d",
      "product_eng_name": "Aoi Foods Muenseiho Soba 250GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%AE%B6%E6%A8%82%E7%89%8C%E7%89%9B%E8%82%89%E5%91%B3%E5%BF%AB%E7%86%9F%E9%80%9A%E5%BF%83%E7%B2%89%2080GM/i/101356763.html",
      "uid": "2ffb233fad1f8170fc3e38e7ffb70ab6",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "家樂牌牛肉味快熟通心粉 80GM",
          "price": "$7",
          "offer": "【3件$17】$17任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220705/dce446c4-8fe4-405c-87de-88f31fab6da6",
          "product_eng_name": "Knorr Quick Serve Beef Macaron 80GM"
        },
        {
          "name": "家樂牌牛肉味快熟通心粉 80GM",
          "price": "$7",
          "offer": "【3件$17】$17任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220705/dce446c4-8fe4-405c-87de-88f31fab6da6",
          "product_eng_name": "Knorr Quick Serve Beef Macaron 80GM"
        }
      ],
      "name": "家樂牌牛肉味快熟通心粉 80GM",
      "price": "$7",
      "offer": "【3件$17】$17任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20220705/dce446c4-8fe4-405c-87de-88f31fab6da6",
      "product_eng_name": "Knorr Quick Serve Beef Macaron 80GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E5%85%AC%E4%BB%94%20%E9%BB%9E%E5%BF%83%E9%BA%B5%EF%BC%8D%E6%B5%B7%E9%AE%AE18%20X%2034%20GM/i/101335696.html",
      "uid": "2034329d66ecc5815ffd9ebf552d1fbf",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱公仔 點心麵－海鮮18 X 34 GM",
          "price": "$62",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231221/0a0c6842-a4ae-3016-8f9f-b6c0eb2485db",
          "product_eng_name": "Doll Dim Sum Seafood Noodle Case 18 X 34 GM"
        },
        {
          "name": "原箱公仔 點心麵－海鮮18 X 34 GM",
          "price": "$62",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231221/0a0c6842-a4ae-3016-8f9f-b6c0eb2485db",
          "product_eng_name": "(無法擷取英文名稱)"
        }
      ],
      "name": "原箱公仔 點心麵－海鮮18 X 34 GM",
      "price": "$62",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20231221/0a0c6842-a4ae-3016-8f9f-b6c0eb2485db",
      "product_eng_name": "(無法擷取英文名稱)"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%A6%8F%E5%AD%97%E4%B8%8A%E6%B9%AF%E4%BC%8A%E9%BA%B5%205%20X%2090GM/i/101350757.html",
      "uid": "8004e93f7692116745dd595e4046c486",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "福字上湯伊麵 5 X 90GM",
          "price": "$15",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250320/b85552e2-43af-3ed2-b521-c1fa8aa3ada8",
          "product_eng_name": "Fuku Instant Noodle 5 X 90GM"
        },
        {
          "name": "福字上湯伊麵 5 X 90GM",
          "price": "$15",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250320/b85552e2-43af-3ed2-b521-c1fa8aa3ada8",
          "product_eng_name": "Fuku Instant Noodle 5 X 90GM"
        }
      ],
      "name": "福字上湯伊麵 5 X 90GM",
      "price": "$15",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250320/b85552e2-43af-3ed2-b521-c1fa8aa3ada8",
      "product_eng_name": "Fuku Instant Noodle 5 X 90GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%99%BE%E5%BE%97%E9%98%BF%E5%A7%A8%E8%9E%BA%E7%B5%B2%E7%B2%89%20500GM/i/101326067.html",
      "uid": "af9a4829851858e9e670c65086b099aa",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "百得阿姨螺絲粉 500GM",
          "price": "$22",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210222/13f3bbf2-6d51-412e-b04b-7aa5eed753b2",
          "product_eng_name": "Barilla Fusilli 500GM"
        },
        {
          "name": "百得阿姨螺絲粉 500GM",
          "price": "$22",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210222/13f3bbf2-6d51-412e-b04b-7aa5eed753b2",
          "product_eng_name": "Barilla Fusilli 500GM"
        }
      ],
      "name": "百得阿姨螺絲粉 500GM",
      "price": "$22",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210222/13f3bbf2-6d51-412e-b04b-7aa5eed753b2",
      "product_eng_name": "Barilla Fusilli 500GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E5%BE%A1%E5%93%81%E7%9A%87%20%E9%BB%91%E8%83%A1%E6%A4%92%E6%8B%8C%E9%BA%B5%20104%20GM/i/113612016.html",
      "uid": "dc87e93b26095f1b93ecfbbd70ba5bc9",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱御品皇 黑胡椒拌麵 104 GM",
          "price": "$120",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230926/66d3d2d6-9a2b-32da-8702-13aa3008f20f",
          "product_eng_name": "Yu Pin King Black Pepper Dry-Stirred Noodles Case 30 x 104GM"
        },
        {
          "name": "原箱御品皇 黑胡椒拌麵 104 GM",
          "price": "$120",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230926/66d3d2d6-9a2b-32da-8702-13aa3008f20f",
          "product_eng_name": "Yu Pin King Black Pepper Dry-Stirred Noodles Case 30 x 104GM"
        }
      ],
      "name": "原箱御品皇 黑胡椒拌麵 104 GM",
      "price": "$120",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230926/66d3d2d6-9a2b-32da-8702-13aa3008f20f",
      "product_eng_name": "Yu Pin King Black Pepper Dry-Stirred Noodles Case 30 x 104GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/Pureland%20%E6%9C%89%E6%A9%9F%E6%B3%B0%E5%9C%8B%E7%99%BC%E8%8A%BD%E7%B3%99%E7%B1%B3%201KG/i/113316793.html",
      "uid": "fb3b6f9248e690d62c837479daaad783",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "Pureland 有機泰國發芽糙米 1KG",
          "price": "$63",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230330/a08cc369-f6c7-446f-8af0-354c53dce6bf",
          "product_eng_name": "Pureland Organic Germinated Bwn 1KG"
        }
      ],
      "name": "Pureland 有機泰國發芽糙米 1KG",
      "price": "$63",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230330/a08cc369-f6c7-446f-8af0-354c53dce6bf",
      "product_eng_name": "Pureland Organic Germinated Bwn 1KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%91%B3%E5%91%B3%E4%B8%80%E5%93%81%E7%8F%8D%E5%91%B3%E7%89%9B%E8%82%89%E5%A4%A7%E7%A2%97%E9%BA%B5%20185GM/i/101346617.html",
      "uid": "89d0b1c8478906191764a3dfc8044bfb",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "味味一品珍味牛肉大碗麵 185GM",
          "price": "$21",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210125/4d7d94b4-0d0b-47f7-a8af-9550017f54c6",
          "product_eng_name": "Weiwei Premium Premium Beef Bowl Noodle 185GM"
        },
        {
          "name": "味味一品珍味牛肉大碗麵 185GM",
          "price": "$21",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210125/4d7d94b4-0d0b-47f7-a8af-9550017f54c6",
          "product_eng_name": "Weiwei Premium Premium Beef Bowl Noodle 185GM"
        }
      ],
      "name": "味味一品珍味牛肉大碗麵 185GM",
      "price": "$21",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210125/4d7d94b4-0d0b-47f7-a8af-9550017f54c6",
      "product_eng_name": "Weiwei Premium Premium Beef Bowl Noodle 185GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%97%A5%E6%B8%85%E5%87%BA%E5%89%8D%E4%B8%80%E4%B8%81%E6%9F%9A%E5%AD%90%E8%83%A1%E6%A4%92%E8%B1%AC%E9%AA%A8%E6%B9%AF%E9%BA%B5%2098GM/i/101573957.html",
      "uid": "1d48ea288a60a00e7e915ac880d2bd95",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "日清出前一丁柚子胡椒豬骨湯麵 98GM",
          "price": "$5",
          "offer": "【8件$28.5】$28.5任揀8件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250407/4f9ae038-f723-3d72-80a1-17b72e5318fc",
          "product_eng_name": "Nissin Demae Iccho Yuzu Pepper Tonkotsu 98GM"
        },
        {
          "name": "日清出前一丁柚子胡椒豬骨湯麵 98GM",
          "price": "$5",
          "offer": "【8件$28.5】$28.5任揀8件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250407/4f9ae038-f723-3d72-80a1-17b72e5318fc",
          "product_eng_name": "Nissin Demae Iccho Yuzu Pepper Tonkotsu 98GM"
        }
      ],
      "name": "日清出前一丁柚子胡椒豬骨湯麵 98GM",
      "price": "$5",
      "offer": "【8件$28.5】$28.5任揀8件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250407/4f9ae038-f723-3d72-80a1-17b72e5318fc",
      "product_eng_name": "Nissin Demae Iccho Yuzu Pepper Tonkotsu 98GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%97%A5%E6%9C%AC%E8%95%8E%E9%BA%A5%E9%BA%B5%20600GM/i/101359746.html",
      "uid": "b4e600231b1cde1f5010cb259b601b52",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "日本蕎麥麵 600GM",
          "price": "$15",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240916/cbb2b22c-b767-3b01-bca5-60e589538961",
          "product_eng_name": "Yoshiya Hyande Soba Noodles 600GM"
        },
        {
          "name": "日本蕎麥麵 600GM",
          "price": "$15",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240916/cbb2b22c-b767-3b01-bca5-60e589538961",
          "product_eng_name": "Yoshiya Hyande Soba Noodles 600GM"
        }
      ],
      "name": "日本蕎麥麵 600GM",
      "price": "$15",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240916/cbb2b22c-b767-3b01-bca5-60e589538961",
      "product_eng_name": "Yoshiya Hyande Soba Noodles 600GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E5%87%BA%E5%89%8D%E4%B8%80%E4%B8%81%20%E9%BA%BB%E6%B2%B9%E6%9D%AF%E9%BA%B5%2070%20GM/i/113559489.html",
      "uid": "006dc421739d395d435d9cf75cc704ce",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱出前一丁 麻油杯麵 70 GM",
          "price": "$170",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231013/73976b82-0abb-3aa0-bfff-98b068d864a3",
          "product_eng_name": "Nissin Demae Iccho Sesame Oil Cup Noodle Case 24 x 70GM"
        },
        {
          "name": "原箱出前一丁 麻油杯麵 70 GM",
          "price": "$170",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231013/73976b82-0abb-3aa0-bfff-98b068d864a3",
          "product_eng_name": "(無法擷取英文名稱)"
        }
      ],
      "name": "原箱出前一丁 麻油杯麵 70 GM",
      "price": "$170",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20231013/73976b82-0abb-3aa0-bfff-98b068d864a3",
      "product_eng_name": "(無法擷取英文名稱)"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E4%B9%9D%E9%AC%BC%E7%B4%94%E6%AD%A3%E8%83%A1%E9%BA%BB%E6%B2%B9%E6%BF%83%E5%8F%A3%20170GM/i/101356339.html",
      "uid": "1dc8b767402bf3cf025a3961af751758",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "九鬼純正胡麻油濃口 170GM",
          "price": "$39",
          "offer": "【2件$49.9】$49.9任揀2件；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20200716/09b80c27-9dfc-4192-9cc6-306604bd3442",
          "product_eng_name": "Kuki Rich Sesame Oil 170GM"
        },
        {
          "name": "九鬼純正胡麻油濃口 170GM",
          "price": "$39",
          "offer": "【2件$49.9】$49.9任揀2件；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20200716/09b80c27-9dfc-4192-9cc6-306604bd3442",
          "product_eng_name": "Kuki Rich Sesame Oil 170GM"
        }
      ],
      "name": "九鬼純正胡麻油濃口 170GM",
      "price": "$39",
      "offer": "【2件$49.9】$49.9任揀2件；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20200716/09b80c27-9dfc-4192-9cc6-306604bd3442",
      "product_eng_name": "Kuki Rich Sesame Oil 170GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/Costa%20d'Oro%E6%84%8F%E5%A4%A7%E5%88%A9%E6%A9%84%E6%AC%96%E6%B2%B9%201LT/i/101381334.html",
      "uid": "edf78c00da9c0dc1820c30aac34db96e",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "Costa d'Oro意大利橄欖油 1LT",
          "price": "$160",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210513/0c93a58b-1ca1-4734-b9f2-30ae35f77481",
          "product_eng_name": "Costa d'Oro Classico Olive Oil 1LT"
        },
        {
          "name": "Costa d'Oro意大利橄欖油 1LT",
          "price": "$160",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210513/0c93a58b-1ca1-4734-b9f2-30ae35f77481",
          "product_eng_name": "Costa d'Oro Classico Olive Oil 1LT"
        }
      ],
      "name": "Costa d'Oro意大利橄欖油 1LT",
      "price": "$160",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210513/0c93a58b-1ca1-4734-b9f2-30ae35f77481",
      "product_eng_name": "Costa d'Oro Classico Olive Oil 1LT"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%88%80%E5%98%9C%20%E9%87%91%E8%A3%9D%E5%81%A5%E5%BA%B7%E8%8A%B1%E7%94%9F%E9%A3%9F%E6%B2%B95%E5%8D%87%205%20LT/i/101342785.html",
      "uid": "029696b89b774213687e01abc4a31711",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "刀嘜 金裝健康花生食油5升 5 LT",
          "price": "$145",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231219/ea7e2df0-ebc4-3262-b009-979bc44457a4",
          "product_eng_name": "Knife Supreme Healthy Peanut Blended Oil 5LT"
        },
        {
          "name": "刀嘜 金裝健康花生食油5升 5 LT",
          "price": "$145",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231219/ea7e2df0-ebc4-3262-b009-979bc44457a4",
          "product_eng_name": "Knife Supreme Healthy Peanut Blended Oil 5LT"
        }
      ],
      "name": "刀嘜 金裝健康花生食油5升 5 LT",
      "price": "$145",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20231219/ea7e2df0-ebc4-3262-b009-979bc44457a4",
      "product_eng_name": "Knife Supreme Healthy Peanut Blended Oil 5LT"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E9%BA%B5%E4%B8%80%E5%BA%B5-%E7%B4%A0%E9%BA%B5%20800GM/i/113339708.html",
      "uid": "7290de3ce29dd1352c6b820781f63de4",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "麵一庵-素麵 800GM",
          "price": "$27",
          "offer": "【2件$50】$50任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230502/f5f99062-5e00-4d39-9aa0-4a68e9fa92de",
          "product_eng_name": "Inosuke Seimen Inosuke Seimen Japan 800GM"
        },
        {
          "name": "麵一庵-素麵 800GM",
          "price": "$27",
          "offer": "【2件$50】$50任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230502/f5f99062-5e00-4d39-9aa0-4a68e9fa92de",
          "product_eng_name": "Inosuke Seimen Inosuke Seimen Japan 800GM"
        }
      ],
      "name": "麵一庵-素麵 800GM",
      "price": "$27",
      "offer": "【2件$50】$50任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230502/f5f99062-5e00-4d39-9aa0-4a68e9fa92de",
      "product_eng_name": "Inosuke Seimen Inosuke Seimen Japan 800GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E8%B6%85%E5%8A%9B%E6%97%A5%E5%BC%8F%E7%83%8F%E5%86%AC%204%20X%20200GM/i/101330389.html",
      "uid": "12e543b9053bab204cbaf98c375769de",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "超力日式烏冬 4 X 200GM",
          "price": "$20",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210429/4bd3c260-dbe5-463b-b775-e83cafe63e91",
          "product_eng_name": "Chewy Japanese Udon 4 X 200GM"
        },
        {
          "name": "超力日式烏冬 4 X 200GM",
          "price": "$20",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210429/4bd3c260-dbe5-463b-b775-e83cafe63e91",
          "product_eng_name": "Chewy Japanese Udon 4 X 200GM"
        }
      ],
      "name": "超力日式烏冬 4 X 200GM",
      "price": "$20",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210429/4bd3c260-dbe5-463b-b775-e83cafe63e91",
      "product_eng_name": "Chewy Japanese Udon 4 X 200GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%B9%B3%E5%95%86%E5%BA%97%E5%8C%97%E6%B5%B7%E9%81%93%E7%B1%B3%202KG/i/101379998.html",
      "uid": "e8feed7ed6794166d353b693de1fcdb8",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "平商店北海道米 2KG",
          "price": "$108",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210126/a45b2e0f-73e9-41a9-b920-dece9572d694",
          "product_eng_name": "Taira Shouten Hokkaido Rice 2KG"
        }
      ],
      "name": "平商店北海道米 2KG",
      "price": "$108",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210126/a45b2e0f-73e9-41a9-b920-dece9572d694",
      "product_eng_name": "Taira Shouten Hokkaido Rice 2KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E9%87%91%E8%B1%A1%E7%89%8C%20%E9%A0%82%E4%B8%8A%E8%8B%BF%E8%8E%89%E9%A6%99%E7%B1%B3%201%20KG/i/113383553.html",
      "uid": "8b95ade742bf765528263c13f2694c1c",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "金象牌 頂上苿莉香米 1 KG",
          "price": "$16",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240925/09e423ad-7a33-3a42-8ad7-ca671567111c",
          "product_eng_name": "Golden Elephant Premium Jasmine Rice 1KG"
        }
      ],
      "name": "金象牌 頂上苿莉香米 1 KG",
      "price": "$16",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240925/09e423ad-7a33-3a42-8ad7-ca671567111c",
      "product_eng_name": "Golden Elephant Premium Jasmine Rice 1KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E8%BE%B2%E5%BF%83%20%E8%BE%9B%E8%BE%A3%E8%8A%9D%E5%A3%AB%E7%82%92%E9%BA%B54%E5%8C%85%20136%20GM/i/114270726.html",
      "uid": "4199868f9074bea890a77fed63fa5e77",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "農心 辛辣芝士炒麵4包 136 GM",
          "price": "$32",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240611/b3afd0dd-4feb-35dc-a7c3-2293454c4e15",
          "product_eng_name": "Nong Shim Shin Stir Fried Noodle with Cheese 4 x 136GM"
        },
        {
          "name": "農心 辛辣芝士炒麵4包 136 GM",
          "price": "$32",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240611/b3afd0dd-4feb-35dc-a7c3-2293454c4e15",
          "product_eng_name": "Nong Shim Shin Stir Fried Noodle with Cheese 4 x 136GM"
        }
      ],
      "name": "農心 辛辣芝士炒麵4包 136 GM",
      "price": "$32",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240611/b3afd0dd-4feb-35dc-a7c3-2293454c4e15",
      "product_eng_name": "Nong Shim Shin Stir Fried Noodle with Cheese 4 x 136GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E8%9E%BA%E9%9C%B8%E7%8E%8B%20%E6%9F%B3%E5%B7%9E%E8%9E%BA%E8%9E%84%E7%B2%89%20330%E5%85%8B/i/101335023.html",
      "uid": "7fb0656e9d3ce155221d96f4b976ac93",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "螺霸王 柳州螺螄粉 330克",
          "price": "$13",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250102/d37a2661-71ae-3034-90e3-eae14d269c5c",
          "product_eng_name": "No Wang Snail Rice Noodles 330GM"
        },
        {
          "name": "螺霸王 柳州螺螄粉 330克",
          "price": "$13",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250102/d37a2661-71ae-3034-90e3-eae14d269c5c",
          "product_eng_name": "No Wang Snail Rice Noodles 330GM"
        }
      ],
      "name": "螺霸王 柳州螺螄粉 330克",
      "price": "$13",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250102/d37a2661-71ae-3034-90e3-eae14d269c5c",
      "product_eng_name": "No Wang Snail Rice Noodles 330GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E4%B8%8D%E5%80%92%E7%BF%81%E5%8D%B3%E9%A3%9F%E4%BA%94%E7%A9%80%E9%A3%AF%20210GM/i/101328668.html",
      "uid": "fa596f81581fae96b20c73ad2f980bd8",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "不倒翁即食五穀飯 210GM",
          "price": "$11",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240917/39166fe6-36f1-3e4f-9ce2-aab5511219bf",
          "product_eng_name": "Ottogi Five Grains Rice 210GM"
        }
      ],
      "name": "不倒翁即食五穀飯 210GM",
      "price": "$11",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240917/39166fe6-36f1-3e4f-9ce2-aab5511219bf",
      "product_eng_name": "Ottogi Five Grains Rice 210GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%BE%A1%E5%93%81%E7%9A%87%E5%84%AA%E8%B3%AA%E6%B3%B0%E5%9C%8B%E8%8C%89%E8%8E%89%E9%A6%99%E7%B1%B3%208KG/i/101381361.html",
      "uid": "3174775aaf1dd14032dc2280ddf82679",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "御品皇優質泰國茉莉香米 8KG",
          "price": "$79",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250219/ff24fd49-0245-3eea-bfee-e062b969ae2d",
          "product_eng_name": "Yu Pin King Thai Jasmine Fragrant Rice 8KG"
        }
      ],
      "name": "御品皇優質泰國茉莉香米 8KG",
      "price": "$79",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250219/ff24fd49-0245-3eea-bfee-e062b969ae2d",
      "product_eng_name": "Yu Pin King Thai Jasmine Fragrant Rice 8KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%97%A5%E6%B8%85%E5%90%88%E5%91%B3%E9%81%93%E9%9B%9E%E6%9D%AF%E9%BA%B5%2075GM/i/101331580.html",
      "uid": "e5a7e082cfca5e2aa7690f3b0c25b415",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "日清合味道雞杯麵 75GM",
          "price": "$8",
          "offer": "【2件$14.5】$14.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250327/cb25df7f-c06f-3224-87ae-f9556c5cb083",
          "product_eng_name": "Nissin Chicken Cup Noodle 75GM"
        },
        {
          "name": "日清合味道雞杯麵 75GM",
          "price": "$8",
          "offer": "【2件$14.5】$14.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250327/cb25df7f-c06f-3224-87ae-f9556c5cb083",
          "product_eng_name": "Nissin Chicken Cup Noodle 75GM"
        }
      ],
      "name": "日清合味道雞杯麵 75GM",
      "price": "$8",
      "offer": "【2件$14.5】$14.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250327/cb25df7f-c06f-3224-87ae-f9556c5cb083",
      "product_eng_name": "Nissin Chicken Cup Noodle 75GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E8%BE%B2%E5%BF%83%20%E7%89%B9%E8%BE%A3%E6%9D%AF%E9%BA%B5%2065%20GM/i/113559419.html",
      "uid": "54f8f4e215846abf58475cf21d4df17a",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱農心 特辣杯麵 65 GM",
          "price": "$144",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231013/2cba8946-337a-3f3f-a150-841b9f01d918",
          "product_eng_name": "Nong Shim Shin Cup Noodle Case 24 x 65GM"
        },
        {
          "name": "原箱農心 特辣杯麵 65 GM",
          "price": "$144",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231013/2cba8946-337a-3f3f-a150-841b9f01d918",
          "product_eng_name": "Nong Shim Shin Cup Noodle Case 24 x 65GM"
        }
      ],
      "name": "原箱農心 特辣杯麵 65 GM",
      "price": "$144",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20231013/2cba8946-337a-3f3f-a150-841b9f01d918",
      "product_eng_name": "Nong Shim Shin Cup Noodle Case 24 x 65GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%8D%85%E7%90%83%E5%98%9C%E5%88%9D%E6%90%BE%E6%A9%84%E6%AC%96%E8%91%B5%E8%8A%B1%E7%B1%BD%E6%B2%B9%203LT/i/101329739.html",
      "uid": "ac1970f01a0a3fee6efa1d5508c2387c",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "獅球嘜初搾橄欖葵花籽油 3LT",
          "price": "$132",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20201008/52c4c050-04ea-4973-afd0-a156378b08b7",
          "product_eng_name": "Lion & Globe Extra Virgin Olive & Sunflower Oil 3LT"
        },
        {
          "name": "獅球嘜初搾橄欖葵花籽油 3LT",
          "price": "$132",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20201008/52c4c050-04ea-4973-afd0-a156378b08b7",
          "product_eng_name": "Lion & Globe Extra Virgin Olive & Sunflower Oil 3LT"
        }
      ],
      "name": "獅球嘜初搾橄欖葵花籽油 3LT",
      "price": "$132",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20201008/52c4c050-04ea-4973-afd0-a156378b08b7",
      "product_eng_name": "Lion & Globe Extra Virgin Olive & Sunflower Oil 3LT"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%97%A5%E6%B8%85%E5%87%BA%E5%89%8D%E4%B8%80%E4%B8%81%E9%BB%91%E8%92%9C%E6%B2%B9%E8%B1%AC%E9%AA%A8%E6%B9%AF%E7%A2%97%E9%BA%B5%20105GM/i/101349359.html",
      "uid": "b7e8fc39d332ad06ad5b54dedc2181e6",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "日清出前一丁黑蒜油豬骨湯碗麵 105GM",
          "price": "$10",
          "offer": "【2件$18】$18任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210518/393cbcc9-ca51-477e-8258-cf1c6a58723a",
          "product_eng_name": "Nissin Demae Iccho Black Garlic Tonkotsu Bowl Noodles 105GM"
        },
        {
          "name": "日清出前一丁黑蒜油豬骨湯碗麵 105GM",
          "price": "$10",
          "offer": "【2件$18】$18任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210518/393cbcc9-ca51-477e-8258-cf1c6a58723a",
          "product_eng_name": "Nissin Demae Iccho Black Garlic Tonkotsu Bowl Noodles 105GM"
        }
      ],
      "name": "日清出前一丁黑蒜油豬骨湯碗麵 105GM",
      "price": "$10",
      "offer": "【2件$18】$18任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210518/393cbcc9-ca51-477e-8258-cf1c6a58723a",
      "product_eng_name": "Nissin Demae Iccho Black Garlic Tonkotsu Bowl Noodles 105GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E6%9D%8E%E9%8C%A6%E8%A8%98%E8%94%A5%E6%B2%B9%E6%8B%8C%E9%BA%B512x110GM/i/114211821.html",
      "uid": "9beede77c29c3a25cdb7d198e01ea617",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱李錦記蔥油拌麵12x110GM",
          "price": "$384",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240719/5f6dd092-4f52-3dfe-92dd-b449558be848",
          "product_eng_name": "Lee Kum Kee Shallot Oil Noodle Case 12 x 110GM"
        },
        {
          "name": "原箱李錦記蔥油拌麵12x110GM",
          "price": "$384",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240719/5f6dd092-4f52-3dfe-92dd-b449558be848",
          "product_eng_name": "Lee Kum Kee Shallot Oil Noodle Case 12 x 110GM"
        }
      ],
      "name": "原箱李錦記蔥油拌麵12x110GM",
      "price": "$384",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240719/5f6dd092-4f52-3dfe-92dd-b449558be848",
      "product_eng_name": "Lee Kum Kee Shallot Oil Noodle Case 12 x 110GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E8%B6%85%E5%8A%9B%E9%8A%80%E7%B5%B2%E7%B1%B3%E7%B2%89%E5%9B%9B%E7%89%87%E8%A3%9D%20280GM/i/101327767.html",
      "uid": "bae8efb0fe3f31b2044370edaea6fe66",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "超力銀絲米粉四片裝 280GM",
          "price": "$20",
          "offer": "【2件$21】$21任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210429/85716963-613f-4f06-aaa2-727ba213ea97",
          "product_eng_name": "Chewy Instant Rice Vermicelli 280GM"
        },
        {
          "name": "超力銀絲米粉四片裝 280GM",
          "price": "$20",
          "offer": "【2件$21】$21任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210429/85716963-613f-4f06-aaa2-727ba213ea97",
          "product_eng_name": "Chewy Instant Rice Vermicelli 280GM"
        }
      ],
      "name": "超力銀絲米粉四片裝 280GM",
      "price": "$20",
      "offer": "【2件$21】$21任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210429/85716963-613f-4f06-aaa2-727ba213ea97",
      "product_eng_name": "Chewy Instant Rice Vermicelli 280GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%A3%BD%E6%A1%83%E9%85%B8%E8%BE%A3%E6%B9%AF%E5%91%B3%E5%B0%8F%E6%A9%8B%E7%B1%B3%E7%B7%9A%204%20X%20215GM/i/101343450.html",
      "uid": "5ad7f0af1f3506466dbce227716103aa",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "壽桃酸辣湯味小橋米線 4 X 215GM",
          "price": "$14",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220505/3eabea5d-281f-44ec-a818-148f89eddc27",
          "product_eng_name": "Sau Tao Hot Sour Rice Verm 4 X 215GM"
        },
        {
          "name": "壽桃酸辣湯味小橋米線 4 X 215GM",
          "price": "$14",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220505/3eabea5d-281f-44ec-a818-148f89eddc27",
          "product_eng_name": "Sau Tao Hot Sour Rice Verm 4 X 215GM"
        }
      ],
      "name": "壽桃酸辣湯味小橋米線 4 X 215GM",
      "price": "$14",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20220505/3eabea5d-281f-44ec-a818-148f89eddc27",
      "product_eng_name": "Sau Tao Hot Sour Rice Verm 4 X 215GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%BE%A1%E5%93%81%E7%9A%87%20%E7%B4%94%E6%AD%A3%E7%B2%9F%E7%B1%B3%E6%B2%B9%205%20LT/i/113510464.html",
      "uid": "9ed2cc610428300e6b4642e9e6ae49bf",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "御品皇 純正粟米油 5 LT",
          "price": "$95",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240704/d5a9da5b-aaf3-3f67-8326-f648ab61dc61",
          "product_eng_name": "Yu Pin King Pure Corn Oil 5LT"
        },
        {
          "name": "御品皇 純正粟米油 5 LT",
          "price": "$95",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240704/d5a9da5b-aaf3-3f67-8326-f648ab61dc61",
          "product_eng_name": "Yu Pin King Pure Corn Oil 5LT"
        }
      ],
      "name": "御品皇 純正粟米油 5 LT",
      "price": "$95",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240704/d5a9da5b-aaf3-3f67-8326-f648ab61dc61",
      "product_eng_name": "Yu Pin King Pure Corn Oil 5LT"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/Macro%20%E6%9C%89%E6%A9%9F%E5%85%A8%E9%BA%A5%E9%95%B7%E9%80%9A%E7%B2%89%20500%E5%85%8B/i/101362679.html",
      "uid": "3d8f9511b99b2f8c772da9dceff2fd34",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "Macro 有機全麥長通粉 500克",
          "price": "$28",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250219/f258a56d-5ba0-3c55-b6af-0ca3ccdd76e7",
          "product_eng_name": "Macro Organic Wholemeal Pasta Penne 500GM"
        },
        {
          "name": "Macro 有機全麥長通粉 500克",
          "price": "$28",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250219/f258a56d-5ba0-3c55-b6af-0ca3ccdd76e7",
          "product_eng_name": "Macro Organic Wholemeal Pasta Penne 500GM"
        }
      ],
      "name": "Macro 有機全麥長通粉 500克",
      "price": "$28",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250219/f258a56d-5ba0-3c55-b6af-0ca3ccdd76e7",
      "product_eng_name": "Macro Organic Wholemeal Pasta Penne 500GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E8%BE%B2%E5%BF%83%E7%89%B9%E8%BE%A3%E9%A6%99%E8%8F%87%E6%8B%89%E9%BA%B5%2030%20X%20120GM/i/101342375.html",
      "uid": "b9dc42bb8c7b04085374f1a092e68d5a",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱農心特辣香菇拉麵 30 X 120GM",
          "price": "$135",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230202/ebd13efe-fd37-4b46-a101-e9950f7e180a",
          "product_eng_name": "Nong Shim Shin Ramyun Case 30 X 120GM"
        },
        {
          "name": "原箱農心特辣香菇拉麵 30 X 120GM",
          "price": "$135",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230202/ebd13efe-fd37-4b46-a101-e9950f7e180a",
          "product_eng_name": "Nong Shim Shin Ramyun Case 30 X 120GM"
        }
      ],
      "name": "原箱農心特辣香菇拉麵 30 X 120GM",
      "price": "$135",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230202/ebd13efe-fd37-4b46-a101-e9950f7e180a",
      "product_eng_name": "Nong Shim Shin Ramyun Case 30 X 120GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%AE%97%E5%AE%B6%E5%BA%9C%E5%B9%B4%E7%B3%95%E6%A2%9D%201KG/i/101339667.html",
      "uid": "935d80367b7db77f30f2b435028506d5",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "宗家府年糕條 1KG",
          "price": "$42",
          "offer": "【2件$49.9】$49.9任揀2件；數量有限，售完即止; 【指定分類享$25換購】每買1件，即可以$25換購1件人氣產品；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20221014/c65d37b0-5857-4546-85cd-159c13dce950",
          "product_eng_name": "Jongga Rice Cake-Tubular 1KG"
        }
      ],
      "name": "宗家府年糕條 1KG",
      "price": "$42",
      "offer": "【2件$49.9】$49.9任揀2件；數量有限，售完即止; 【指定分類享$25換購】每買1件，即可以$25換購1件人氣產品；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20221014/c65d37b0-5857-4546-85cd-159c13dce950",
      "product_eng_name": "Jongga Rice Cake-Tubular 1KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%BE%A1%E5%93%81%E7%9A%87%20%E8%92%9C%E9%A6%99%E8%8A%B1%E7%94%B2%E5%91%B3%E6%B9%AF%E9%BA%B5%20101%20GM/i/113463999.html",
      "uid": "a63c14bf35f2e1ee9f5bc1c65acb21ba",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "御品皇 蒜香花甲味湯麵 101 GM",
          "price": "$4",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240925/7debeb52-14a9-3834-aaed-cfdeb1a0c7dc",
          "product_eng_name": "Yu Pin King Garlic Clam Flavour Soup Noodles 101GM"
        },
        {
          "name": "御品皇 蒜香花甲味湯麵 101 GM",
          "price": "$4",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240925/7debeb52-14a9-3834-aaed-cfdeb1a0c7dc",
          "product_eng_name": "(無法擷取英文名稱)"
        }
      ],
      "name": "御品皇 蒜香花甲味湯麵 101 GM",
      "price": "$4",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240925/7debeb52-14a9-3834-aaed-cfdeb1a0c7dc",
      "product_eng_name": "(無法擷取英文名稱)"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E4%BA%94%E8%B1%90%E7%89%8C%E7%8F%8D%E7%8F%A0%E7%B1%B3%205KGM/i/101342416.html",
      "uid": "2bc655756ff1c61c1693fab17f0fee8b",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "五豐牌珍珠米 5KGM",
          "price": "$56",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250307/6d2cb924-8cf0-3f70-8d78-314ddc52a640",
          "product_eng_name": "Ng Fung Pearl Rice 5KG"
        }
      ],
      "name": "五豐牌珍珠米 5KGM",
      "price": "$56",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250307/6d2cb924-8cf0-3f70-8d78-314ddc52a640",
      "product_eng_name": "Ng Fung Pearl Rice 5KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E9%87%91%E6%BB%BF%E5%A0%82%20%E9%A0%82%E7%B4%9A%E6%9D%B1%E5%8C%97%E5%A4%A7%E7%B1%B3%203%20KG/i/101322723.html",
      "uid": "c9bea8f80d3ce577435da1a07f0ed572",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "金滿堂 頂級東北大米 3 KG",
          "price": "$45",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240606/03be93cf-095d-3ca0-9d38-463db0649a78",
          "product_eng_name": "Golden Hall Premium Short Grain White Rice 3KG"
        }
      ],
      "name": "金滿堂 頂級東北大米 3 KG",
      "price": "$45",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240606/03be93cf-095d-3ca0-9d38-463db0649a78",
      "product_eng_name": "Golden Hall Premium Short Grain White Rice 3KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%97%A5%E6%B8%85%E6%BF%83%E9%A6%99%E9%BA%BB%E6%B2%B9%20130GM/i/102105931.html",
      "uid": "bdc74709701ac6f6a02a3b58006ea75c",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "日清濃香麻油 130GM",
          "price": "$25",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220419/5ca3b6a4-048d-4ec4-8e24-d62005d5cd0a",
          "product_eng_name": "Nissin Sesame Oil 130GM"
        },
        {
          "name": "日清濃香麻油 130GM",
          "price": "$25",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220419/5ca3b6a4-048d-4ec4-8e24-d62005d5cd0a",
          "product_eng_name": "Nissin Sesame Oil 130GM"
        }
      ],
      "name": "日清濃香麻油 130GM",
      "price": "$25",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20220419/5ca3b6a4-048d-4ec4-8e24-d62005d5cd0a",
      "product_eng_name": "Nissin Sesame Oil 130GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E7%B5%B1%E4%B8%80%E6%BB%BF%E6%BC%A2%E5%A4%A7%E9%A4%90%20%E7%B4%85%E7%87%92%E7%89%9B%E8%82%89%E7%A2%97%E9%BA%B5%2012%20X%20187GM/i/113465659.html",
      "uid": "d70b871e5395ec5b422d6437c294a358",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱統一滿漢大餐 紅燒牛肉碗麵 12 X 187GM",
          "price": "$180",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230728/09c7c244-78ba-3310-b7cc-cf33c4e642ce",
          "product_eng_name": "Imperial Big Meal Beef Bowl Noodle Case 12 x 187GM"
        },
        {
          "name": "原箱統一滿漢大餐 紅燒牛肉碗麵 12 X 187GM",
          "price": "$180",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230728/09c7c244-78ba-3310-b7cc-cf33c4e642ce",
          "product_eng_name": "Imperial Big Meal Beef Bowl Noodle Case 12 x 187GM"
        }
      ],
      "name": "原箱統一滿漢大餐 紅燒牛肉碗麵 12 X 187GM",
      "price": "$180",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230728/09c7c244-78ba-3310-b7cc-cf33c4e642ce",
      "product_eng_name": "Imperial Big Meal Beef Bowl Noodle Case 12 x 187GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%99%BE%E5%BE%97%E9%98%BF%E5%A7%A8%E9%80%9A%E5%BF%83%E7%B2%89%20500GM/i/101326070.html",
      "uid": "01492bd38c0f2ce70f4ce2a4d8ae73d5",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "百得阿姨通心粉 500GM",
          "price": "$22",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240916/e9e641cd-02b1-3ec1-a8ff-7175d2d82537",
          "product_eng_name": "Barilla Chifferi N°41 500GM"
        },
        {
          "name": "百得阿姨通心粉 500GM",
          "price": "$22",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240916/e9e641cd-02b1-3ec1-a8ff-7175d2d82537",
          "product_eng_name": "Barilla Chifferi N°41 500GM"
        }
      ],
      "name": "百得阿姨通心粉 500GM",
      "price": "$22",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240916/e9e641cd-02b1-3ec1-a8ff-7175d2d82537",
      "product_eng_name": "Barilla Chifferi N°41 500GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E8%BE%B2%E5%BF%83%E8%BE%A3%E7%99%BD%E8%8F%9C%E5%A4%A7%E7%A2%97%E9%BA%B5%20117GM/i/101327819.html",
      "uid": "5699354fc6b4a3bb9b4db1a56ec54073",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "農心辣白菜大碗麵 117GM",
          "price": "$9",
          "offer": "【2件$12】$12任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210520/1749b2dc-c88b-4802-a6ad-49d7411bfd8b",
          "product_eng_name": "Nong Shim Kimchi Bowl Noodle 117GM"
        },
        {
          "name": "農心辣白菜大碗麵 117GM",
          "price": "$9",
          "offer": "【2件$12】$12任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210520/1749b2dc-c88b-4802-a6ad-49d7411bfd8b",
          "product_eng_name": "Nong Shim Kimchi Bowl Noodle 117GM"
        }
      ],
      "name": "農心辣白菜大碗麵 117GM",
      "price": "$9",
      "offer": "【2件$12】$12任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210520/1749b2dc-c88b-4802-a6ad-49d7411bfd8b",
      "product_eng_name": "Nong Shim Kimchi Bowl Noodle 117GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E8%BE%B2%E5%BF%83%E9%9F%93%E5%9C%8B%E7%89%88%E8%BE%9B%E8%BE%A3%E9%BA%B5%2020X120G%202.4%20KG/i/113735141.html",
      "uid": "8510d492861ea0f481bfb4ac4cc6d382",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "農心韓國版辛辣麵 20X120G 2.4 KG",
          "price": "$88",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240312/1e84bff9-2092-3061-a2aa-396e4dd8f26e",
          "product_eng_name": "Nong Shim Korea Shim Ramyun 20X120G 2.4KG"
        },
        {
          "name": "農心韓國版辛辣麵 20X120G 2.4 KG",
          "price": "$88",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240312/1e84bff9-2092-3061-a2aa-396e4dd8f26e",
          "product_eng_name": "Nong Shim Korea Shim Ramyun 20X120G 2.4KG"
        }
      ],
      "name": "農心韓國版辛辣麵 20X120G 2.4 KG",
      "price": "$88",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240312/1e84bff9-2092-3061-a2aa-396e4dd8f26e",
      "product_eng_name": "Nong Shim Korea Shim Ramyun 20X120G 2.4KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%BE%A1%E5%93%81%E7%9A%87%20%E8%92%9C%E9%A6%99%E9%BA%BB%E9%86%AC%E6%8B%8C%E9%BA%B5%20115GM/i/114331531.html",
      "uid": "835c6e8e2fae04ed377dcc89c5477ade",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "御品皇 蒜香麻醬拌麵 115GM",
          "price": "$4",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20241106/9dacd4f1-571e-38c4-83aa-6e85196f416a",
          "product_eng_name": "Yu Pin King Garlic Sesame Sauce Dry-stirred Noodles 115G"
        },
        {
          "name": "御品皇 蒜香麻醬拌麵 115GM",
          "price": "$4",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20241106/9dacd4f1-571e-38c4-83aa-6e85196f416a",
          "product_eng_name": "Yu Pin King Garlic Sesame Sauce Dry-stirred Noodles 115G"
        }
      ],
      "name": "御品皇 蒜香麻醬拌麵 115GM",
      "price": "$4",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20241106/9dacd4f1-571e-38c4-83aa-6e85196f416a",
      "product_eng_name": "Yu Pin King Garlic Sesame Sauce Dry-stirred Noodles 115G"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/ACE%20%E8%AE%9A%E5%B2%90%E9%A2%A8%E5%91%B3%E7%83%8F%E5%86%AC%20400%20GM/i/101343672.html",
      "uid": "7cca7652ad92eb3afe147df343b57bf8",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "ACE 讚岐風味烏冬 400 GM",
          "price": "$26",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230606/0c069aa1-705e-47f1-8f5d-57bf6b0b8a13",
          "product_eng_name": "ACE Sanuki Style Udon 400GM"
        },
        {
          "name": "ACE 讚岐風味烏冬 400 GM",
          "price": "$26",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230606/0c069aa1-705e-47f1-8f5d-57bf6b0b8a13",
          "product_eng_name": "ACE Sanuki Style Udon 400GM"
        }
      ],
      "name": "ACE 讚岐風味烏冬 400 GM",
      "price": "$26",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230606/0c069aa1-705e-47f1-8f5d-57bf6b0b8a13",
      "product_eng_name": "ACE Sanuki Style Udon 400GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/Meadows%E6%A9%84%E6%AC%96%E6%9E%9C%E6%B8%A3%E6%B2%B9%201LT/i/101837279.html",
      "uid": "2c12992ac4ce84403144cc9db6dd62ee",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "Meadows橄欖果渣油 1LT",
          "price": "$95",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231204/195103db-6cd6-3022-b6bf-274074a4acec",
          "product_eng_name": "Meadows Pomace Olive Oil 1LT"
        },
        {
          "name": "Meadows橄欖果渣油 1LT",
          "price": "$95",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231204/195103db-6cd6-3022-b6bf-274074a4acec",
          "product_eng_name": "Meadows Pomace Olive Oil 1LT"
        }
      ],
      "name": "Meadows橄欖果渣油 1LT",
      "price": "$95",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20231204/195103db-6cd6-3022-b6bf-274074a4acec",
      "product_eng_name": "Meadows Pomace Olive Oil 1LT"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E9%87%91%E9%BC%8E%20%E6%B3%B0%E5%9C%8B%E9%A0%82%E7%B4%9A%E8%8C%89%E8%8E%89%E9%A6%99%E7%B1%B3%208KG/i/101342413.html",
      "uid": "627a4c474ed624e5632d8f1d51ffd56f",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "金鼎 泰國頂級茉莉香米 8KG",
          "price": "$125",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250319/94b02989-2e28-3e37-9b73-62d44064e491",
          "product_eng_name": "Golden Tripod Thai Hom Mali Rice 8KG"
        }
      ],
      "name": "金鼎 泰國頂級茉莉香米 8KG",
      "price": "$125",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250319/94b02989-2e28-3e37-9b73-62d44064e491",
      "product_eng_name": "Golden Tripod Thai Hom Mali Rice 8KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%A3%BD%E6%A1%83%E7%89%8C%E4%B8%8A%E6%B5%B7%E9%BA%B5%20340GM/i/101334860.html",
      "uid": "d0cbd2feb1bc8e464080feef788de00f",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "壽桃牌上海麵 340GM",
          "price": "$9",
          "offer": "【2件$11】$11任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220505/57525500-27bb-4434-bace-1c438c86567f",
          "product_eng_name": "Sau Tao Shanghai Noodle 340GM"
        },
        {
          "name": "壽桃牌上海麵 340GM",
          "price": "$9",
          "offer": "【2件$11】$11任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220505/57525500-27bb-4434-bace-1c438c86567f",
          "product_eng_name": "Sau Tao Shanghai Noodle 340GM"
        }
      ],
      "name": "壽桃牌上海麵 340GM",
      "price": "$9",
      "offer": "【2件$11】$11任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20220505/57525500-27bb-4434-bace-1c438c86567f",
      "product_eng_name": "Sau Tao Shanghai Noodle 340GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%97%A5%E6%B8%85%E5%87%BA%E5%89%8D%E4%B8%80%E4%B8%81%E9%BB%91%E8%92%9C%E6%B2%B9%E8%B1%AC%E9%AA%A8%E6%B9%AF%E6%9D%AF%E9%BA%B5%2070GM/i/101336169.html",
      "uid": "a8f85a66ecaf7f81e158b0f15befe66a",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "日清出前一丁黑蒜油豬骨湯杯麵 70GM",
          "price": "$8",
          "offer": "【2件$14.5】$14.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250327/e170378b-82b3-3e2f-9065-3ebf0a7afff1",
          "product_eng_name": "Nissin Demae Iccho Black Garlic Oil Tonkotsu Cup Noodles 70GM"
        },
        {
          "name": "日清出前一丁黑蒜油豬骨湯杯麵 70GM",
          "price": "$8",
          "offer": "【2件$14.5】$14.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250327/e170378b-82b3-3e2f-9065-3ebf0a7afff1",
          "product_eng_name": "Nissin Demae Iccho Black Garlic Oil Tonkotsu Cup Noodles 70GM"
        }
      ],
      "name": "日清出前一丁黑蒜油豬骨湯杯麵 70GM",
      "price": "$8",
      "offer": "【2件$14.5】$14.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250327/e170378b-82b3-3e2f-9065-3ebf0a7afff1",
      "product_eng_name": "Nissin Demae Iccho Black Garlic Oil Tonkotsu Cup Noodles 70GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E6%97%A5%E6%B8%85%E5%90%88%E5%91%B3%E9%81%93%E6%B5%B7%E9%AE%AE%E6%9D%AF%E9%BA%B5%2072GM/i/101340443.html",
      "uid": "28b3dd5cdc2c2a969d1a90b0706527f2",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱日清合味道海鮮杯麵 72GM",
          "price": "$170",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230202/a1ea2f48-c1e7-41b3-99bf-f3d8a02c9c1a",
          "product_eng_name": "Nissin Cup Noodles Seafood Case 72GM"
        },
        {
          "name": "原箱日清合味道海鮮杯麵 72GM",
          "price": "$170",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230202/a1ea2f48-c1e7-41b3-99bf-f3d8a02c9c1a",
          "product_eng_name": "Nissin Cup Noodles Seafood Case 72GM"
        }
      ],
      "name": "原箱日清合味道海鮮杯麵 72GM",
      "price": "$170",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230202/a1ea2f48-c1e7-41b3-99bf-f3d8a02c9c1a",
      "product_eng_name": "Nissin Cup Noodles Seafood Case 72GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%9D%8E%E9%8C%A6%E8%A8%98%E7%B4%94%E7%9F%B3%E7%A3%A8%E8%8A%9D%E9%BA%BB%E6%B2%B9%20207ML/i/101575948.html",
      "uid": "297839c2a2b166642753d25fb01219e3",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "李錦記純石磨芝麻油 207ML",
          "price": "$30",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210524/4d73562b-2ea8-4139-88df-e4c26f65ad56",
          "product_eng_name": "Lee Kum Kee Pure Ground Frag. Sesame Oil 207ML"
        },
        {
          "name": "李錦記純石磨芝麻油 207ML",
          "price": "$30",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210524/4d73562b-2ea8-4139-88df-e4c26f65ad56",
          "product_eng_name": "Lee Kum Kee Pure Ground Frag. Sesame Oil 207ML"
        }
      ],
      "name": "李錦記純石磨芝麻油 207ML",
      "price": "$30",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210524/4d73562b-2ea8-4139-88df-e4c26f65ad56",
      "product_eng_name": "Lee Kum Kee Pure Ground Frag. Sesame Oil 207ML"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E8%BE%B2%E5%BF%83%E7%9F%B3%E9%8D%8B%E6%9D%AF%E9%BA%B5%2070GM/i/101328975.html",
      "uid": "23ed9a0c42a7cb6a0086a5a0e590bc4c",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "農心石鍋杯麵 70GM",
          "price": "$8",
          "offer": "【3件$18】$18任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240916/76779350-6190-399b-90d0-6767a312ba81",
          "product_eng_name": "Nong Shim Claypot Cup Noodles 70GM"
        },
        {
          "name": "農心石鍋杯麵 70GM",
          "price": "$8",
          "offer": "【3件$18】$18任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240916/76779350-6190-399b-90d0-6767a312ba81",
          "product_eng_name": "Nong Shim Claypot Cup Noodles 70GM"
        }
      ],
      "name": "農心石鍋杯麵 70GM",
      "price": "$8",
      "offer": "【3件$18】$18任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240916/76779350-6190-399b-90d0-6767a312ba81",
      "product_eng_name": "Nong Shim Claypot Cup Noodles 70GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%99%BE%E5%BE%97%E9%98%BF%E5%A7%A8%E5%A4%A9%E4%BD%BF%E9%BA%B5%20500GM/i/101326088.html",
      "uid": "1dac5f6323bb224d4f413bfc148cedeb",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "百得阿姨天使麵 500GM",
          "price": "$22",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240916/3a6686c0-21d0-3e00-b7c3-55bf1ca76c08",
          "product_eng_name": "Barilla Angel Hair 500GM"
        },
        {
          "name": "百得阿姨天使麵 500GM",
          "price": "$22",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240916/3a6686c0-21d0-3e00-b7c3-55bf1ca76c08",
          "product_eng_name": "Barilla Angel Hair 500GM"
        }
      ],
      "name": "百得阿姨天使麵 500GM",
      "price": "$22",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240916/3a6686c0-21d0-3e00-b7c3-55bf1ca76c08",
      "product_eng_name": "Barilla Angel Hair 500GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%8D%85%E7%90%83%E5%98%9C%E7%B2%9F%E7%B1%B3%E6%B2%B9%E5%84%AA%E6%83%A0%E8%A3%9D%204%20X%20900ML/i/101358989.html",
      "uid": "33c34e2ef5734a46ee63dca0067e4443",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "獅球嘜粟米油優惠裝 4 X 900ML",
          "price": "$107",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230109/b71ca8c5-ff78-49e2-979f-6541656ba6d3",
          "product_eng_name": "Lion & Globe Pure Corn Oil 4x900ML"
        },
        {
          "name": "獅球嘜粟米油優惠裝 4 X 900ML",
          "price": "$107",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230109/b71ca8c5-ff78-49e2-979f-6541656ba6d3",
          "product_eng_name": "Lion & Globe Pure Corn Oil 4x900ML"
        }
      ],
      "name": "獅球嘜粟米油優惠裝 4 X 900ML",
      "price": "$107",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230109/b71ca8c5-ff78-49e2-979f-6541656ba6d3",
      "product_eng_name": "Lion & Globe Pure Corn Oil 4x900ML"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/De%20Cecco%20A-Z%E5%AD%97%E6%AF%8D%E7%B2%89%20N173%20500GM/i/101372231.html",
      "uid": "5102ba17147b01767c6b2555771a14fe",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "De Cecco A-Z字母粉 N173 500GM",
          "price": "$29",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240917/7e13cb88-0980-393b-be25-006a58731c79",
          "product_eng_name": "(無法擷取英文名稱)"
        },
        {
          "name": "De Cecco A-Z字母粉 N173 500GM",
          "price": "$29",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240917/7e13cb88-0980-393b-be25-006a58731c79",
          "product_eng_name": "De Cecco Alfabeto N173 500GM"
        }
      ],
      "name": "De Cecco A-Z字母粉 N173 500GM",
      "price": "$29",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240917/7e13cb88-0980-393b-be25-006a58731c79",
      "product_eng_name": "De Cecco Alfabeto N173 500GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/ACE%E6%97%A5%E6%9C%AC%E8%AE%9A%E5%B2%90%E7%83%8F%E5%86%AC%20%204%20X%20200GM/i/101336106.html",
      "uid": "1a2b2aa9d39caf161a740f599e8679d9",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "ACE日本讚岐烏冬 4 X 200GM",
          "price": "$20",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210126/6573f23b-4ae9-47b3-80a9-c693bf0abc50",
          "product_eng_name": "ACE Sanuki Udon 4 x 200GM"
        },
        {
          "name": "ACE日本讚岐烏冬 4 X 200GM",
          "price": "$20",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210126/6573f23b-4ae9-47b3-80a9-c693bf0abc50",
          "product_eng_name": "ACE Sanuki Udon 4 x 200GM"
        }
      ],
      "name": "ACE日本讚岐烏冬 4 X 200GM",
      "price": "$20",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210126/6573f23b-4ae9-47b3-80a9-c693bf0abc50",
      "product_eng_name": "ACE Sanuki Udon 4 x 200GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E8%90%AC%E6%AD%B2%20%E7%B2%9F%E7%B1%B3%E6%B2%B9%203%20X%20900ML/i/113488329.html",
      "uid": "6f90810e6478962a8d6a61ad0137f021",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "萬歲 粟米油 3 X 900ML",
          "price": "$80",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240729/d6772c06-325c-3993-b301-fe2771473fe4",
          "product_eng_name": "Mazola Corn Oil 3 X 900ML"
        },
        {
          "name": "萬歲 粟米油 3 X 900ML",
          "price": "$80",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240729/d6772c06-325c-3993-b301-fe2771473fe4",
          "product_eng_name": "Mazola Corn Oil 3 X 900ML"
        }
      ],
      "name": "萬歲 粟米油 3 X 900ML",
      "price": "$80",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240729/d6772c06-325c-3993-b301-fe2771473fe4",
      "product_eng_name": "Mazola Corn Oil 3 X 900ML"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%85%AC%E4%BB%94%E5%8E%9F%E5%91%B3%E7%B1%B3%E7%B2%89%2070GM/i/101322589.html",
      "uid": "ce6073f76831bd7baa14a3beab21bc43",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "公仔原味米粉 70GM",
          "price": "$4",
          "offer": "【3件$9】$9任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20241029/83b8a93e-dcfd-323e-8961-52d1fcae5327",
          "product_eng_name": "Doll Instant Mei Fun 70GM"
        },
        {
          "name": "公仔原味米粉 70GM",
          "price": "$4",
          "offer": "【3件$9】$9任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20241029/83b8a93e-dcfd-323e-8961-52d1fcae5327",
          "product_eng_name": "Doll Instant Mei Fun 70GM"
        }
      ],
      "name": "公仔原味米粉 70GM",
      "price": "$4",
      "offer": "【3件$9】$9任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20241029/83b8a93e-dcfd-323e-8961-52d1fcae5327",
      "product_eng_name": "Doll Instant Mei Fun 70GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E5%85%AC%E4%BB%94%20%E9%9B%AA%E8%8F%9C%E8%82%89%E7%B5%B2%E7%A2%97%E7%B1%B3%2012%20X%2077GM/i/113465674.html",
      "uid": "4316dcb419cb733ec9143d8548dfacc9",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱公仔 雪菜肉絲碗米 12 X 77GM",
          "price": "$50",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250320/f64bd06b-7950-32b7-acc5-cf011ef00837",
          "product_eng_name": "Doll Vegetabel & Pork Mifun Case 12 X 77GM"
        },
        {
          "name": "原箱公仔 雪菜肉絲碗米 12 X 77GM",
          "price": "$50",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250320/f64bd06b-7950-32b7-acc5-cf011ef00837",
          "product_eng_name": "Doll Vegetabel & Pork Mifun Case 12 X 77GM"
        }
      ],
      "name": "原箱公仔 雪菜肉絲碗米 12 X 77GM",
      "price": "$50",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250320/f64bd06b-7950-32b7-acc5-cf011ef00837",
      "product_eng_name": "Doll Vegetabel & Pork Mifun Case 12 X 77GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%BE%A1%E5%93%81%E7%9A%87%20%E7%B4%85%E7%87%92%E7%89%9B%E8%82%89%E5%91%B3%E6%B9%AF%E9%BA%B5%2098%20GM/i/113463984.html",
      "uid": "a4c466bb577efd6b5a16f3bff4f559fc",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "御品皇 紅燒牛肉味湯麵 98 GM",
          "price": "$4",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240925/3c297a84-89ee-348b-aee4-f066d192e810",
          "product_eng_name": "Yu Pin King Braised Beef Flavour Soup Noodles 98GM"
        },
        {
          "name": "御品皇 紅燒牛肉味湯麵 98 GM",
          "price": "$4",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240925/3c297a84-89ee-348b-aee4-f066d192e810",
          "product_eng_name": "Yu Pin King Braised Beef Flavour Soup Noodles 98GM"
        }
      ],
      "name": "御品皇 紅燒牛肉味湯麵 98 GM",
      "price": "$4",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240925/3c297a84-89ee-348b-aee4-f066d192e810",
      "product_eng_name": "Yu Pin King Braised Beef Flavour Soup Noodles 98GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E8%B6%85%E5%8A%9B%E9%86%AC%E7%88%86%E6%9D%AF%E7%B1%B3%E7%B2%89%E9%85%B8%E8%8F%9C%2012%20X%20102GM/i/113267699.html",
      "uid": "da7adb44713096a65903584e31d5af53",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱超力醬爆杯米粉酸菜 12 X 102GM",
          "price": "$81",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20221125/60df0a2e-b384-4cb4-90a0-2f38d31744c5",
          "product_eng_name": "Chewy Pickled Vermicelli Cup Case 12 X 102GM"
        },
        {
          "name": "原箱超力醬爆杯米粉酸菜 12 X 102GM",
          "price": "$81",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20221125/60df0a2e-b384-4cb4-90a0-2f38d31744c5",
          "product_eng_name": "Chewy Pickled Vermicelli Cup Case 12 X 102GM"
        }
      ],
      "name": "原箱超力醬爆杯米粉酸菜 12 X 102GM",
      "price": "$81",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20221125/60df0a2e-b384-4cb4-90a0-2f38d31744c5",
      "product_eng_name": "Chewy Pickled Vermicelli Cup Case 12 X 102GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E6%8B%89%E9%BA%B5%E8%AA%AA%E8%B1%9A%E9%AA%A8%E5%8F%89%E7%87%92%E6%8B%89%E9%BA%B5%2012%20X%20141.4GM/i/101340629.html",
      "uid": "fc1dbdd72bf72e1f6a39ce17981f60f9",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱拉麵說豚骨叉燒拉麵 12 X 141.4GM",
          "price": "$288",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231229/572b16dd-61ee-37b4-8646-001ba42468d7",
          "product_eng_name": "Ramen Talk BBQ Pork Noodles Case 12 x 141.4GM"
        },
        {
          "name": "原箱拉麵說豚骨叉燒拉麵 12 X 141.4GM",
          "price": "$288",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231229/572b16dd-61ee-37b4-8646-001ba42468d7",
          "product_eng_name": "Ramen Talk BBQ Pork Noodles Case 12 x 141.4GM"
        }
      ],
      "name": "原箱拉麵說豚骨叉燒拉麵 12 X 141.4GM",
      "price": "$288",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20231229/572b16dd-61ee-37b4-8646-001ba42468d7",
      "product_eng_name": "Ramen Talk BBQ Pork Noodles Case 12 x 141.4GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%A5%A7%E5%88%A9%E7%89%8C%20%E7%B4%94%E6%AD%A3%E6%A9%84%E6%AC%96%E6%B2%B9%201%20LT/i/113734411.html",
      "uid": "c8ce24579ac6854da61dce283a118caf",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "奧利牌 純正橄欖油 1 LT",
          "price": "$154",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240306/de60df78-fa19-3445-b6d3-d034da15492c",
          "product_eng_name": "Olitalia 100% Pure Olive Oil 1LT"
        },
        {
          "name": "奧利牌 純正橄欖油 1 LT",
          "price": "$154",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240306/de60df78-fa19-3445-b6d3-d034da15492c",
          "product_eng_name": "Olitalia 100% Pure Olive Oil 1LT"
        }
      ],
      "name": "奧利牌 純正橄欖油 1 LT",
      "price": "$154",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240306/de60df78-fa19-3445-b6d3-d034da15492c",
      "product_eng_name": "Olitalia 100% Pure Olive Oil 1LT"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%99%BE%E7%9B%8A%E7%B4%94%E6%A9%84%E6%AC%96%E6%B2%B9%201LT/i/113318813.html",
      "uid": "f8987e2dae63ae70b2450c77a171f1b3",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "百益純橄欖油 1LT",
          "price": "$169",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240425/6d14a780-dacf-32a3-9c45-4a7bd8bcda31",
          "product_eng_name": "Filippo Berio Pure Olive Oil 1LT"
        },
        {
          "name": "百益純橄欖油 1LT",
          "price": "$169",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240425/6d14a780-dacf-32a3-9c45-4a7bd8bcda31",
          "product_eng_name": "Filippo Berio Pure Olive Oil 1LT"
        }
      ],
      "name": "百益純橄欖油 1LT",
      "price": "$169",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240425/6d14a780-dacf-32a3-9c45-4a7bd8bcda31",
      "product_eng_name": "Filippo Berio Pure Olive Oil 1LT"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%97%A5%E6%B8%85%E5%90%88%E5%91%B3%E9%81%93%E5%8F%BB%E6%B2%99%E5%91%B3%E6%9D%AF%E9%BA%B5%2075GM/i/101355267.html",
      "uid": "7a48c91079a4d67531fb198253e31236",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "日清合味道叻沙味杯麵 75GM",
          "price": "$8",
          "offer": "【2件$14.5】$14.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250327/d56abfc1-2a1d-3407-b9d5-62ca3bcf027e",
          "product_eng_name": "Nissin Laksa Flavour Cup Noodles 75GM"
        },
        {
          "name": "日清合味道叻沙味杯麵 75GM",
          "price": "$8",
          "offer": "【2件$14.5】$14.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250327/d56abfc1-2a1d-3407-b9d5-62ca3bcf027e",
          "product_eng_name": "Nissin Laksa Flavour Cup Noodles 75GM"
        }
      ],
      "name": "日清合味道叻沙味杯麵 75GM",
      "price": "$8",
      "offer": "【2件$14.5】$14.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250327/d56abfc1-2a1d-3407-b9d5-62ca3bcf027e",
      "product_eng_name": "Nissin Laksa Flavour Cup Noodles 75GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%91%B3%E5%8D%83%E9%9B%9E%E6%B9%AF%E6%8B%89%E9%BA%B52%E4%BA%BA%E4%BB%BD%20296GM/i/113247884.html",
      "uid": "1d0f8fc7b83154f2d1e4caf7b2c9a1ae",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "味千雞湯拉麵2人份 296GM",
          "price": "$10",
          "offer": "【指定分類享$25換購】每買1件，即可以$25換購1件人氣產品；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240902/1dd475b8-0894-3bb8-b5f3-3f7c7e6a8c2f",
          "product_eng_name": "Ajisen Ramen Chicken Broth Ramens 2 Serving 296GM"
        },
        {
          "name": "味千雞湯拉麵2人份 296GM",
          "price": "$10",
          "offer": "【指定分類享$25換購】每買1件，即可以$25換購1件人氣產品；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240902/1dd475b8-0894-3bb8-b5f3-3f7c7e6a8c2f",
          "product_eng_name": "Ajisen Ramen Chicken Broth Ramens 2 Serving 296GM"
        }
      ],
      "name": "味千雞湯拉麵2人份 296GM",
      "price": "$10",
      "offer": "【指定分類享$25換購】每買1件，即可以$25換購1件人氣產品；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240902/1dd475b8-0894-3bb8-b5f3-3f7c7e6a8c2f",
      "product_eng_name": "Ajisen Ramen Chicken Broth Ramens 2 Serving 296GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E7%84%A1%E9%9B%99%E6%9D%AF%E8%A3%9D%E9%85%B8%E8%8F%9C%E9%AD%9A%E7%B2%89%20%2012%20X%20150GM/i/113267689.html",
      "uid": "b579da48bc0072d4262924d127f35aaa",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱無雙杯裝酸菜魚粉 12 X 150GM",
          "price": "$84",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20221125/f5620235-2a9a-4a88-b43e-75458145b6b5",
          "product_eng_name": "Muso Pickle & Fish Cup Noodle Case 12 X 150GM"
        },
        {
          "name": "原箱無雙杯裝酸菜魚粉 12 X 150GM",
          "price": "$84",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20221125/f5620235-2a9a-4a88-b43e-75458145b6b5",
          "product_eng_name": "Muso Pickle & Fish Cup Noodle Case 12 X 150GM"
        }
      ],
      "name": "原箱無雙杯裝酸菜魚粉 12 X 150GM",
      "price": "$84",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20221125/f5620235-2a9a-4a88-b43e-75458145b6b5",
      "product_eng_name": "Muso Pickle & Fish Cup Noodle Case 12 X 150GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E5%85%AC%E4%BB%94%20%E9%A6%99%E8%BE%A3%E9%86%AC%E7%82%92%E9%BA%B5%E7%8E%8B%2012%20X%20120GM/i/101342374.html",
      "uid": "58da839dcf133c6c84a149537615bda3",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱公仔 香辣醬炒麵王 12 X 120GM",
          "price": "$78",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230209/99fd8304-3129-47cd-a601-9954fe7e8f1f",
          "product_eng_name": "Doll Fried Noodle-Chilli 12 X 120GM"
        },
        {
          "name": "原箱公仔 香辣醬炒麵王 12 X 120GM",
          "price": "$78",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230209/99fd8304-3129-47cd-a601-9954fe7e8f1f",
          "product_eng_name": "Doll Fried Noodle-Chilli 12 X 120GM"
        }
      ],
      "name": "原箱公仔 香辣醬炒麵王 12 X 120GM",
      "price": "$78",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230209/99fd8304-3129-47cd-a601-9954fe7e8f1f",
      "product_eng_name": "Doll Fried Noodle-Chilli 12 X 120GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%A3%BD%E6%A1%83%E9%8A%80%E9%87%9D%E7%B2%89%20200GM/i/101576795.html",
      "uid": "e59ec75f5d66f78bbeea2c49947a201d",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "壽桃銀針粉 200GM",
          "price": "$16",
          "offer": "【2件$20】$20任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220505/58eb66c8-38d4-4f4f-8d0f-828471b50167",
          "product_eng_name": "Sau Tao Silver Pin Noodle 200GM"
        },
        {
          "name": "壽桃銀針粉 200GM",
          "price": "$16",
          "offer": "【2件$20】$20任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220505/58eb66c8-38d4-4f4f-8d0f-828471b50167",
          "product_eng_name": "Sau Tao Silver Pin Noodle 200GM"
        }
      ],
      "name": "壽桃銀針粉 200GM",
      "price": "$16",
      "offer": "【2件$20】$20任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20220505/58eb66c8-38d4-4f4f-8d0f-828471b50167",
      "product_eng_name": "Sau Tao Silver Pin Noodle 200GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E9%87%91%E9%B3%B3%E6%B3%B0%E5%9C%8B%E9%A0%82%E7%B4%9A%E7%B4%85%E7%B1%B3%201.5KGM/i/101381424.html",
      "uid": "d0f2b50b6d7d85e35311ae218fba657b",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "金鳳泰國頂級紅米 1.5KGM",
          "price": "$49",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250307/db72ddb6-7cd0-3214-8777-e9f2f83dd1cb",
          "product_eng_name": "Golden Phoenix Thai Red Cargo Rice 1.5KG"
        }
      ],
      "name": "金鳳泰國頂級紅米 1.5KGM",
      "price": "$49",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250307/db72ddb6-7cd0-3214-8777-e9f2f83dd1cb",
      "product_eng_name": "Golden Phoenix Thai Red Cargo Rice 1.5KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E7%84%A1%E9%9B%99%E9%85%B8%E8%BE%A3%E7%B2%89%E6%9D%AF%E8%A3%9D%2012%20X%20140GM/i/113267684.html",
      "uid": "00047d6698b8868a7d73b182bcda5534",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱無雙酸辣粉杯裝 12 X 140GM",
          "price": "$84",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20221125/f8f0fb27-6907-46c0-9d63-fb96cfd73ec2",
          "product_eng_name": "Muso Sour & Spicy Cup Noodle Case 12 X 140GM"
        },
        {
          "name": "原箱無雙酸辣粉杯裝 12 X 140GM",
          "price": "$84",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20221125/f8f0fb27-6907-46c0-9d63-fb96cfd73ec2",
          "product_eng_name": "Muso Sour & Spicy Cup Noodle Case 12 X 140GM"
        }
      ],
      "name": "原箱無雙酸辣粉杯裝 12 X 140GM",
      "price": "$84",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20221125/f8f0fb27-6907-46c0-9d63-fb96cfd73ec2",
      "product_eng_name": "Muso Sour & Spicy Cup Noodle Case 12 X 140GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/De%20Cecco%E6%84%8F%E5%A4%A7%E5%88%A9%E8%9D%B4%E8%9D%B6%E7%B2%89%20N93%20500GM/i/101322671.html",
      "uid": "7a3638c2c6a272c12d0a82e1ff9925f6",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "De Cecco意大利蝴蝶粉 N93 500GM",
          "price": "$30",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240917/f90ff3c2-cfb6-36c9-b971-99b60c3c63e2",
          "product_eng_name": "De Cecco Farfalle n°93 500GM"
        },
        {
          "name": "De Cecco意大利蝴蝶粉 N93 500GM",
          "price": "$30",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240917/f90ff3c2-cfb6-36c9-b971-99b60c3c63e2",
          "product_eng_name": "De Cecco Farfalle n°93 500GM"
        }
      ],
      "name": "De Cecco意大利蝴蝶粉 N93 500GM",
      "price": "$30",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240917/f90ff3c2-cfb6-36c9-b971-99b60c3c63e2",
      "product_eng_name": "De Cecco Farfalle n°93 500GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%8D%85%E7%90%83%E5%98%9C%E5%88%9D%E6%90%BE%E6%A9%84%E6%AC%96%E8%8A%A5%E8%8A%B1%E7%B1%BD%E6%B2%B9%20600ML/i/101326646.html",
      "uid": "0ae714694eca2e47ecced7b86f8e4491",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "獅球嘜初搾橄欖芥花籽油 600ML",
          "price": "$28",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210126/24c30258-70b5-4675-96d6-c7385fc7d296",
          "product_eng_name": "Lion & Globe Extra Virgin Olive Canola Oil 600ML"
        },
        {
          "name": "獅球嘜初搾橄欖芥花籽油 600ML",
          "price": "$28",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210126/24c30258-70b5-4675-96d6-c7385fc7d296",
          "product_eng_name": "Lion & Globe Extra Virgin Olive Canola Oil 600ML"
        }
      ],
      "name": "獅球嘜初搾橄欖芥花籽油 600ML",
      "price": "$28",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210126/24c30258-70b5-4675-96d6-c7385fc7d296",
      "product_eng_name": "Lion & Globe Extra Virgin Olive Canola Oil 600ML"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/Meadows%E6%89%81%E6%84%8F%E7%B2%89n13%20500GM/i/101579434.html",
      "uid": "9c612367b96dc48173203ba013f97656",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "Meadows扁意粉n13 500GM",
          "price": "$16",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231204/c347b9db-9da0-3821-ab58-1d8aa059659c",
          "product_eng_name": "Meadows Linguine N13 500GM"
        },
        {
          "name": "Meadows扁意粉n13 500GM",
          "price": "$16",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231204/c347b9db-9da0-3821-ab58-1d8aa059659c",
          "product_eng_name": "Meadows Linguine N13 500GM"
        }
      ],
      "name": "Meadows扁意粉n13 500GM",
      "price": "$16",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20231204/c347b9db-9da0-3821-ab58-1d8aa059659c",
      "product_eng_name": "Meadows Linguine N13 500GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%A4%A7%E5%B8%AB%E5%A7%90%20%E9%A0%82%E7%B4%9A%E7%91%A4%E6%9F%B1%E8%9D%A6%E5%AD%90%E9%BA%B5(%E7%B2%97)%206%E5%80%8B%E8%A3%9D/i/101341731.html",
      "uid": "0c2acbe00490c663faf0220e902d8a16",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "大師姐 頂級瑤柱蝦子麵(粗) 6個裝",
          "price": "$98",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250122/ac9ed331-8458-30fb-a71f-c4732a19e1d5",
          "product_eng_name": "Dashijie Dried Scallop & Dried Shrimp Roe Noodles (Thick)"
        },
        {
          "name": "大師姐 頂級瑤柱蝦子麵(粗) 6個裝",
          "price": "$98",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250122/ac9ed331-8458-30fb-a71f-c4732a19e1d5",
          "product_eng_name": "Dashijie Dried Scallop & Dried Shrimp Roe Noodles (Thick)"
        }
      ],
      "name": "大師姐 頂級瑤柱蝦子麵(粗) 6個裝",
      "price": "$98",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250122/ac9ed331-8458-30fb-a71f-c4732a19e1d5",
      "product_eng_name": "Dashijie Dried Scallop & Dried Shrimp Roe Noodles (Thick)"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%B2%A9%E6%89%8B%E7%B8%A3%20%E6%B1%9F%E5%88%BA%E7%B1%B3%202KG/i/101346870.html",
      "uid": "9ff2193167fdc93b58d5c144e6bc9c73",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "岩手縣 江刺米 2KG",
          "price": "$74",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240510/e0e2ea04-0c5c-3980-a6bb-8f7f27f1adcb",
          "product_eng_name": "Iwate Esashi Japanese Rice 2KG"
        }
      ],
      "name": "岩手縣 江刺米 2KG",
      "price": "$74",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240510/e0e2ea04-0c5c-3980-a6bb-8f7f27f1adcb",
      "product_eng_name": "Iwate Esashi Japanese Rice 2KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%8D%85%E7%90%83%E5%98%9C%E7%B2%9F%E7%B1%B3%E6%B2%B9%203LT/i/101326092.html",
      "uid": "27e8a3a29a0160c1472efcacacfd5ef4",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "獅球嘜粟米油 3LT",
          "price": "$95",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230317/17e57ed8-7d9f-4c4f-9003-9d17ef3f697b",
          "product_eng_name": "Lion & Globe Corn Oil 3LT"
        },
        {
          "name": "獅球嘜粟米油 3LT",
          "price": "$95",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230317/17e57ed8-7d9f-4c4f-9003-9d17ef3f697b",
          "product_eng_name": "Lion & Globe Corn Oil 3LT"
        }
      ],
      "name": "獅球嘜粟米油 3LT",
      "price": "$95",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230317/17e57ed8-7d9f-4c4f-9003-9d17ef3f697b",
      "product_eng_name": "Lion & Globe Corn Oil 3LT"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E8%BE%B2%E5%BF%83%20%E7%9F%B3%E9%8D%8B%E6%8B%89%E9%BA%B5%20600%20GM/i/113559454.html",
      "uid": "0eb6ac0dee54e7058006abaf24a81c70",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱農心 石鍋拉麵 600 GM",
          "price": "$158",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231013/1c624aab-380f-3faf-b993-24e10a27ad4a",
          "product_eng_name": "Nong Shim Claypot Ramyun 40 x 120GM"
        },
        {
          "name": "原箱農心 石鍋拉麵 600 GM",
          "price": "$158",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231013/1c624aab-380f-3faf-b993-24e10a27ad4a",
          "product_eng_name": "Nong Shim Claypot Ramyun 40 x 120GM"
        }
      ],
      "name": "原箱農心 石鍋拉麵 600 GM",
      "price": "$158",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20231013/1c624aab-380f-3faf-b993-24e10a27ad4a",
      "product_eng_name": "Nong Shim Claypot Ramyun 40 x 120GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%AA%BD%E5%92%AA%E8%83%A1%E6%A4%92%E6%B9%AF%E9%BA%B5%205%20X%2080GM/i/101339993.html",
      "uid": "550f8cc3da407012823294b8131e89a6",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "媽咪胡椒湯麵 5 X 80GM",
          "price": "$21",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231011/43c1224b-4f0c-31f1-90ba-cd2d9be7e571",
          "product_eng_name": "Mamee Pepper Noodles 5 X 80GM"
        },
        {
          "name": "媽咪胡椒湯麵 5 X 80GM",
          "price": "$21",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231011/43c1224b-4f0c-31f1-90ba-cd2d9be7e571",
          "product_eng_name": "Mamee Pepper Noodles 5 X 80GM"
        }
      ],
      "name": "媽咪胡椒湯麵 5 X 80GM",
      "price": "$21",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20231011/43c1224b-4f0c-31f1-90ba-cd2d9be7e571",
      "product_eng_name": "Mamee Pepper Noodles 5 X 80GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E8%B6%85%E5%8A%9B%20%E9%A6%99%E8%8F%87%E7%87%89%E9%9B%9E%E5%91%B3%E7%A2%97%E7%B1%B3%E7%B2%89%2098%20GM/i/101379666.html",
      "uid": "b73b2829863ef571d46ea6bebd96f1f9",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "超力 香菇燉雞味碗米粉 98 GM",
          "price": "$12",
          "offer": "【2件$14.5】$14.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240823/e5d6dfca-f0f9-3834-b5ea-72cae96b89e7",
          "product_eng_name": "Chewy Chicken and Mushroom Bowl Vermicelli 98GM"
        },
        {
          "name": "超力 香菇燉雞味碗米粉 98 GM",
          "price": "$12",
          "offer": "【2件$14.5】$14.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240823/e5d6dfca-f0f9-3834-b5ea-72cae96b89e7",
          "product_eng_name": "Chewy Chicken and Mushroom Bowl Vermicelli 98GM"
        }
      ],
      "name": "超力 香菇燉雞味碗米粉 98 GM",
      "price": "$12",
      "offer": "【2件$14.5】$14.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240823/e5d6dfca-f0f9-3834-b5ea-72cae96b89e7",
      "product_eng_name": "Chewy Chicken and Mushroom Bowl Vermicelli 98GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%97%A5%E6%B8%85%E5%90%88%E5%91%B3%E9%81%93%E5%91%A8%E6%89%93%E8%98%91%E8%8F%87%E6%B5%B7%E9%AE%AE%E6%9D%AF%E9%BA%B5%2075GM/i/101382612.html",
      "uid": "e959a693251e27c765f5599289133699",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "日清合味道周打蘑菇海鮮杯麵 75GM",
          "price": "$8",
          "offer": "【2件$14.5】$14.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250327/54d4b71d-4739-331a-aa8b-680de8d10f6f",
          "product_eng_name": "Nissin Mushroom Seafood Cup Noodles 75GM"
        },
        {
          "name": "日清合味道周打蘑菇海鮮杯麵 75GM",
          "price": "$8",
          "offer": "【2件$14.5】$14.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250327/54d4b71d-4739-331a-aa8b-680de8d10f6f",
          "product_eng_name": "Nissin Mushroom Seafood Cup Noodles 75GM"
        }
      ],
      "name": "日清合味道周打蘑菇海鮮杯麵 75GM",
      "price": "$8",
      "offer": "【2件$14.5】$14.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250327/54d4b71d-4739-331a-aa8b-680de8d10f6f",
      "product_eng_name": "Nissin Mushroom Seafood Cup Noodles 75GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%A6%8F%E5%AD%97%E4%B8%8A%E6%B9%AF%E7%B1%B3%E7%B2%89%205%20X%2065GM/i/101351322.html",
      "uid": "ca6c9f876b76b655f84d1706d9c9f287",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "福字上湯米粉 5 X 65GM",
          "price": "$15",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250320/c3172bbc-2062-3863-a026-55931ecd1f4b",
          "product_eng_name": "Fuku Instant Rice Noodle 5 X 65GM"
        },
        {
          "name": "福字上湯米粉 5 X 65GM",
          "price": "$15",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250320/c3172bbc-2062-3863-a026-55931ecd1f4b",
          "product_eng_name": "Fuku Instant Rice Noodle 5 X 65GM"
        }
      ],
      "name": "福字上湯米粉 5 X 65GM",
      "price": "$15",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250320/c3172bbc-2062-3863-a026-55931ecd1f4b",
      "product_eng_name": "Fuku Instant Rice Noodle 5 X 65GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%97%A5%E6%B8%85%E5%90%88%E5%91%B3%E9%81%93%E4%BA%94%E9%A6%99%E7%89%9B%E8%82%89%E6%9D%AF%E9%BA%B5%2075GM/i/101339849.html",
      "uid": "29c72513b562b07dffded5474cad0f08",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "日清合味道五香牛肉杯麵 75GM",
          "price": "$8",
          "offer": "【2件$14.5】$14.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250327/a6023674-cd53-3b88-89eb-7ae496f73cdc",
          "product_eng_name": "(無法擷取英文名稱)"
        },
        {
          "name": "日清合味道五香牛肉杯麵 75GM",
          "price": "$8",
          "offer": "【2件$14.5】$14.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250327/a6023674-cd53-3b88-89eb-7ae496f73cdc",
          "product_eng_name": "Nissin Cup Noodles Beef 75GM"
        }
      ],
      "name": "日清合味道五香牛肉杯麵 75GM",
      "price": "$8",
      "offer": "【2件$14.5】$14.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250327/a6023674-cd53-3b88-89eb-7ae496f73cdc",
      "product_eng_name": "Nissin Cup Noodles Beef 75GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E9%87%91%E9%B3%B3%E6%B3%B0%E5%9C%8B%E9%A0%82%E7%B4%9A%E9%A6%99%E7%B1%B3%203KGM/i/101342430.html",
      "uid": "9366700ae524f93ea760f29ac0ffe7be",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "金鳳泰國頂級香米 3KGM",
          "price": "$63",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250307/db5b757e-3c26-3c55-9004-e0198f2871f3",
          "product_eng_name": "Golden Phoenix Thai Hom Mali Rice 3KG"
        }
      ],
      "name": "金鳳泰國頂級香米 3KGM",
      "price": "$63",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250307/db5b757e-3c26-3c55-9004-e0198f2871f3",
      "product_eng_name": "Golden Phoenix Thai Hom Mali Rice 3KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%8D%85%E7%90%83%E5%98%9C%E5%88%9D%E6%90%BE%E6%A9%84%E6%AC%96%E6%B2%B9%201LT/i/101355901.html",
      "uid": "2fdd35ed906dca96a56d360b1e352c62",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "獅球嘜初搾橄欖油 1LT",
          "price": "$130",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20200501/bdabf554-700b-47a6-9daf-49f19f2b7d77",
          "product_eng_name": "Lion & Globe Extra Virgin Olive Oil 1LT"
        },
        {
          "name": "獅球嘜初搾橄欖油 1LT",
          "price": "$130",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20200501/bdabf554-700b-47a6-9daf-49f19f2b7d77",
          "product_eng_name": "Lion & Globe Extra Virgin Olive Oil 1LT"
        }
      ],
      "name": "獅球嘜初搾橄欖油 1LT",
      "price": "$130",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20200501/bdabf554-700b-47a6-9daf-49f19f2b7d77",
      "product_eng_name": "Lion & Globe Extra Virgin Olive Oil 1LT"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E8%BE%B2%E5%BF%83%E9%9F%93%E5%9C%8B%E7%89%88%E8%BE%9B%E8%BE%A3%E9%BA%B5%205%20X%20120GM/i/101371296.html",
      "uid": "e7afc4589f28b486bef88b4435586c7f",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "農心韓國版辛辣麵 5 X 120GM",
          "price": "$46",
          "offer": "【2件$48】$48任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210520/b1070d08-8219-4883-a7a3-7b2a2a51fbe7",
          "product_eng_name": "Nong Shim Korean Shin Noodles 5 X 120GM"
        },
        {
          "name": "農心韓國版辛辣麵 5 X 120GM",
          "price": "$46",
          "offer": "【2件$48】$48任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210520/b1070d08-8219-4883-a7a3-7b2a2a51fbe7",
          "product_eng_name": "Nong Shim Korean Shin Noodles 5 X 120GM"
        }
      ],
      "name": "農心韓國版辛辣麵 5 X 120GM",
      "price": "$46",
      "offer": "【2件$48】$48任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210520/b1070d08-8219-4883-a7a3-7b2a2a51fbe7",
      "product_eng_name": "Nong Shim Korean Shin Noodles 5 X 120GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%97%A5%E6%B8%85%E6%98%A5%E9%9B%A8%E9%9F%93%E5%BC%8F%E6%B3%A1%E8%8F%9C%E7%B2%89%E7%B5%B2%E6%B9%AF%2043GM/i/101346820.html",
      "uid": "987c45495e547da25b282b203a1b169e",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "日清春雨韓式泡菜粉絲湯 43GM",
          "price": "$11",
          "offer": "【2件$16】$16任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210513/3039a714-8777-4ca1-bdd9-91f0bf9bc6e1",
          "product_eng_name": "Nissin Harusame Kimchi Cup Vermicelli 43GM"
        },
        {
          "name": "日清春雨韓式泡菜粉絲湯 43GM",
          "price": "$11",
          "offer": "【2件$16】$16任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210513/3039a714-8777-4ca1-bdd9-91f0bf9bc6e1",
          "product_eng_name": "Nissin Harusame Kimchi Cup Vermicelli 43GM"
        }
      ],
      "name": "日清春雨韓式泡菜粉絲湯 43GM",
      "price": "$11",
      "offer": "【2件$16】$16任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210513/3039a714-8777-4ca1-bdd9-91f0bf9bc6e1",
      "product_eng_name": "Nissin Harusame Kimchi Cup Vermicelli 43GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E5%BE%A1%E5%93%81%E7%9A%87%20%E7%B4%85%E7%87%92%E7%89%9B%E8%82%89%E6%B9%AF%E9%BA%B5%2098%20GM/i/113612096.html",
      "uid": "aeed49c5dffc54487e8039d48ec726f8",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱御品皇 紅燒牛肉湯麵 98 GM",
          "price": "$120",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230926/55643590-4c60-396c-81b2-9b76b61de350",
          "product_eng_name": "Yu Pin King Braised Beef Flavour Soup Noodles Case 30 x 98GM"
        },
        {
          "name": "原箱御品皇 紅燒牛肉湯麵 98 GM",
          "price": "$120",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230926/55643590-4c60-396c-81b2-9b76b61de350",
          "product_eng_name": "Yu Pin King Braised Beef Flavour Soup Noodles Case 30 x 98GM"
        }
      ],
      "name": "原箱御品皇 紅燒牛肉湯麵 98 GM",
      "price": "$120",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230926/55643590-4c60-396c-81b2-9b76b61de350",
      "product_eng_name": "Yu Pin King Braised Beef Flavour Soup Noodles Case 30 x 98GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%87%BA%E5%89%8D%E4%B8%80%E4%B8%81-%E8%B3%80%E5%B9%B4%E8%A3%9D%20%E5%8C%97%E6%B5%B7%E9%81%93%E5%B0%8F%E9%BA%A5%E7%B2%89%E9%BA%BB%E6%B2%B9%E5%91%B3%E5%8D%B3%E9%A3%9F%E9%BA%B55%E5%8C%85%E8%A3%9D%E6%96%B0%E6%98%A5%E7%89%88%20100%20GM/i/113264039.html",
      "uid": "a5b6b2688e827b4e338f75186203235d",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "出前一丁-賀年裝 北海道小麥粉麻油味即食麵5包裝新春版 100 GM",
          "price": "$20",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20241230/d25a8ffe-02cf-3149-b346-5954e2bb6856",
          "product_eng_name": "DEMAE CNY RAMEN SESAME OIL FLAVOUR INSTANT NOODLE 5P CNY 100 GM"
        },
        {
          "name": "出前一丁-賀年裝 北海道小麥粉麻油味即食麵5包裝新春版 100 GM",
          "price": "$20",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20241230/d25a8ffe-02cf-3149-b346-5954e2bb6856",
          "product_eng_name": "DEMAE CNY RAMEN SESAME OIL FLAVOUR INSTANT NOODLE 5P CNY 100 GM"
        }
      ],
      "name": "出前一丁-賀年裝 北海道小麥粉麻油味即食麵5包裝新春版 100 GM",
      "price": "$20",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20241230/d25a8ffe-02cf-3149-b346-5954e2bb6856",
      "product_eng_name": "DEMAE CNY RAMEN SESAME OIL FLAVOUR INSTANT NOODLE 5P CNY 100 GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/ACE%20%E7%89%B9%E6%92%B0%E5%96%AC%E9%BA%A5%E9%BA%B5%20360GM/i/101357841.html",
      "uid": "7055ae33ee4b35ef943e63f51dfc7d99",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "ACE 特撰喬麥麵 360GM",
          "price": "$19",
          "offer": "【3件$50】$50任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240425/957e9dc3-d189-3ba4-80dc-3a527179d963",
          "product_eng_name": "ACE Tokusen Zarusoba 360GM"
        },
        {
          "name": "ACE 特撰喬麥麵 360GM",
          "price": "$19",
          "offer": "【3件$50】$50任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240425/957e9dc3-d189-3ba4-80dc-3a527179d963",
          "product_eng_name": "ACE Tokusen Zarusoba 360GM"
        }
      ],
      "name": "ACE 特撰喬麥麵 360GM",
      "price": "$19",
      "offer": "【3件$50】$50任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240425/957e9dc3-d189-3ba4-80dc-3a527179d963",
      "product_eng_name": "ACE Tokusen Zarusoba 360GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%BE%A1%E5%93%81%E7%9A%87%E5%84%AA%E8%B3%AA%E6%B3%B0%E5%9C%8B%E8%8C%89%E8%8E%89%E9%A6%99%E7%B1%B3%205KG/i/101381360.html",
      "uid": "cb43a99a60671d959954535bf8803df8",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "御品皇優質泰國茉莉香米 5KG",
          "price": "$55",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250219/f4b15870-c407-3c21-a9df-e750d6adee56",
          "product_eng_name": "Yu Pin King Thai Jasmine Fragrant Rice 5KG"
        }
      ],
      "name": "御品皇優質泰國茉莉香米 5KG",
      "price": "$55",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250219/f4b15870-c407-3c21-a9df-e750d6adee56",
      "product_eng_name": "Yu Pin King Thai Jasmine Fragrant Rice 5KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E5%85%AC%E4%BB%94%20%E5%8E%9F%E5%91%B3%E7%B1%B3%E7%B2%89%2030%20X%2070GM/i/113509244.html",
      "uid": "930eb45c773dd1b5e2a62daf3279c6c0",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱公仔 原味米粉 30 X 70GM",
          "price": "$88",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230728/e1992922-2bb8-3e8b-b547-e16217c09e7c",
          "product_eng_name": "Doll Instant Mifun 30 X 70GM"
        },
        {
          "name": "原箱公仔 原味米粉 30 X 70GM",
          "price": "$88",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230728/e1992922-2bb8-3e8b-b547-e16217c09e7c",
          "product_eng_name": "Doll Instant Mifun 30 X 70GM"
        }
      ],
      "name": "原箱公仔 原味米粉 30 X 70GM",
      "price": "$88",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230728/e1992922-2bb8-3e8b-b547-e16217c09e7c",
      "product_eng_name": "Doll Instant Mifun 30 X 70GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E7%99%BE%E5%8B%9D%E5%BB%9A%20%E6%96%B0%E5%8A%A0%E5%9D%A1%E5%8F%BB%E6%B2%99%E6%8B%89%E9%BA%B512%20X%20185%20GM/i/101335798.html",
      "uid": "ed9fdea66784e0171137a787d4e9bb62",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱百勝廚 新加坡叻沙拉麵12 X 185 GM",
          "price": "$372",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240315/051f26f5-357e-3818-a58c-cf5dfb8c5bd4",
          "product_eng_name": "Prima Taste Laksa La Mian Case 12 X 185 GM"
        },
        {
          "name": "原箱百勝廚 新加坡叻沙拉麵12 X 185 GM",
          "price": "$372",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240315/051f26f5-357e-3818-a58c-cf5dfb8c5bd4",
          "product_eng_name": "Prima Taste Laksa La Mian Case 12 X 185 GM"
        }
      ],
      "name": "原箱百勝廚 新加坡叻沙拉麵12 X 185 GM",
      "price": "$372",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240315/051f26f5-357e-3818-a58c-cf5dfb8c5bd4",
      "product_eng_name": "Prima Taste Laksa La Mian Case 12 X 185 GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E4%BB%8A%E9%BA%A5%E9%83%8E%20%E7%89%9B%E8%82%89%E7%83%8F%E5%86%AC%E9%BA%B5%20149GM/i/113563234.html",
      "uid": "0b2bf0502ec4e5abb389c5bb764b9fc2",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "今麥郎 牛肉烏冬麵 149GM",
          "price": "$22",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240124/f6f24c35-1bf1-34c2-be08-d7a7bbed3e0e",
          "product_eng_name": "Jinmailang Beef Udon 149GM"
        },
        {
          "name": "今麥郎 牛肉烏冬麵 149GM",
          "price": "$22",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240124/f6f24c35-1bf1-34c2-be08-d7a7bbed3e0e",
          "product_eng_name": "Jinmailang Beef Udon 149GM"
        }
      ],
      "name": "今麥郎 牛肉烏冬麵 149GM",
      "price": "$22",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240124/f6f24c35-1bf1-34c2-be08-d7a7bbed3e0e",
      "product_eng_name": "Jinmailang Beef Udon 149GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/Grove%E7%89%9B%E6%B2%B9%E6%9E%9C%E6%B2%B9%20250ML/i/101331719.html",
      "uid": "a4c57337d6caa951d676afe65f2aa75e",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "Grove牛油果油 250ML",
          "price": "$109",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240208/af7635fa-64c5-3d04-bfbb-bc958becc14a",
          "product_eng_name": "Grove Extra Virgin Cold Pressed Avocado Oil 250ML"
        },
        {
          "name": "Grove牛油果油 250ML",
          "price": "$109",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240208/af7635fa-64c5-3d04-bfbb-bc958becc14a",
          "product_eng_name": "Grove Extra Virgin Cold Pressed Avocado Oil 250ML"
        }
      ],
      "name": "Grove牛油果油 250ML",
      "price": "$109",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240208/af7635fa-64c5-3d04-bfbb-bc958becc14a",
      "product_eng_name": "Grove Extra Virgin Cold Pressed Avocado Oil 250ML"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E8%BE%B2%E5%BF%83%E7%94%9F%E7%94%9F%E7%83%8F%E5%86%AC%E7%A2%97%E9%BA%B5%20276GM/i/101351997.html",
      "uid": "acfa067c9b584c729d0ff5fdb1b84b75",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "農心生生烏冬碗麵 276GM",
          "price": "$33",
          "offer": "【2件$29】$29任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210520/0b5cdff5-d84d-449d-accb-e14b07dfe109",
          "product_eng_name": "(無法擷取英文名稱)"
        },
        {
          "name": "農心生生烏冬碗麵 276GM",
          "price": "$33",
          "offer": "【2件$29】$29任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210520/0b5cdff5-d84d-449d-accb-e14b07dfe109",
          "product_eng_name": "Nong Shim Saeng Saeng Udon Bowl 276GM"
        }
      ],
      "name": "農心生生烏冬碗麵 276GM",
      "price": "$33",
      "offer": "【2件$29】$29任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210520/0b5cdff5-d84d-449d-accb-e14b07dfe109",
      "product_eng_name": "Nong Shim Saeng Saeng Udon Bowl 276GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E8%B6%85%E5%8A%9B%E9%8A%80%E7%B5%B2%E7%B1%B3%E7%B2%89%205%20X%2065GM/i/101354653.html",
      "uid": "324535114eaff417411d572610dddf39",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "超力銀絲米粉 5 X 65GM",
          "price": "$30",
          "offer": "【2件$35】$35任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240916/7693c7cd-adef-3be4-940e-b99748ec07b4",
          "product_eng_name": "Chewy Instant Mei Fun 5 X 65GM"
        },
        {
          "name": "超力銀絲米粉 5 X 65GM",
          "price": "$30",
          "offer": "【2件$35】$35任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240916/7693c7cd-adef-3be4-940e-b99748ec07b4",
          "product_eng_name": "Chewy Instant Mei Fun 5 X 65GM"
        }
      ],
      "name": "超力銀絲米粉 5 X 65GM",
      "price": "$30",
      "offer": "【2件$35】$35任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240916/7693c7cd-adef-3be4-940e-b99748ec07b4",
      "product_eng_name": "Chewy Instant Mei Fun 5 X 65GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%97%A5%E6%B8%85%E5%90%88%E5%91%B3%E9%81%93%E5%A4%A7%E6%9D%AF%E6%B5%B7%E9%AE%AE%E5%91%B3%E5%8D%B3%E9%A3%9F%E9%BA%B5%20100GM/i/101857785.html",
      "uid": "0db105a89711cef0eece5b3acf7e765e",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "日清合味道大杯海鮮味即食麵 100GM",
          "price": "$11",
          "offer": "【2件$18】$18任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240711/09c7af18-731d-384a-bea5-66b749e04eed",
          "product_eng_name": "Nissin Cup Noodles Big Cup Seafood Flavour Noodle 100GM"
        },
        {
          "name": "日清合味道大杯海鮮味即食麵 100GM",
          "price": "$11",
          "offer": "【2件$18】$18任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240711/09c7af18-731d-384a-bea5-66b749e04eed",
          "product_eng_name": "Nissin Cup Noodles Big Cup Seafood Flavour Noodle 100GM"
        }
      ],
      "name": "日清合味道大杯海鮮味即食麵 100GM",
      "price": "$11",
      "offer": "【2件$18】$18任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240711/09c7af18-731d-384a-bea5-66b749e04eed",
      "product_eng_name": "Nissin Cup Noodles Big Cup Seafood Flavour Noodle 100GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/Kiki%E9%A3%9F%E5%93%81%E6%A4%92%E9%BA%BB%E6%8B%8C%E9%BA%B5%205%20X%2090GM/i/101362827.html",
      "uid": "503ebc7249a41ec6f0f9737984c10168",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "Kiki食品椒麻拌麵 5 X 90GM",
          "price": "$45",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20200430/e4b97605-6535-4b54-98da-f9de550c2d38",
          "product_eng_name": "KiKi Sichuan Spices Dry-Stirred Noodles 5 x 90GM"
        },
        {
          "name": "Kiki食品椒麻拌麵 5 X 90GM",
          "price": "$45",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20200430/e4b97605-6535-4b54-98da-f9de550c2d38",
          "product_eng_name": "KiKi Sichuan Spices Dry-Stirred Noodles 5 x 90GM"
        }
      ],
      "name": "Kiki食品椒麻拌麵 5 X 90GM",
      "price": "$45",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20200430/e4b97605-6535-4b54-98da-f9de550c2d38",
      "product_eng_name": "KiKi Sichuan Spices Dry-Stirred Noodles 5 x 90GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E8%BE%B2%E5%BF%83%E5%92%96%E5%96%B1%E6%8B%89%E9%BA%B5%205%20X%20116GM/i/101359562.html",
      "uid": "378ec9e28ee603a92f7c771ef9165747",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "農心咖喱拉麵 5 X 116GM",
          "price": "$17",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210520/51f98617-1eab-43e3-90e8-806bd89b4477",
          "product_eng_name": "Nong Shim Curry Noodle 5 X 116GM"
        },
        {
          "name": "農心咖喱拉麵 5 X 116GM",
          "price": "$17",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210520/51f98617-1eab-43e3-90e8-806bd89b4477",
          "product_eng_name": "Nong Shim Curry Noodle 5 X 116GM"
        }
      ],
      "name": "農心咖喱拉麵 5 X 116GM",
      "price": "$17",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210520/51f98617-1eab-43e3-90e8-806bd89b4477",
      "product_eng_name": "Nong Shim Curry Noodle 5 X 116GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E8%B6%85%E5%8A%9B%20%E9%87%91%E6%B9%AF%E8%82%A5%E7%89%9B%E5%91%B3%E7%A2%97%E7%B1%B3%E7%B2%89%20102%20GM/i/101328407.html",
      "uid": "6dd72c351a386daff541f98b53053084",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "超力 金湯肥牛味碗米粉 102 GM",
          "price": "$12",
          "offer": "【2件$14.5】$14.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240823/6cc7cfe2-63f2-3059-8476-d6089714a206",
          "product_eng_name": "Chewy Sour Golden Soup Beef Bowl Vermicelli 102GM"
        },
        {
          "name": "超力 金湯肥牛味碗米粉 102 GM",
          "price": "$12",
          "offer": "【2件$14.5】$14.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240823/6cc7cfe2-63f2-3059-8476-d6089714a206",
          "product_eng_name": "Chewy Sour Golden Soup Beef Bowl Vermicelli 102GM"
        }
      ],
      "name": "超力 金湯肥牛味碗米粉 102 GM",
      "price": "$12",
      "offer": "【2件$14.5】$14.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240823/6cc7cfe2-63f2-3059-8476-d6089714a206",
      "product_eng_name": "Chewy Sour Golden Soup Beef Bowl Vermicelli 102GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1KIKI%E9%A3%9F%E5%93%81%E9%9B%9C%E8%B2%A8%20%E8%94%A5%E6%B2%B9%E6%8B%8C%E9%BA%B55%E5%8C%85%E8%A3%9D10%20X%2090%20GM/i/101335783.html",
      "uid": "b228f8a64f0a069bc121763a98fb64dd",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱KIKI食品雜貨 蔥油拌麵5包裝10 X 90 GM",
          "price": "$480",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231221/df1bf0e3-d8b8-38fb-9493-4a833c77b639",
          "product_eng_name": "Kiki Scallion Oil Dry-Stirred Noodles Case 50 x 90GM"
        },
        {
          "name": "原箱KIKI食品雜貨 蔥油拌麵5包裝10 X 90 GM",
          "price": "$480",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231221/df1bf0e3-d8b8-38fb-9493-4a833c77b639",
          "product_eng_name": "Kiki Scallion Oil Dry-Stirred Noodles Case 50 x 90GM"
        }
      ],
      "name": "原箱KIKI食品雜貨 蔥油拌麵5包裝10 X 90 GM",
      "price": "$480",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20231221/df1bf0e3-d8b8-38fb-9493-4a833c77b639",
      "product_eng_name": "Kiki Scallion Oil Dry-Stirred Noodles Case 50 x 90GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%BE%8E%E6%8B%BE%E6%B4%BE%20%E5%A4%A7%E9%96%98%E8%9F%B9%E8%8F%8C%E8%8F%87%E7%B2%A5%E6%96%99%201KG/i/101341323.html",
      "uid": "945b36ba07e650313c99ae30d868dfa7",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "美拾派 大閘蟹菌菇粥料 1KG",
          "price": "$108",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240105/a6dd3a45-1cf0-32e8-bced-3d7a40cc59b5",
          "product_eng_name": "Meysypal Crab Mushroom Congee 1KG"
        },
        {
          "name": "美拾派 大閘蟹菌菇粥料 1KG",
          "price": "$108",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240105/a6dd3a45-1cf0-32e8-bced-3d7a40cc59b5",
          "product_eng_name": "Meysypal Crab Mushroom Congee 1KG"
        }
      ],
      "name": "美拾派 大閘蟹菌菇粥料 1KG",
      "price": "$108",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240105/a6dd3a45-1cf0-32e8-bced-3d7a40cc59b5",
      "product_eng_name": "Meysypal Crab Mushroom Congee 1KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%97%A5%E6%B8%85%E5%92%9A%E5%85%B5%E8%A1%9B%E8%85%90%E7%9A%AE%E7%83%8F%E5%86%AC%2095GM/i/101326919.html",
      "uid": "4ed4facf0d727a155c2b7c0a8efb8758",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "日清咚兵衛腐皮烏冬 95GM",
          "price": "$11",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20241029/6889e512-4d76-3456-8615-228fa93346f1",
          "product_eng_name": "Nissin Donbei Kitsune Udon 95GM"
        },
        {
          "name": "日清咚兵衛腐皮烏冬 95GM",
          "price": "$11",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20241029/6889e512-4d76-3456-8615-228fa93346f1",
          "product_eng_name": "Nissin Donbei Kitsune Udon 95GM"
        }
      ],
      "name": "日清咚兵衛腐皮烏冬 95GM",
      "price": "$11",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20241029/6889e512-4d76-3456-8615-228fa93346f1",
      "product_eng_name": "Nissin Donbei Kitsune Udon 95GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%97%A5%E6%B8%85%E7%B6%A0%E8%8C%B6%E5%91%B3%E8%95%8E%E9%BA%A5%E9%BA%B5%20200GM/i/101341377.html",
      "uid": "e84ca5de81aadf614b1f5655a9e56bd5",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "日清綠茶味蕎麥麵 200GM",
          "price": "$36",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240422/6cf15f28-37ee-3ad1-849f-20afb75c7ef7",
          "product_eng_name": "Nissin Soba with Green Tea Flavour 200GM"
        },
        {
          "name": "日清綠茶味蕎麥麵 200GM",
          "price": "$36",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240422/6cf15f28-37ee-3ad1-849f-20afb75c7ef7",
          "product_eng_name": "Nissin Soba with Green Tea Flavour 200GM"
        }
      ],
      "name": "日清綠茶味蕎麥麵 200GM",
      "price": "$36",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240422/6cf15f28-37ee-3ad1-849f-20afb75c7ef7",
      "product_eng_name": "Nissin Soba with Green Tea Flavour 200GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%BE%A1%E5%93%81%E7%9A%87%E7%B4%94%E6%AD%A3%E8%8A%A5%E8%8A%B1%E7%B1%BD%E6%B2%B9%203%20X%20900ML/i/101367274.html",
      "uid": "99703e46475fa6e6f0ff34c91b8d9be9",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "御品皇純正芥花籽油 3 X 900ML",
          "price": "$62",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210426/c1611660-19a9-4a3a-9a98-9bcd2af02b22",
          "product_eng_name": "Yu Pin King Canola Oil 3 X 900ML"
        },
        {
          "name": "御品皇純正芥花籽油 3 X 900ML",
          "price": "$62",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210426/c1611660-19a9-4a3a-9a98-9bcd2af02b22",
          "product_eng_name": "Yu Pin King Canola Oil 3 X 900ML"
        }
      ],
      "name": "御品皇純正芥花籽油 3 X 900ML",
      "price": "$62",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210426/c1611660-19a9-4a3a-9a98-9bcd2af02b22",
      "product_eng_name": "Yu Pin King Canola Oil 3 X 900ML"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E6%97%A5%E6%B8%85%E5%87%BA%E5%89%8D%E4%B8%80%E4%B8%81%E9%BA%BB%E6%B2%B9%E5%8D%B3%E9%A3%9F%E9%BA%B5%2030%20X%20100GM/i/101343929.html",
      "uid": "e3b2f46a7d28954391553c595e9b7e01",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱日清出前一丁麻油即食麵 30 X 100GM",
          "price": "$105",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230117/67023921-5b8c-43f2-bca7-c08d53aef08b",
          "product_eng_name": "Nissin Demae Iccho Sesame Oil Noodle Case 30 X 100GM"
        },
        {
          "name": "原箱日清出前一丁麻油即食麵 30 X 100GM",
          "price": "$105",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230117/67023921-5b8c-43f2-bca7-c08d53aef08b",
          "product_eng_name": "Nissin Demae Iccho Sesame Oil Noodle Case 30 X 100GM"
        }
      ],
      "name": "原箱日清出前一丁麻油即食麵 30 X 100GM",
      "price": "$105",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230117/67023921-5b8c-43f2-bca7-c08d53aef08b",
      "product_eng_name": "Nissin Demae Iccho Sesame Oil Noodle Case 30 X 100GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E4%BF%9D%E5%BE%97%20%E7%89%B9%E7%B4%9A%E5%88%9D%E6%A6%A8%E6%A9%84%E6%AC%96%E6%B2%B9%201LT/i/113267719.html",
      "uid": "abc7ecb3b6a7025955758ac6a35191aa",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "保得 特級初榨橄欖油 1LT",
          "price": "$159",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230209/edb9fd2b-6309-4b62-a0ed-737411df44cb",
          "product_eng_name": "Bontaste Extra Virgin Olive Oil 1LT"
        },
        {
          "name": "保得 特級初榨橄欖油 1LT",
          "price": "$159",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230209/edb9fd2b-6309-4b62-a0ed-737411df44cb",
          "product_eng_name": "Bontaste Extra Virgin Olive Oil 1LT"
        }
      ],
      "name": "保得 特級初榨橄欖油 1LT",
      "price": "$159",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230209/edb9fd2b-6309-4b62-a0ed-737411df44cb",
      "product_eng_name": "Bontaste Extra Virgin Olive Oil 1LT"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E5%AD%94%E9%9B%80%E7%89%8C%20%E6%9D%B1%E8%8E%9E%E7%B1%B3%E7%B2%8930%20X%20454%20GM/i/101335797.html",
      "uid": "de5e4c8bf6bbedc39b3cd0c973359085",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱孔雀牌 東莞米粉30 X 454 GM",
          "price": "$384",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231221/54270d0e-005c-3b94-896f-52e8d26a4a3f",
          "product_eng_name": "Peacock Dongguan Rice Verm Case 30 X 454 GM"
        },
        {
          "name": "原箱孔雀牌 東莞米粉30 X 454 GM",
          "price": "$384",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231221/54270d0e-005c-3b94-896f-52e8d26a4a3f",
          "product_eng_name": "Peacock Dongguan Rice Verm Case 30 X 454 GM"
        }
      ],
      "name": "原箱孔雀牌 東莞米粉30 X 454 GM",
      "price": "$384",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20231221/54270d0e-005c-3b94-896f-52e8d26a4a3f",
      "product_eng_name": "Peacock Dongguan Rice Verm Case 30 X 454 GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%A5%BD%E6%AD%A1%E8%9E%BA%20%E5%B0%8F%E9%BE%8D%E8%9D%A6%E5%91%B3%E8%9E%BA%E8%9E%84%E7%B2%89%20320%20GM/i/102692381.html",
      "uid": "934c259fe23d1dd05c8434720b174902",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "好歡螺 小龍蝦味螺螄粉 320 GM",
          "price": "$19",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250402/a6b3f85d-a73f-33e3-9fd8-aebeafd654db",
          "product_eng_name": "HAO HUAN LUO SNAIL RICE NOODLES CRAYFISHTASTE 320 GM"
        },
        {
          "name": "好歡螺 小龍蝦味螺螄粉 320 GM",
          "price": "$19",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250402/a6b3f85d-a73f-33e3-9fd8-aebeafd654db",
          "product_eng_name": "HAO HUAN LUO SNAIL RICE NOODLES CRAYFISHTASTE 320 GM"
        }
      ],
      "name": "好歡螺 小龍蝦味螺螄粉 320 GM",
      "price": "$19",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250402/a6b3f85d-a73f-33e3-9fd8-aebeafd654db",
      "product_eng_name": "HAO HUAN LUO SNAIL RICE NOODLES CRAYFISHTASTE 320 GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%87%9F%E5%A4%9A%E5%82%B3%E7%B5%B1%E6%92%88%E9%BA%B5%205%20X%2085GM/i/101348756.html",
      "uid": "fc8fd040d2c317a5b3c9103302218bd0",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "營多傳統撈麵 5 X 85GM",
          "price": "$17",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240718/b4f6ce6e-b51f-37c3-acde-99d7c7a1808a",
          "product_eng_name": "Indomie Goreng Fried Noodle 5 X 85GM"
        },
        {
          "name": "營多傳統撈麵 5 X 85GM",
          "price": "$17",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240718/b4f6ce6e-b51f-37c3-acde-99d7c7a1808a",
          "product_eng_name": "Indomie Goreng Fried Noodle 5 X 85GM"
        }
      ],
      "name": "營多傳統撈麵 5 X 85GM",
      "price": "$17",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240718/b4f6ce6e-b51f-37c3-acde-99d7c7a1808a",
      "product_eng_name": "Indomie Goreng Fried Noodle 5 X 85GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%85%AC%E4%BB%94%E7%89%B9%E8%89%B2%E9%A6%99%E8%BE%A3%E9%86%AC%E7%82%92%E9%BA%B5%E7%8E%8B%20120GM/i/101328300.html",
      "uid": "4419bcdfa855cfd35d1ccebe43c238fb",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "公仔特色香辣醬炒麵王 120GM",
          "price": "$7",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250320/d61a05a5-a18a-3e7e-876b-f0e323655762",
          "product_eng_name": "Doll Fried Chili Noodles 120GM"
        },
        {
          "name": "公仔特色香辣醬炒麵王 120GM",
          "price": "$7",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250320/d61a05a5-a18a-3e7e-876b-f0e323655762",
          "product_eng_name": "Doll Fried Chili Noodles 120GM"
        }
      ],
      "name": "公仔特色香辣醬炒麵王 120GM",
      "price": "$7",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250320/d61a05a5-a18a-3e7e-876b-f0e323655762",
      "product_eng_name": "Doll Fried Chili Noodles 120GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%A4%A7%E5%B8%AB%E5%A7%90%20%E9%A0%82%E7%B4%9A%E7%89%9B%E8%82%9D%E8%8F%8C%E9%BA%B5(%E5%B9%BC)%206%E5%80%8B%E8%A3%9D/i/115007856.html",
      "uid": "ead54277b1ec500231782ecb485a4fe5",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "大師姐 頂級牛肝菌麵(幼) 6個裝",
          "price": "$98",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250122/98cf7f5a-6452-370c-b96b-6d953c9269c7",
          "product_eng_name": "Dashijie Porcini Noodles (Fine)"
        },
        {
          "name": "大師姐 頂級牛肝菌麵(幼) 6個裝",
          "price": "$98",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250122/98cf7f5a-6452-370c-b96b-6d953c9269c7",
          "product_eng_name": "Dashijie Porcini Noodles (Fine)"
        }
      ],
      "name": "大師姐 頂級牛肝菌麵(幼) 6個裝",
      "price": "$98",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250122/98cf7f5a-6452-370c-b96b-6d953c9269c7",
      "product_eng_name": "Dashijie Porcini Noodles (Fine)"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E6%97%A5%E6%B8%85%E6%98%A5%E9%9B%A8%20%E9%9F%93%E5%BC%8F%E6%B3%A1%E8%8F%9C%E7%B2%89%E7%B5%B2%2012%20X%2043GM/i/113465549.html",
      "uid": "188a6cb4505c8f30c19fadf49711fd3c",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱日清春雨 韓式泡菜粉絲 12 X 43GM",
          "price": "$94",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230728/618ce034-10e5-3f53-a80d-b6b46e938ffc",
          "product_eng_name": "Nissin Harusame Kimchi Cup Vermicelli Case 12 X 43GM"
        },
        {
          "name": "原箱日清春雨 韓式泡菜粉絲 12 X 43GM",
          "price": "$94",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230728/618ce034-10e5-3f53-a80d-b6b46e938ffc",
          "product_eng_name": "Nissin Harusame Kimchi Cup Vermicelli Case 12 X 43GM"
        }
      ],
      "name": "原箱日清春雨 韓式泡菜粉絲 12 X 43GM",
      "price": "$94",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230728/618ce034-10e5-3f53-a80d-b6b46e938ffc",
      "product_eng_name": "Nissin Harusame Kimchi Cup Vermicelli Case 12 X 43GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%AD%94%E9%9B%80%E7%89%8C%E6%9D%B1%E8%8E%9E%E7%B1%B3%E7%B2%89%20454GM/i/101357773.html",
      "uid": "b9d137f41c32f33f803c132300c79646",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "孔雀牌東莞米粉 454GM",
          "price": "$13",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230321/afb6376c-6df6-4a06-922e-7a5f401e70e7",
          "product_eng_name": "Peacock Dongguan Rice Vermicelli 454GM"
        },
        {
          "name": "孔雀牌東莞米粉 454GM",
          "price": "$13",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230321/afb6376c-6df6-4a06-922e-7a5f401e70e7",
          "product_eng_name": "Peacock Dongguan Rice Vermicelli 454GM"
        }
      ],
      "name": "孔雀牌東莞米粉 454GM",
      "price": "$13",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230321/afb6376c-6df6-4a06-922e-7a5f401e70e7",
      "product_eng_name": "Peacock Dongguan Rice Vermicelli 454GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/De%20Cecco%E6%84%8F%E5%A4%A7%E5%88%A9%E9%80%9A%E5%BF%83%E7%B2%89%20N33%20500GM/i/101322582.html",
      "uid": "61aaa2b1fe51495f5e2c32a82b701814",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "De Cecco意大利通心粉 N33 500GM",
          "price": "$29",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240917/d54e9830-affd-3246-aafc-a0e23d223a6d",
          "product_eng_name": "Dececco Chifferi Rigati n°33 500GM"
        },
        {
          "name": "De Cecco意大利通心粉 N33 500GM",
          "price": "$29",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240917/d54e9830-affd-3246-aafc-a0e23d223a6d",
          "product_eng_name": "Dececco Chifferi Rigati n°33 500GM"
        }
      ],
      "name": "De Cecco意大利通心粉 N33 500GM",
      "price": "$29",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240917/d54e9830-affd-3246-aafc-a0e23d223a6d",
      "product_eng_name": "Dececco Chifferi Rigati n°33 500GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E8%BE%9B%E8%BE%A3%E8%8A%9D%E5%A3%AB%E7%82%92%E9%BA%B5(%E7%A2%97%E8%A3%9D)/i/114326961.html",
      "uid": "ba6830aa73aa470e0c7b41044454a41e",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "辛辣芝士炒麵(碗裝)",
          "price": "$20",
          "offer": "【2件$26】$26任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240923/3cff54b8-adfe-397b-a063-f1fb3880e52e",
          "product_eng_name": "(無法擷取英文名稱)"
        },
        {
          "name": "辛辣芝士炒麵(碗裝)",
          "price": "$20",
          "offer": "【2件$26】$26任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240923/3cff54b8-adfe-397b-a063-f1fb3880e52e",
          "product_eng_name": "Shin Stir Fry Cheese Bowl 105GM"
        }
      ],
      "name": "辛辣芝士炒麵(碗裝)",
      "price": "$20",
      "offer": "【2件$26】$26任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240923/3cff54b8-adfe-397b-a063-f1fb3880e52e",
      "product_eng_name": "Shin Stir Fry Cheese Bowl 105GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%A3%BD%E6%A1%83%E7%89%B9%E7%B4%9A%E8%9D%A6%E5%AD%90%E9%BA%B5%E6%A1%B6%E8%A3%9D%20880GM/i/101350024.html",
      "uid": "631253067bfa61aca8b40384a1d60b53",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "壽桃特級蝦子麵桶裝 880GM",
          "price": "$36",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220505/77172bcd-9951-420a-ab1e-6acd365c3c9e",
          "product_eng_name": "Sau Tao Shrimp Noodles 880GM"
        },
        {
          "name": "壽桃特級蝦子麵桶裝 880GM",
          "price": "$36",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220505/77172bcd-9951-420a-ab1e-6acd365c3c9e",
          "product_eng_name": "Sau Tao Shrimp Noodles 880GM"
        }
      ],
      "name": "壽桃特級蝦子麵桶裝 880GM",
      "price": "$36",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20220505/77172bcd-9951-420a-ab1e-6acd365c3c9e",
      "product_eng_name": "Sau Tao Shrimp Noodles 880GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%BE%A1%E5%93%81%E7%9A%87%20%E7%B4%94%E6%AD%A3%E8%8A%A5%E8%8A%B1%E7%B1%BD%E6%B2%B9%205%20LT/i/113510469.html",
      "uid": "a553810eebff0857f004088f2cd884d8",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "御品皇 純正芥花籽油 5 LT",
          "price": "$95",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240704/a6956449-840b-346c-9b61-2f35f1d748b6",
          "product_eng_name": "Yu Pin King Pure Canola Oil 5LT"
        },
        {
          "name": "御品皇 純正芥花籽油 5 LT",
          "price": "$95",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240704/a6956449-840b-346c-9b61-2f35f1d748b6",
          "product_eng_name": "Yu Pin King Pure Canola Oil 5LT"
        }
      ],
      "name": "御品皇 純正芥花籽油 5 LT",
      "price": "$95",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240704/a6956449-840b-346c-9b61-2f35f1d748b6",
      "product_eng_name": "Yu Pin King Pure Canola Oil 5LT"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%85%AC%E4%BB%94%E9%BB%9E%E5%BF%83%E9%BA%B5(%E5%92%8C%E9%A2%A8%E8%B1%9A%E9%AA%A8%E6%B9%AF%E5%91%B3)%2036GM/i/101359991.html",
      "uid": "77ad5e9b7e8913758fb76fdf8233dfef",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "公仔點心麵(和風豚骨湯味) 36GM",
          "price": "$4",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210621/3140d692-cae0-4aab-bbff-f82c1f46a6ef",
          "product_eng_name": "Doll Japanese Tonkotsu Flavour 36GM"
        },
        {
          "name": "公仔點心麵(和風豚骨湯味) 36GM",
          "price": "$4",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210621/3140d692-cae0-4aab-bbff-f82c1f46a6ef",
          "product_eng_name": "Doll Japanese Tonkotsu Flavour 36GM"
        }
      ],
      "name": "公仔點心麵(和風豚骨湯味) 36GM",
      "price": "$4",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210621/3140d692-cae0-4aab-bbff-f82c1f46a6ef",
      "product_eng_name": "Doll Japanese Tonkotsu Flavour 36GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E7%84%A1%E9%9B%99%E9%BA%BB%E8%BE%A3%E7%B2%89%E6%9D%AF%E8%A3%9D%20%2012%20X%20125GM/i/113267694.html",
      "uid": "10db2682c88c853ac74178bfead8b736",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱無雙麻辣粉杯裝 12 X 125GM",
          "price": "$84",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20221125/975137d7-9604-4894-8a9f-45945406f2be",
          "product_eng_name": "Muso Sichuan Spicy Cup Case 12 X 125GM"
        },
        {
          "name": "原箱無雙麻辣粉杯裝 12 X 125GM",
          "price": "$84",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20221125/975137d7-9604-4894-8a9f-45945406f2be",
          "product_eng_name": "Muso Sichuan Spicy Cup Case 12 X 125GM"
        }
      ],
      "name": "原箱無雙麻辣粉杯裝 12 X 125GM",
      "price": "$84",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20221125/975137d7-9604-4894-8a9f-45945406f2be",
      "product_eng_name": "Muso Sichuan Spicy Cup Case 12 X 125GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E9%BB%9E%E9%BB%9E%E7%B6%A0%E6%9C%89%E6%A9%9F%E7%B4%85%E7%B1%B3%E8%88%87%E7%B3%99%E7%B1%B3%201KG/i/101343994.html",
      "uid": "1824f5c92f89f444738293909766a199",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "點點綠有機紅米與糙米 1KG",
          "price": "$45",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250320/7e31336d-501c-3a25-a54f-c17735d087e3",
          "product_eng_name": "Green Dot Dot Org Red Rice & Brown Rice 1KG"
        }
      ],
      "name": "點點綠有機紅米與糙米 1KG",
      "price": "$45",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250320/7e31336d-501c-3a25-a54f-c17735d087e3",
      "product_eng_name": "Green Dot Dot Org Red Rice & Brown Rice 1KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%85%AC%E4%BB%94%20%E9%BB%9E%E5%BF%83%E9%BA%B5%EF%BC%8D%E6%B5%B7%E9%AE%AE%2034GM/i/101358947.html",
      "uid": "55035e4f338a554f8a4c82f9c994c159",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "公仔 點心麵－海鮮 34GM",
          "price": "$4",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20241029/31902198-d423-3d10-a2ed-8c64bde2169f",
          "product_eng_name": "Doll Dim Sum Noodle Seafood 34GM"
        },
        {
          "name": "公仔 點心麵－海鮮 34GM",
          "price": "$4",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20241029/31902198-d423-3d10-a2ed-8c64bde2169f",
          "product_eng_name": "Doll Dim Sum Noodle Seafood 34GM"
        }
      ],
      "name": "公仔 點心麵－海鮮 34GM",
      "price": "$4",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20241029/31902198-d423-3d10-a2ed-8c64bde2169f",
      "product_eng_name": "Doll Dim Sum Noodle Seafood 34GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/SUNAOSHI%20%E7%89%B9%E9%81%B8%E8%95%8E%E9%BA%A5%E9%BA%B5%20360%20GM/i/101322264.html",
      "uid": "85c2a02b09cac56c84ff2e0df18116a7",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "SUNAOSHI 特選蕎麥麵 360 GM",
          "price": "$8",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240422/fc5d7b58-b9fc-3896-941c-4ab30d8037ce",
          "product_eng_name": "Sunaoshi Soba 360GM"
        },
        {
          "name": "SUNAOSHI 特選蕎麥麵 360 GM",
          "price": "$8",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240422/fc5d7b58-b9fc-3896-941c-4ab30d8037ce",
          "product_eng_name": "Sunaoshi Soba 360GM"
        }
      ],
      "name": "SUNAOSHI 特選蕎麥麵 360 GM",
      "price": "$8",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240422/fc5d7b58-b9fc-3896-941c-4ab30d8037ce",
      "product_eng_name": "Sunaoshi Soba 360GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%97%A5%E6%B8%85%E6%96%B0%E6%84%8F%E6%B4%BE%E5%8D%A1%E9%82%A6%E5%B0%BC%E8%8A%9D%E5%A3%AB%E7%85%99%E8%82%89%E5%91%B3%2092GM/i/101356829.html",
      "uid": "35c80588e129e491a53c2d8fdd16fd4c",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "日清新意派卡邦尼芝士煙肉味 92GM",
          "price": "$11",
          "offer": "【2件$17】$17任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210513/c9991bad-2dad-4b24-94a2-521a6ae77c71",
          "product_eng_name": "Nissin Nupasta Carbonara Cup Type 92GM"
        },
        {
          "name": "日清新意派卡邦尼芝士煙肉味 92GM",
          "price": "$11",
          "offer": "【2件$17】$17任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210513/c9991bad-2dad-4b24-94a2-521a6ae77c71",
          "product_eng_name": "Nissin Nupasta Carbonara Cup Type 92GM"
        }
      ],
      "name": "日清新意派卡邦尼芝士煙肉味 92GM",
      "price": "$11",
      "offer": "【2件$17】$17任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210513/c9991bad-2dad-4b24-94a2-521a6ae77c71",
      "product_eng_name": "Nissin Nupasta Carbonara Cup Type 92GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%87%BA%E5%89%8D%E4%B8%80%E4%B8%81%20%E9%9F%93%E8%BE%A3%E6%B5%B7%E9%AE%AE%E5%91%B3%E5%8D%B3%E9%A3%9F%E9%BA%B5%2098%20GM/i/101328521.html",
      "uid": "a4660211b94fe4077b1dbce8f8197819",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "出前一丁 韓辣海鮮味即食麵 98 GM",
          "price": "$5",
          "offer": "【8件$28.5】$28.5任揀8件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250407/8dd2a630-8e09-394b-8aaa-f842b996cfe8",
          "product_eng_name": "Nissin Demae Iccho Spicy Seafood Noodle 98GM"
        },
        {
          "name": "出前一丁 韓辣海鮮味即食麵 98 GM",
          "price": "$5",
          "offer": "【8件$28.5】$28.5任揀8件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250407/8dd2a630-8e09-394b-8aaa-f842b996cfe8",
          "product_eng_name": "Nissin Demae Iccho Spicy Seafood Noodle 98GM"
        }
      ],
      "name": "出前一丁 韓辣海鮮味即食麵 98 GM",
      "price": "$5",
      "offer": "【8件$28.5】$28.5任揀8件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250407/8dd2a630-8e09-394b-8aaa-f842b996cfe8",
      "product_eng_name": "Nissin Demae Iccho Spicy Seafood Noodle 98GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E5%85%AC%E4%BB%94%20%E5%87%B1%E8%92%82%E9%BB%9E%E5%BF%83%E9%BA%B5%2033%20GM/i/113566514.html",
      "uid": "aef39d1f99c3620567be07e2e97ad101",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱公仔 凱蒂點心麵 33 GM",
          "price": "$66",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230920/d732b8b3-e5d4-30c5-909b-1cade82ee905",
          "product_eng_name": "Doll Hello Kitty Dim Sum Noodles Case 18 x 33GM"
        },
        {
          "name": "原箱公仔 凱蒂點心麵 33 GM",
          "price": "$66",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230920/d732b8b3-e5d4-30c5-909b-1cade82ee905",
          "product_eng_name": "Doll Hello Kitty Dim Sum Noodles Case 18 x 33GM"
        }
      ],
      "name": "原箱公仔 凱蒂點心麵 33 GM",
      "price": "$66",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230920/d732b8b3-e5d4-30c5-909b-1cade82ee905",
      "product_eng_name": "Doll Hello Kitty Dim Sum Noodles Case 18 x 33GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E4%B8%89%E9%A4%8A%E8%96%AF%E4%BB%94%E6%8B%89%E9%BA%B5%205%20X%20120GM/i/101346171.html",
      "uid": "c0bb76121bc709b5764e328373c14d2a",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "三養薯仔拉麵 5 X 120GM",
          "price": "$36",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230209/4660d76c-1f33-43bd-b9f1-726c0509d768",
          "product_eng_name": "Samyang Potato Ramen 5 X 120GM"
        },
        {
          "name": "三養薯仔拉麵 5 X 120GM",
          "price": "$36",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230209/4660d76c-1f33-43bd-b9f1-726c0509d768",
          "product_eng_name": "Samyang Potato Ramen 5 X 120GM"
        }
      ],
      "name": "三養薯仔拉麵 5 X 120GM",
      "price": "$36",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230209/4660d76c-1f33-43bd-b9f1-726c0509d768",
      "product_eng_name": "Samyang Potato Ramen 5 X 120GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%8F%96%E4%BF%9D%E4%B9%83%E7%B3%BB%E9%AB%98%E7%B4%9A%E7%B4%A0%E9%BA%B5%20300GM/i/101322677.html",
      "uid": "b7c2bbf5ff477e470b0dc51953a12871",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "揖保乃系高級素麵 300GM",
          "price": "$58",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240529/8bd01073-d2b4-34dd-b297-863cc28e3e2a",
          "product_eng_name": "IBONOITO IBONOITO SOMEN 300GM"
        },
        {
          "name": "揖保乃系高級素麵 300GM",
          "price": "$58",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240529/8bd01073-d2b4-34dd-b297-863cc28e3e2a",
          "product_eng_name": "IBONOITO IBONOITO SOMEN 300GM"
        }
      ],
      "name": "揖保乃系高級素麵 300GM",
      "price": "$58",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240529/8bd01073-d2b4-34dd-b297-863cc28e3e2a",
      "product_eng_name": "IBONOITO IBONOITO SOMEN 300GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%A6%8F%E5%AD%97%E5%86%AC%E8%94%AD%E5%8A%9F%E7%B1%B3%E7%B2%89%205%20X%2060GM/i/101578494.html",
      "uid": "b08765fdebf3e693a97bb2556645d79c",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "福字冬蔭功米粉 5 X 60GM",
          "price": "$16",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210920/6d64d9af-d808-40ba-b392-2068b025284c",
          "product_eng_name": "Fuku Tom Yum Mifun 5 X 60GM"
        },
        {
          "name": "福字冬蔭功米粉 5 X 60GM",
          "price": "$16",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210920/6d64d9af-d808-40ba-b392-2068b025284c",
          "product_eng_name": "Fuku Tom Yum Mifun 5 X 60GM"
        }
      ],
      "name": "福字冬蔭功米粉 5 X 60GM",
      "price": "$16",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210920/6d64d9af-d808-40ba-b392-2068b025284c",
      "product_eng_name": "Fuku Tom Yum Mifun 5 X 60GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E6%97%A5%E6%B8%85%E5%90%88%E5%91%B3%E9%81%93%20%E9%AE%AE%E8%9D%A6%E6%9D%AF%E9%BA%B5%2075GM/i/101363778.html",
      "uid": "d400c51307720bfc4dd5be3b72b95b76",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱日清合味道 鮮蝦杯麵 75GM",
          "price": "$170",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230202/d5585acb-169e-4319-b4a8-f85a71803157",
          "product_eng_name": "Nissin Prawn Cup Noodle Case 24 x 75GM"
        },
        {
          "name": "原箱日清合味道 鮮蝦杯麵 75GM",
          "price": "$170",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230202/d5585acb-169e-4319-b4a8-f85a71803157",
          "product_eng_name": "(無法擷取英文名稱)"
        }
      ],
      "name": "原箱日清合味道 鮮蝦杯麵 75GM",
      "price": "$170",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230202/d5585acb-169e-4319-b4a8-f85a71803157",
      "product_eng_name": "(無法擷取英文名稱)"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E5%A3%BD%E6%A1%83%20%E4%B8%8A%E6%B5%B7%E9%BA%B524%20X%20340%20GM/i/101335811.html",
      "uid": "c526966cc6577ebbd7f449fdb256259b",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱壽桃 上海麵24 X 340 GM",
          "price": "$228",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231221/80e60370-0f24-38cf-929e-40dcd8d19026",
          "product_eng_name": "Sau Tao Shanghai Noodle Case 24 X 340 GM"
        },
        {
          "name": "原箱壽桃 上海麵24 X 340 GM",
          "price": "$228",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231221/80e60370-0f24-38cf-929e-40dcd8d19026",
          "product_eng_name": "Sau Tao Shanghai Noodle Case 24 X 340 GM"
        }
      ],
      "name": "原箱壽桃 上海麵24 X 340 GM",
      "price": "$228",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20231221/80e60370-0f24-38cf-929e-40dcd8d19026",
      "product_eng_name": "Sau Tao Shanghai Noodle Case 24 X 340 GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%8D%85%E7%90%83%E5%98%9C%E5%88%9D%E6%90%BE%E6%A9%84%E6%AC%96%E8%91%B5%E8%8A%B1%E7%B1%BD%E6%B2%B9%203%20X%20900ML/i/101370128.html",
      "uid": "3891224df2df3a542235b12abc7c2de7",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "獅球嘜初搾橄欖葵花籽油 3 X 900ML",
          "price": "$129",
          "offer": "【買1件送1件贈品】購買每1件，即送1件人氣贈品；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230726/a070bca4-f40d-4771-927a-9c6f53847dd9",
          "product_eng_name": "Lion & Globe Extra Virgin Olive & Sunflower Oil 3 X 900ML"
        },
        {
          "name": "獅球嘜初搾橄欖葵花籽油 3 X 900ML",
          "price": "$129",
          "offer": "【買1件送1件贈品】購買每1件，即送1件人氣贈品；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230726/a070bca4-f40d-4771-927a-9c6f53847dd9",
          "product_eng_name": "Lion & Globe Extra Virgin Olive & Sunflower Oil 3 X 900ML"
        }
      ],
      "name": "獅球嘜初搾橄欖葵花籽油 3 X 900ML",
      "price": "$129",
      "offer": "【買1件送1件贈品】購買每1件，即送1件人氣贈品；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230726/a070bca4-f40d-4771-927a-9c6f53847dd9",
      "product_eng_name": "Lion & Globe Extra Virgin Olive & Sunflower Oil 3 X 900ML"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%97%A5%E6%B8%85%E5%90%88%E5%91%B3%E9%81%93%20%E5%A4%A7%E6%9D%AF%E4%BA%94%E9%A6%99%E7%89%9B%E8%82%89%E5%91%B3%20100%20GM/i/101379297.html",
      "uid": "6805376bdf7667d67b62765bd9d8b65c",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "日清合味道 大杯五香牛肉味 100 GM",
          "price": "$11",
          "offer": "【2件$18】$18任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240823/f874fe72-2688-3cab-a1d1-d7dc107e204d",
          "product_eng_name": "Nissin Big Cup Beef Noodles 100GM"
        },
        {
          "name": "日清合味道 大杯五香牛肉味 100 GM",
          "price": "$11",
          "offer": "【2件$18】$18任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240823/f874fe72-2688-3cab-a1d1-d7dc107e204d",
          "product_eng_name": "Nissin Big Cup Beef Noodles 100GM"
        }
      ],
      "name": "日清合味道 大杯五香牛肉味 100 GM",
      "price": "$11",
      "offer": "【2件$18】$18任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240823/f874fe72-2688-3cab-a1d1-d7dc107e204d",
      "product_eng_name": "Nissin Big Cup Beef Noodles 100GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%AD%A3%E5%AE%97%E6%88%90%E9%83%BD%E9%85%B8%E8%BE%A3%E7%B2%89%E5%B9%BC%E8%96%AF%E7%B2%89%20108GM/i/101346890.html",
      "uid": "0f7d07672c2df77b3a5896cc5f878f59",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "正宗成都酸辣粉幼薯粉 108GM",
          "price": "$19",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240226/e57452fb-6d68-38df-94c9-d65a88294c42",
          "product_eng_name": "Chengdu Style Hot & Sour Vermicelli Como Pack 108GM"
        },
        {
          "name": "正宗成都酸辣粉幼薯粉 108GM",
          "price": "$19",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240226/e57452fb-6d68-38df-94c9-d65a88294c42",
          "product_eng_name": "Chengdu Style Hot & Sour Vermicelli Como Pack 108GM"
        }
      ],
      "name": "正宗成都酸辣粉幼薯粉 108GM",
      "price": "$19",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240226/e57452fb-6d68-38df-94c9-d65a88294c42",
      "product_eng_name": "Chengdu Style Hot & Sour Vermicelli Como Pack 108GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%8D%85%E7%90%83%E5%98%9C%E8%8A%A5%E8%8A%B1%E7%B1%BD%E6%B2%B9%203%20X%20900ML/i/101340728.html",
      "uid": "dcbf322381a98afc9034a001c83a74ea",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "獅球嘜芥花籽油 3 X 900ML",
          "price": "$75",
          "offer": "【買1件送1件贈品】購買每1件，即送1件人氣贈品；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20241227/2e083f34-3e45-3d8f-bc6d-486e385179b9",
          "product_eng_name": "Lion & Globe Canola Oil 3 X 900ML"
        },
        {
          "name": "獅球嘜芥花籽油 3 X 900ML",
          "price": "$75",
          "offer": "【買1件送1件贈品】購買每1件，即送1件人氣贈品；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20241227/2e083f34-3e45-3d8f-bc6d-486e385179b9",
          "product_eng_name": "Lion & Globe Canola Oil 3 X 900ML"
        }
      ],
      "name": "獅球嘜芥花籽油 3 X 900ML",
      "price": "$75",
      "offer": "【買1件送1件贈品】購買每1件，即送1件人氣贈品；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20241227/2e083f34-3e45-3d8f-bc6d-486e385179b9",
      "product_eng_name": "Lion & Globe Canola Oil 3 X 900ML"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%97%A5%E6%B8%85%E5%90%88%E5%91%B3%E9%81%93%E5%A4%A7%E6%9D%AF%E8%B1%AC%E9%AA%A8%E6%BF%83%E6%B9%AF%E5%91%B3%E5%8D%B3%E9%A3%9F%E9%BA%B5%20107GM/i/101857784.html",
      "uid": "f265c8241d7b96ac703c89d035dc781d",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "日清合味道大杯豬骨濃湯味即食麵 107GM",
          "price": "$11",
          "offer": "【2件$18】$18任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240711/1dd7aceb-bfa6-30b4-b17f-3325fce56acb",
          "product_eng_name": "Nissin Big Cup Tonkotsu Noodles 107GM"
        },
        {
          "name": "日清合味道大杯豬骨濃湯味即食麵 107GM",
          "price": "$11",
          "offer": "【2件$18】$18任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240711/1dd7aceb-bfa6-30b4-b17f-3325fce56acb",
          "product_eng_name": "Nissin Big Cup Tonkotsu Noodles 107GM"
        }
      ],
      "name": "日清合味道大杯豬骨濃湯味即食麵 107GM",
      "price": "$11",
      "offer": "【2件$18】$18任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240711/1dd7aceb-bfa6-30b4-b17f-3325fce56acb",
      "product_eng_name": "Nissin Big Cup Tonkotsu Noodles 107GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%97%A5%E6%B8%85%E5%87%BA%E5%89%8D%E4%B8%80%E4%B8%81%E9%9B%9E%E8%93%89%E5%8D%B3%E9%A3%9F%E9%BA%B5%20100GM/i/101322565.html",
      "uid": "d19abc4a3f7ac85b87dc225e9ef48eba",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "日清出前一丁雞蓉即食麵 100GM",
          "price": "$5",
          "offer": "【8件$28.5】$28.5任揀8件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250407/360f028b-0fe6-3047-831e-0326cea496f3",
          "product_eng_name": "Nissin Demae Iccho Chicken Instant Noodle 100GM"
        },
        {
          "name": "日清出前一丁雞蓉即食麵 100GM",
          "price": "$5",
          "offer": "【8件$28.5】$28.5任揀8件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250407/360f028b-0fe6-3047-831e-0326cea496f3",
          "product_eng_name": "Nissin Demae Iccho Chicken Instant Noodle 100GM"
        }
      ],
      "name": "日清出前一丁雞蓉即食麵 100GM",
      "price": "$5",
      "offer": "【8件$28.5】$28.5任揀8件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250407/360f028b-0fe6-3047-831e-0326cea496f3",
      "product_eng_name": "Nissin Demae Iccho Chicken Instant Noodle 100GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E8%BE%B2%E5%BF%83%E8%BE%A3%E7%99%BD%E8%8F%9C%E8%8A%9D%E5%A3%AB%E5%A4%A7%E7%A2%97%E9%BA%B5%20117GM/i/102108946.html",
      "uid": "fbcb9d26235e033c59eb5d9128ca8433",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "農心辣白菜芝士大碗麵 117GM",
          "price": "$11",
          "offer": "【2件$12】$12任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220615/d5282b88-ae01-469b-9095-4ae6adc42bf6",
          "product_eng_name": "Nong Shim Kimchi Cheese Big Bowl Noodles 117GM"
        },
        {
          "name": "農心辣白菜芝士大碗麵 117GM",
          "price": "$11",
          "offer": "【2件$12】$12任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220615/d5282b88-ae01-469b-9095-4ae6adc42bf6",
          "product_eng_name": "Nong Shim Kimchi Cheese Big Bowl Noodles 117GM"
        }
      ],
      "name": "農心辣白菜芝士大碗麵 117GM",
      "price": "$11",
      "offer": "【2件$12】$12任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20220615/d5282b88-ae01-469b-9095-4ae6adc42bf6",
      "product_eng_name": "Nong Shim Kimchi Cheese Big Bowl Noodles 117GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%99%BE%E5%BE%97%E9%98%BF%E5%A7%A8%E8%9D%B4%E8%9D%B6%E5%BD%A2%E9%80%9A%E7%B2%89%20500GM/i/101343451.html",
      "uid": "f83215c24f9ebaff48cc8da2b26e8fba",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "百得阿姨蝴蝶形通粉 500GM",
          "price": "$23",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240916/0d1d52e4-8ecd-3658-ac28-7a6cfd640a80",
          "product_eng_name": "Barilla Farfalle 500GM"
        },
        {
          "name": "百得阿姨蝴蝶形通粉 500GM",
          "price": "$23",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240916/0d1d52e4-8ecd-3658-ac28-7a6cfd640a80",
          "product_eng_name": "Barilla Farfalle 500GM"
        }
      ],
      "name": "百得阿姨蝴蝶形通粉 500GM",
      "price": "$23",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240916/0d1d52e4-8ecd-3658-ac28-7a6cfd640a80",
      "product_eng_name": "Barilla Farfalle 500GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/Meadows%E6%B8%85%E6%B7%A1%E6%A9%84%E6%AC%96%E6%B2%B9%20500ML/i/101837286.html",
      "uid": "f98aa6ed74e0d785fd96ba6448847cbb",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "Meadows清淡橄欖油 500ML",
          "price": "$82",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231204/a18db26f-86fa-394d-803e-110a5af13e7a",
          "product_eng_name": "Meadows Extra Light Olive Oil 500ML"
        },
        {
          "name": "Meadows清淡橄欖油 500ML",
          "price": "$82",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231204/a18db26f-86fa-394d-803e-110a5af13e7a",
          "product_eng_name": "Meadows Extra Light Olive Oil 500ML"
        }
      ],
      "name": "Meadows清淡橄欖油 500ML",
      "price": "$82",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20231204/a18db26f-86fa-394d-803e-110a5af13e7a",
      "product_eng_name": "Meadows Extra Light Olive Oil 500ML"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%A3%BD%E6%A1%83qq%E9%AE%91%E9%AD%9A%E9%9B%9E%E6%B9%AF%E7%A2%97%E8%A3%9D%E7%B2%89%E7%B5%B2%2072GM/i/101340596.html",
      "uid": "4c88e21ffa1079be722b575aa470b3b0",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "壽桃qq鮑魚雞湯碗裝粉絲 72GM",
          "price": "$6",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220505/856f641a-17b9-4c75-a518-25299351eab0",
          "product_eng_name": "Sau Tao QQ Abalone & Chicken Bowl Vermicelli 72GM"
        },
        {
          "name": "壽桃qq鮑魚雞湯碗裝粉絲 72GM",
          "price": "$6",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220505/856f641a-17b9-4c75-a518-25299351eab0",
          "product_eng_name": "Sau Tao QQ Abalone & Chicken Bowl Vermicelli 72GM"
        }
      ],
      "name": "壽桃qq鮑魚雞湯碗裝粉絲 72GM",
      "price": "$6",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20220505/856f641a-17b9-4c75-a518-25299351eab0",
      "product_eng_name": "Sau Tao QQ Abalone & Chicken Bowl Vermicelli 72GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/Chew%20Chew%E6%84%8F%E5%A4%A7%E5%88%A9%E7%B2%89%201PC/i/101342790.html",
      "uid": "d8a2acadd8f1377c368ad750b414f4b2",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "Chew Chew意大利粉 1PC",
          "price": "$17",
          "offer": "【2件$28】$28任揀2件；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210429/948be3db-6623-4a16-9b2b-178e79e0c7c4",
          "product_eng_name": "Chew Chew Spaghetti 1PC"
        },
        {
          "name": "Chew Chew意大利粉 1PC",
          "price": "$17",
          "offer": "【2件$28】$28任揀2件；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210429/948be3db-6623-4a16-9b2b-178e79e0c7c4",
          "product_eng_name": "Chew Chew Spaghetti 1PC"
        }
      ],
      "name": "Chew Chew意大利粉 1PC",
      "price": "$17",
      "offer": "【2件$28】$28任揀2件；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210429/948be3db-6623-4a16-9b2b-178e79e0c7c4",
      "product_eng_name": "Chew Chew Spaghetti 1PC"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/Pureland%20%E6%9C%89%E6%A9%9F%E5%81%A5%E5%BA%B7%E4%B8%89%E8%89%B2%E7%B1%B3%201KG/i/113316803.html",
      "uid": "2021774092663f3f181b4955280f61fb",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "Pureland 有機健康三色米 1KG",
          "price": "$50",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230330/0f4f9979-f720-4954-8399-c29d8ea63c4a",
          "product_eng_name": "Pureland Organic Whole In One 1KG"
        }
      ],
      "name": "Pureland 有機健康三色米 1KG",
      "price": "$50",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230330/0f4f9979-f720-4954-8399-c29d8ea63c4a",
      "product_eng_name": "Pureland Organic Whole In One 1KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E9%87%91%E8%B1%A1%E7%89%8C%E9%A0%82%E4%B8%8A%E8%8C%89%E8%8E%89%E9%A6%99%E7%B1%B3%2015KG/i/101342765.html",
      "uid": "353cf1933b56b39e5ce96abccebb8023",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "金象牌頂上茉莉香米 15KG",
          "price": "$195",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250407/7608f121-0314-38ea-878b-0fbb87ad71b6",
          "product_eng_name": "Golden Elephant Premium Jasmine Rice 15KG"
        }
      ],
      "name": "金象牌頂上茉莉香米 15KG",
      "price": "$195",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250407/7608f121-0314-38ea-878b-0fbb87ad71b6",
      "product_eng_name": "Golden Elephant Premium Jasmine Rice 15KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%BE%A1%E5%93%81%E7%9A%87%20%E7%B4%85%E6%B2%B9%E9%A6%99%E8%BE%A3%E6%8B%8C%E9%BA%B5%2098GM/i/113463989.html",
      "uid": "afd4ed2652127d9afa7e7079fcd8241d",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "御品皇 紅油香辣拌麵 98GM",
          "price": "$4",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240925/6df9b987-c2a7-3401-a591-dc5f5c4dba4a",
          "product_eng_name": "Yu Pin King Chili Oil Dry-Stirred Noodles 98GM"
        },
        {
          "name": "御品皇 紅油香辣拌麵 98GM",
          "price": "$4",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240925/6df9b987-c2a7-3401-a591-dc5f5c4dba4a",
          "product_eng_name": "Yu Pin King Chili Oil Dry-Stirred Noodles 98GM"
        }
      ],
      "name": "御品皇 紅油香辣拌麵 98GM",
      "price": "$4",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240925/6df9b987-c2a7-3401-a591-dc5f5c4dba4a",
      "product_eng_name": "Yu Pin King Chili Oil Dry-Stirred Noodles 98GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%8D%85%E7%90%83%E5%98%9C%E7%B4%94%E6%AD%A3%E6%A9%84%E6%AC%96%E6%B2%B9%201LT/i/101355911.html",
      "uid": "eea34c381646b670168e6449cb443f84",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "獅球嘜純正橄欖油 1LT",
          "price": "$109",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230324/6b85241d-f568-4f25-87d7-73bf51ecdf29",
          "product_eng_name": "Lion & Globe Pure Olive Oil 1LT"
        },
        {
          "name": "獅球嘜純正橄欖油 1LT",
          "price": "$109",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230324/6b85241d-f568-4f25-87d7-73bf51ecdf29",
          "product_eng_name": "Lion & Globe Pure Olive Oil 1LT"
        }
      ],
      "name": "獅球嘜純正橄欖油 1LT",
      "price": "$109",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230324/6b85241d-f568-4f25-87d7-73bf51ecdf29",
      "product_eng_name": "Lion & Globe Pure Olive Oil 1LT"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%97%A5%E6%B8%85%E5%87%BA%E5%89%8D%E4%B8%80%E4%B8%81%E8%B1%AC%E9%AA%A8%E6%BF%83%E6%B9%AF%E9%BA%B5%205%20X%20100GM%20(%E6%AC%BE%E5%BC%8F%E9%9A%A8%E6%A9%9F%E7%99%BC%E8%B2%A8)/i/101353643.html",
      "uid": "b2ae63d5370fb57d3d5bbdd1fc4aafb0",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "日清出前一丁豬骨濃湯麵 5 X 100GM (款式隨機發貨)",
          "price": "$20",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20241101/356f127e-4648-3b1a-bf66-6b646ff39447",
          "product_eng_name": "Nissin Demae Iccho Tonkotsu Noodles 5 X 100GM (random Package Delivery)"
        },
        {
          "name": "日清出前一丁豬骨濃湯麵 5 X 100GM (款式隨機發貨)",
          "price": "$20",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20241101/356f127e-4648-3b1a-bf66-6b646ff39447",
          "product_eng_name": "Nissin Demae Iccho Tonkotsu Noodles 5 X 100GM (random Package Delivery)"
        }
      ],
      "name": "日清出前一丁豬骨濃湯麵 5 X 100GM (款式隨機發貨)",
      "price": "$20",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20241101/356f127e-4648-3b1a-bf66-6b646ff39447",
      "product_eng_name": "Nissin Demae Iccho Tonkotsu Noodles 5 X 100GM (random Package Delivery)"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%99%BD%E8%B1%A1%20%E8%B6%85%E5%A4%A7%E6%A1%B6%20%E7%B4%85%E7%87%92%E7%89%9B%E8%82%89%E9%BA%B5%20%E7%A2%97%E9%BA%B5%20144GM/i/101344890.html",
      "uid": "1d54f5879529ae14b09a2623c44a24cf",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "白象 超大桶 紅燒牛肉麵 碗麵 144GM",
          "price": "$8",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250307/c8f0712e-bf35-363e-9973-4957586e2d9d",
          "product_eng_name": "Baixiang Braised Beef Big Bowl Ndl 144G"
        },
        {
          "name": "白象 超大桶 紅燒牛肉麵 碗麵 144GM",
          "price": "$8",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250307/c8f0712e-bf35-363e-9973-4957586e2d9d",
          "product_eng_name": "Baixiang Braised Beef Big Bowl Ndl 144G"
        }
      ],
      "name": "白象 超大桶 紅燒牛肉麵 碗麵 144GM",
      "price": "$8",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250307/c8f0712e-bf35-363e-9973-4957586e2d9d",
      "product_eng_name": "Baixiang Braised Beef Big Bowl Ndl 144G"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E5%87%BA%E5%89%8D%E4%B8%80%E4%B8%81%20%E9%BB%91%E8%92%9C%E6%B2%B9%E8%B1%AC%E9%AA%A8%E6%B9%AF%E7%A2%97%E9%BA%B5%20105%20GM/i/113559414.html",
      "uid": "30d3f341597e7a0a2a94d2c0da33aee6",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱出前一丁 黑蒜油豬骨湯碗麵 105 GM",
          "price": "$95",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231013/e2a603c2-f83e-3dc8-8cfe-0394ccff0753",
          "product_eng_name": "Nissin Demae Iccho Black Garlic Oil Tonkotsu Bowl Noodle Case 12 x 105GM"
        },
        {
          "name": "原箱出前一丁 黑蒜油豬骨湯碗麵 105 GM",
          "price": "$95",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231013/e2a603c2-f83e-3dc8-8cfe-0394ccff0753",
          "product_eng_name": "Nissin Demae Iccho Black Garlic Oil Tonkotsu Bowl Noodle Case 12 x 105GM"
        }
      ],
      "name": "原箱出前一丁 黑蒜油豬骨湯碗麵 105 GM",
      "price": "$95",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20231013/e2a603c2-f83e-3dc8-8cfe-0394ccff0753",
      "product_eng_name": "Nissin Demae Iccho Black Garlic Oil Tonkotsu Bowl Noodle Case 12 x 105GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E8%BE%B2%E5%BF%83%E7%89%B9%E8%BE%A3%E5%A4%A7%E7%A2%97%E9%BA%B5%20114GM/i/101350444.html",
      "uid": "615165e6f2b15495fce1d844087461ef",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "農心特辣大碗麵 114GM",
          "price": "$9",
          "offer": "【2件$12】$12任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220614/6b6adec6-9c14-4b51-a0e2-6d19d32f7d8b",
          "product_eng_name": "Nong Shim Shin Bowl Noodle 114GM"
        },
        {
          "name": "農心特辣大碗麵 114GM",
          "price": "$9",
          "offer": "【2件$12】$12任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220614/6b6adec6-9c14-4b51-a0e2-6d19d32f7d8b",
          "product_eng_name": "Nong Shim Shin Bowl Noodle 114GM"
        }
      ],
      "name": "農心特辣大碗麵 114GM",
      "price": "$9",
      "offer": "【2件$12】$12任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20220614/6b6adec6-9c14-4b51-a0e2-6d19d32f7d8b",
      "product_eng_name": "Nong Shim Shin Bowl Noodle 114GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%97%A5%E6%B8%85%E5%87%BA%E5%89%8D%E4%B8%80%E4%B8%81%E9%BA%BB%E6%B2%B9%E6%9D%AF%E9%BA%B5%2070GM/i/101323400.html",
      "uid": "3bf9b451a0fcf7435ac64e40b873fce8",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "日清出前一丁麻油杯麵 70GM",
          "price": "$8",
          "offer": "【2件$14.5】$14.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250327/06186b46-4290-355f-b6bc-7e9226c0c06d",
          "product_eng_name": "Nissin Demae Iccho Sesame Oil Cup Noodles 70GM"
        },
        {
          "name": "日清出前一丁麻油杯麵 70GM",
          "price": "$8",
          "offer": "【2件$14.5】$14.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250327/06186b46-4290-355f-b6bc-7e9226c0c06d",
          "product_eng_name": "Nissin Demae Iccho Sesame Oil Cup Noodles 70GM"
        }
      ],
      "name": "日清出前一丁麻油杯麵 70GM",
      "price": "$8",
      "offer": "【2件$14.5】$14.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250327/06186b46-4290-355f-b6bc-7e9226c0c06d",
      "product_eng_name": "Nissin Demae Iccho Sesame Oil Cup Noodles 70GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%97%A5%E6%B8%85%E5%87%BA%E5%89%8D%E4%B8%80%E4%B8%81%E5%8C%97%E6%B5%B7%E9%81%93%E5%B0%8F%E9%BA%A5%E7%B2%89%E8%B1%AC%E9%AA%A8%E6%B9%AF%E9%BA%B5%205%20X%20100GM/i/101843861.html",
      "uid": "64a880e18ebba90643d2f19c0319a424",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "日清出前一丁北海道小麥粉豬骨湯麵 5 X 100GM",
          "price": "$21",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240920/46139c4f-067c-392a-8458-446bef8d4e38",
          "product_eng_name": "Nissin Demae Iccho Hokkaido Wheat Flour Tonkotsu Flavour 5 X 100GM"
        },
        {
          "name": "日清出前一丁北海道小麥粉豬骨湯麵 5 X 100GM",
          "price": "$21",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240920/46139c4f-067c-392a-8458-446bef8d4e38",
          "product_eng_name": "Nissin Demae Iccho Hokkaido Wheat Flour Tonkotsu Flavour 5 X 100GM"
        }
      ],
      "name": "日清出前一丁北海道小麥粉豬骨湯麵 5 X 100GM",
      "price": "$21",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240920/46139c4f-067c-392a-8458-446bef8d4e38",
      "product_eng_name": "Nissin Demae Iccho Hokkaido Wheat Flour Tonkotsu Flavour 5 X 100GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%9D%8E%E9%8C%A6%E8%A8%98%E6%B2%99%E7%88%B9%E6%B9%AF%E9%BA%B5%20156GM/i/102970306.html",
      "uid": "74b1f1bc576f0924d600be31a6c2882a",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "李錦記沙爹湯麵 156GM",
          "price": "$8",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20241227/6a4260f2-ea7c-35b0-814d-75b6f4a01300",
          "product_eng_name": "Lee Kum Kee Noodle In Satay Soup 156GM"
        },
        {
          "name": "李錦記沙爹湯麵 156GM",
          "price": "$8",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20241227/6a4260f2-ea7c-35b0-814d-75b6f4a01300",
          "product_eng_name": "Lee Kum Kee Noodle In Satay Soup 156GM"
        }
      ],
      "name": "李錦記沙爹湯麵 156GM",
      "price": "$8",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20241227/6a4260f2-ea7c-35b0-814d-75b6f4a01300",
      "product_eng_name": "Lee Kum Kee Noodle In Satay Soup 156GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/Meadows%E6%A9%84%E6%AC%96%E6%B2%B9%201LT/i/101837276.html",
      "uid": "0670fd6cd89cd1293550629eb44c6970",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "Meadows橄欖油 1LT",
          "price": "$132",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231204/2193d1d6-5359-3651-a9c4-fd7d2b747fc3",
          "product_eng_name": "Meadows Olive Oil 1LT"
        },
        {
          "name": "Meadows橄欖油 1LT",
          "price": "$132",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231204/2193d1d6-5359-3651-a9c4-fd7d2b747fc3",
          "product_eng_name": "Meadows Olive Oil 1LT"
        }
      ],
      "name": "Meadows橄欖油 1LT",
      "price": "$132",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20231204/2193d1d6-5359-3651-a9c4-fd7d2b747fc3",
      "product_eng_name": "Meadows Olive Oil 1LT"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%88%80%E5%98%9C%E8%87%BB%E5%93%81%E5%81%A5%E5%BA%B7%E6%B2%B9%E9%85%B8%E6%BF%83%E9%A6%99%E8%8A%B1%E7%94%9F%E6%B2%B95%E5%8D%87/i/101329687.html",
      "uid": "83a2bd65eab05a05c0a69e88c10c7911",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "刀嘜臻品健康油酸濃香花生油5升",
          "price": "$199",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240813/c6616c81-007c-39c8-ae0f-e2157e0010b3",
          "product_eng_name": "Knife Deluxe High Oleic Formula Peanut Oil 5L"
        },
        {
          "name": "刀嘜臻品健康油酸濃香花生油5升",
          "price": "$199",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240813/c6616c81-007c-39c8-ae0f-e2157e0010b3",
          "product_eng_name": "Knife Deluxe High Oleic Formula Peanut Oil 5L"
        }
      ],
      "name": "刀嘜臻品健康油酸濃香花生油5升",
      "price": "$199",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240813/c6616c81-007c-39c8-ae0f-e2157e0010b3",
      "product_eng_name": "Knife Deluxe High Oleic Formula Peanut Oil 5L"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%97%A5%E6%B8%85%E5%90%88%E5%91%B3%E9%81%93%E5%92%96%E5%96%B1%E6%B5%B7%E9%AE%AE%E6%9D%AF%E9%BA%B5%2075GM/i/101339842.html",
      "uid": "f81e8c2118d45dfde5d8b4354f376b73",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "日清合味道咖喱海鮮杯麵 75GM",
          "price": "$8",
          "offer": "【2件$14.5】$14.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250327/4e2e0a33-2e48-3bd4-83b6-1267e1d792d0",
          "product_eng_name": "Nissin Curry Seafood Cup Noodle 75GM"
        },
        {
          "name": "日清合味道咖喱海鮮杯麵 75GM",
          "price": "$8",
          "offer": "【2件$14.5】$14.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250327/4e2e0a33-2e48-3bd4-83b6-1267e1d792d0",
          "product_eng_name": "Nissin Curry Seafood Cup Noodle 75GM"
        }
      ],
      "name": "日清合味道咖喱海鮮杯麵 75GM",
      "price": "$8",
      "offer": "【2件$14.5】$14.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250327/4e2e0a33-2e48-3bd4-83b6-1267e1d792d0",
      "product_eng_name": "Nissin Curry Seafood Cup Noodle 75GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E4%BF%9D%E5%BE%97%20%E8%91%B5%E8%8A%B1%E7%B1%BD%E6%B2%B9%203%20LT/i/113735606.html",
      "uid": "c85d65bdc0325a93a171394a980de716",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "保得 葵花籽油 3 LT",
          "price": "$119",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240312/312dd898-70c3-3552-afff-265dd4240f8e",
          "product_eng_name": "Bontaste Sunflower Seed Oil 3LT"
        },
        {
          "name": "保得 葵花籽油 3 LT",
          "price": "$119",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240312/312dd898-70c3-3552-afff-265dd4240f8e",
          "product_eng_name": "Bontaste Sunflower Seed Oil 3LT"
        }
      ],
      "name": "保得 葵花籽油 3 LT",
      "price": "$119",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240312/312dd898-70c3-3552-afff-265dd4240f8e",
      "product_eng_name": "Bontaste Sunflower Seed Oil 3LT"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%A3%BD%E6%A1%83%E7%89%8C%E6%97%A5%E5%BC%8F%E7%83%8F%E5%86%AC%E9%BA%B5%204%20X%20200GM/i/101353333.html",
      "uid": "97e1ebd4beaa8665d3e287729a5aca77",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "壽桃牌日式烏冬麵 4 X 200GM",
          "price": "$10",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220505/3c36f5da-9263-405a-bbc7-e2cab71ef938",
          "product_eng_name": "Sau Tao Japanese Udon 4 X 200GM"
        },
        {
          "name": "壽桃牌日式烏冬麵 4 X 200GM",
          "price": "$10",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220505/3c36f5da-9263-405a-bbc7-e2cab71ef938",
          "product_eng_name": "Sau Tao Japanese Udon 4 X 200GM"
        }
      ],
      "name": "壽桃牌日式烏冬麵 4 X 200GM",
      "price": "$10",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20220505/3c36f5da-9263-405a-bbc7-e2cab71ef938",
      "product_eng_name": "Sau Tao Japanese Udon 4 X 200GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E8%81%96%E8%B3%A2%E6%AF%8D%E7%9B%B4%E7%B4%8B%E9%80%9A%E7%B2%89%20500G/i/101349517.html",
      "uid": "df31019702c929f8bbbdcc8b045a18ec",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "聖賢母直紋通粉 500G",
          "price": "$16",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240913/fd24cd4a-9994-3354-aff0-f7cf6cf1dcce",
          "product_eng_name": "San Remo #18 Penne 500G"
        },
        {
          "name": "聖賢母直紋通粉 500G",
          "price": "$16",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240913/fd24cd4a-9994-3354-aff0-f7cf6cf1dcce",
          "product_eng_name": "San Remo #18 Penne 500G"
        }
      ],
      "name": "聖賢母直紋通粉 500G",
      "price": "$16",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240913/fd24cd4a-9994-3354-aff0-f7cf6cf1dcce",
      "product_eng_name": "San Remo #18 Penne 500G"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E6%97%A5%E6%B8%85%E6%98%A5%E9%9B%A8%20%E8%B6%8A%E5%BC%8F%E9%9B%9E%E8%82%89%E7%B2%89%E7%B5%B2%2012%20X%2048GM/i/113465539.html",
      "uid": "eddb5e9581931da802a0183d1c7c0815",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱日清春雨 越式雞肉粉絲 12 X 48GM",
          "price": "$94",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230728/4c6c89c1-bd39-328a-a418-e7802fda08d7",
          "product_eng_name": "Nissin Harusame Chicken Cup Vermicelli Case 12 X 48GM"
        },
        {
          "name": "原箱日清春雨 越式雞肉粉絲 12 X 48GM",
          "price": "$94",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230728/4c6c89c1-bd39-328a-a418-e7802fda08d7",
          "product_eng_name": "Nissin Harusame Chicken Cup Vermicelli Case 12 X 48GM"
        }
      ],
      "name": "原箱日清春雨 越式雞肉粉絲 12 X 48GM",
      "price": "$94",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230728/4c6c89c1-bd39-328a-a418-e7802fda08d7",
      "product_eng_name": "Nissin Harusame Chicken Cup Vermicelli Case 12 X 48GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/Meadows%E8%9E%BA%E7%B5%B2%E7%B2%89%20N16%20500GM/i/101579432.html",
      "uid": "c87fc743f9758d1d6cce5116e82a4ef5",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "Meadows螺絲粉 N16 500GM",
          "price": "$16",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231204/b01a2a0c-1a91-3e11-b47c-5af110ac0daf",
          "product_eng_name": "Meadows Fusilli N16 500GM"
        },
        {
          "name": "Meadows螺絲粉 N16 500GM",
          "price": "$16",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231204/b01a2a0c-1a91-3e11-b47c-5af110ac0daf",
          "product_eng_name": "Meadows Fusilli N16 500GM"
        }
      ],
      "name": "Meadows螺絲粉 N16 500GM",
      "price": "$16",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20231204/b01a2a0c-1a91-3e11-b47c-5af110ac0daf",
      "product_eng_name": "Meadows Fusilli N16 500GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%91%B3%E5%8D%83%E6%8B%89%E9%BA%B55%E4%BA%BA%E4%BB%BD%20500GM/i/113247919.html",
      "uid": "5f8cc25a2365ac737300a18bb9cd7fea",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "味千拉麵5人份 500GM",
          "price": "$19",
          "offer": "【指定分類享$25換購】每買1件，即可以$25換購1件人氣產品；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20221108/5d1be58b-f763-493d-97bb-1a882593d9c3",
          "product_eng_name": "Ajisen Ramen 5 Serving 500GM"
        },
        {
          "name": "味千拉麵5人份 500GM",
          "price": "$19",
          "offer": "【指定分類享$25換購】每買1件，即可以$25換購1件人氣產品；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20221108/5d1be58b-f763-493d-97bb-1a882593d9c3",
          "product_eng_name": "Ajisen Ramen 5 Serving 500GM"
        }
      ],
      "name": "味千拉麵5人份 500GM",
      "price": "$19",
      "offer": "【指定分類享$25換購】每買1件，即可以$25換購1件人氣產品；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20221108/5d1be58b-f763-493d-97bb-1a882593d9c3",
      "product_eng_name": "Ajisen Ramen 5 Serving 500GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/Meadows%E6%A9%84%E6%AC%96%E6%B2%B9%20500ML/i/101837287.html",
      "uid": "f7c98f381217435c5cc5fe492a84230d",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "Meadows橄欖油 500ML",
          "price": "$82",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231204/c4ca783e-2377-3f0d-b14a-c0dd6950846c",
          "product_eng_name": "Meadows Olive Oil 500ML"
        },
        {
          "name": "Meadows橄欖油 500ML",
          "price": "$82",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231204/c4ca783e-2377-3f0d-b14a-c0dd6950846c",
          "product_eng_name": "Meadows Olive Oil 500ML"
        }
      ],
      "name": "Meadows橄欖油 500ML",
      "price": "$82",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20231204/c4ca783e-2377-3f0d-b14a-c0dd6950846c",
      "product_eng_name": "Meadows Olive Oil 500ML"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E8%A2%8B%E9%BC%A0%E7%89%8C%E8%8C%89%E8%8E%89%E9%A6%99%E7%B1%B3%205KG/i/101330024.html",
      "uid": "ddd1b3c6fa47f365a3b9369673f28f1d",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "袋鼠牌茉莉香米 5KG",
          "price": "$65",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210521/b932e42e-ad2d-41d1-b06a-02adce46624c",
          "product_eng_name": "Kangaroo Jasmine Rice 5KG"
        }
      ],
      "name": "袋鼠牌茉莉香米 5KG",
      "price": "$65",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210521/b932e42e-ad2d-41d1-b06a-02adce46624c",
      "product_eng_name": "Kangaroo Jasmine Rice 5KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E4%B8%89%E9%A4%8A%E8%B6%85%E7%B4%9A%E7%89%B9%E8%BE%A3%E9%9B%9E%E8%82%89%E7%82%92%E9%BA%B5%20140GM/i/101357187.html",
      "uid": "4d2023eaaf605cb9d97bba01273be427",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "三養超級特辣雞肉炒麵 140GM",
          "price": "$33",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20200413/70ceb026-f736-4a83-8a78-3d5bde0f7fe4",
          "product_eng_name": "Samyang Hot Chicken Ramen 140GM"
        },
        {
          "name": "三養超級特辣雞肉炒麵 140GM",
          "price": "$33",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20200413/70ceb026-f736-4a83-8a78-3d5bde0f7fe4",
          "product_eng_name": "Samyang Hot Chicken Ramen 140GM"
        }
      ],
      "name": "三養超級特辣雞肉炒麵 140GM",
      "price": "$33",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20200413/70ceb026-f736-4a83-8a78-3d5bde0f7fe4",
      "product_eng_name": "Samyang Hot Chicken Ramen 140GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%99%BE%E7%9B%8A%E8%91%A1%E8%90%84%E7%B1%BD%E6%B2%B9%20750ML/i/101382125.html",
      "uid": "70b082f1054759ab832feb68ac1431e2",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "百益葡萄籽油 750ML",
          "price": "$72",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20241120/80854306-afa9-3048-a6f1-2ff59ba06de7",
          "product_eng_name": "Filippo Berio Grapeseed Oil 750ML"
        },
        {
          "name": "百益葡萄籽油 750ML",
          "price": "$72",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20241120/80854306-afa9-3048-a6f1-2ff59ba06de7",
          "product_eng_name": "Filippo Berio Grapeseed Oil 750ML"
        }
      ],
      "name": "百益葡萄籽油 750ML",
      "price": "$72",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20241120/80854306-afa9-3048-a6f1-2ff59ba06de7",
      "product_eng_name": "Filippo Berio Grapeseed Oil 750ML"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%AE%B6%E6%A8%82%E7%89%8C%E9%9B%9E%E6%B9%AF%E5%91%B3%E5%BF%AB%E7%86%9F%E9%80%9A%E5%BF%83%E7%B2%89%2080GM/i/101356764.html",
      "uid": "761bd67f24679885c3ea7677b7a22614",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "家樂牌雞湯味快熟通心粉 80GM",
          "price": "$7",
          "offer": "【3件$17】$17任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240917/83f919b5-6eba-3dfa-b410-d1d0936eab2c",
          "product_eng_name": "Knorr Chicken Macaroni 80GM"
        },
        {
          "name": "家樂牌雞湯味快熟通心粉 80GM",
          "price": "$7",
          "offer": "【3件$17】$17任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240917/83f919b5-6eba-3dfa-b410-d1d0936eab2c",
          "product_eng_name": "Knorr Chicken Macaroni 80GM"
        }
      ],
      "name": "家樂牌雞湯味快熟通心粉 80GM",
      "price": "$7",
      "offer": "【3件$17】$17任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240917/83f919b5-6eba-3dfa-b410-d1d0936eab2c",
      "product_eng_name": "Knorr Chicken Macaroni 80GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%8D%85%E7%90%83%E5%98%9C%E5%88%9D%E6%90%BE%E7%89%9B%E6%B2%B9%E6%9E%9C%E8%8A%A5%E8%8A%B1%E7%B1%BD%203%20X%20900ML/i/101355272.html",
      "uid": "585a19a978fbfdb829d10b3b59ca50bf",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "獅球嘜初搾牛油果芥花籽 3 X 900ML",
          "price": "$116",
          "offer": "【買1件送1件贈品】購買每1件，即送1件人氣贈品；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20200826/69de901b-6ce3-4a1e-961a-34607c6788e5",
          "product_eng_name": "Lion & Globe Extra Virgin Avocado Oil With Canola Oil 3 X 900ML"
        },
        {
          "name": "獅球嘜初搾牛油果芥花籽 3 X 900ML",
          "price": "$116",
          "offer": "【買1件送1件贈品】購買每1件，即送1件人氣贈品；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20200826/69de901b-6ce3-4a1e-961a-34607c6788e5",
          "product_eng_name": "Lion & Globe Extra Virgin Avocado Oil With Canola Oil 3 X 900ML"
        }
      ],
      "name": "獅球嘜初搾牛油果芥花籽 3 X 900ML",
      "price": "$116",
      "offer": "【買1件送1件贈品】購買每1件，即送1件人氣贈品；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20200826/69de901b-6ce3-4a1e-961a-34607c6788e5",
      "product_eng_name": "Lion & Globe Extra Virgin Avocado Oil With Canola Oil 3 X 900ML"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%88%80%E5%98%9C%20%E9%87%91%E8%A3%9D%E6%BF%83%E9%A6%99%E8%8A%B1%E7%94%9F%E6%B2%B9%204%20X%20900ML/i/101344991.html",
      "uid": "4e30c2f977aee41b2d19bbf995260321",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "刀嘜 金裝濃香花生油 4 X 900ML",
          "price": "$123",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240215/f55182e8-9c33-3add-82c7-f1d2295a4af9",
          "product_eng_name": "Knife Supreme Peanut Oil 4x900ML"
        },
        {
          "name": "刀嘜 金裝濃香花生油 4 X 900ML",
          "price": "$123",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240215/f55182e8-9c33-3add-82c7-f1d2295a4af9",
          "product_eng_name": "Knife Supreme Peanut Oil 4x900ML"
        }
      ],
      "name": "刀嘜 金裝濃香花生油 4 X 900ML",
      "price": "$123",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240215/f55182e8-9c33-3add-82c7-f1d2295a4af9",
      "product_eng_name": "Knife Supreme Peanut Oil 4x900ML"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%84%A1%E9%9B%99%E9%BA%BB%E8%BE%A3%E7%B2%89%E6%9D%AF%E8%A3%9D%20125GM/i/102126386.html",
      "uid": "f830cdf1207dcbd3d6238d5d10cd8df3",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "無雙麻辣粉杯裝 125GM",
          "price": "$16",
          "offer": "【2件$15】$15任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240502/9393bce5-8247-3ea4-9f0d-b2ac2b92e277",
          "product_eng_name": "Muso Sichuan Spicy Sweet Potato Noodles 125GM"
        },
        {
          "name": "無雙麻辣粉杯裝 125GM",
          "price": "$16",
          "offer": "【2件$15】$15任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240502/9393bce5-8247-3ea4-9f0d-b2ac2b92e277",
          "product_eng_name": "Muso Sichuan Spicy Sweet Potato Noodles 125GM"
        }
      ],
      "name": "無雙麻辣粉杯裝 125GM",
      "price": "$16",
      "offer": "【2件$15】$15任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240502/9393bce5-8247-3ea4-9f0d-b2ac2b92e277",
      "product_eng_name": "Muso Sichuan Spicy Sweet Potato Noodles 125GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%A3%BD%E6%A1%83%E6%B2%99%E5%97%B2%E7%89%9B%E8%82%89%E9%BA%B5%20140GM/i/101848033.html",
      "uid": "88e0a0c1570195d7321049fd91f45383",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "壽桃沙嗲牛肉麵 140GM",
          "price": "$6",
          "offer": "【3件$22】$22任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220505/e5dbb41a-1304-41cb-a783-a30d94d51639",
          "product_eng_name": "(無法擷取英文名稱)"
        },
        {
          "name": "壽桃沙嗲牛肉麵 140GM",
          "price": "$6",
          "offer": "【3件$22】$22任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220505/e5dbb41a-1304-41cb-a783-a30d94d51639",
          "product_eng_name": "Sau Tao Satay Beef Noodles 140GM"
        }
      ],
      "name": "壽桃沙嗲牛肉麵 140GM",
      "price": "$6",
      "offer": "【3件$22】$22任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20220505/e5dbb41a-1304-41cb-a783-a30d94d51639",
      "product_eng_name": "Sau Tao Satay Beef Noodles 140GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1DE%20CECCO%20%E6%84%8F%E5%A4%A7%E5%88%A9%E7%B2%89N1224%20X%20500%20GM/i/101335846.html",
      "uid": "8f6ab49a01974682bd804b4f0d990b8c",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱DE CECCO 意大利粉N1224 X 500 GM",
          "price": "$590",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231215/6a474d24-af12-3c04-83a5-223a5defea70",
          "product_eng_name": "De Cecco Spaghetti N12 Case 24 X 500 GM"
        },
        {
          "name": "原箱DE CECCO 意大利粉N1224 X 500 GM",
          "price": "$590",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231215/6a474d24-af12-3c04-83a5-223a5defea70",
          "product_eng_name": "De Cecco Spaghetti N12 Case 24 X 500 GM"
        }
      ],
      "name": "原箱DE CECCO 意大利粉N1224 X 500 GM",
      "price": "$590",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20231215/6a474d24-af12-3c04-83a5-223a5defea70",
      "product_eng_name": "De Cecco Spaghetti N12 Case 24 X 500 GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/Meadows%20Essentials%E6%97%A5%E5%BC%8F%E7%83%8F%E5%86%AC%204%20X%20200GM/i/101845398.html",
      "uid": "7120b5272b093c5e5524729fbaedb9e7",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "Meadows Essentials日式烏冬 4 X 200GM",
          "price": "$6",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220624/fab00050-2724-467b-a6d8-7b9aa5ac7d05",
          "product_eng_name": "Meadows Essentials Japanese Udon 4 X 200GM"
        },
        {
          "name": "Meadows Essentials日式烏冬 4 X 200GM",
          "price": "$6",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220624/fab00050-2724-467b-a6d8-7b9aa5ac7d05",
          "product_eng_name": "Meadows Essentials Japanese Udon 4 X 200GM"
        }
      ],
      "name": "Meadows Essentials日式烏冬 4 X 200GM",
      "price": "$6",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20220624/fab00050-2724-467b-a6d8-7b9aa5ac7d05",
      "product_eng_name": "Meadows Essentials Japanese Udon 4 X 200GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%A4%A7%E5%B8%AB%E5%A7%90%20%E9%A0%82%E7%B4%9A%E7%89%9B%E8%82%9D%E8%8F%8C%E9%BA%B5(%E7%B2%97)%206%E5%80%8B%E8%A3%9D/i/101341760.html",
      "uid": "294efbd8fdb835a6e6e89cd7d8595a7e",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "大師姐 頂級牛肝菌麵(粗) 6個裝",
          "price": "$98",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250122/b52ff229-533f-3abf-9835-49c21a0eeb6d",
          "product_eng_name": "Dashijie Porcini Noodles (Thick)"
        },
        {
          "name": "大師姐 頂級牛肝菌麵(粗) 6個裝",
          "price": "$98",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250122/b52ff229-533f-3abf-9835-49c21a0eeb6d",
          "product_eng_name": "Dashijie Porcini Noodles (Thick)"
        }
      ],
      "name": "大師姐 頂級牛肝菌麵(粗) 6個裝",
      "price": "$98",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250122/b52ff229-533f-3abf-9835-49c21a0eeb6d",
      "product_eng_name": "Dashijie Porcini Noodles (Thick)"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%97%A5%E6%B8%85%E5%90%88%E5%91%B3%E9%81%93%E9%AE%AE%E8%9D%A6%E7%95%AA%E8%8C%84%E6%BF%83%E6%B9%AF%E6%9D%AF%E9%BA%B5%2075GM/i/102912571.html",
      "uid": "255aec8c3cb3ec7b868b20d9b01177e2",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "日清合味道鮮蝦番茄濃湯杯麵 75GM",
          "price": "$8",
          "offer": "【2件$14.5】$14.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250327/95057d77-538f-3c9e-94e9-5c84e4cf57cd",
          "product_eng_name": "Nissin Cup Noodles Shrimp & Tomato 75GM"
        },
        {
          "name": "日清合味道鮮蝦番茄濃湯杯麵 75GM",
          "price": "$8",
          "offer": "【2件$14.5】$14.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250327/95057d77-538f-3c9e-94e9-5c84e4cf57cd",
          "product_eng_name": "Nissin Cup Noodles Shrimp & Tomato 75GM"
        }
      ],
      "name": "日清合味道鮮蝦番茄濃湯杯麵 75GM",
      "price": "$8",
      "offer": "【2件$14.5】$14.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250327/95057d77-538f-3c9e-94e9-5c84e4cf57cd",
      "product_eng_name": "Nissin Cup Noodles Shrimp & Tomato 75GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E8%BE%B2%E5%BF%83%E9%9F%93%E5%9C%8B%E9%BB%91%E7%89%88%E8%BE%9B%E8%BE%A3%E9%BA%B5%20134GM/i/101351524.html",
      "uid": "93da442290513881c1548a3db3774383",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "農心韓國黑版辛辣麵 134GM",
          "price": "$39",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240916/4c717705-5069-3c4a-85ee-3c0d9b9b1ffa",
          "product_eng_name": "Nong Shim Black Spicy Noodles 134GM"
        },
        {
          "name": "農心韓國黑版辛辣麵 134GM",
          "price": "$39",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240916/4c717705-5069-3c4a-85ee-3c0d9b9b1ffa",
          "product_eng_name": "Nong Shim Black Spicy Noodles 134GM"
        }
      ],
      "name": "農心韓國黑版辛辣麵 134GM",
      "price": "$39",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240916/4c717705-5069-3c4a-85ee-3c0d9b9b1ffa",
      "product_eng_name": "Nong Shim Black Spicy Noodles 134GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%8F%A0%E6%B1%9F%E6%A9%8B%E7%89%8C%E6%B1%9F%E9%96%80%E6%8E%92%E7%B2%89%20454GM/i/101336155.html",
      "uid": "023eb12214a9e26688c8f1bb73331fc7",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "珠江橋牌江門排粉 454GM",
          "price": "$10",
          "offer": "【2件$19】$19任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240917/9c65e007-de11-3acf-ac0b-d51d95fdc96e",
          "product_eng_name": "Pearl River Bridge Kong Moon Rice Stick 454GM"
        },
        {
          "name": "珠江橋牌江門排粉 454GM",
          "price": "$10",
          "offer": "【2件$19】$19任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240917/9c65e007-de11-3acf-ac0b-d51d95fdc96e",
          "product_eng_name": "Pearl River Bridge Kong Moon Rice Stick 454GM"
        }
      ],
      "name": "珠江橋牌江門排粉 454GM",
      "price": "$10",
      "offer": "【2件$19】$19任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240917/9c65e007-de11-3acf-ac0b-d51d95fdc96e",
      "product_eng_name": "Pearl River Bridge Kong Moon Rice Stick 454GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%BE%A1%E5%93%81%E7%9A%87%20%E8%94%A5%E6%B2%B9%E6%8B%8C%E9%BA%B5%20103%20GM/i/113463974.html",
      "uid": "3874f3ae84786033a93156f281db8322",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "御品皇 蔥油拌麵 103 GM",
          "price": "$4",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240925/f2924419-5634-30e1-9535-90219037e99f",
          "product_eng_name": "Yu Pin King Scallion Oil Dry-Stirred Noodles 103GM"
        },
        {
          "name": "御品皇 蔥油拌麵 103 GM",
          "price": "$4",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240925/f2924419-5634-30e1-9535-90219037e99f",
          "product_eng_name": "Yu Pin King Scallion Oil Dry-Stirred Noodles 103GM"
        }
      ],
      "name": "御品皇 蔥油拌麵 103 GM",
      "price": "$4",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240925/f2924419-5634-30e1-9535-90219037e99f",
      "product_eng_name": "Yu Pin King Scallion Oil Dry-Stirred Noodles 103GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E4%B8%89%E9%A4%8A%20%E5%A5%B6%E6%B2%B9%E7%8E%AB%E7%91%B0%E8%BE%A3%E9%9B%9E%E6%92%88%E9%BA%B5%20140%20GM/i/114326951.html",
      "uid": "009e82d1cd91e67225b139eef329018d",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "三養 奶油玫瑰辣雞撈麵 140 GM",
          "price": "$39",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240826/47f12c29-6aa4-3eaf-9ae3-cc3423ff86b3",
          "product_eng_name": "Samyang Rosé Buldak Hot Chicken Ramen 5 x 140GM"
        },
        {
          "name": "三養 奶油玫瑰辣雞撈麵 140 GM",
          "price": "$39",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240826/47f12c29-6aa4-3eaf-9ae3-cc3423ff86b3",
          "product_eng_name": "Samyang Rosé Buldak Hot Chicken Ramen 5 x 140GM"
        }
      ],
      "name": "三養 奶油玫瑰辣雞撈麵 140 GM",
      "price": "$39",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240826/47f12c29-6aa4-3eaf-9ae3-cc3423ff86b3",
      "product_eng_name": "Samyang Rosé Buldak Hot Chicken Ramen 5 x 140GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E5%AE%B6%E6%A8%82%E7%89%8C%20%E7%89%9B%E8%82%89%E5%91%B3%E9%80%9A%E5%BF%83%E7%B2%89%2030%20X%2080GM/i/101360281.html",
      "uid": "7816ea24da664e98561c65d83f03acb9",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱家樂牌 牛肉味通心粉 30 X 80GM",
          "price": "$150",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230213/c6886237-60c4-440d-bd8d-3a187ccb4cbf",
          "product_eng_name": "Knorr Beef Macaroni Case 30 X 80GM"
        },
        {
          "name": "原箱家樂牌 牛肉味通心粉 30 X 80GM",
          "price": "$150",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230213/c6886237-60c4-440d-bd8d-3a187ccb4cbf",
          "product_eng_name": "Knorr Beef Macaroni Case 30 X 80GM"
        }
      ],
      "name": "原箱家樂牌 牛肉味通心粉 30 X 80GM",
      "price": "$150",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230213/c6886237-60c4-440d-bd8d-3a187ccb4cbf",
      "product_eng_name": "Knorr Beef Macaroni Case 30 X 80GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E9%BA%B5%E4%B8%80%E5%BA%B5-%E6%97%A5%E6%9C%AC%E8%95%8E%E9%BA%A5%E9%BA%B5%20720GM/i/113339683.html",
      "uid": "4adaa7b66c71d726e25933b4788b23d9",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "麵一庵-日本蕎麥麵 720GM",
          "price": "$27",
          "offer": "【2件$50】$50任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230502/b958c37c-cfca-47ad-9e46-121a7bf06460",
          "product_eng_name": "Inosuke Seimen Inosuke Seimen Japan Soba 720GM"
        },
        {
          "name": "麵一庵-日本蕎麥麵 720GM",
          "price": "$27",
          "offer": "【2件$50】$50任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230502/b958c37c-cfca-47ad-9e46-121a7bf06460",
          "product_eng_name": "Inosuke Seimen Inosuke Seimen Japan Soba 720GM"
        }
      ],
      "name": "麵一庵-日本蕎麥麵 720GM",
      "price": "$27",
      "offer": "【2件$50】$50任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230502/b958c37c-cfca-47ad-9e46-121a7bf06460",
      "product_eng_name": "Inosuke Seimen Inosuke Seimen Japan Soba 720GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%84%A1%E9%9B%99%E9%85%B8%E8%BE%A3%E7%B2%89%20140GM/i/102126381.html",
      "uid": "d2f2268474d7831be7421b660a2f9135",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "無雙酸辣粉 140GM",
          "price": "$16",
          "offer": "【2件$15】$15任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240502/accf946d-7572-3e24-aa8a-06b5e03a6a74",
          "product_eng_name": "Muso Sour & Spicy Sweet Potato Noodles 140GM"
        },
        {
          "name": "無雙酸辣粉 140GM",
          "price": "$16",
          "offer": "【2件$15】$15任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240502/accf946d-7572-3e24-aa8a-06b5e03a6a74",
          "product_eng_name": "Muso Sour & Spicy Sweet Potato Noodles 140GM"
        }
      ],
      "name": "無雙酸辣粉 140GM",
      "price": "$16",
      "offer": "【2件$15】$15任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240502/accf946d-7572-3e24-aa8a-06b5e03a6a74",
      "product_eng_name": "Muso Sour & Spicy Sweet Potato Noodles 140GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%97%A5%E6%B8%85%E5%92%9A%E5%85%B5%E8%A1%9B%E5%A4%A9%E5%A9%A6%E7%BE%85%E6%9D%AF%E7%83%8F%E5%86%AC%20(%E5%8D%B3%E9%A3%9F%E9%BA%B5)/i/101384735.html",
      "uid": "b64618797f3006d5cd89be3dc49e575e",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "日清咚兵衛天婦羅杯烏冬 (即食麵)",
          "price": "$10",
          "offer": "【2件$18】$18任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20241028/fcd43e5a-36c8-347e-a461-2c9d48c127e1",
          "product_eng_name": "(無法擷取英文名稱)"
        },
        {
          "name": "日清咚兵衛天婦羅杯烏冬 (即食麵)",
          "price": "$10",
          "offer": "【2件$18】$18任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20241028/fcd43e5a-36c8-347e-a461-2c9d48c127e1",
          "product_eng_name": "Nissin Donbei Tempura Cup Udon (Instant Noodle)"
        }
      ],
      "name": "日清咚兵衛天婦羅杯烏冬 (即食麵)",
      "price": "$10",
      "offer": "【2件$18】$18任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20241028/fcd43e5a-36c8-347e-a461-2c9d48c127e1",
      "product_eng_name": "Nissin Donbei Tempura Cup Udon (Instant Noodle)"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%B5%B1%E4%B8%80%E6%BB%BF%E6%BC%A2%E5%A4%A7%E9%A4%90%E9%BA%BB%E8%BE%A3%E9%8D%8B%E7%89%9B%E8%82%89%E5%A4%A7%E7%A2%97%E9%BA%B5%20204GM/i/101341788.html",
      "uid": "e6edb274b7c1936bbc86969bf85bacda",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "統一滿漢大餐麻辣鍋牛肉大碗麵 204GM",
          "price": "$32",
          "offer": "【2件$32】$32任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20200414/04ca8a30-82ab-4c48-bb02-7167c550737a",
          "product_eng_name": "Uni President Imperial Big Meal Super Hot Pot Bowl Noodle 204GM"
        },
        {
          "name": "統一滿漢大餐麻辣鍋牛肉大碗麵 204GM",
          "price": "$32",
          "offer": "【2件$32】$32任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20200414/04ca8a30-82ab-4c48-bb02-7167c550737a",
          "product_eng_name": "Uni President Imperial Big Meal Super Hot Pot Bowl Noodle 204GM"
        }
      ],
      "name": "統一滿漢大餐麻辣鍋牛肉大碗麵 204GM",
      "price": "$32",
      "offer": "【2件$32】$32任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20200414/04ca8a30-82ab-4c48-bb02-7167c550737a",
      "product_eng_name": "Uni President Imperial Big Meal Super Hot Pot Bowl Noodle 204GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%97%A5%E6%B8%85%E5%90%88%E5%91%B3%E9%81%93%E5%91%A8%E6%89%93%E8%9C%86%E6%B9%AF%E5%91%B3%E6%9D%AF%E9%BA%B5%2075GM/i/101337695.html",
      "uid": "eb573fadbe094680957e2a725c9fe48f",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "日清合味道周打蜆湯味杯麵 75GM",
          "price": "$8",
          "offer": "【2件$14.5】$14.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250327/632c621d-8334-3044-ae06-be52d07c699d",
          "product_eng_name": "Nissin Cup Noodles Clam Chowder 75GM"
        },
        {
          "name": "日清合味道周打蜆湯味杯麵 75GM",
          "price": "$8",
          "offer": "【2件$14.5】$14.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250327/632c621d-8334-3044-ae06-be52d07c699d",
          "product_eng_name": "Nissin Cup Noodles Clam Chowder 75GM"
        }
      ],
      "name": "日清合味道周打蜆湯味杯麵 75GM",
      "price": "$8",
      "offer": "【2件$14.5】$14.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250327/632c621d-8334-3044-ae06-be52d07c699d",
      "product_eng_name": "Nissin Cup Noodles Clam Chowder 75GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%A3%BD%E6%A1%83%E9%9B%AA%E8%8F%9C%E7%81%AB%E9%B4%A8%E5%B0%8F%E6%A9%8B%E7%B1%B3%E7%B7%9A%204%20X%20215GM/i/101343348.html",
      "uid": "e2f738ae6025ca7a3fb4d7cb67c90acc",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "壽桃雪菜火鴨小橋米線 4 X 215GM",
          "price": "$14",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220505/b85ac391-8185-498c-98b9-2e67e683db82",
          "product_eng_name": "Sau Tao Mustard Green Duck Flavour Rice Vermicelli 4 X 215GM"
        },
        {
          "name": "壽桃雪菜火鴨小橋米線 4 X 215GM",
          "price": "$14",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220505/b85ac391-8185-498c-98b9-2e67e683db82",
          "product_eng_name": "Sau Tao Mustard Green Duck Flavour Rice Vermicelli 4 X 215GM"
        }
      ],
      "name": "壽桃雪菜火鴨小橋米線 4 X 215GM",
      "price": "$14",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20220505/b85ac391-8185-498c-98b9-2e67e683db82",
      "product_eng_name": "Sau Tao Mustard Green Duck Flavour Rice Vermicelli 4 X 215GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%8D%85%E7%90%83%E5%98%9C%E7%B2%9F%E7%B1%B3%E6%B2%B9%205LT/i/101338381.html",
      "uid": "950232ed091f22b6695286788f2bd523",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "獅球嘜粟米油 5LT",
          "price": "$149",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230317/8e095fd4-4159-48ec-a31e-361a975b1053",
          "product_eng_name": "Lion & Globe Corn Oil 5LT"
        },
        {
          "name": "獅球嘜粟米油 5LT",
          "price": "$149",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230317/8e095fd4-4159-48ec-a31e-361a975b1053",
          "product_eng_name": "Lion & Globe Corn Oil 5LT"
        }
      ],
      "name": "獅球嘜粟米油 5LT",
      "price": "$149",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230317/8e095fd4-4159-48ec-a31e-361a975b1053",
      "product_eng_name": "Lion & Globe Corn Oil 5LT"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%A3%BD%E6%A1%83%E6%B2%B3%E7%B2%89%20360GM/i/101359428.html",
      "uid": "6cd13e47e16200f28785e2c55d8e4482",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "壽桃河粉 360GM",
          "price": "$20",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220615/bef6a69f-d39d-4ff7-9465-5c566310d618",
          "product_eng_name": "Sau Tao Ho Fan 360GM"
        },
        {
          "name": "壽桃河粉 360GM",
          "price": "$20",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220615/bef6a69f-d39d-4ff7-9465-5c566310d618",
          "product_eng_name": "Sau Tao Ho Fan 360GM"
        }
      ],
      "name": "壽桃河粉 360GM",
      "price": "$20",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20220615/bef6a69f-d39d-4ff7-9465-5c566310d618",
      "product_eng_name": "Sau Tao Ho Fan 360GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%8D%85%E7%90%83%E5%98%9C%E5%81%A5%E5%BA%B7%E7%B1%B3%E7%B3%A0%E6%B2%B9(%E9%9B%B6%E5%8F%8D%E5%BC%8F%E8%84%82%E8%82%AA)%202%20X%20900ML/i/102697426.html",
      "uid": "2584da69c6e48bb4671f3dae0a7de550",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "獅球嘜健康米糠油(零反式脂肪) 2 X 900ML",
          "price": "$76",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220613/23aea994-05ee-4ae7-b2b9-d9f6c6ba75ec",
          "product_eng_name": "Lion & Globe Pure Rice Bran Oil (Zero Trans Fat) 2 X 900ML"
        },
        {
          "name": "獅球嘜健康米糠油(零反式脂肪) 2 X 900ML",
          "price": "$76",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220613/23aea994-05ee-4ae7-b2b9-d9f6c6ba75ec",
          "product_eng_name": "Lion & Globe Pure Rice Bran Oil (Zero Trans Fat) 2 X 900ML"
        }
      ],
      "name": "獅球嘜健康米糠油(零反式脂肪) 2 X 900ML",
      "price": "$76",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20220613/23aea994-05ee-4ae7-b2b9-d9f6c6ba75ec",
      "product_eng_name": "Lion & Globe Pure Rice Bran Oil (Zero Trans Fat) 2 X 900ML"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E8%BE%B2%E5%BF%83%E7%84%A1%E5%91%B3%E7%B2%89%E6%8B%89%E9%BA%B5%205%20X%20110GM/i/101358048.html",
      "uid": "4a7c16f374fd079308ddd295440a8815",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "農心無味粉拉麵 5 X 110GM",
          "price": "$10",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231011/7afd7741-8987-3028-8374-d7b17b9d4b43",
          "product_eng_name": "Nong Shim Korean Plain Noodles 5 X 110GM"
        },
        {
          "name": "農心無味粉拉麵 5 X 110GM",
          "price": "$10",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231011/7afd7741-8987-3028-8374-d7b17b9d4b43",
          "product_eng_name": "Nong Shim Korean Plain Noodles 5 X 110GM"
        }
      ],
      "name": "農心無味粉拉麵 5 X 110GM",
      "price": "$10",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20231011/7afd7741-8987-3028-8374-d7b17b9d4b43",
      "product_eng_name": "Nong Shim Korean Plain Noodles 5 X 110GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%97%A5%E6%B8%85%E5%90%88%E5%91%B3%E9%81%93%20%E8%8A%9D%E5%A3%AB%E5%92%96%E5%96%B1%E5%91%B3%E5%A4%A7%E6%9D%AF%E9%BA%B5%E6%9D%AF%E9%BA%B5%20113%20GM/i/102126996.html",
      "uid": "2fad6bae1ebe1d74168966d4b2f298a4",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "日清合味道 芝士咖喱味大杯麵杯麵 113 GM",
          "price": "$11",
          "offer": "【2件$18】$18任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240711/892108de-a4f9-34d3-a9fe-7f14f508b160",
          "product_eng_name": "Nissin Big Cup Cheese Curry Noodles 113GM"
        },
        {
          "name": "日清合味道 芝士咖喱味大杯麵杯麵 113 GM",
          "price": "$11",
          "offer": "【2件$18】$18任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240711/892108de-a4f9-34d3-a9fe-7f14f508b160",
          "product_eng_name": "Nissin Big Cup Cheese Curry Noodles 113GM"
        }
      ],
      "name": "日清合味道 芝士咖喱味大杯麵杯麵 113 GM",
      "price": "$11",
      "offer": "【2件$18】$18任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240711/892108de-a4f9-34d3-a9fe-7f14f508b160",
      "product_eng_name": "Nissin Big Cup Cheese Curry Noodles 113GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E9%BB%9E%E9%BB%9E%E7%B6%A0%E6%9C%89%E6%A9%9F%E7%B4%85%E7%B1%B3%201KG/i/101343989.html",
      "uid": "159eb7aa065542294f860af344d74166",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "點點綠有機紅米 1KG",
          "price": "$47",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250320/3c7257dc-c38e-31ca-b60a-ead2dbc14193",
          "product_eng_name": "Green Dot Dot Organic Red Rice 1KG"
        }
      ],
      "name": "點點綠有機紅米 1KG",
      "price": "$47",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250320/3c7257dc-c38e-31ca-b60a-ead2dbc14193",
      "product_eng_name": "Green Dot Dot Organic Red Rice 1KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E8%BE%B2%E5%BF%83%E9%AD%B7%E9%AD%9A%E9%BA%B5%205%20X%20124GM/i/101371311.html",
      "uid": "8295082e649c3a475fa9a75dd6a57f53",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "農心魷魚麵 5 X 124GM",
          "price": "$25",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210520/b8fb5ed2-cbf8-4bf4-ac39-cfc8386894bf",
          "product_eng_name": "Nong Shim Champong Noodle 5 X 124GM"
        },
        {
          "name": "農心魷魚麵 5 X 124GM",
          "price": "$25",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210520/b8fb5ed2-cbf8-4bf4-ac39-cfc8386894bf",
          "product_eng_name": "Nong Shim Champong Noodle 5 X 124GM"
        }
      ],
      "name": "農心魷魚麵 5 X 124GM",
      "price": "$25",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210520/b8fb5ed2-cbf8-4bf4-ac39-cfc8386894bf",
      "product_eng_name": "Nong Shim Champong Noodle 5 X 124GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%A3%BD%E6%A1%83%E5%B9%BC%E8%9D%A6%E5%AD%90%E9%BA%B5%20454GM/i/101342531.html",
      "uid": "6de1ec171a9c43e16cadfb9aecc10eb3",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "壽桃幼蝦子麵 454GM",
          "price": "$14",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220505/d7cf0145-0c1d-4535-9fd0-2c398820d156",
          "product_eng_name": "Sau Tao Thin Shrimp Noodles 454GM"
        },
        {
          "name": "壽桃幼蝦子麵 454GM",
          "price": "$14",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220505/d7cf0145-0c1d-4535-9fd0-2c398820d156",
          "product_eng_name": "Sau Tao Thin Shrimp Noodles 454GM"
        }
      ],
      "name": "壽桃幼蝦子麵 454GM",
      "price": "$14",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20220505/d7cf0145-0c1d-4535-9fd0-2c398820d156",
      "product_eng_name": "Sau Tao Thin Shrimp Noodles 454GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E8%BE%B2%E5%BF%83%20%E7%94%9F%E7%94%9F%E7%83%8F%E5%86%AC%E7%A2%97%E9%BA%B512%20X%20276%20GM/i/101335793.html",
      "uid": "6c4d86aa99f9ad6ac93ca9365444ace9",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱農心 生生烏冬碗麵12 X 276 GM",
          "price": "$174",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231221/33c34366-9f9f-3d36-8ea7-272878a2f70d",
          "product_eng_name": "Nong Shim Saengsaeng Udon-Bowl Case 12 X 276 GM"
        },
        {
          "name": "原箱農心 生生烏冬碗麵12 X 276 GM",
          "price": "$174",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231221/33c34366-9f9f-3d36-8ea7-272878a2f70d",
          "product_eng_name": "Nong Shim Saengsaeng Udon-Bowl Case 12 X 276 GM"
        }
      ],
      "name": "原箱農心 生生烏冬碗麵12 X 276 GM",
      "price": "$174",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20231221/33c34366-9f9f-3d36-8ea7-272878a2f70d",
      "product_eng_name": "Nong Shim Saengsaeng Udon-Bowl Case 12 X 276 GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E4%BF%9D%E5%BE%97%20%E7%89%9B%E6%B2%B9%E6%9E%9C%E6%B2%B9%20500%20ML/i/113488354.html",
      "uid": "0abfbf2041452788222581b6a015193b",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "保得 牛油果油 500 ML",
          "price": "$89",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240509/c3967419-33bc-395b-8d94-ba55a47b2c7f",
          "product_eng_name": "Bontaste Avocado Oil 500ML"
        },
        {
          "name": "保得 牛油果油 500 ML",
          "price": "$89",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240509/c3967419-33bc-395b-8d94-ba55a47b2c7f",
          "product_eng_name": "Bontaste Avocado Oil 500ML"
        }
      ],
      "name": "保得 牛油果油 500 ML",
      "price": "$89",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240509/c3967419-33bc-395b-8d94-ba55a47b2c7f",
      "product_eng_name": "Bontaste Avocado Oil 500ML"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%A4%A9%E9%B5%9D%E7%89%8C%20%E6%98%9F%E6%B4%B2%E7%82%92%E7%B1%B3%E7%B2%89%20400%20GM/i/102768596.html",
      "uid": "7e15da98c60174ed28665ab682409cb6",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "天鵝牌 星洲炒米粉 400 GM",
          "price": "$19",
          "offer": "【2件$27】$27任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230508/207b9b40-ccd8-45ec-90f7-6401238054f6",
          "product_eng_name": "SWAN Dried Rice Stick 400GM"
        },
        {
          "name": "天鵝牌 星洲炒米粉 400 GM",
          "price": "$19",
          "offer": "【2件$27】$27任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230508/207b9b40-ccd8-45ec-90f7-6401238054f6",
          "product_eng_name": "SWAN Dried Rice Stick 400GM"
        }
      ],
      "name": "天鵝牌 星洲炒米粉 400 GM",
      "price": "$19",
      "offer": "【2件$27】$27任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230508/207b9b40-ccd8-45ec-90f7-6401238054f6",
      "product_eng_name": "SWAN Dried Rice Stick 400GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E4%BA%94%E8%B1%90%E7%89%8C%E7%89%B9%E7%BA%A7%E8%8C%89%E8%8E%89%E9%A6%99%E7%B1%B3%205KGM/i/101342428.html",
      "uid": "7d13e79a259d58b91637ebf8a7278dcd",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "五豐牌特级茉莉香米 5KGM",
          "price": "$49",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250307/3b08b4a3-89bb-3534-826b-8bd1cb3f69a9",
          "product_eng_name": "Ng Fung premium Jasmine rice 5KG"
        }
      ],
      "name": "五豐牌特级茉莉香米 5KGM",
      "price": "$49",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250307/3b08b4a3-89bb-3534-826b-8bd1cb3f69a9",
      "product_eng_name": "Ng Fung premium Jasmine rice 5KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%BE%A1%E5%93%81%E7%9A%87%E9%A0%82%E7%B4%9A%E6%B3%B0%E5%9C%8B%E8%8C%89%E8%8E%89%E9%A6%99%E7%B1%B3%208KG/i/101381358.html",
      "uid": "50ef396ec7b71b5a7bab86f3acf053da",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "御品皇頂級泰國茉莉香米 8KG",
          "price": "$98",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250306/93cc105e-f744-3df3-9b48-987cab5246ef",
          "product_eng_name": "Yu Pin King Thai Hom Mali Rice 8KG"
        }
      ],
      "name": "御品皇頂級泰國茉莉香米 8KG",
      "price": "$98",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250306/93cc105e-f744-3df3-9b48-987cab5246ef",
      "product_eng_name": "Yu Pin King Thai Hom Mali Rice 8KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E9%87%91%E9%B3%B3%20%E6%B3%B0%E5%9C%8B%E9%A0%82%E7%B4%9A%E8%8C%89%E8%8E%89%E9%A6%99%E7%B1%B3%2015KG/i/101361282.html",
      "uid": "959ac289879f4a058837ee66b5927b06",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "金鳳 泰國頂級茉莉香米 15KG",
          "price": "$259",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210104/7f52e9b3-0ef9-43fe-8a40-1d413fbd6202",
          "product_eng_name": "Golden Phoenix Thai Jasmine Rice 15KG"
        }
      ],
      "name": "金鳳 泰國頂級茉莉香米 15KG",
      "price": "$259",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210104/7f52e9b3-0ef9-43fe-8a40-1d413fbd6202",
      "product_eng_name": "Golden Phoenix Thai Jasmine Rice 15KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E5%87%BA%E5%89%8D%E4%B8%80%E4%B8%81%20%E9%BB%91%E8%92%9C%E6%B2%B9%E8%B1%AC%E9%AA%A8%E6%B9%AF%E6%9D%AF%E9%BA%B5%2070%20GM/i/113559509.html",
      "uid": "581a1ba3999e2e348f4043bc033a6b5b",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱出前一丁 黑蒜油豬骨湯杯麵 70 GM",
          "price": "$170",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231013/9d481a6d-e43b-3bdf-bc98-a3cffd03604c",
          "product_eng_name": "(無法擷取英文名稱)"
        },
        {
          "name": "原箱出前一丁 黑蒜油豬骨湯杯麵 70 GM",
          "price": "$170",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231013/9d481a6d-e43b-3bdf-bc98-a3cffd03604c",
          "product_eng_name": "Nissin Demae Iccho Black Garlic Oil Tonkotsu Cup Noodle Case 24 x 70GM"
        }
      ],
      "name": "原箱出前一丁 黑蒜油豬骨湯杯麵 70 GM",
      "price": "$170",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20231013/9d481a6d-e43b-3bdf-bc98-a3cffd03604c",
      "product_eng_name": "Nissin Demae Iccho Black Garlic Oil Tonkotsu Cup Noodle Case 24 x 70GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/De%20Cecco%E8%96%AF%E7%B2%89%E7%B2%92%20500GM/i/101334630.html",
      "uid": "a0e3f8975653cd9f99ce9df61cf30de6",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "De Cecco薯粉粒 500GM",
          "price": "$29",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240917/8e42c7f9-6618-3ca6-bad4-d233b2d9eb19",
          "product_eng_name": "De Cecco Potato Gnocchi 500GM"
        },
        {
          "name": "De Cecco薯粉粒 500GM",
          "price": "$29",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240917/8e42c7f9-6618-3ca6-bad4-d233b2d9eb19",
          "product_eng_name": "De Cecco Potato Gnocchi 500GM"
        }
      ],
      "name": "De Cecco薯粉粒 500GM",
      "price": "$29",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240917/8e42c7f9-6618-3ca6-bad4-d233b2d9eb19",
      "product_eng_name": "De Cecco Potato Gnocchi 500GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/Meadows%E7%89%9B%E6%B2%B9%E6%9E%9C%E6%B2%B91L/i/114303981.html",
      "uid": "574ea67291d6865c6b98d26d41156617",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "Meadows牛油果油1L",
          "price": "$113",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240703/7da3b1ad-c17e-31be-856c-9504ca26bf29",
          "product_eng_name": "Meadows Avocado Oil 1L"
        },
        {
          "name": "Meadows牛油果油1L",
          "price": "$113",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240703/7da3b1ad-c17e-31be-856c-9504ca26bf29",
          "product_eng_name": "Meadows Avocado Oil 1L"
        }
      ],
      "name": "Meadows牛油果油1L",
      "price": "$113",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240703/7da3b1ad-c17e-31be-856c-9504ca26bf29",
      "product_eng_name": "Meadows Avocado Oil 1L"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%A3%BD%E6%A1%83%E7%89%8C%E6%A5%B5%E5%93%81%E9%AE%91%E9%AD%9A%E6%92%88%E9%BA%B5%20570GM/i/101340931.html",
      "uid": "1812acc02765c562fa18e24422550f60",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "壽桃牌極品鮑魚撈麵 570GM",
          "price": "$36",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220505/d9ea7bd2-e88b-4f04-bc55-8ec3cf7ad683",
          "product_eng_name": "Sau Tao Abalone Noodles Mix 570GM"
        },
        {
          "name": "壽桃牌極品鮑魚撈麵 570GM",
          "price": "$36",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220505/d9ea7bd2-e88b-4f04-bc55-8ec3cf7ad683",
          "product_eng_name": "Sau Tao Abalone Noodles Mix 570GM"
        }
      ],
      "name": "壽桃牌極品鮑魚撈麵 570GM",
      "price": "$36",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20220505/d9ea7bd2-e88b-4f04-bc55-8ec3cf7ad683",
      "product_eng_name": "Sau Tao Abalone Noodles Mix 570GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%9B%9B%E6%B4%B2%E7%B4%AB%E8%8F%9C%E6%B9%AF%E9%BA%B5%205%20X%2090GM/i/101354287.html",
      "uid": "f8bbb03bfe5ab67bab729937b5da5992",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "四洲紫菜湯麵 5 X 90GM",
          "price": "$8",
          "offer": "【2件$30】$30任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210125/bee45f9f-89b0-4865-99b7-3f47130c1e16",
          "product_eng_name": "Four Seas Seaweed Noodle 5 X 90GM"
        },
        {
          "name": "四洲紫菜湯麵 5 X 90GM",
          "price": "$8",
          "offer": "【2件$30】$30任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210125/bee45f9f-89b0-4865-99b7-3f47130c1e16",
          "product_eng_name": "Four Seas Seaweed Noodle 5 X 90GM"
        }
      ],
      "name": "四洲紫菜湯麵 5 X 90GM",
      "price": "$8",
      "offer": "【2件$30】$30任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210125/bee45f9f-89b0-4865-99b7-3f47130c1e16",
      "product_eng_name": "Four Seas Seaweed Noodle 5 X 90GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%AF%8C%E7%94%B0%E7%B2%BE%E7%B1%B3%20%E6%96%B0%E7%80%89%E7%B8%A3%E8%B6%8A%E5%85%89%E7%B1%B3%201.8KG/i/113486549.html",
      "uid": "32381ccc786329eb5e7b53e7fe79cc87",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "富田精米 新瀉縣越光米 1.8KG",
          "price": "$65",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230726/740a9a8a-e06a-4b88-813b-e379542bd950",
          "product_eng_name": "Tomita Brand Nigata Koshihikari Rice 1.8KG"
        }
      ],
      "name": "富田精米 新瀉縣越光米 1.8KG",
      "price": "$65",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230726/740a9a8a-e06a-4b88-813b-e379542bd950",
      "product_eng_name": "Tomita Brand Nigata Koshihikari Rice 1.8KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E9%87%91%E8%B1%A1%E7%89%8C%E5%8D%B3%E9%A3%9F%E8%8C%89%E8%8E%89%E9%A6%99%E7%B1%B3%E9%A3%AF%20170GM/i/101350476.html",
      "uid": "99aa12484e10504cdca31f8eed7d9439",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "金象牌即食茉莉香米飯 170GM",
          "price": "$11",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210521/2e0ac95f-8d91-4f07-ad2b-99a0bd4910d6",
          "product_eng_name": "Golden Elephant Cooked Jasmine Rice 170GM"
        },
        {
          "name": "金象牌即食茉莉香米飯 170GM",
          "price": "$11",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210521/2e0ac95f-8d91-4f07-ad2b-99a0bd4910d6",
          "product_eng_name": "Golden Elephant Cooked Jasmine Rice 170GM"
        }
      ],
      "name": "金象牌即食茉莉香米飯 170GM",
      "price": "$11",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210521/2e0ac95f-8d91-4f07-ad2b-99a0bd4910d6",
      "product_eng_name": "Golden Elephant Cooked Jasmine Rice 170GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E6%97%A5%E6%B8%85%E5%90%88%E5%91%B3%E9%81%93%20%E5%92%96%E5%96%B1%E6%B5%B7%E9%AE%AE%E6%9D%AF%E9%BA%B5%2024%20X%2075GM/i/101334424.html",
      "uid": "1aef86c17726b72172b72ee7aa1daf78",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱日清合味道 咖喱海鮮杯麵 24 X 75GM",
          "price": "$170",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230202/0e60785e-0faf-49b0-a480-0e36396ab3be",
          "product_eng_name": "Nissin Curry Seefood Cup Ndle Case 24 X 75GM"
        },
        {
          "name": "原箱日清合味道 咖喱海鮮杯麵 24 X 75GM",
          "price": "$170",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230202/0e60785e-0faf-49b0-a480-0e36396ab3be",
          "product_eng_name": "Nissin Curry Seefood Cup Ndle Case 24 X 75GM"
        }
      ],
      "name": "原箱日清合味道 咖喱海鮮杯麵 24 X 75GM",
      "price": "$170",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230202/0e60785e-0faf-49b0-a480-0e36396ab3be",
      "product_eng_name": "Nissin Curry Seefood Cup Ndle Case 24 X 75GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%9B%BE%E6%8B%8C%E9%BA%B5%E9%BA%BB%E6%B2%B9%E6%A4%92%E9%A6%99%E6%8B%8C%E9%BA%B5%20468GM/i/102971746.html",
      "uid": "1b0518847ca3f357354a85eca13947f2",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "曾拌麵麻油椒香拌麵 468GM",
          "price": "$69",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220902/ffbd45ec-3be5-4b02-859b-61f386c925d3",
          "product_eng_name": "Tsengs Noodle Sesame Oil Sichuen Pepper Noodle 468GM"
        },
        {
          "name": "曾拌麵麻油椒香拌麵 468GM",
          "price": "$69",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220902/ffbd45ec-3be5-4b02-859b-61f386c925d3",
          "product_eng_name": "Tsengs Noodle Sesame Oil Sichuen Pepper Noodle 468GM"
        }
      ],
      "name": "曾拌麵麻油椒香拌麵 468GM",
      "price": "$69",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20220902/ffbd45ec-3be5-4b02-859b-61f386c925d3",
      "product_eng_name": "Tsengs Noodle Sesame Oil Sichuen Pepper Noodle 468GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/De%20Cecco%E5%A4%A7%E9%80%9A%E5%BF%83%E7%B2%89%20500GM/i/101369877.html",
      "uid": "178d6a27dd60bb712f1223caacb16113",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "De Cecco大通心粉 500GM",
          "price": "$29",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240917/49a44e06-0eac-3078-bd1f-6388d47f9a48",
          "product_eng_name": "De Cecco Penne 500GM"
        },
        {
          "name": "De Cecco大通心粉 500GM",
          "price": "$29",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240917/49a44e06-0eac-3078-bd1f-6388d47f9a48",
          "product_eng_name": "(無法擷取英文名稱)"
        }
      ],
      "name": "De Cecco大通心粉 500GM",
      "price": "$29",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240917/49a44e06-0eac-3078-bd1f-6388d47f9a48",
      "product_eng_name": "(無法擷取英文名稱)"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E4%BA%94%E6%9C%A8%E7%94%B0%E8%88%8D%E8%92%BF%E9%BA%A5%E9%BA%B5%20200GM/i/101322100.html",
      "uid": "d481723c70955ffd9ece2b47a0672c8c",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "五木田舍蒿麥麵 200GM",
          "price": "$17",
          "offer": "【3件$50】$50任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250218/3a8746a8-2738-3074-a258-073c45232272",
          "product_eng_name": "Itsuki Inaka Soba 200GM"
        },
        {
          "name": "五木田舍蒿麥麵 200GM",
          "price": "$17",
          "offer": "【3件$50】$50任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250218/3a8746a8-2738-3074-a258-073c45232272",
          "product_eng_name": "Itsuki Inaka Soba 200GM"
        }
      ],
      "name": "五木田舍蒿麥麵 200GM",
      "price": "$17",
      "offer": "【3件$50】$50任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250218/3a8746a8-2738-3074-a258-073c45232272",
      "product_eng_name": "Itsuki Inaka Soba 200GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%97%A5%E6%B8%85%E6%98%A5%E9%9B%A8%E8%B6%8A%E5%BC%8F%E9%9B%9E%E8%82%89%E9%A6%99%E8%8F%9C%E7%B2%89%E7%B5%B2%2048GM/i/101346894.html",
      "uid": "92e1a18d28b12fd39e102d9b14a00ff0",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "日清春雨越式雞肉香菜粉絲 48GM",
          "price": "$11",
          "offer": "【2件$16】$16任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210513/f2b951c8-e9f2-494e-888f-aa52a4bf722a",
          "product_eng_name": "Nissin Harusame Vietnam Chicken Vermicelli 48GM"
        },
        {
          "name": "日清春雨越式雞肉香菜粉絲 48GM",
          "price": "$11",
          "offer": "【2件$16】$16任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210513/f2b951c8-e9f2-494e-888f-aa52a4bf722a",
          "product_eng_name": "Nissin Harusame Vietnam Chicken Vermicelli 48GM"
        }
      ],
      "name": "日清春雨越式雞肉香菜粉絲 48GM",
      "price": "$11",
      "offer": "【2件$16】$16任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210513/f2b951c8-e9f2-494e-888f-aa52a4bf722a",
      "product_eng_name": "Nissin Harusame Vietnam Chicken Vermicelli 48GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E9%87%91%E9%B3%B3%E9%A0%82%E7%B4%9A%E9%A6%99%E7%B1%B3%2010KG/i/101324109.html",
      "uid": "abe7c5099cc6f146bc49ef109f63a086",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "金鳳頂級香米 10KG",
          "price": "$194",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250320/4a33c3ec-f5c9-357d-a239-56c065228fba",
          "product_eng_name": "Golden Phoenix Hom Mali Rice 10KG"
        }
      ],
      "name": "金鳳頂級香米 10KG",
      "price": "$194",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250320/4a33c3ec-f5c9-357d-a239-56c065228fba",
      "product_eng_name": "Golden Phoenix Hom Mali Rice 10KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E8%B6%85%E5%8A%9B%E8%B6%85%E5%8A%9B%E6%B1%9F%E8%A5%BF%E7%B1%B3%E7%B7%9A%20400GM/i/101379680.html",
      "uid": "a7bbfefb0644fd8d309853468f304754",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "超力超力江西米線 400GM",
          "price": "$9",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240916/c2bf520a-c2e9-3bc2-8ec6-4919be59846e",
          "product_eng_name": "Chewy Jiang Xi Rice Stick 400GM"
        },
        {
          "name": "超力超力江西米線 400GM",
          "price": "$9",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240916/c2bf520a-c2e9-3bc2-8ec6-4919be59846e",
          "product_eng_name": "(無法擷取英文名稱)"
        }
      ],
      "name": "超力超力江西米線 400GM",
      "price": "$9",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240916/c2bf520a-c2e9-3bc2-8ec6-4919be59846e",
      "product_eng_name": "(無法擷取英文名稱)"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%B0%B8%E6%A8%82%E7%B2%89%E9%BA%B5%E5%BB%A0%E8%83%A1%E6%A4%92%E8%B1%AC%E9%AA%A8%E6%B9%AF%E9%BA%B5%2012PC/i/113323273.html",
      "uid": "97ae918c69e6eca2b5f8aa2d5c015f2c",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "永樂粉麵廠胡椒豬骨湯麵 12PC",
          "price": "$90",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230411/af3f4f6b-9445-48b7-85ed-deee6570de2a",
          "product_eng_name": "Wing Lok Pepper Pork Soup Noodle 12PC"
        },
        {
          "name": "永樂粉麵廠胡椒豬骨湯麵 12PC",
          "price": "$90",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230411/af3f4f6b-9445-48b7-85ed-deee6570de2a",
          "product_eng_name": "Wing Lok Pepper Pork Soup Noodle 12PC"
        }
      ],
      "name": "永樂粉麵廠胡椒豬骨湯麵 12PC",
      "price": "$90",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230411/af3f4f6b-9445-48b7-85ed-deee6570de2a",
      "product_eng_name": "Wing Lok Pepper Pork Soup Noodle 12PC"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E5%A4%A9%E7%87%9F%E5%9D%8A%20%E6%B7%AE%E5%B1%B1%E9%BA%B512%20X%20480%20GM/i/101335792.html",
      "uid": "e67a6b3460917767d8588046595d410e",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱天營坊 淮山麵12 X 480 GM",
          "price": "$280",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231221/67b353b0-a542-3ba3-a174-7ae062710346",
          "product_eng_name": "(無法擷取英文名稱)"
        },
        {
          "name": "原箱天營坊 淮山麵12 X 480 GM",
          "price": "$280",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231221/67b353b0-a542-3ba3-a174-7ae062710346",
          "product_eng_name": "Natural Nutrition Area Yam Noodle Case 12 X 480 GM"
        }
      ],
      "name": "原箱天營坊 淮山麵12 X 480 GM",
      "price": "$280",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20231221/67b353b0-a542-3ba3-a174-7ae062710346",
      "product_eng_name": "Natural Nutrition Area Yam Noodle Case 12 X 480 GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%97%A5%E6%B8%85%E5%90%88%E5%91%B3%E9%81%93%E5%86%AC%E9%99%B0%E5%8A%9F%E5%91%B3%E6%9D%AF%E9%BA%B5%2074GM/i/101346184.html",
      "uid": "2f6f7150726dcc89c1f5471bbba4e09a",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "日清合味道冬陰功味杯麵 74GM",
          "price": "$8",
          "offer": "【2件$14.5】$14.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250327/ed8ad16c-b78a-3b37-9454-eb72817cf2d4",
          "product_eng_name": "Nissin Cup Noodles Tom Yum Goong 74GM"
        },
        {
          "name": "日清合味道冬陰功味杯麵 74GM",
          "price": "$8",
          "offer": "【2件$14.5】$14.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250327/ed8ad16c-b78a-3b37-9454-eb72817cf2d4",
          "product_eng_name": "Nissin Cup Noodles Tom Yum Goong 74GM"
        }
      ],
      "name": "日清合味道冬陰功味杯麵 74GM",
      "price": "$8",
      "offer": "【2件$14.5】$14.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250327/ed8ad16c-b78a-3b37-9454-eb72817cf2d4",
      "product_eng_name": "Nissin Cup Noodles Tom Yum Goong 74GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%AE%B6%E6%A8%82%E7%89%8C%E9%AE%91%E9%9B%9E%E5%91%B3%E5%BF%AB%E7%86%9F%E9%80%9A%E5%BF%83%E7%B2%89%2080GM/i/101338133.html",
      "uid": "b63ea82e9ea21b6a2d76c29e6a5f112d",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "家樂牌鮑雞味快熟通心粉 80GM",
          "price": "$7",
          "offer": "【3件$17】$17任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240917/4cd38af4-5f39-30dc-8ca9-a7ed6a81e977",
          "product_eng_name": "Knorr Quick Serve Abalone & Chicken Macaroni 80GM"
        },
        {
          "name": "家樂牌鮑雞味快熟通心粉 80GM",
          "price": "$7",
          "offer": "【3件$17】$17任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240917/4cd38af4-5f39-30dc-8ca9-a7ed6a81e977",
          "product_eng_name": "Knorr Quick Serve Abalone & Chicken Macaroni 80GM"
        }
      ],
      "name": "家樂牌鮑雞味快熟通心粉 80GM",
      "price": "$7",
      "offer": "【3件$17】$17任揀3件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240917/4cd38af4-5f39-30dc-8ca9-a7ed6a81e977",
      "product_eng_name": "Knorr Quick Serve Abalone & Chicken Macaroni 80GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%88%80%E5%98%9C%20%E7%B4%94%E6%AD%A3%E7%B2%9F%E7%B1%B3%E6%B2%B9%205%20LT/i/113616046.html",
      "uid": "1e81ad6fe1a715122b5e89a2272dd81a",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "刀嘜 純正粟米油 5 LT",
          "price": "$149",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231011/e23a2e8d-7bcd-365e-8f6d-b90b6fb42d9d",
          "product_eng_name": "Knife Pure Corn Oil 5LT"
        },
        {
          "name": "刀嘜 純正粟米油 5 LT",
          "price": "$149",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231011/e23a2e8d-7bcd-365e-8f6d-b90b6fb42d9d",
          "product_eng_name": "Knife Pure Corn Oil 5LT"
        }
      ],
      "name": "刀嘜 純正粟米油 5 LT",
      "price": "$149",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20231011/e23a2e8d-7bcd-365e-8f6d-b90b6fb42d9d",
      "product_eng_name": "Knife Pure Corn Oil 5LT"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E8%BE%B2%E5%BF%83%E9%BB%91%E7%89%88%E8%BE%9B%E8%BE%A3%E5%A4%A7%E7%A2%97%E9%BA%B5%20101GM/i/101337532.html",
      "uid": "ffb6fe286fd0525e8f98e93d68477ee1",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "農心黑版辛辣大碗麵 101GM",
          "price": "$16",
          "offer": "【2件$26】$26任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210520/e5649e04-95be-47ff-bea1-cc46ce081aaf",
          "product_eng_name": "Nong Shim Black Shin Noodles 101GM"
        },
        {
          "name": "農心黑版辛辣大碗麵 101GM",
          "price": "$16",
          "offer": "【2件$26】$26任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210520/e5649e04-95be-47ff-bea1-cc46ce081aaf",
          "product_eng_name": "Nong Shim Black Shin Noodles 101GM"
        }
      ],
      "name": "農心黑版辛辣大碗麵 101GM",
      "price": "$16",
      "offer": "【2件$26】$26任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210520/e5649e04-95be-47ff-bea1-cc46ce081aaf",
      "product_eng_name": "Nong Shim Black Shin Noodles 101GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%97%A5%E6%B8%85%E5%90%88%E5%91%B3%E9%81%93%E4%BB%80%E9%8C%A6%E6%9D%AF%E9%BA%B5%2075GM/i/101331581.html",
      "uid": "4d8b4febbfb9936566f388c88f0db460",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "日清合味道什錦杯麵 75GM",
          "price": "$8",
          "offer": "【2件$14.5】$14.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250327/71230b3c-822b-3c81-b2ef-b6a563fa7509",
          "product_eng_name": "Nissin Pork Chowder Cup Noodles 75GM"
        },
        {
          "name": "日清合味道什錦杯麵 75GM",
          "price": "$8",
          "offer": "【2件$14.5】$14.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250327/71230b3c-822b-3c81-b2ef-b6a563fa7509",
          "product_eng_name": "Nissin Pork Chowder Cup Noodles 75GM"
        }
      ],
      "name": "日清合味道什錦杯麵 75GM",
      "price": "$8",
      "offer": "【2件$14.5】$14.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250327/71230b3c-822b-3c81-b2ef-b6a563fa7509",
      "product_eng_name": "Nissin Pork Chowder Cup Noodles 75GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%A5%BD%E9%81%8B%E7%89%8C%E5%81%A5%E6%80%A1%E7%B1%B3%202KG/i/101359750.html",
      "uid": "95f595cdf47f2b6d9c745227a9fad4f6",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "好運牌健怡米 2KG",
          "price": "$38",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230317/078df7fc-628a-4afb-812c-afd8a7c58c41",
          "product_eng_name": "Lucky Brand Mixed Rice 2KG"
        }
      ],
      "name": "好運牌健怡米 2KG",
      "price": "$38",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230317/078df7fc-628a-4afb-812c-afd8a7c58c41",
      "product_eng_name": "Lucky Brand Mixed Rice 2KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E4%B8%8D%E7%AD%89%E9%AD%B7%E9%AD%9A%E7%B1%BD%E8%94%A5%E6%B2%B9%E6%8B%8C%E9%BA%B5%20125%E5%85%8B/i/101355024.html",
      "uid": "1e9a92d7f109d0d0ebad8f70b22ce871",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "不等魷魚籽蔥油拌麵 125克",
          "price": "$14",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240417/b706d6d7-5368-33c7-a878-e8c583c4755d",
          "product_eng_name": "Budeng Squid Roe Scallion Oil Noodles 125G"
        },
        {
          "name": "不等魷魚籽蔥油拌麵 125克",
          "price": "$14",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240417/b706d6d7-5368-33c7-a878-e8c583c4755d",
          "product_eng_name": "Budeng Squid Roe Scallion Oil Noodles 125G"
        }
      ],
      "name": "不等魷魚籽蔥油拌麵 125克",
      "price": "$14",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240417/b706d6d7-5368-33c7-a878-e8c583c4755d",
      "product_eng_name": "Budeng Squid Roe Scallion Oil Noodles 125G"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%85%AC%E4%BB%94%E8%A0%94%E6%B2%B9%E6%B5%B7%E9%AE%AE%E7%82%92%E9%BA%B5%E7%8E%8B%20118GM/i/101328305.html",
      "uid": "4e5c481662d75b42611048a3ab0a6dcf",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "公仔蠔油海鮮炒麵王 118GM",
          "price": "$7",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250320/3c87e420-0a05-37b0-b18a-b98573e9e249",
          "product_eng_name": "Doll Fried Noodle Oyster Seafood 118GM"
        },
        {
          "name": "公仔蠔油海鮮炒麵王 118GM",
          "price": "$7",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250320/3c87e420-0a05-37b0-b18a-b98573e9e249",
          "product_eng_name": "Doll Fried Noodle Oyster Seafood 118GM"
        }
      ],
      "name": "公仔蠔油海鮮炒麵王 118GM",
      "price": "$7",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250320/3c87e420-0a05-37b0-b18a-b98573e9e249",
      "product_eng_name": "Doll Fried Noodle Oyster Seafood 118GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%A6%8F%E5%AD%97%E9%9B%9E%E6%B1%81%E4%BC%8A%E9%BA%B5%2065GM/i/101343616.html",
      "uid": "3a2686616a28166769c07174b75e7306",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "福字雞汁伊麵 65GM",
          "price": "$2",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210513/98db26c2-a214-4cd0-b4b5-68f951264a1c",
          "product_eng_name": "Fuku Chicken Instant Noodle 65GM"
        },
        {
          "name": "福字雞汁伊麵 65GM",
          "price": "$2",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210513/98db26c2-a214-4cd0-b4b5-68f951264a1c",
          "product_eng_name": "Fuku Chicken Instant Noodle 65GM"
        }
      ],
      "name": "福字雞汁伊麵 65GM",
      "price": "$2",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210513/98db26c2-a214-4cd0-b4b5-68f951264a1c",
      "product_eng_name": "Fuku Chicken Instant Noodle 65GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E9%87%91%E9%A6%99%E8%8C%89%E8%8E%89%E9%A6%99%E7%B1%B3%E7%8E%8B%205KG/i/101349563.html",
      "uid": "f8e8768f1d2c8ddea2bd7145de1721d3",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "金香茉莉香米王 5KG",
          "price": "$59",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230726/43ae61af-bbce-43d3-a52f-07cc32dc3f09",
          "product_eng_name": "Kam Heung Premium Jasmine Rice 5KG"
        }
      ],
      "name": "金香茉莉香米王 5KG",
      "price": "$59",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230726/43ae61af-bbce-43d3-a52f-07cc32dc3f09",
      "product_eng_name": "Kam Heung Premium Jasmine Rice 5KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%99%BD%E8%B1%A1%20%E9%A6%99%E8%8F%9C%E7%A2%97%E9%BA%B5%20115%20GM/i/113738746.html",
      "uid": "e39c91986734a6012c5abb468414fa65",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "白象 香菜碗麵 115 GM",
          "price": "$15",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240314/edd1608c-16ff-3147-80a0-76af59ace164",
          "product_eng_name": "BAIXIANG CORIANDER BOWL NOODL 115 GM"
        },
        {
          "name": "白象 香菜碗麵 115 GM",
          "price": "$15",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240314/edd1608c-16ff-3147-80a0-76af59ace164",
          "product_eng_name": "BAIXIANG CORIANDER BOWL NOODL 115 GM"
        }
      ],
      "name": "白象 香菜碗麵 115 GM",
      "price": "$15",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240314/edd1608c-16ff-3147-80a0-76af59ace164",
      "product_eng_name": "BAIXIANG CORIANDER BOWL NOODL 115 GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%A3%BD%E6%A1%83%E7%B4%B0%E5%88%87%E7%83%8F%E5%86%AC%203%20X%20200GM/i/101372658.html",
      "uid": "eb554add0988571b6276f482b1183110",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "壽桃細切烏冬 3 X 200GM",
          "price": "$9",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220505/953fa307-bccd-4976-bd97-0ced558210a4",
          "product_eng_name": "Sau Tao Japanese Udon 3 X 200GM"
        },
        {
          "name": "壽桃細切烏冬 3 X 200GM",
          "price": "$9",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220505/953fa307-bccd-4976-bd97-0ced558210a4",
          "product_eng_name": "Sau Tao Japanese Udon 3 X 200GM"
        }
      ],
      "name": "壽桃細切烏冬 3 X 200GM",
      "price": "$9",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20220505/953fa307-bccd-4976-bd97-0ced558210a4",
      "product_eng_name": "Sau Tao Japanese Udon 3 X 200GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%A8%82%E5%AE%B6%E9%BB%91%E9%87%91%E6%84%8F%E5%A4%A7%E5%88%A9%E7%89%B9%E7%B4%94%E6%A9%84%E6%AC%96%E6%B2%B9%20750%E6%AF%AB%E5%8D%87/i/101335005.html",
      "uid": "e12e29d848f2b1fb15e58bb4ad1dab3f",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "樂家黑金意大利特純橄欖油 750毫升",
          "price": "$186",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20241007/e2bfcdec-6c6c-3b8d-acd0-d4ad3ccbb2a3",
          "product_eng_name": "Colavita Premium Italian Extra Virgin Olive Oil 750ml"
        },
        {
          "name": "樂家黑金意大利特純橄欖油 750毫升",
          "price": "$186",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20241007/e2bfcdec-6c6c-3b8d-acd0-d4ad3ccbb2a3",
          "product_eng_name": "Colavita Premium Italian Extra Virgin Olive Oil 750ml"
        }
      ],
      "name": "樂家黑金意大利特純橄欖油 750毫升",
      "price": "$186",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20241007/e2bfcdec-6c6c-3b8d-acd0-d4ad3ccbb2a3",
      "product_eng_name": "Colavita Premium Italian Extra Virgin Olive Oil 750ml"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E8%B6%85%E5%8A%9B%E9%87%91%E8%A3%9D%E9%8A%80%E7%B5%B2%E9%A6%99%E7%B1%B3%208KG/i/101330090.html",
      "uid": "b3fd1a3bd9c7219df44c69a249170bc6",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "超力金裝銀絲香米 8KG",
          "price": "$102",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250407/0fbc5526-459a-3377-948a-7ffd6990c5f1",
          "product_eng_name": "Chewy Golden Premium Thai Hom Mali Rice 8KG"
        }
      ],
      "name": "超力金裝銀絲香米 8KG",
      "price": "$102",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250407/0fbc5526-459a-3377-948a-7ffd6990c5f1",
      "product_eng_name": "Chewy Golden Premium Thai Hom Mali Rice 8KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/De%20Cecco%E6%84%8F%E5%A4%A7%E5%88%A9%E7%B4%B0%E9%80%9A%E5%BF%83%E7%B2%89n180%20500GM/i/101322602.html",
      "uid": "96e03cfcaf0162235c893b9e6d73f419",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "De Cecco意大利細通心粉n180 500GM",
          "price": "$29",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240917/b0c11670-7dff-372e-a06e-7731ef9283a9",
          "product_eng_name": "De Cecco Lumachine N180 500GM"
        },
        {
          "name": "De Cecco意大利細通心粉n180 500GM",
          "price": "$29",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240917/b0c11670-7dff-372e-a06e-7731ef9283a9",
          "product_eng_name": "(無法擷取英文名稱)"
        }
      ],
      "name": "De Cecco意大利細通心粉n180 500GM",
      "price": "$29",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240917/b0c11670-7dff-372e-a06e-7731ef9283a9",
      "product_eng_name": "(無法擷取英文名稱)"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E8%B6%85%E5%8A%9B%E9%86%AC%E7%88%86%E6%9D%AF-%E8%80%81%E5%A3%87%E9%85%B8%E8%8F%9C%E7%B1%B3%E7%B2%89%20102GM/i/102810706.html",
      "uid": "90aa3a943c8bb653150119ca6d8e2e2f",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "超力醬爆杯-老壇酸菜米粉 102GM",
          "price": "$10",
          "offer": "【2件$13.5】$13.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240916/0c02794f-3f22-302a-8200-53e2a1264ddf",
          "product_eng_name": "Chewy Cup Instant Vermicelli Laotan Pickled Flavour 102GM"
        },
        {
          "name": "超力醬爆杯-老壇酸菜米粉 102GM",
          "price": "$10",
          "offer": "【2件$13.5】$13.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240916/0c02794f-3f22-302a-8200-53e2a1264ddf",
          "product_eng_name": "Chewy Cup Instant Vermicelli Laotan Pickled Flavour 102GM"
        }
      ],
      "name": "超力醬爆杯-老壇酸菜米粉 102GM",
      "price": "$10",
      "offer": "【2件$13.5】$13.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240916/0c02794f-3f22-302a-8200-53e2a1264ddf",
      "product_eng_name": "Chewy Cup Instant Vermicelli Laotan Pickled Flavour 102GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%B7%BA%E4%BA%95%E6%84%9B%E7%9F%A5%E4%B9%8B%E9%A6%99%E7%84%A1%E6%B4%97%E7%B1%B3%202KG/i/101573381.html",
      "uid": "681f2be54ee4f756157c86fd66b9f06c",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "淺井愛知之香無洗米 2KG",
          "price": "$99",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210512/33d3f363-1da1-4901-a5a0-1a5b7161c7ff",
          "product_eng_name": "Azai Aichi Rica Musenmai 2KG"
        }
      ],
      "name": "淺井愛知之香無洗米 2KG",
      "price": "$99",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210512/33d3f363-1da1-4901-a5a0-1a5b7161c7ff",
      "product_eng_name": "Azai Aichi Rica Musenmai 2KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E9%87%91%E9%B3%B3%20%E6%B3%B0%E5%9C%8B%E9%A0%82%E7%B4%9A%E9%A6%99%E7%B1%B3%201KG/i/101478821.html",
      "uid": "f3514f6437041c1b47d46a6b5897a641",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "金鳳 泰國頂級香米 1KG",
          "price": "$32",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20221228/a76cd13e-f22d-4653-b232-11b521b95704",
          "product_eng_name": "Golden Phoenix Thai Hommali Rice 1KG"
        }
      ],
      "name": "金鳳 泰國頂級香米 1KG",
      "price": "$32",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20221228/a76cd13e-f22d-4653-b232-11b521b95704",
      "product_eng_name": "Golden Phoenix Thai Hommali Rice 1KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E4%B8%8D%E7%AD%89%20%E8%98%87%E5%BC%8F%E8%9F%B9%E9%BB%83%E9%BA%B5%20210%20GM/i/113623236.html",
      "uid": "f93a350c8d2f93c8aac29bf8e3781cc7",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "不等 蘇式蟹黃麵 210 GM",
          "price": "$28",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240930/b46c9a11-5992-3382-b629-297d13c222c6",
          "product_eng_name": "Budeng Crab Su Style Crab Noodles 210GM"
        },
        {
          "name": "不等 蘇式蟹黃麵 210 GM",
          "price": "$28",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240930/b46c9a11-5992-3382-b629-297d13c222c6",
          "product_eng_name": "Budeng Crab Su Style Crab Noodles 210GM"
        }
      ],
      "name": "不等 蘇式蟹黃麵 210 GM",
      "price": "$28",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240930/b46c9a11-5992-3382-b629-297d13c222c6",
      "product_eng_name": "Budeng Crab Su Style Crab Noodles 210GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%88%80%E5%98%9C%20%E7%B4%94%E6%AD%A3%E8%8A%B1%E7%94%9F%E6%B2%B9%E5%84%AA%E6%83%A0%E8%A3%9D%204%20X%20900ML/i/101346289.html",
      "uid": "f45fd76efaee18f00735a69ddc01f215",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "刀嘜 純正花生油優惠裝 4 X 900ML",
          "price": "$129",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250320/0fd02d59-4661-3efe-bd43-9a00e12d5343",
          "product_eng_name": "Knife Pure Peanut Oil 4x900ML"
        },
        {
          "name": "刀嘜 純正花生油優惠裝 4 X 900ML",
          "price": "$129",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250320/0fd02d59-4661-3efe-bd43-9a00e12d5343",
          "product_eng_name": "Knife Pure Peanut Oil 4x900ML"
        }
      ],
      "name": "刀嘜 純正花生油優惠裝 4 X 900ML",
      "price": "$129",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250320/0fd02d59-4661-3efe-bd43-9a00e12d5343",
      "product_eng_name": "Knife Pure Peanut Oil 4x900ML"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E9%87%91%E8%B1%A1%E7%89%8C%E5%8D%B3%E9%A3%9F%E6%97%A5%E6%9C%AC%E7%94%A2%E7%B1%B3%E9%A3%AF%20170GM/i/101357270.html",
      "uid": "8176e568594629622f0bbf2f9ec8b137",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "金象牌即食日本產米飯 170GM",
          "price": "$13",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210521/3e756a49-0fcd-4bb0-9ff2-2d6757fadc9e",
          "product_eng_name": "Golden Elephant Cooked Japanese Rice 170GM"
        },
        {
          "name": "金象牌即食日本產米飯 170GM",
          "price": "$13",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210521/3e756a49-0fcd-4bb0-9ff2-2d6757fadc9e",
          "product_eng_name": "Golden Elephant Cooked Japanese Rice 170GM"
        }
      ],
      "name": "金象牌即食日本產米飯 170GM",
      "price": "$13",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210521/3e756a49-0fcd-4bb0-9ff2-2d6757fadc9e",
      "product_eng_name": "Golden Elephant Cooked Japanese Rice 170GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E4%B8%8D%E5%80%92%E7%BF%81%E8%BE%A3%E5%91%B3%E9%87%91%E6%8B%89%E9%BA%B5%205%20X%20120GM/i/101342807.html",
      "uid": "f7fc95badeb46896435719f01823473e",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "不倒翁辣味金拉麵 5 X 120GM",
          "price": "$28",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231011/4d797429-a3ca-3228-911d-8a3b73e87f8e",
          "product_eng_name": "Ottogi Jin Ramen (Hot) 5 x 120GM"
        },
        {
          "name": "不倒翁辣味金拉麵 5 X 120GM",
          "price": "$28",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231011/4d797429-a3ca-3228-911d-8a3b73e87f8e",
          "product_eng_name": "Ottogi Jin Ramen (Hot) 5 x 120GM"
        }
      ],
      "name": "不倒翁辣味金拉麵 5 X 120GM",
      "price": "$28",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20231011/4d797429-a3ca-3228-911d-8a3b73e87f8e",
      "product_eng_name": "Ottogi Jin Ramen (Hot) 5 x 120GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%A3%BD%E6%A1%83%E9%AE%91%E9%AD%9A%E9%9B%9E%E6%B9%AF%E6%B2%B3%205%20X%2075GM/i/101322514.html",
      "uid": "226363733693ca89790f7abfc1939b29",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "壽桃鮑魚雞湯河 5 X 75GM",
          "price": "$20",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220505/7aa756af-38d5-4070-a40d-50e3e88732e7",
          "product_eng_name": "Sau Tao Abalone & Chicken Ho Fan 5 X 75GM"
        },
        {
          "name": "壽桃鮑魚雞湯河 5 X 75GM",
          "price": "$20",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220505/7aa756af-38d5-4070-a40d-50e3e88732e7",
          "product_eng_name": "Sau Tao Abalone & Chicken Ho Fan 5 X 75GM"
        }
      ],
      "name": "壽桃鮑魚雞湯河 5 X 75GM",
      "price": "$20",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20220505/7aa756af-38d5-4070-a40d-50e3e88732e7",
      "product_eng_name": "Sau Tao Abalone & Chicken Ho Fan 5 X 75GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/VIFON%20%E8%B6%8A%E5%8D%97%E7%89%9B%E8%82%89%E5%91%B3%E6%B9%AF%E6%B2%B3%E7%B2%895%E5%8C%85%E8%A3%9D%2060%20GM/i/113401218.html",
      "uid": "30b37640bf4f8d9ef80cd468c38dbbd6",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "VIFON 越南牛肉味湯河粉5包裝 60 GM",
          "price": "$20",
          "offer": "【2件$35】$35任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240916/39797f57-2fdc-3d10-bb4d-cc45ac2355ce",
          "product_eng_name": "VIFON Beef Noodles Rice 5 X 60GM"
        },
        {
          "name": "VIFON 越南牛肉味湯河粉5包裝 60 GM",
          "price": "$20",
          "offer": "【2件$35】$35任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240916/39797f57-2fdc-3d10-bb4d-cc45ac2355ce",
          "product_eng_name": "(無法擷取英文名稱)"
        }
      ],
      "name": "VIFON 越南牛肉味湯河粉5包裝 60 GM",
      "price": "$20",
      "offer": "【2件$35】$35任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240916/39797f57-2fdc-3d10-bb4d-cc45ac2355ce",
      "product_eng_name": "(無法擷取英文名稱)"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%BB%BF%E5%B0%8F%E9%A3%BD%20%E8%82%A5%E6%B1%81%E6%8B%89%E9%BA%B5%E6%9D%AF%E9%9D%A2%20112.6G/i/101341193.html",
      "uid": "cdf7cc0eab8d72626ba356fda3039b80",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "滿小飽 肥汁拉麵杯面 112.6G",
          "price": "$9",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240124/c38a4123-6cc2-37a2-a45e-bbbb06de233c",
          "product_eng_name": "Man Xiao Bao Ramen Noodle And Rich Sauce Cup 112.6G"
        },
        {
          "name": "滿小飽 肥汁拉麵杯面 112.6G",
          "price": "$9",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240124/c38a4123-6cc2-37a2-a45e-bbbb06de233c",
          "product_eng_name": "Man Xiao Bao Ramen Noodle And Rich Sauce Cup 112.6G"
        }
      ],
      "name": "滿小飽 肥汁拉麵杯面 112.6G",
      "price": "$9",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240124/c38a4123-6cc2-37a2-a45e-bbbb06de233c",
      "product_eng_name": "Man Xiao Bao Ramen Noodle And Rich Sauce Cup 112.6G"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%A4%A7%E5%B8%AB%E5%A7%90%20%E5%85%A8%E8%9B%8B%E9%BA%B5(%E7%B2%97)%206%E5%80%8B%E8%A3%9D/i/101341771.html",
      "uid": "600ca049a5dff6ba18a5a3301bfb0181",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "大師姐 全蛋麵(粗) 6個裝",
          "price": "$78",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250122/2545e218-0be4-36e7-bc45-c55471d07b7a",
          "product_eng_name": "Dashijie Egg Noodle (Thick)"
        },
        {
          "name": "大師姐 全蛋麵(粗) 6個裝",
          "price": "$78",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250122/2545e218-0be4-36e7-bc45-c55471d07b7a",
          "product_eng_name": "Dashijie Egg Noodle (Thick)"
        }
      ],
      "name": "大師姐 全蛋麵(粗) 6個裝",
      "price": "$78",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250122/2545e218-0be4-36e7-bc45-c55471d07b7a",
      "product_eng_name": "Dashijie Egg Noodle (Thick)"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E8%81%96%E8%B3%A2%E6%AF%8D%E7%B4%B0%E6%A2%9D%E6%84%8F%E5%A4%A7%E5%88%A9%E7%B2%89%232%20500G/i/101347121.html",
      "uid": "4d8584ce128b00ca465fd70f31e627b2",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "聖賢母細條意大利粉#2 500G",
          "price": "$15",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240913/1e9c9064-b40e-3ce3-960f-5cef54cc0e12",
          "product_eng_name": "San Remo #2 Vermicelli 500G"
        },
        {
          "name": "聖賢母細條意大利粉#2 500G",
          "price": "$15",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240913/1e9c9064-b40e-3ce3-960f-5cef54cc0e12",
          "product_eng_name": "San Remo #2 Vermicelli 500G"
        }
      ],
      "name": "聖賢母細條意大利粉#2 500G",
      "price": "$15",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240913/1e9c9064-b40e-3ce3-960f-5cef54cc0e12",
      "product_eng_name": "San Remo #2 Vermicelli 500G"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E8%B6%85%E5%8A%9B%20%E8%92%9C%E9%A6%99%E8%82%89%E7%A2%8E%E5%91%B3%E6%B3%B0%E7%B1%B3%E7%B2%895%E5%8C%85%E8%A3%9D%2060%20GM/i/113401203.html",
      "uid": "67529f2962132b78a40ad6aec8da2b09",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "超力 蒜香肉碎味泰米粉5包裝 60 GM",
          "price": "$24",
          "offer": "【2件$25】$25任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240916/a5b0bbe8-6a62-3517-88b6-be2dc655f831",
          "product_eng_name": "(無法擷取英文名稱)"
        },
        {
          "name": "超力 蒜香肉碎味泰米粉5包裝 60 GM",
          "price": "$24",
          "offer": "【2件$25】$25任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240916/a5b0bbe8-6a62-3517-88b6-be2dc655f831",
          "product_eng_name": "Chewy Pork With Garlic Fla Thai Rice Verm 5 X 60GM"
        }
      ],
      "name": "超力 蒜香肉碎味泰米粉5包裝 60 GM",
      "price": "$24",
      "offer": "【2件$25】$25任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240916/a5b0bbe8-6a62-3517-88b6-be2dc655f831",
      "product_eng_name": "Chewy Pork With Garlic Fla Thai Rice Verm 5 X 60GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%9D%8E%E5%AD%90%E6%9F%92%20%E6%9F%B3%E5%B7%9E%E8%9E%BA%E8%9E%84%E7%B2%89%20330G/i/101328383.html",
      "uid": "1e915e359b7d3f867d036b052c014fe9",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "李子柒 柳州螺螄粉 330G",
          "price": "$16",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240717/d84faa33-2c33-315c-ae2d-7cb919b15cfd",
          "product_eng_name": "Liziqi Snail Rice Noodle Soup (Liuzhou Luosifen) 330GM"
        },
        {
          "name": "李子柒 柳州螺螄粉 330G",
          "price": "$16",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240717/d84faa33-2c33-315c-ae2d-7cb919b15cfd",
          "product_eng_name": "Liziqi Snail Rice Noodle Soup (Liuzhou Luosifen) 330GM"
        }
      ],
      "name": "李子柒 柳州螺螄粉 330G",
      "price": "$16",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240717/d84faa33-2c33-315c-ae2d-7cb919b15cfd",
      "product_eng_name": "Liziqi Snail Rice Noodle Soup (Liuzhou Luosifen) 330GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%A6%8F%E5%AD%97%E9%9D%9E%E6%B2%B9%E7%82%B8%E6%8B%89%E9%BA%B5%205%20X%2080GM/i/101353051.html",
      "uid": "905b797b29d39e5f2d2221fa88d1d99b",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "福字非油炸拉麵 5 X 80GM",
          "price": "$15",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250320/e15b1544-a3cd-341d-8400-d39065ec95e6",
          "product_eng_name": "Fuku Non Fried Noodle 5 X 80GM"
        },
        {
          "name": "福字非油炸拉麵 5 X 80GM",
          "price": "$15",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250320/e15b1544-a3cd-341d-8400-d39065ec95e6",
          "product_eng_name": "Fuku Non Fried Noodle 5 X 80GM"
        }
      ],
      "name": "福字非油炸拉麵 5 X 80GM",
      "price": "$15",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250320/e15b1544-a3cd-341d-8400-d39065ec95e6",
      "product_eng_name": "Fuku Non Fried Noodle 5 X 80GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/Meadows%E9%95%B7%E9%80%9A%E7%B2%89n18%20500GM/i/101579430.html",
      "uid": "c89bb826f782f903ecde435a7518266f",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "Meadows長通粉n18 500GM",
          "price": "$16",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231204/fe35cff4-3e80-381d-8726-ee482199b51f",
          "product_eng_name": "Meadows Penne Rigate N18 500GM"
        },
        {
          "name": "Meadows長通粉n18 500GM",
          "price": "$16",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231204/fe35cff4-3e80-381d-8726-ee482199b51f",
          "product_eng_name": "Meadows Penne Rigate N18 500GM"
        }
      ],
      "name": "Meadows長通粉n18 500GM",
      "price": "$16",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20231204/fe35cff4-3e80-381d-8726-ee482199b51f",
      "product_eng_name": "Meadows Penne Rigate N18 500GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%88%80%E5%98%9C%E8%87%BB%E5%93%81%E5%81%A5%E5%BA%B7%E6%B2%B9%E9%85%B8%E6%BF%83%E9%A6%99%E8%8A%B1%E7%94%9F%E6%B2%B93x900ml/i/101329666.html",
      "uid": "094b5e20980c63db74f34e6e6a36dadb",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "刀嘜臻品健康油酸濃香花生油3x900ml",
          "price": "$134",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240813/72755f11-b67d-3792-b40a-0166013b0371",
          "product_eng_name": "Knife Deluxe High Oleic Formula Peanut Oil 3x900ml"
        },
        {
          "name": "刀嘜臻品健康油酸濃香花生油3x900ml",
          "price": "$134",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240813/72755f11-b67d-3792-b40a-0166013b0371",
          "product_eng_name": "Knife Deluxe High Oleic Formula Peanut Oil 3x900ml"
        }
      ],
      "name": "刀嘜臻品健康油酸濃香花生油3x900ml",
      "price": "$134",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240813/72755f11-b67d-3792-b40a-0166013b0371",
      "product_eng_name": "Knife Deluxe High Oleic Formula Peanut Oil 3x900ml"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E4%BF%9D%E5%BE%97%20%E6%A9%84%E6%AC%96%E6%9E%9C%E6%B8%A3%E6%B2%B9%202%20X%201LT/i/113267964.html",
      "uid": "d8fc902bd5564dfbde10138843ae8ee9",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "保得 橄欖果渣油 2 X 1LT",
          "price": "$160",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230209/a6d6bda3-bbe8-48fa-94ba-27eb0f8e73bd",
          "product_eng_name": "Bontaste Pomace Olive Oil 2 x 1LT"
        },
        {
          "name": "保得 橄欖果渣油 2 X 1LT",
          "price": "$160",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230209/a6d6bda3-bbe8-48fa-94ba-27eb0f8e73bd",
          "product_eng_name": "Bontaste Pomace Olive Oil 2 x 1LT"
        }
      ],
      "name": "保得 橄欖果渣油 2 X 1LT",
      "price": "$160",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230209/a6d6bda3-bbe8-48fa-94ba-27eb0f8e73bd",
      "product_eng_name": "Bontaste Pomace Olive Oil 2 x 1LT"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%A3%BD%E6%A1%83%E7%B4%85%E8%96%AF%E7%B2%89%E8%A2%8B%E8%A3%9D%20300GM/i/101427739.html",
      "uid": "bdc0247a56eaf2ca2cdfd6161a1d74c6",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "壽桃紅薯粉袋裝 300GM",
          "price": "$9",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220505/a99fa727-1fe9-4fd8-bc01-4ee0b0dda010",
          "product_eng_name": "Sau Tao Sweet Potato Vermicelli 300GM"
        },
        {
          "name": "壽桃紅薯粉袋裝 300GM",
          "price": "$9",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220505/a99fa727-1fe9-4fd8-bc01-4ee0b0dda010",
          "product_eng_name": "Sau Tao Sweet Potato Vermicelli 300GM"
        }
      ],
      "name": "壽桃紅薯粉袋裝 300GM",
      "price": "$9",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20220505/a99fa727-1fe9-4fd8-bc01-4ee0b0dda010",
      "product_eng_name": "Sau Tao Sweet Potato Vermicelli 300GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%88%80%E5%98%9C%20%E7%B4%94%E6%AD%A3%E8%8A%A5%E8%8A%B1%E7%B1%BD%E6%B2%B9%20750ML/i/101359789.html",
      "uid": "bb30d1ebe06b7b791e526e58f2a448d6",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "刀嘜 純正芥花籽油 750ML",
          "price": "$38",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240520/e9496207-8aff-3291-94d5-c5515deb0c78",
          "product_eng_name": "Knife Pure Canola Oil 750ML"
        },
        {
          "name": "刀嘜 純正芥花籽油 750ML",
          "price": "$38",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240520/e9496207-8aff-3291-94d5-c5515deb0c78",
          "product_eng_name": "Knife Pure Canola Oil 750ML"
        }
      ],
      "name": "刀嘜 純正芥花籽油 750ML",
      "price": "$38",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240520/e9496207-8aff-3291-94d5-c5515deb0c78",
      "product_eng_name": "Knife Pure Canola Oil 750ML"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%97%A5%E6%B8%85%E5%90%88%E5%91%B3%E9%81%93%E9%A6%99%E8%BE%A3%E7%89%9B%E8%82%89%E5%91%B3%E6%9D%AF%E9%BA%B5%2075GM/i/101357234.html",
      "uid": "22b2ef46405e7508f9bd255fba5d071b",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "日清合味道香辣牛肉味杯麵 75GM",
          "price": "$8",
          "offer": "【2件$14.5】$14.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250327/a0b7b529-0958-33ad-92a3-171c0c65b82d",
          "product_eng_name": "(無法擷取英文名稱)"
        },
        {
          "name": "日清合味道香辣牛肉味杯麵 75GM",
          "price": "$8",
          "offer": "【2件$14.5】$14.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250327/a0b7b529-0958-33ad-92a3-171c0c65b82d",
          "product_eng_name": "Nissin Cup Noodles Spicy Beef 75GM"
        }
      ],
      "name": "日清合味道香辣牛肉味杯麵 75GM",
      "price": "$8",
      "offer": "【2件$14.5】$14.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250327/a0b7b529-0958-33ad-92a3-171c0c65b82d",
      "product_eng_name": "Nissin Cup Noodles Spicy Beef 75GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%A4%A7%E5%9C%B0%E4%B9%8B%E4%BD%9C%E5%81%A5%E5%BA%B7%E8%92%9F%E8%92%BB%E7%83%8F%E5%86%AC%20200GM/i/101366769.html",
      "uid": "406793ee1dd8fcd10bd89882a1cb4c2e",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "大地之作健康蒟蒻烏冬 200GM",
          "price": "$6",
          "offer": "【指定分類享$25換購】每買1件，即可以$25換購1件人氣產品；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220915/c6ec0538-764f-41bb-bb78-c09a9fda9a1b",
          "product_eng_name": "Nature's Creation Konnyaku Udon 200Gm"
        },
        {
          "name": "大地之作健康蒟蒻烏冬 200GM",
          "price": "$6",
          "offer": "【指定分類享$25換購】每買1件，即可以$25換購1件人氣產品；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220915/c6ec0538-764f-41bb-bb78-c09a9fda9a1b",
          "product_eng_name": "Nature's Creation Konnyaku Udon 200Gm"
        }
      ],
      "name": "大地之作健康蒟蒻烏冬 200GM",
      "price": "$6",
      "offer": "【指定分類享$25換購】每買1件，即可以$25換購1件人氣產品；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20220915/c6ec0538-764f-41bb-bb78-c09a9fda9a1b",
      "product_eng_name": "Nature's Creation Konnyaku Udon 200Gm"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E4%BA%94%E8%B1%90%E9%80%9A%E5%BF%83%E7%B1%B3%E7%B2%89%20454GM/i/101334656.html",
      "uid": "3b05dc557e181ed9947c04a420825611",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "五豐通心米粉 454GM",
          "price": "$8",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210513/ace7ea9b-ce81-4ba0-b46e-b5b9600a2679",
          "product_eng_name": "Ng Fung Rice Macaroni 454GM"
        },
        {
          "name": "五豐通心米粉 454GM",
          "price": "$8",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210513/ace7ea9b-ce81-4ba0-b46e-b5b9600a2679",
          "product_eng_name": "Ng Fung Rice Macaroni 454GM"
        }
      ],
      "name": "五豐通心米粉 454GM",
      "price": "$8",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210513/ace7ea9b-ce81-4ba0-b46e-b5b9600a2679",
      "product_eng_name": "Ng Fung Rice Macaroni 454GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%A3%BD%E6%A1%83%E5%84%AA%E8%B3%AA%E5%85%89%E8%BA%AB%E9%BA%B5%20350GM/i/101355749.html",
      "uid": "2a0406aa731b4cd1a35fa90baa6e0df5",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "壽桃優質光身麵 350GM",
          "price": "$8",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220505/94e4c3d6-e1bb-4ebf-ba22-74e5d6ebaca0",
          "product_eng_name": "Sau Tao Dried Noodle 350GM"
        },
        {
          "name": "壽桃優質光身麵 350GM",
          "price": "$8",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220505/94e4c3d6-e1bb-4ebf-ba22-74e5d6ebaca0",
          "product_eng_name": "Sau Tao Dried Noodle 350GM"
        }
      ],
      "name": "壽桃優質光身麵 350GM",
      "price": "$8",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20220505/94e4c3d6-e1bb-4ebf-ba22-74e5d6ebaca0",
      "product_eng_name": "Sau Tao Dried Noodle 350GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%A3%BD%E6%A1%83%E7%89%8C%E6%96%B0%E5%8A%A0%E5%9D%A1%E7%B1%B3%E7%B2%89%20400GM/i/101346733.html",
      "uid": "558b3c82ba167435c51dde97357e33b7",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "壽桃牌新加坡米粉 400GM",
          "price": "$15",
          "offer": "【2件$17】$17任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220505/67c20a98-cb30-4343-b189-0af70fe10478",
          "product_eng_name": "Sau Tao Singpore Rice Vermicelli 400GM"
        },
        {
          "name": "壽桃牌新加坡米粉 400GM",
          "price": "$15",
          "offer": "【2件$17】$17任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220505/67c20a98-cb30-4343-b189-0af70fe10478",
          "product_eng_name": "Sau Tao Singpore Rice Vermicelli 400GM"
        }
      ],
      "name": "壽桃牌新加坡米粉 400GM",
      "price": "$15",
      "offer": "【2件$17】$17任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20220505/67c20a98-cb30-4343-b189-0af70fe10478",
      "product_eng_name": "Sau Tao Singpore Rice Vermicelli 400GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E8%90%AC%E5%A1%94%E7%89%8C%E9%BE%8D%E5%8F%A3%E7%B2%89%E7%B5%B2%20250GM/i/101351070.html",
      "uid": "17c8f2fe368796af6ab5ea79f6217984",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "萬塔牌龍口粉絲 250GM",
          "price": "$8",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210125/731f518e-069e-4661-b71c-a2c48f089dbd",
          "product_eng_name": "Man Pagoda Longkou Vermicelli 250GM"
        },
        {
          "name": "萬塔牌龍口粉絲 250GM",
          "price": "$8",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210125/731f518e-069e-4661-b71c-a2c48f089dbd",
          "product_eng_name": "Man Pagoda Longkou Vermicelli 250GM"
        }
      ],
      "name": "萬塔牌龍口粉絲 250GM",
      "price": "$8",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210125/731f518e-069e-4661-b71c-a2c48f089dbd",
      "product_eng_name": "Man Pagoda Longkou Vermicelli 250GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E8%B6%85%E5%8A%9B%E9%86%AC%E7%88%86%E6%9D%AF%20x%20%E9%AD%94%E7%89%A9%E7%8D%B5%E4%BA%BA%206PC/i/101342357.html",
      "uid": "bf21c12045f8c56b65a8b5eeaf3bd769",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "超力醬爆杯 x 魔物獵人 6PC",
          "price": "$35",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250214/c5ed2051-6e5f-3f7e-bdef-eb49f3c0b3ed",
          "product_eng_name": "Chewy Cup Instant Vermicelli x Monster Hunter - 6 cups"
        },
        {
          "name": "超力醬爆杯 x 魔物獵人 6PC",
          "price": "$35",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250214/c5ed2051-6e5f-3f7e-bdef-eb49f3c0b3ed",
          "product_eng_name": "Chewy Cup Instant Vermicelli x Monster Hunter - 6 cups"
        }
      ],
      "name": "超力醬爆杯 x 魔物獵人 6PC",
      "price": "$35",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250214/c5ed2051-6e5f-3f7e-bdef-eb49f3c0b3ed",
      "product_eng_name": "Chewy Cup Instant Vermicelli x Monster Hunter - 6 cups"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E4%B8%89%E9%A4%8A%E7%89%9B%E9%AA%A8%E5%91%B3%E7%99%BD%E6%B9%AF%E9%BA%B5%20110GM/i/101327282.html",
      "uid": "5a78d454d0bfd286073a24864ae54e21",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "三養牛骨味白湯麵 110GM",
          "price": "$33",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230202/5d15ee6d-d689-4d17-b10b-baa5e1c3d99b",
          "product_eng_name": "Samyang Beef Bone Soup Noodle 110GM"
        },
        {
          "name": "三養牛骨味白湯麵 110GM",
          "price": "$33",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230202/5d15ee6d-d689-4d17-b10b-baa5e1c3d99b",
          "product_eng_name": "Samyang Beef Bone Soup Noodle 110GM"
        }
      ],
      "name": "三養牛骨味白湯麵 110GM",
      "price": "$33",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230202/5d15ee6d-d689-4d17-b10b-baa5e1c3d99b",
      "product_eng_name": "Samyang Beef Bone Soup Noodle 110GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E5%87%BA%E5%89%8D%E4%B8%80%E4%B8%81%20%E7%89%9B%E8%82%89%E5%8D%B3%E9%A3%9F%E9%BA%B5%2030%20X%20100GM/i/101334335.html",
      "uid": "17b271c25702e3564df97132efadf9ce",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱出前一丁 牛肉即食麵 30 X 100GM",
          "price": "$105",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231013/e49b1724-ff48-3051-b67f-fdee7e677d7f",
          "product_eng_name": "Nissin Demae Iccho Beef Instant Noodle Case 30 x 100GM"
        },
        {
          "name": "原箱出前一丁 牛肉即食麵 30 X 100GM",
          "price": "$105",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231013/e49b1724-ff48-3051-b67f-fdee7e677d7f",
          "product_eng_name": "Nissin Demae Iccho Beef Instant Noodle Case 30 x 100GM"
        }
      ],
      "name": "原箱出前一丁 牛肉即食麵 30 X 100GM",
      "price": "$105",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20231013/e49b1724-ff48-3051-b67f-fdee7e677d7f",
      "product_eng_name": "Nissin Demae Iccho Beef Instant Noodle Case 30 x 100GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E6%97%A5%E6%B8%85%E6%B5%B7%E9%AE%AE%E5%91%B3%E5%A4%A7%E6%9D%AF%E9%BA%B5%2012%20X%20100%20GM/i/113465609.html",
      "uid": "3f898175d3e977d5da269e8e620b2678",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱日清海鮮味大杯麵 12 X 100 GM",
          "price": "$105",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230728/e66ec348-2081-3567-bcd8-62585024b0ef",
          "product_eng_name": "Nissin Big Cup Seafood Case 12 X 100 GM"
        },
        {
          "name": "原箱日清海鮮味大杯麵 12 X 100 GM",
          "price": "$105",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230728/e66ec348-2081-3567-bcd8-62585024b0ef",
          "product_eng_name": "Nissin Big Cup Seafood Case 12 X 100 GM"
        }
      ],
      "name": "原箱日清海鮮味大杯麵 12 X 100 GM",
      "price": "$105",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230728/e66ec348-2081-3567-bcd8-62585024b0ef",
      "product_eng_name": "Nissin Big Cup Seafood Case 12 X 100 GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E8%9F%B9%E7%8E%8B%E9%BA%B5%E5%8D%B3%E9%A3%9F%E9%BA%B5(%E9%BA%BB%E6%B2%B9)%205%20X%2085GM/i/101874541.html",
      "uid": "5ef615d2810237200e1640cb1ff2b90c",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "蟹王麵即食麵(麻油) 5 X 85GM",
          "price": "$30",
          "offer": "【2件$50】$50任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220216/0d58c311-a3ee-4f29-99dd-5a16d2f127e7",
          "product_eng_name": "Crab King Noodle Instant Ramen 5 x 85GM"
        },
        {
          "name": "蟹王麵即食麵(麻油) 5 X 85GM",
          "price": "$30",
          "offer": "【2件$50】$50任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220216/0d58c311-a3ee-4f29-99dd-5a16d2f127e7",
          "product_eng_name": "Crab King Noodle Instant Ramen 5 x 85GM"
        }
      ],
      "name": "蟹王麵即食麵(麻油) 5 X 85GM",
      "price": "$30",
      "offer": "【2件$50】$50任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20220216/0d58c311-a3ee-4f29-99dd-5a16d2f127e7",
      "product_eng_name": "Crab King Noodle Instant Ramen 5 x 85GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%88%80%E5%98%9C%20%E9%87%91%E8%A3%9D%E5%81%A5%E5%BA%B7%E8%8A%B1%E7%94%9F%E9%A3%9F%E6%B2%B9900X3%20900%20ML/i/101379662.html",
      "uid": "9df4f2b52c0f091bd41f0693ceb5f41e",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米",
        "油"
      ],
      "history": [
        {
          "name": "刀嘜 金裝健康花生食油900X3 900 ML",
          "price": "$89",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231219/4185a18f-0ad6-30e1-8b71-2721a21caa79",
          "product_eng_name": "Knife Supreme Healthy Peanut Blended Oil 3 x 900ML"
        },
        {
          "name": "刀嘜 金裝健康花生食油900X3 900 ML",
          "price": "$89",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231219/4185a18f-0ad6-30e1-8b71-2721a21caa79",
          "product_eng_name": "Knife Supreme Healthy Peanut Blended Oil 3 x 900ML"
        }
      ],
      "name": "刀嘜 金裝健康花生食油900X3 900 ML",
      "price": "$89",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20231219/4185a18f-0ad6-30e1-8b71-2721a21caa79",
      "product_eng_name": "Knife Supreme Healthy Peanut Blended Oil 3 x 900ML"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%BE%A1%E5%93%81%E7%9A%87%E9%A0%82%E7%B4%9A%E6%B3%B0%E5%9C%8B%E8%8C%89%E8%8E%89%E9%A6%99%E7%B1%B3%205KG/i/101381359.html",
      "uid": "c90a7c8899cec443958d5c076b127b7c",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "御品皇頂級泰國茉莉香米 5KG",
          "price": "$62",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250306/d34ed9fd-e6f2-3963-ac98-9e3f8fcae92d",
          "product_eng_name": "Yu Pin King Thai Hom Mali Rice 5KG"
        }
      ],
      "name": "御品皇頂級泰國茉莉香米 5KG",
      "price": "$62",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250306/d34ed9fd-e6f2-3963-ac98-9e3f8fcae92d",
      "product_eng_name": "Yu Pin King Thai Hom Mali Rice 5KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E8%A2%8B%E9%BC%A0%E7%89%8C%E4%BD%8E%E5%8D%87%E7%B3%96%E6%8C%87%E6%95%B8%E7%99%BD%E7%B1%B3%202KG/i/101340750.html",
      "uid": "76cb6f69a9acafd2c1f3cf06e1c6d2a5",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "米"
      ],
      "history": [
        {
          "name": "袋鼠牌低升糖指數白米 2KG",
          "price": "$59",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230209/a5674b36-14d8-4053-9e36-2a50747ddaaf",
          "product_eng_name": "Kangaroo Brand Low Gi Rice 2KG"
        }
      ],
      "name": "袋鼠牌低升糖指數白米 2KG",
      "price": "$59",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230209/a5674b36-14d8-4053-9e36-2a50747ddaaf",
      "product_eng_name": "Kangaroo Brand Low Gi Rice 2KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%9C%89%E4%BD%A0%E4%B8%80%E9%9D%A2%E6%89%8B%E5%B7%A5%E6%97%A5%E6%9B%AC%E9%BA%B5%EF%BC%88%E5%9C%93%E9%BA%B5%EF%BC%89480GM/i/101357769.html",
      "uid": "07aaa4bb4214198cd53f021133030f7d",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "有你一面手工日曬麵（圓麵）480GM",
          "price": "$18",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240321/93c4f0b1-1819-3f62-b56a-c87e5fc80693",
          "product_eng_name": "You Ni Yi Mian Fine Round Noodle 480GM"
        }
      ],
      "name": "有你一面手工日曬麵（圓麵）480GM",
      "price": "$18",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240321/93c4f0b1-1819-3f62-b56a-c87e5fc80693",
      "product_eng_name": "You Ni Yi Mian Fine Round Noodle 480GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/Meadows%E6%84%8F%E5%A4%A7%E5%88%A9%E7%B4%B0%E9%BA%B5n2%20500GM/i/101579438.html",
      "uid": "6044788a52e884e5c0e7856fdc92b573",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "Meadows意大利細麵n2 500GM",
          "price": "$16",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231204/ef1a6ca8-0a4a-3dba-8b92-6a0672f9f697",
          "product_eng_name": "Meadows Vermicelli N2 500GM"
        }
      ],
      "name": "Meadows意大利細麵n2 500GM",
      "price": "$16",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20231204/ef1a6ca8-0a4a-3dba-8b92-6a0672f9f697",
      "product_eng_name": "Meadows Vermicelli N2 500GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/Meadows%E6%84%8F%E5%A4%A7%E5%88%A9%E7%B2%89n5%20500GM/i/101579429.html",
      "uid": "375ea1902e0ed3cc7833c6ff383cc324",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "Meadows意大利粉n5 500GM",
          "price": "$16",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231204/88ead757-a4e4-383d-aad2-eda302c54f7d",
          "product_eng_name": "Meadows Spaghetti N5 500GM"
        }
      ],
      "name": "Meadows意大利粉n5 500GM",
      "price": "$16",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20231204/88ead757-a4e4-383d-aad2-eda302c54f7d",
      "product_eng_name": "Meadows Spaghetti N5 500GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E8%BE%B2%E5%BF%83%E5%AE%89%E5%9F%8E%E6%B9%AF%E9%BA%B5%205%20X%20125GM/i/101381810.html",
      "uid": "34a9e49a76e4831236e9d08d27180546",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "農心安城湯麵 5 X 125GM",
          "price": "$25",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240916/5c3a846d-a9ba-3c83-8351-a39fcbdd868d",
          "product_eng_name": "Nong Shim An Sung Soup Noodles 5 X 125GM"
        }
      ],
      "name": "農心安城湯麵 5 X 125GM",
      "price": "$25",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240916/5c3a846d-a9ba-3c83-8351-a39fcbdd868d",
      "product_eng_name": "Nong Shim An Sung Soup Noodles 5 X 125GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/De%20Cecco%E6%84%8F%E5%A4%A7%E5%88%A9%E8%9E%BA%E7%B5%B2%E7%B2%89n34%20500GM/i/101322717.html",
      "uid": "bfd077b3aaac7e24ebdc690d030febce",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "De Cecco意大利螺絲粉n34 500GM",
          "price": "$29",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240917/71339056-1726-31cf-8ced-65c5c82fd37f",
          "product_eng_name": "De Cecco Fusilli n°34 500GM"
        }
      ],
      "name": "De Cecco意大利螺絲粉n34 500GM",
      "price": "$29",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240917/71339056-1726-31cf-8ced-65c5c82fd37f",
      "product_eng_name": "De Cecco Fusilli n°34 500GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%A3%BD%E6%A1%83%E5%A4%8F%E9%96%80%E9%BA%B5%E7%B7%9A%20300GM/i/101339258.html",
      "uid": "747f0b968b9828277a4933a96f52d358",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "壽桃夏門麵線 300GM",
          "price": "$8",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220505/fb6918ef-f2b6-45b0-8965-eca517a975e6",
          "product_eng_name": "Sau Tao Vermicelli 300GM"
        }
      ],
      "name": "壽桃夏門麵線 300GM",
      "price": "$8",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20220505/fb6918ef-f2b6-45b0-8965-eca517a975e6",
      "product_eng_name": "Sau Tao Vermicelli 300GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E5%85%AC%E4%BB%94%20%E9%9B%AA%E8%8F%9C%E5%91%B3%E7%B1%B3%E7%B2%89%2030%20X%2070GM/i/101353106.html",
      "uid": "3e02581df7f4763f566153c930482ef2",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱公仔 雪菜味米粉 30 X 70GM",
          "price": "$88",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230728/6af758cd-d9b1-3a4c-a09e-0cdfd156c864",
          "product_eng_name": "Doll Picked Vegetable Mifun Case 30 X 70GM"
        }
      ],
      "name": "原箱公仔 雪菜味米粉 30 X 70GM",
      "price": "$88",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230728/6af758cd-d9b1-3a4c-a09e-0cdfd156c864",
      "product_eng_name": "Doll Picked Vegetable Mifun Case 30 X 70GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E8%BE%B2%E5%BF%83%20%E8%BE%A3%E7%99%BD%E8%8F%9C%E6%8B%89%E9%BA%B5%20600%20GM/i/113559449.html",
      "uid": "2e2e5bf467ffe69bc29532f694839e24",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱農心 辣白菜拉麵 600 GM",
          "price": "$158",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231013/fdca346c-2cdd-3485-b91b-128337f53923",
          "product_eng_name": "Nong Shim Kimchi Ramyun Case 40 x 120GM"
        }
      ],
      "name": "原箱農心 辣白菜拉麵 600 GM",
      "price": "$158",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20231013/fdca346c-2cdd-3485-b91b-128337f53923",
      "product_eng_name": "Nong Shim Kimchi Ramyun Case 40 x 120GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%97%A5%E6%B8%85%E5%90%88%E5%91%B3%E9%81%93%E9%A6%99%E8%BE%A3%E6%B5%B7%E9%AE%AE%E5%A4%A7%E6%9D%AF%E9%BA%B5%20103GM/i/101857783.html",
      "uid": "90606bfda13a965715abd960972491dc",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "日清合味道香辣海鮮大杯麵 103GM",
          "price": "$11",
          "offer": "【2件$18】$18任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240711/ab54669e-03b8-3580-971a-1b8ce513e289",
          "product_eng_name": "Nissin Big Cup Spicy Seafood Flavour Noodles 103GM"
        }
      ],
      "name": "日清合味道香辣海鮮大杯麵 103GM",
      "price": "$11",
      "offer": "【2件$18】$18任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240711/ab54669e-03b8-3580-971a-1b8ce513e289",
      "product_eng_name": "Nissin Big Cup Spicy Seafood Flavour Noodles 103GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1KIKI%E9%A3%9F%E5%93%81%E9%9B%9C%E8%B2%A8%20%E6%A4%92%E9%BA%BB%E6%8B%8C%E9%BA%B55%E5%8C%85%E8%A3%9D10%20X%2090%20GM/i/101335765.html",
      "uid": "94affd8a3c1f2fb96c78b9ef9fefcb8d",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱KIKI食品雜貨 椒麻拌麵5包裝10 X 90 GM",
          "price": "$480",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231221/7ead5d8f-c747-3d14-9b89-f81eb1111b83",
          "product_eng_name": "KiKi Sichuan Spices Dry-Stirred Noodles Case 50 x 90GM"
        }
      ],
      "name": "原箱KIKI食品雜貨 椒麻拌麵5包裝10 X 90 GM",
      "price": "$480",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20231221/7ead5d8f-c747-3d14-9b89-f81eb1111b83",
      "product_eng_name": "KiKi Sichuan Spices Dry-Stirred Noodles Case 50 x 90GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E8%AE%9A%E5%B2%90%20%E4%BA%94%E4%BA%BA%E7%9C%BE%E7%83%8F%E5%86%AC%20500%20GM/i/114217196.html",
      "uid": "b058d20b6a3a257b66700cef8b2c1280",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "讚岐 五人眾烏冬 500 GM",
          "price": "$40",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240529/6a519ece-3f94-3151-8a36-a4e0d152f89b",
          "product_eng_name": "Sanuki Goninshu Udon 500GM"
        }
      ],
      "name": "讚岐 五人眾烏冬 500 GM",
      "price": "$40",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240529/6a519ece-3f94-3151-8a36-a4e0d152f89b",
      "product_eng_name": "Sanuki Goninshu Udon 500GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E6%97%A5%E6%B8%85%E6%96%B0%E6%84%8F%E6%B4%BE%20%E5%8D%A1%E9%82%A6%E5%B0%BC%E6%9D%AF%E6%84%8F%E7%B2%89%2012%20X%2092GM/i/101352274.html",
      "uid": "46a64f3e6d19caf7ccbc8e2aecfef2c7",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱日清新意派 卡邦尼杯意粉 12 X 92GM",
          "price": "$98",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230728/0897df6c-4338-3e09-a7e7-ae1047e7baaa",
          "product_eng_name": "Nissin Nupasta Carbonara Cup Case 12 X 92GM"
        }
      ],
      "name": "原箱日清新意派 卡邦尼杯意粉 12 X 92GM",
      "price": "$98",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230728/0897df6c-4338-3e09-a7e7-ae1047e7baaa",
      "product_eng_name": "Nissin Nupasta Carbonara Cup Case 12 X 92GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%BB%BF%E5%B0%8F%E9%A3%BD%20%E8%82%A5%E6%B1%81%E7%B1%B3%E7%B7%9A(%E9%99%84%E9%9F%BF%E9%88%90)%20310GM/i/113493904.html",
      "uid": "bb506080ef497489a988725f5da20489",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "滿小飽 肥汁米線(附響鈐) 310GM",
          "price": "$23",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240108/d2786174-bacc-3f1c-a87e-c565a406dc7e",
          "product_eng_name": "Man Xiao Bao Rice Noodles With Rich Sauce 310GM"
        }
      ],
      "name": "滿小飽 肥汁米線(附響鈐) 310GM",
      "price": "$23",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240108/d2786174-bacc-3f1c-a87e-c565a406dc7e",
      "product_eng_name": "Man Xiao Bao Rice Noodles With Rich Sauce 310GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%9C%89%E6%A9%9F%E5%B0%BC%E5%A5%A7%E6%9C%89%E6%A9%9F%E5%B0%8F%E9%BA%A5%E8%BB%8A%E5%9C%96%E6%A1%88%E7%B2%89%20250GM/i/101338354.html",
      "uid": "f373c2ca45bb2ba342dd6c50f27ae229",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "有機尼奧有機小麥車圖案粉 250GM",
          "price": "$21",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20200413/24d3420b-3e77-450f-875e-05f1b98b1e40",
          "product_eng_name": "Alce Nero Organic Vehicle Pasta 250GM"
        }
      ],
      "name": "有機尼奧有機小麥車圖案粉 250GM",
      "price": "$21",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20200413/24d3420b-3e77-450f-875e-05f1b98b1e40",
      "product_eng_name": "Alce Nero Organic Vehicle Pasta 250GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%97%A5%E6%B8%85%E5%90%88%E5%91%B3%E9%81%93xo%E9%86%AC%E6%B5%B7%E9%AE%AE%E5%91%B3%E6%9D%AF%E9%BA%B5%2075GM/i/101353219.html",
      "uid": "9e384b231213a4317cb31653cba62cf5",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "日清合味道xo醬海鮮味杯麵 75GM",
          "price": "$8",
          "offer": "【2件$14.5】$14.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250327/72a5eb28-754b-338c-8df9-c625c708145b",
          "product_eng_name": "Nissin Cup Noodles Xo S.Seafood 75GM"
        }
      ],
      "name": "日清合味道xo醬海鮮味杯麵 75GM",
      "price": "$8",
      "offer": "【2件$14.5】$14.5任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250327/72a5eb28-754b-338c-8df9-c625c708145b",
      "product_eng_name": "Nissin Cup Noodles Xo S.Seafood 75GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%97%A5%E6%B8%85%E5%87%BA%E5%89%8D%E4%B8%80%E4%B8%81%E9%BA%BB%E6%B2%B9%E5%91%B3%E7%A2%97%E9%BA%B5%2099GM/i/101357031.html",
      "uid": "2b446f232632102b3b55f59475709282",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "日清出前一丁麻油味碗麵 99GM",
          "price": "$10",
          "offer": "【2件$18】$18任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20200414/242cd64b-c82f-42e1-bdb4-a409c6621484",
          "product_eng_name": "Nissin Demae Iccho Sesame Oil Bowl Noodles 99GM"
        }
      ],
      "name": "日清出前一丁麻油味碗麵 99GM",
      "price": "$10",
      "offer": "【2件$18】$18任揀2件；數量有限，售完即止; 【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20200414/242cd64b-c82f-42e1-bdb4-a409c6621484",
      "product_eng_name": "Nissin Demae Iccho Sesame Oil Bowl Noodles 99GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%BE%A1%E5%93%81%E7%9A%87%20%E6%A4%92%E9%BA%BB%E6%8B%8C%E9%BA%B5%20101GM/i/114331521.html",
      "uid": "7dc234e00ad56d1c878c2132c09aedb9",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "御品皇 椒麻拌麵 101GM",
          "price": "$4",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20241106/26b7aecb-4301-3cd7-a4cb-2ea0c1439169",
          "product_eng_name": "Yu Pin King Chili Peppercorn Dry-stirred Noodles 101G"
        }
      ],
      "name": "御品皇 椒麻拌麵 101GM",
      "price": "$4",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20241106/26b7aecb-4301-3cd7-a4cb-2ea0c1439169",
      "product_eng_name": "Yu Pin King Chili Peppercorn Dry-stirred Noodles 101G"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E8%9E%BA%E9%9C%B8%E7%8E%8B%20%E7%B4%AB%E8%98%87%E5%91%B3%20%E8%9E%BA%E8%9E%84%E7%B2%89%20360%E5%85%8B/i/114918506.html",
      "uid": "fc9db45b9c6ea64afc08b3d6ad3ad44e",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "螺霸王 紫蘇味 螺螄粉 360克",
          "price": "$13",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250102/7cd18d59-3221-3276-a2c6-04a78184d83b",
          "product_eng_name": "No Wang Perilla Flaours Rice Noodles 360GM"
        }
      ],
      "name": "螺霸王 紫蘇味 螺螄粉 360克",
      "price": "$13",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250102/7cd18d59-3221-3276-a2c6-04a78184d83b",
      "product_eng_name": "No Wang Perilla Flaours Rice Noodles 360GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E5%AE%B6%E6%A8%82%E7%89%8C%20%E8%B1%AC%E9%AA%A8%E5%91%B3%E5%BF%AB%E7%86%9F%E9%80%9A%E5%BF%83%E7%B2%89%2030%20X%2080GM/i/101346830.html",
      "uid": "22bd4543dac6639764f3a6cb5e9c3827",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱家樂牌 豬骨味快熟通心粉 30 X 80GM",
          "price": "$150",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230213/8614894f-6566-4e7a-b52b-1059f8a862cb",
          "product_eng_name": "Knorr Pork Macaroni Case 30 X 80GM"
        }
      ],
      "name": "原箱家樂牌 豬骨味快熟通心粉 30 X 80GM",
      "price": "$150",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230213/8614894f-6566-4e7a-b52b-1059f8a862cb",
      "product_eng_name": "Knorr Pork Macaroni Case 30 X 80GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%86%8A%E4%BA%95%E8%AE%9A%E5%B2%90%E7%83%8F%E5%86%AC%204%20X%20200GM/i/101322140.html",
      "uid": "2ff42acc9d9523fbd896ce56f4bac491",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "熊井讚岐烏冬 4 X 200GM",
          "price": "$20",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210126/2d407e79-52a4-459c-8763-2a7ab0d83abe",
          "product_eng_name": "Kumai Sanuki Udon 4 X 200GM"
        }
      ],
      "name": "熊井讚岐烏冬 4 X 200GM",
      "price": "$20",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210126/2d407e79-52a4-459c-8763-2a7ab0d83abe",
      "product_eng_name": "Kumai Sanuki Udon 4 X 200GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%8E%9F%E7%AE%B1%E5%87%BA%E5%89%8D%E4%B8%80%E4%B8%81%E5%8C%97%E6%B5%B7%E9%81%93%20%E5%B0%8F%E9%BA%A5%E7%B2%89%E9%9B%9E%E7%99%BD%E6%B9%AF%20500%20GM/i/113557369.html",
      "uid": "6daa5056429c7429ebbeb41b6351e0d1",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "原箱出前一丁北海道 小麥粉雞白湯 500 GM",
          "price": "$120",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231013/c9b65b2d-ad59-3908-854b-10da8e27a9ec",
          "product_eng_name": "Nissin Demae Iccho Hokkaido Wheat Flour Tori Paitan Noodles Case 30 x 100GM"
        }
      ],
      "name": "原箱出前一丁北海道 小麥粉雞白湯 500 GM",
      "price": "$120",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20231013/c9b65b2d-ad59-3908-854b-10da8e27a9ec",
      "product_eng_name": "Nissin Demae Iccho Hokkaido Wheat Flour Tori Paitan Noodles Case 30 x 100GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E8%BE%B2%E5%BF%83%E9%9F%93%E5%BC%8F%E7%A7%98%E8%A3%BD%E6%8B%8C%E9%BA%B5%205%20X%20132GM/i/101359567.html",
      "uid": "a9521c0a5c47e2733eb7f63cc21376e1",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "即食粉麵/飯"
      ],
      "history": [
        {
          "name": "農心韓式秘製拌麵 5 X 132GM",
          "price": "$17",
          "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210520/a09913d4-3887-4bb1-9ce7-d1e38a10ff6c",
          "product_eng_name": "Nong Shim Kimchi Dried Noodle 5 X 132GM"
        }
      ],
      "name": "農心韓式秘製拌麵 5 X 132GM",
      "price": "$17",
      "offer": "【指定分類享$12換購】每買1件，即可以$12換購1件人氣產品；每單限享此優惠1次；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210520/a09913d4-3887-4bb1-9ce7-d1e38a10ff6c",
      "product_eng_name": "Nong Shim Kimchi Dried Noodle 5 X 132GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%8D%85%E7%90%83%E5%98%9C%20%E5%88%9D%E6%90%BE%E6%A9%84%E6%AC%96%E8%8A%A5%E8%8A%B1%E7%B1%BD%E6%B2%B9%204%20X%20900ML/i/101335831.html",
      "uid": "ac823c08e513fb6b6cdc69638aeb31b3",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "油"
      ],
      "history": [
        {
          "name": "獅球嘜 初搾橄欖芥花籽油 4 X 900ML",
          "price": "$119",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240502/b5a05016-1067-31a4-926d-ea942f60a9e2",
          "product_eng_name": "Lion & Globe Extra Virgin Olive Oil with Canola Oil 4 X 900ML"
        }
      ],
      "name": "獅球嘜 初搾橄欖芥花籽油 4 X 900ML",
      "price": "$119",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240502/b5a05016-1067-31a4-926d-ea942f60a9e2",
      "product_eng_name": "Lion & Globe Extra Virgin Olive Oil with Canola Oil 4 X 900ML"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%88%80%E5%98%9C%E7%B6%AD%E4%BB%96%E5%91%BDE%E5%81%A5%E5%BA%B7%E8%8A%B1%E7%94%9F%E9%A3%9F%E6%B2%B9%205%E5%8D%87/i/101329704.html",
      "uid": "87c9a51f78671254906aa06f010af6b6",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "油"
      ],
      "history": [
        {
          "name": "刀嘜維他命E健康花生食油 5升",
          "price": "$135",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240813/f3dd7880-2196-3668-ad9d-8864037606c1",
          "product_eng_name": "Knife Vitamin E Peanut Blended Oil 5L"
        }
      ],
      "name": "刀嘜維他命E健康花生食油 5升",
      "price": "$135",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240813/f3dd7880-2196-3668-ad9d-8864037606c1",
      "product_eng_name": "Knife Vitamin E Peanut Blended Oil 5L"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%8D%85%E7%90%83%E5%98%9C%E5%81%A5%E5%BA%B7%E7%B2%9F%E7%B1%B3%E6%B2%B9(%E9%9B%B6%E5%8F%8D%E5%BC%8F%E8%84%82%E8%82%AA)%203%20X%20900ML/i/102697391.html",
      "uid": "9171f9afcc824fba397d0f4246f64dab",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "油"
      ],
      "history": [
        {
          "name": "獅球嘜健康粟米油(零反式脂肪) 3 X 900ML",
          "price": "$89",
          "offer": "【買1件送1件贈品】購買每1件，即送1件人氣贈品；數量有限，售完即止",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220613/5117a167-b013-4ea8-86e5-c35e505d26ba",
          "product_eng_name": "Lion & Globe Pure Corn Oil (Zero Trans Fat) 3 X 900ML"
        }
      ],
      "name": "獅球嘜健康粟米油(零反式脂肪) 3 X 900ML",
      "price": "$89",
      "offer": "【買1件送1件贈品】購買每1件，即送1件人氣贈品；數量有限，售完即止",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20220613/5117a167-b013-4ea8-86e5-c35e505d26ba",
      "product_eng_name": "Lion & Globe Pure Corn Oil (Zero Trans Fat) 3 X 900ML"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/Meadows%E7%89%9B%E6%B2%B9%E6%9E%9C%E6%B2%B9500ML/i/114303976.html",
      "uid": "3f25778fc51ff0b2361cc3d00f950dda",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "油"
      ],
      "history": [
        {
          "name": "Meadows牛油果油500ML",
          "price": "$62",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240703/b4b242d0-8d80-3704-a9c6-da2a35880dd0",
          "product_eng_name": "Meadows Avocado Oil 500ML"
        }
      ],
      "name": "Meadows牛油果油500ML",
      "price": "$62",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240703/b4b242d0-8d80-3704-a9c6-da2a35880dd0",
      "product_eng_name": "Meadows Avocado Oil 500ML"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/Meadows%E8%91%A1%E8%90%84%E7%B1%BD%E6%B2%B9%201LT/i/101837278.html",
      "uid": "cb8624f4274462c9440df623c774c788",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "油"
      ],
      "history": [
        {
          "name": "Meadows葡萄籽油 1LT",
          "price": "$109",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231204/e060a044-2a46-36c7-9a5a-115deb7dd850",
          "product_eng_name": "Meadows Grape Seed Oil 1LT"
        }
      ],
      "name": "Meadows葡萄籽油 1LT",
      "price": "$109",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20231204/e060a044-2a46-36c7-9a5a-115deb7dd850",
      "product_eng_name": "Meadows Grape Seed Oil 1LT"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%A5%A7%E5%B0%BC%E7%89%8C%E6%A9%84%E6%AC%96%E6%9E%9C%E6%B8%A3%E6%B2%B9%201%E5%85%AC%E5%8D%87/i/101348603.html",
      "uid": "19a69035029bc95fbd9d62dd61964e80",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "油"
      ],
      "history": [
        {
          "name": "奧尼牌橄欖果渣油 1公升",
          "price": "$104",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240306/1a5437eb-2b49-3af1-a1ca-b03830747ee7",
          "product_eng_name": "Olitalia Pomace Olive Oil 1L"
        }
      ],
      "name": "奧尼牌橄欖果渣油 1公升",
      "price": "$104",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240306/1a5437eb-2b49-3af1-a1ca-b03830747ee7",
      "product_eng_name": "Olitalia Pomace Olive Oil 1L"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%8D%85%E7%90%83%E5%98%9C%E7%B2%9F%E7%B1%B3%E6%B2%B9%20600ML/i/101340729.html",
      "uid": "686289a31278af1467ed1725d14e5be7",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "油"
      ],
      "history": [
        {
          "name": "獅球嘜粟米油 600ML",
          "price": "$24",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20200413/15901b7f-e38a-4a09-8733-bd9d4390c04f",
          "product_eng_name": "Lion & Globe Corn Oil 600ML"
        }
      ],
      "name": "獅球嘜粟米油 600ML",
      "price": "$24",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20200413/15901b7f-e38a-4a09-8733-bd9d4390c04f",
      "product_eng_name": "Lion & Globe Corn Oil 600ML"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%99%BD%E7%BF%BC%E7%89%8C%E8%87%AA%E7%99%BC%E7%B2%89%201KG/i/101326538.html",
      "uid": "91288dbfd4bd6dc18836b6fe2d336925",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "麵粉、烘焙用料、梳打粉"
      ],
      "history": [
        {
          "name": "白翼牌自發粉 1KG",
          "price": "$37",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20200204/4ba666fb-ff93-42be-9bf8-55e5ccc6287a",
          "product_eng_name": "White Wings Self Raising Flour 1KG"
        }
      ],
      "name": "白翼牌自發粉 1KG",
      "price": "$37",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20200204/4ba666fb-ff93-42be-9bf8-55e5ccc6287a",
      "product_eng_name": "White Wings Self Raising Flour 1KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E8%A2%8B%E9%BC%A0%E7%89%8C%E8%87%AA%E7%99%BC%E7%B2%89%20800GM/i/101341661.html",
      "uid": "6f93d556411ae80f92d43c45f69e99cf",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "麵粉、烘焙用料、梳打粉"
      ],
      "history": [
        {
          "name": "袋鼠牌自發粉 800GM",
          "price": "$34",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20200413/73ad2321-e804-4b2f-b3f3-f5d0e0f7f6e8",
          "product_eng_name": "Kangaroo Self Raising Flour 800GM"
        }
      ],
      "name": "袋鼠牌自發粉 800GM",
      "price": "$34",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20200413/73ad2321-e804-4b2f-b3f3-f5d0e0f7f6e8",
      "product_eng_name": "Kangaroo Self Raising Flour 800GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%9D%8E%E7%A5%A5%E5%92%8C%20%E6%9C%A8%E8%96%AF%E7%B2%89%20300%20GM/i/113308119.html",
      "uid": "0252687132ed395dabf8d163b5bbd44a",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "麵粉、烘焙用料、梳打粉"
      ],
      "history": [
        {
          "name": "李祥和 木薯粉 300 GM",
          "price": "$18",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20241030/ccd8c4d3-e9e0-38a2-9792-67ffbff0be63",
          "product_eng_name": "TAPIOCA STARCH"
        }
      ],
      "name": "李祥和 木薯粉 300 GM",
      "price": "$18",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20241030/ccd8c4d3-e9e0-38a2-9792-67ffbff0be63",
      "product_eng_name": "TAPIOCA STARCH"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%BE%8E%E5%9C%8B%E8%B2%9D%E8%92%82%E6%9C%B1%E5%8F%A4%E5%8A%9B%E6%96%B9%E5%A1%8A%E8%9B%8B%E7%B3%95%E7%B2%89%2016.3OZ/i/101345609.html",
      "uid": "f71947301e3caea699ce4c1e3a155804",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "麵粉、烘焙用料、梳打粉"
      ],
      "history": [
        {
          "name": "美國貝蒂朱古力方塊蛋糕粉 16.3OZ",
          "price": "$30",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240527/7bcd5af5-8533-322a-bdaa-f9e3772c6a4c",
          "product_eng_name": "Betty Crocker Fudge Brownie Mix 16.3 OZ"
        }
      ],
      "name": "美國貝蒂朱古力方塊蛋糕粉 16.3OZ",
      "price": "$30",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240527/7bcd5af5-8533-322a-bdaa-f9e3772c6a4c",
      "product_eng_name": "Betty Crocker Fudge Brownie Mix 16.3 OZ"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%BE%8E%E5%9C%8B%E8%B2%9D%E8%92%82%E7%8F%AD%E6%88%9F%E7%B2%89%20500GM/i/101345608.html",
      "uid": "c8c44252c47345cc3cd679d1cc19a57c",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "麵粉、烘焙用料、梳打粉"
      ],
      "history": [
        {
          "name": "美國貝蒂班戟粉 500GM",
          "price": "$30",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20241003/1fe13444-80a8-3702-be43-d3bac00735c0",
          "product_eng_name": "Betty Crocker Combined Pancake Mix 500GM"
        }
      ],
      "name": "美國貝蒂班戟粉 500GM",
      "price": "$30",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20241003/1fe13444-80a8-3702-be43-d3bac00735c0",
      "product_eng_name": "Betty Crocker Combined Pancake Mix 500GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%BE%8E%E5%9C%8B%E8%B2%9D%E8%92%82%E9%9B%99%E9%87%8D%E6%9C%B1%E5%8F%A4%E5%8A%9B%E6%9B%B2%E5%A5%87%E7%B2%89%2017.5OZ/i/101324658.html",
      "uid": "870a77909357130af575922b79dad9c8",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "麵粉、烘焙用料、梳打粉"
      ],
      "history": [
        {
          "name": "美國貝蒂雙重朱古力曲奇粉 17.5OZ",
          "price": "$30",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250206/7ce53154-1b67-3e71-923b-c9c2918bcad9",
          "product_eng_name": "Betty Crocker Double Chocolate Cookie Mix 17.5OZ"
        }
      ],
      "name": "美國貝蒂雙重朱古力曲奇粉 17.5OZ",
      "price": "$30",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250206/7ce53154-1b67-3e71-923b-c9c2918bcad9",
      "product_eng_name": "Betty Crocker Double Chocolate Cookie Mix 17.5OZ"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%A3%AE%E6%B0%B8%E7%9B%92%E8%A3%9D%E5%85%8B%E6%88%9F%E7%B2%89%20300GM/i/101347268.html",
      "uid": "b307a0646f52a8b32ec0b749842eb3ed",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "麵粉、烘焙用料、梳打粉"
      ],
      "history": [
        {
          "name": "森永盒裝克戟粉 300GM",
          "price": "$29",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220516/1b596db3-8b28-471c-9958-ce11cbc24989",
          "product_eng_name": "Morinaga Hot Cake Mix Box 300GM"
        }
      ],
      "name": "森永盒裝克戟粉 300GM",
      "price": "$29",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20220516/1b596db3-8b28-471c-9958-ce11cbc24989",
      "product_eng_name": "Morinaga Hot Cake Mix Box 300GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E9%87%91%E5%83%8F%E7%89%8C%E9%BA%B5%E9%A3%BD%E9%BA%B5%E7%B2%89%201KG/i/101357423.html",
      "uid": "38f08083e79c93d6d266c710e5216c24",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "麵粉、烘焙用料、梳打粉"
      ],
      "history": [
        {
          "name": "金像牌麵飽麵粉 1KG",
          "price": "$30",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20200413/4109e59c-dbd5-4f2a-bef9-3b051b30a2e0",
          "product_eng_name": "Golden Statue Flour Bread 1KG"
        }
      ],
      "name": "金像牌麵飽麵粉 1KG",
      "price": "$30",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20200413/4109e59c-dbd5-4f2a-bef9-3b051b30a2e0",
      "product_eng_name": "Golden Statue Flour Bread 1KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%B3%9B%E6%B4%8B%E7%89%8C%E8%90%AC%E7%94%A8%E7%82%B8%E7%B2%89%20200GM/i/101343887.html",
      "uid": "2b02319d31178db063f2ac212fb565e3",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "麵粉、烘焙用料、梳打粉"
      ],
      "history": [
        {
          "name": "泛洋牌萬用炸粉 200GM",
          "price": "$9",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20200430/0def1718-1301-4121-8a8d-a6eaafb5dfb9",
          "product_eng_name": "Pan Pacific Fried Powder 200GM"
        }
      ],
      "name": "泛洋牌萬用炸粉 200GM",
      "price": "$9",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20200430/0def1718-1301-4121-8a8d-a6eaafb5dfb9",
      "product_eng_name": "Pan Pacific Fried Powder 200GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%97%A5%E6%9C%AC%E8%A3%BD%E7%B2%89%E5%A4%A9%E5%A9%A6%E7%BE%85%E7%82%B8%E7%B2%89%20500GM/i/101322279.html",
      "uid": "eede1364d0f2df3bb9c0e41b6c0020c3",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "麵粉、烘焙用料、梳打粉"
      ],
      "history": [
        {
          "name": "日本製粉天婦羅炸粉 500GM",
          "price": "$24",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20200430/b7614765-a447-477f-a5b7-139b3f624911",
          "product_eng_name": "Nippn Tempura Powder 500GM"
        }
      ],
      "name": "日本製粉天婦羅炸粉 500GM",
      "price": "$24",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20200430/b7614765-a447-477f-a5b7-139b3f624911",
      "product_eng_name": "Nippn Tempura Powder 500GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/MARMITE%20%E9%A6%AC%E9%BA%A5%E9%86%AC%20250%20GM/i/113728431.html",
      "uid": "b0610938dd677aabe16f288399c072f0",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "麵粉、烘焙用料、梳打粉"
      ],
      "history": [
        {
          "name": "MARMITE 馬麥醬 250 GM",
          "price": "$69",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240222/8b8ea271-17f1-3065-ada7-50a6a775810f",
          "product_eng_name": "Marmite Yeast Extract 250GM"
        }
      ],
      "name": "MARMITE 馬麥醬 250 GM",
      "price": "$69",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240222/8b8ea271-17f1-3065-ada7-50a6a775810f",
      "product_eng_name": "Marmite Yeast Extract 250GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%A4%AA%E5%8F%A4%E7%B3%96%E9%9C%9C%201LB/i/101332245.html",
      "uid": "b86ba42983ded23dd2a0d957920890df",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "麵粉、烘焙用料、梳打粉"
      ],
      "history": [
        {
          "name": "太古糖霜 1LB",
          "price": "$16",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20200414/e1a0b0b0-6567-493c-862d-11675b767915",
          "product_eng_name": "Taikoo Icing Sugar 1LB"
        }
      ],
      "name": "太古糖霜 1LB",
      "price": "$16",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20200414/e1a0b0b0-6567-493c-862d-11675b767915",
      "product_eng_name": "Taikoo Icing Sugar 1LB"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/Marie%E5%8D%83%E5%B1%A4%E7%89%9B%E6%B2%B9%E9%85%A5%E7%9A%AE%20230GM/i/102115631.html",
      "uid": "0ab032352c136933961de153606060cb",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "麵粉、烘焙用料、梳打粉"
      ],
      "history": [
        {
          "name": "Marie千層牛油酥皮 230GM",
          "price": "$47",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220624/8fd5ed48-fcc6-4048-9ede-bf760f994667",
          "product_eng_name": "Marie Puff Pastry Dough Rolls 230GM"
        }
      ],
      "name": "Marie千層牛油酥皮 230GM",
      "price": "$47",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20220624/8fd5ed48-fcc6-4048-9ede-bf760f994667",
      "product_eng_name": "Marie Puff Pastry Dough Rolls 230GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%89%8B%E9%8E%9A%E7%89%8C%E7%B4%94%E6%AD%A3%E6%A2%B3%E6%89%93%E7%B2%89%2016OZ/i/101343812.html",
      "uid": "af4bcc214e2fc104ad1f63a4823beaa7",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "麵粉、烘焙用料、梳打粉"
      ],
      "history": [
        {
          "name": "手鎚牌純正梳打粉 16OZ",
          "price": "$16",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20210510/51ff1060-f0ae-4fdd-9f47-24951c04585f",
          "product_eng_name": "Arm & Hammer Pure Baking Soda 16OZ"
        }
      ],
      "name": "手鎚牌純正梳打粉 16OZ",
      "price": "$16",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20210510/51ff1060-f0ae-4fdd-9f47-24951c04585f",
      "product_eng_name": "Arm & Hammer Pure Baking Soda 16OZ"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%B3%9B%E6%B4%8B%E7%89%8C%E6%B3%A1%E6%89%93%E7%B2%89%2056GM/i/101350535.html",
      "uid": "7a6eca5399cc474181856f42f6e7718a",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "麵粉、烘焙用料、梳打粉"
      ],
      "history": [
        {
          "name": "泛洋牌泡打粉 56GM",
          "price": "$9",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20201009/046b934c-1a8a-4885-bfbc-02f23dd8d882",
          "product_eng_name": "Pan Pacific Baking Powder 56GM"
        }
      ],
      "name": "泛洋牌泡打粉 56GM",
      "price": "$9",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20201009/046b934c-1a8a-4885-bfbc-02f23dd8d882",
      "product_eng_name": "Pan Pacific Baking Powder 56GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%A4%A7%E5%88%A9%E7%89%8C%E9%9B%B2%E5%91%A2%E6%8B%BF%E5%91%B3%E9%A6%99%E6%B2%B9%2028ML/i/101348315.html",
      "uid": "b9a40dab95730ad4f9f9ab3013522ced",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "麵粉、烘焙用料、梳打粉"
      ],
      "history": [
        {
          "name": "大利牌雲呢拿味香油 28ML",
          "price": "$19",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20200414/8d1f17aa-a893-479e-a2da-068b7c1d0fea",
          "product_eng_name": "Rayners Vanilla Essence 28ML"
        }
      ],
      "name": "大利牌雲呢拿味香油 28ML",
      "price": "$19",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20200414/8d1f17aa-a893-479e-a2da-068b7c1d0fea",
      "product_eng_name": "Rayners Vanilla Essence 28ML"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%B3%9B%E6%B4%8B%E7%89%8C%E9%85%B5%E6%AF%8D%E7%B2%89%2050GM/i/101341773.html",
      "uid": "eff6ec4a1893ca8fc024e2e1901a7fca",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "麵粉、烘焙用料、梳打粉"
      ],
      "history": [
        {
          "name": "泛洋牌酵母粉 50GM",
          "price": "$10",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20200413/7540c7ec-cfaa-40ee-a778-84305b8fe351",
          "product_eng_name": "Pan Pacific Active Dried Yeast 50GM"
        }
      ],
      "name": "泛洋牌酵母粉 50GM",
      "price": "$10",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20200413/7540c7ec-cfaa-40ee-a778-84305b8fe351",
      "product_eng_name": "Pan Pacific Active Dried Yeast 50GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/MEADOWS%20%E9%BB%91%E5%8A%A0%E4%BE%96%E5%AD%90%E5%91%B3%E5%95%AB%E5%96%B1%E7%B2%89%2080%20GM/i/113309474.html",
      "uid": "6e11061663b0cc7eb950aff3d16e9cd2",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "麵粉、烘焙用料、梳打粉"
      ],
      "history": [
        {
          "name": "MEADOWS 黑加侖子味啫喱粉 80 GM",
          "price": "$5",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231221/df6fd058-9487-3c5b-b92f-38aa3f4c895f",
          "product_eng_name": "Meadows Jelly Mix Blackcurrant 80GM"
        }
      ],
      "name": "MEADOWS 黑加侖子味啫喱粉 80 GM",
      "price": "$5",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20231221/df6fd058-9487-3c5b-b92f-38aa3f4c895f",
      "product_eng_name": "Meadows Jelly Mix Blackcurrant 80GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%B3%95%E5%9C%8B%E7%87%95%E5%AD%90%E7%89%8C%E5%8D%B3%E6%BA%B6%E9%85%B5%E6%AF%8D%E7%B2%89%2055GM/i/101338178.html",
      "uid": "4282cca8cd26c37c5c84b4e1f6d217ed",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "麵粉、烘焙用料、梳打粉"
      ],
      "history": [
        {
          "name": "法國燕子牌即溶酵母粉 55GM",
          "price": "$30",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240816/30bda2a3-2240-30c6-b519-e7687e179f58",
          "product_eng_name": "Saf Instant Baker Instant Yeast 55GM"
        }
      ],
      "name": "法國燕子牌即溶酵母粉 55GM",
      "price": "$30",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240816/30bda2a3-2240-30c6-b519-e7687e179f58",
      "product_eng_name": "Saf Instant Baker Instant Yeast 55GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/Essentials%20%E8%98%87%E6%89%93%E7%B2%89%20500%20%E5%85%8B/i/101362647.html",
      "uid": "fce3278ca7d069008da09a6be0d5ac99",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "麵粉、烘焙用料、梳打粉"
      ],
      "history": [
        {
          "name": "Essentials 蘇打粉 500 克",
          "price": "$25",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250219/54434938-f269-3e6c-b67d-d0995cdb5527",
          "product_eng_name": "Essentials Bicarbonate Soda 500GM"
        }
      ],
      "name": "Essentials 蘇打粉 500 克",
      "price": "$25",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250219/54434938-f269-3e6c-b67d-d0995cdb5527",
      "product_eng_name": "Essentials Bicarbonate Soda 500GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%A5%BD%E5%8B%92%E6%BB%8B%20%E5%A4%A9%E7%84%B6%E7%94%9C%E8%8F%8A%E4%BB%A3%E7%B3%96%E7%BD%90%E8%A3%9D%20350%20GM/i/113726056.html",
      "uid": "a684d24c0482f752bfd0bb4c86e203aa",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "麵粉、烘焙用料、梳打粉"
      ],
      "history": [
        {
          "name": "好勒滋 天然甜菊代糖罐裝 350 GM",
          "price": "$109",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240220/7a77d1a4-345e-3337-a795-2f969ace4cd0",
          "product_eng_name": "WHOLE EARTH STEVIA CANISTER 350 GM"
        }
      ],
      "name": "好勒滋 天然甜菊代糖罐裝 350 GM",
      "price": "$109",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240220/7a77d1a4-345e-3337-a795-2f969ace4cd0",
      "product_eng_name": "WHOLE EARTH STEVIA CANISTER 350 GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%A5%BD%E6%99%82%20%E7%84%A1%E7%B3%96%E5%8F%AF%E5%8F%AF%E7%B2%89%20226GM/i/103005696.html",
      "uid": "8cc27783e9b54ff15c55ad4ab73dd24c",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "麵粉、烘焙用料、梳打粉"
      ],
      "history": [
        {
          "name": "好時 無糖可可粉 226GM",
          "price": "$75",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20221025/50a7a71d-5468-4e5b-bc4e-d9bb31f8cb83",
          "product_eng_name": "Hershey's Unsweetened Cocoa 226GM"
        }
      ],
      "name": "好時 無糖可可粉 226GM",
      "price": "$75",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20221025/50a7a71d-5468-4e5b-bc4e-d9bb31f8cb83",
      "product_eng_name": "Hershey's Unsweetened Cocoa 226GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/Woolworths%20%E9%9B%B2%E5%91%A2%E6%8B%BF%E5%91%B3%E9%A6%99%E6%B2%B9%20200%E6%AF%AB%E5%8D%87/i/101362667.html",
      "uid": "14d57f2a8f64db48b26b431ddb6740d1",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "麵粉、烘焙用料、梳打粉"
      ],
      "history": [
        {
          "name": "Woolworths 雲呢拿味香油 200毫升",
          "price": "$60",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20250219/c12aec5c-725b-3fdc-8a83-e78ae6af0781",
          "product_eng_name": "Woolworths Vanilla Extract 200Ml"
        }
      ],
      "name": "Woolworths 雲呢拿味香油 200毫升",
      "price": "$60",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20250219/c12aec5c-725b-3fdc-8a83-e78ae6af0781",
      "product_eng_name": "Woolworths Vanilla Extract 200Ml"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%A5%BD%E6%99%82%E7%89%9B%E5%A5%B6%E6%9C%B1%E5%8F%A4%E5%8A%9B%E7%A2%8E%E7%89%87%20326GM/i/101367752.html",
      "uid": "2b8ca3f95a52c5a769f89007e26b51c4",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "麵粉、烘焙用料、梳打粉"
      ],
      "history": [
        {
          "name": "好時牛奶朱古力碎片 326GM",
          "price": "$58",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20200414/e3a6cfba-2cc6-4b67-b004-9bca9d1816ab",
          "product_eng_name": "Hershey's Milk Chocolate Chips 326GM"
        }
      ],
      "name": "好時牛奶朱古力碎片 326GM",
      "price": "$58",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20200414/e3a6cfba-2cc6-4b67-b004-9bca9d1816ab",
      "product_eng_name": "Hershey's Milk Chocolate Chips 326GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%AE%B6%E6%A8%82%E7%89%8C%E9%B7%B9%E7%B2%9F%E7%B2%89%20420GM/i/101323039.html",
      "uid": "820b1504488adefa9036ec9e52d19f05",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "麵粉、烘焙用料、梳打粉"
      ],
      "history": [
        {
          "name": "家樂牌鷹粟粉 420GM",
          "price": "$14",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220705/7fe9b47f-b8b9-4083-bf2f-e0004d5f7379",
          "product_eng_name": "Knorr Kingsford's Corn Starch 420GM"
        }
      ],
      "name": "家樂牌鷹粟粉 420GM",
      "price": "$14",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20220705/7fe9b47f-b8b9-4083-bf2f-e0004d5f7379",
      "product_eng_name": "Knorr Kingsford's Corn Starch 420GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%97%A5%E6%B8%85%E8%A3%BD%E7%B2%89%E5%BC%B7%E5%8A%9B%E5%B0%8F%E9%BA%A5%E7%B2%89-%E9%AB%98%E7%AD%8B%E7%B2%89%201KG/i/101322457.html",
      "uid": "8f6165bf219642e8171a299705c4297b",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "麵粉、烘焙用料、梳打粉"
      ],
      "history": [
        {
          "name": "日清製粉強力小麥粉-高筋粉 1KG",
          "price": "$58",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20200430/1b0cbe25-2d92-4251-a82d-e96e2bcec529",
          "product_eng_name": "Nisshin Camellia Wheat Flour 1KG"
        }
      ],
      "name": "日清製粉強力小麥粉-高筋粉 1KG",
      "price": "$58",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20200430/1b0cbe25-2d92-4251-a82d-e96e2bcec529",
      "product_eng_name": "Nisshin Camellia Wheat Flour 1KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E9%87%91%E7%89%8C%E9%BA%B5%E7%B2%89%202LB/i/101366984.html",
      "uid": "0a80e05d4f276aa0c18f33a681a13506",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "麵粉、烘焙用料、梳打粉"
      ],
      "history": [
        {
          "name": "金牌麵粉 2LB",
          "price": "$35",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230327/b1f27d07-2271-4bb2-9e80-e66f5123e4d9",
          "product_eng_name": "Gold Medal All Purpose Flour 2LB"
        }
      ],
      "name": "金牌麵粉 2LB",
      "price": "$35",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230327/b1f27d07-2271-4bb2-9e80-e66f5123e4d9",
      "product_eng_name": "Gold Medal All Purpose Flour 2LB"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/Meadows%E7%B2%9F%E7%B2%89%20420GM/i/101577722.html",
      "uid": "76b495bcb3a2ed458a7a59e1ea0a3aec",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "麵粉、烘焙用料、梳打粉"
      ],
      "history": [
        {
          "name": "Meadows粟粉 420GM",
          "price": "$10",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20231204/0737435b-729f-3d8c-985f-b71718349966",
          "product_eng_name": "Meadows Corn Starch 420GM"
        }
      ],
      "name": "Meadows粟粉 420GM",
      "price": "$10",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20231204/0737435b-729f-3d8c-985f-b71718349966",
      "product_eng_name": "Meadows Corn Starch 420GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/Bob's%20Red%20Mill%20%E9%9D%A2%E7%B2%89%2080OZ/i/101323133.html",
      "uid": "fc7e7f4dc2098af3045154a9e1bbd6eb",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "麵粉、烘焙用料、梳打粉"
      ],
      "history": [
        {
          "name": "Bob's Red Mill 面粉 80OZ",
          "price": "$62",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230810/7133bb5c-98ea-388e-9a66-06c3cd564b81",
          "product_eng_name": "Bob's Red Mill Unbleached White All-Purpose Flour 80OZ"
        }
      ],
      "name": "Bob's Red Mill 面粉 80OZ",
      "price": "$62",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230810/7133bb5c-98ea-388e-9a66-06c3cd564b81",
      "product_eng_name": "Bob's Red Mill Unbleached White All-Purpose Flour 80OZ"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/CJ%E5%84%AA%E8%B3%AA%E5%B0%8F%E9%BA%A5%E7%B2%89%E6%9C%AB%E4%B8%AD%E7%AD%8B%201KG/i/101358585.html",
      "uid": "c67429605c483ae1148ff6fcd74c76a5",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "麵粉、烘焙用料、梳打粉"
      ],
      "history": [
        {
          "name": "CJ優質小麥粉末中筋 1KG",
          "price": "$24",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230523/34f83a97-2b26-4bb4-b00b-e9ed6846b3bb",
          "product_eng_name": "CJ Premium Wheat Flour Medium Gluten 1KG"
        }
      ],
      "name": "CJ優質小麥粉末中筋 1KG",
      "price": "$24",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230523/34f83a97-2b26-4bb4-b00b-e9ed6846b3bb",
      "product_eng_name": "CJ Premium Wheat Flour Medium Gluten 1KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E6%B3%AE%E5%A1%98%E7%B4%94%E6%AD%A3%E9%A6%AC%E8%B9%84%E7%B2%89%20500GM/i/101341179.html",
      "uid": "6d002a91d407596ccf9ae0cc193bf17d",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "麵粉、烘焙用料、梳打粉"
      ],
      "history": [
        {
          "name": "泮塘純正馬蹄粉 500GM",
          "price": "$56",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230316/2a6bd20c-d49f-4b49-8da2-fd53c3b0d958",
          "product_eng_name": "Pan Tang Flour Water Chestnut 500GM"
        }
      ],
      "name": "泮塘純正馬蹄粉 500GM",
      "price": "$56",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230316/2a6bd20c-d49f-4b49-8da2-fd53c3b0d958",
      "product_eng_name": "Pan Tang Flour Water Chestnut 500GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E9%9B%99%E8%A2%8B%E9%BC%A0%E7%89%8C%E6%B0%B4%E7%A3%A8%E7%B2%98%E7%B1%B3%E7%B2%89%20600GM/i/101344800.html",
      "uid": "d4673a473dcbf0089a1b9187833f4bd9",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "麵粉、烘焙用料、梳打粉"
      ],
      "history": [
        {
          "name": "雙袋鼠牌水磨粘米粉 600GM",
          "price": "$12",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230320/24d6db16-57cd-4e71-b45b-adfaf2a7e400",
          "product_eng_name": "D.Kangaroo Rice Flour 600GM"
        }
      ],
      "name": "雙袋鼠牌水磨粘米粉 600GM",
      "price": "$12",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230320/24d6db16-57cd-4e71-b45b-adfaf2a7e400",
      "product_eng_name": "D.Kangaroo Rice Flour 600GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E7%99%BD%E7%BF%BC%E7%89%8C%E9%BA%B5%E7%B2%89%201KG/i/101326532.html",
      "uid": "718049793beb09275eb85f2a49f0b6fd",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "麵粉、烘焙用料、梳打粉"
      ],
      "history": [
        {
          "name": "白翼牌麵粉 1KG",
          "price": "$37",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20200204/dfd432b8-8584-4ba2-8a5e-054cb8ea95d7",
          "product_eng_name": "White Wings Plain Flour 1KG"
        }
      ],
      "name": "白翼牌麵粉 1KG",
      "price": "$37",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20200204/dfd432b8-8584-4ba2-8a5e-054cb8ea95d7",
      "product_eng_name": "White Wings Plain Flour 1KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/CJ%E5%84%AA%E8%B3%AA%E5%B0%8F%E9%BA%A5%E7%B2%89%E6%9C%AB%E9%AB%98%E7%AD%8B%201KG/i/101358584.html",
      "uid": "cf0450e2456d4552a3b89a2544e592a3",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "麵粉、烘焙用料、梳打粉"
      ],
      "history": [
        {
          "name": "CJ優質小麥粉末高筋 1KG",
          "price": "$24",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230523/ddcb5990-f117-4e23-a9c8-51d5b618acfc",
          "product_eng_name": "CJ Premium Wheat Flour Hi-Gluten 1KG"
        }
      ],
      "name": "CJ優質小麥粉末高筋 1KG",
      "price": "$24",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230523/ddcb5990-f117-4e23-a9c8-51d5b618acfc",
      "product_eng_name": "CJ Premium Wheat Flour Hi-Gluten 1KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E9%9B%99%E8%A2%8B%E9%BC%A0%E7%89%8C%E6%B0%B4%E7%A3%A8%E7%B3%AF%E7%B1%B3%E7%B2%89%20600GM/i/101344794.html",
      "uid": "a4703db161a3332933607fe5751d20c6",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "麵粉、烘焙用料、梳打粉"
      ],
      "history": [
        {
          "name": "雙袋鼠牌水磨糯米粉 600GM",
          "price": "$16",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230320/06996cce-829b-4301-838f-bd93c23adf09",
          "product_eng_name": "D.Kangaroo Glutinuous Rice Flour 600GM"
        }
      ],
      "name": "雙袋鼠牌水磨糯米粉 600GM",
      "price": "$16",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230320/06996cce-829b-4301-838f-bd93c23adf09",
      "product_eng_name": "D.Kangaroo Glutinuous Rice Flour 600GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/CJ%E5%84%AA%E8%B3%AA%E5%B0%8F%E9%BA%A5%E7%B2%89%E6%9C%AB%E4%BD%8E%E7%AD%8B%201KG/i/101358699.html",
      "uid": "42fa3bc1a50ed0c858c23d5c1c228882",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "麵粉、烘焙用料、梳打粉"
      ],
      "history": [
        {
          "name": "CJ優質小麥粉末低筋 1KG",
          "price": "$24",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230523/9ebdcdeb-773a-4543-9003-c7cb5819a953",
          "product_eng_name": "CJ Low Gluten Wheat Flour 1KG"
        }
      ],
      "name": "CJ優質小麥粉末低筋 1KG",
      "price": "$24",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230523/9ebdcdeb-773a-4543-9003-c7cb5819a953",
      "product_eng_name": "CJ Low Gluten Wheat Flour 1KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/Bob's%20Red%20Mill%E9%BA%B5%E5%8C%85%E7%B2%89%205LB/i/101332428.html",
      "uid": "f62c47426ad9e93610b3346264dd8351",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "麵粉、烘焙用料、梳打粉"
      ],
      "history": [
        {
          "name": "Bob's Red Mill麵包粉 5LB",
          "price": "$68",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20201019/2801a307-8b71-4c51-a693-e7a0e4da0dfa",
          "product_eng_name": "Bob's Red Mill Artisan Bread Flour 5LB"
        }
      ],
      "name": "Bob's Red Mill麵包粉 5LB",
      "price": "$68",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20201019/2801a307-8b71-4c51-a693-e7a0e4da0dfa",
      "product_eng_name": "Bob's Red Mill Artisan Bread Flour 5LB"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/Bob's%20Red%20Mill%E5%85%A8%E9%BA%A5%E9%BA%B5%E7%B2%89%2080OZ/i/101323139.html",
      "uid": "49c9cff7a7821e5307365729eb9edd19",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "麵粉、烘焙用料、梳打粉"
      ],
      "history": [
        {
          "name": "Bob's Red Mill全麥麵粉 80OZ",
          "price": "$55",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20220322/fa20b9d4-5108-4ebc-9430-ab35480df8b4",
          "product_eng_name": "Bob's Red Mill Whole Wheat Flour 80OZ"
        }
      ],
      "name": "Bob's Red Mill全麥麵粉 80OZ",
      "price": "$55",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20220322/fa20b9d4-5108-4ebc-9430-ab35480df8b4",
      "product_eng_name": "Bob's Red Mill Whole Wheat Flour 80OZ"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/Meadows%E5%A4%9A%E7%94%A8%E9%80%94%E9%BA%B5%E7%B2%89%20908GM/i/101577725.html",
      "uid": "d7d342189f39263d56229831abd85739",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "麵粉、烘焙用料、梳打粉"
      ],
      "history": [
        {
          "name": "Meadows多用途麵粉 908GM",
          "price": "$19",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240102/d99d893f-968d-3b76-a57b-fdb4ab487c47",
          "product_eng_name": "Meadows All Purpose Flour 908GM"
        }
      ],
      "name": "Meadows多用途麵粉 908GM",
      "price": "$19",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240102/d99d893f-968d-3b76-a57b-fdb4ab487c47",
      "product_eng_name": "Meadows All Purpose Flour 908GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E4%B9%9D%E9%BE%8D%E9%BA%B5%E7%B2%89%20%E5%98%89%E7%A6%BE%E7%89%8C%E7%89%B9%E7%B4%9A%E9%AB%98%E7%AD%8B%E9%BA%B5%E7%B2%89%201%20KG/i/113364183.html",
      "uid": "af46cec7cc785dcece7c7ca0a0f00616",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "麵粉、烘焙用料、梳打粉"
      ],
      "history": [
        {
          "name": "九龍麵粉 嘉禾牌特級高筋麵粉 1 KG",
          "price": "$36",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230704/97223d8d-4799-473f-be52-b0718f2dcc35",
          "product_eng_name": "KL Flour Mills Yellow Label Bread Flour 1KG"
        }
      ],
      "name": "九龍麵粉 嘉禾牌特級高筋麵粉 1 KG",
      "price": "$36",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230704/97223d8d-4799-473f-be52-b0718f2dcc35",
      "product_eng_name": "KL Flour Mills Yellow Label Bread Flour 1KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E5%AE%B6%E6%A8%82%E7%89%8C%E9%B7%B9%E7%B2%9F%E7%B2%89%20227GM/i/101330064.html",
      "uid": "64c00b66b606b5f27047dc8ce69c918c",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "麵粉、烘焙用料、梳打粉"
      ],
      "history": [
        {
          "name": "家樂牌鷹粟粉 227GM",
          "price": "$8",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240726/4ac2ce8b-76bf-3545-ae8e-2ebfc77da916",
          "product_eng_name": "Knorr Kingsford's Corn Startch 227GM"
        }
      ],
      "name": "家樂牌鷹粟粉 227GM",
      "price": "$8",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240726/4ac2ce8b-76bf-3545-ae8e-2ebfc77da916",
      "product_eng_name": "Knorr Kingsford's Corn Startch 227GM"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/%E4%B9%9D%E9%BE%8D%E9%BA%B5%E7%B2%89%20%E5%98%89%E7%A6%BE%E7%89%8C%E5%B0%88%E6%A5%AD%E7%B4%9A%E9%AB%98%E7%AD%8B%E9%BA%B5%E7%B2%89%201%20KG/i/113364228.html",
      "uid": "2fbd2e29b02ab8a1f75fbc753f61d85c",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "麵粉、烘焙用料、梳打粉"
      ],
      "history": [
        {
          "name": "九龍麵粉 嘉禾牌專業級高筋麵粉 1 KG",
          "price": "$36",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20230704/1e89b970-cbd6-4cf9-8692-a390af30d760",
          "product_eng_name": "KL Flour Mills Yellow Label Maste Grade Bread Flour 1KG"
        }
      ],
      "name": "九龍麵粉 嘉禾牌專業級高筋麵粉 1 KG",
      "price": "$36",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20230704/1e89b970-cbd6-4cf9-8692-a390af30d760",
      "product_eng_name": "KL Flour Mills Yellow Label Maste Grade Bread Flour 1KG"
    },
    {
      "url": "https://www.wellcome.com.hk/zh-hant/p/Meadows%E8%87%AA%E7%99%BC%E7%B2%89%20800GM/i/101577724.html",
      "uid": "a02ab5f36073b3b7879faa1496da679d",
      "main_category": [
        "糧油"
      ],
      "sub_categories": [
        "麵粉、烘焙用料、梳打粉"
      ],
      "history": [
        {
          "name": "Meadows自發粉 800GM",
          "price": "$18",
          "offer": "(無特別促銷)",
          "date": "07/04/2025",
          "image_url": "https://img.rtacdn-os.com/20240102/26dc3124-28fd-3e4d-8cea-6766bfb1d627",
          "product_eng_name": "Meadows Self Raising Flour 800GM"
        }
      ],
      "name": "Meadows自發粉 800GM",
      "price": "$18",
      "offer": "(無特別促銷)",
      "date": "07/04/2025",
      "image_url": "https://img.rtacdn-os.com/20240102/26dc3124-28fd-3e4d-8cea-6766bfb1d627",
      "product_eng_name": "Meadows Self Raising Flour 800GM"
    },
]
# ==============================================================================

def fix_grain_oil_inline(data_input, output_file):
    print("開始處理資料...")
    
    # 1. 識別資料結構 (List 或 Dict)
    products = []
    if isinstance(data_input, list):
        products = data_input
    elif isinstance(data_input, dict) and 'products' in data_input:
        products = data_input['products']
    else:
        print("錯誤：資料格式無法識別，請確保 source_data 是 List [ ... ] 或包含 'products' 的 Dict。")
        return

    fixed_count = 0
    
    # 2. 執行修正邏輯
    for product in products:
        # 檢查 main_category 是否包含 "糧油"
        main_cats = product.get('main_category', [])
        if "糧油" in main_cats:
            sub_cats = product.get('sub_categories', [])
            
            # 去除重複 (Deduplicate)
            unique_subs = list(set(sub_cats))
            
            # 修正邏輯：如果有多於一個分類，且包含「米」
            if len(unique_subs) > 1 and "米" in unique_subs:
                # 移除「米」，保留更具體的分類 (如 "即食粉麵/飯" 或 "油")
                unique_subs.remove("米")
                
                # 安全網：如果移除後變空了 (例如原本只有 ["米", "米"])，則把 "米" 加回去
                if not unique_subs:
                    unique_subs = ["米"]
                
                # 更新產品資料
                product['sub_categories'] = unique_subs
                fixed_count += 1

    print(f"修正完成！共修正了 {fixed_count} 個產品。")
    
    # 3. 輸出結果
    # 因為輸入是 List，這裡也輸出 List 格式
    output_data = products
    
    print(f"正在儲存至 {output_file} ...")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)
    print("完成。")

if __name__ == "__main__":
    # 執行修正，結果儲存為 debug-1.json
    fix_grain_oil_inline(source_data, 'debug-1.json')