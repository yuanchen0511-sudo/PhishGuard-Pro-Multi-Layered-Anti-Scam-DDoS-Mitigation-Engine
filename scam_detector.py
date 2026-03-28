import requests
import socket
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def generate_wordcloud(text, filename="scam_cloud.png"):
    # 這裡我們手動加入 font_path，指向 Windows 內建的微軟正黑體
    wc = WordCloud(
        font_path="C:/Windows/Fonts/msjh.ttc", 
        width=800, 
        height=400, 
        background_color='white',
        colormap='Reds'
    ).generate(text)
    
    plt.figure(figsize=(10, 5))  # <--- 檢查這一行，前面要跟上面的 wc 對齊！
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.savefig(filename)
    print(f"🎨 文字雲已生成！請查看資料夾中的: {filename}")
def analyze_scam_site(url):
    print(f"🔎 正在分析網址: {url}\n" + "-"*30)
    risk_score = 0
    
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')
        web_text = soup.get_text()

        # 1. 安全檢查 (功能 B)
        if not url.startswith("https"): risk_score += 30
        
        # 2. 關鍵字比對 (功能 C)
        scam_keywords = ["飆股", "獲利", "加LINE", "領取", "中獎", "兼職", "投資", "保證", "財富"]
        found_text = ""
        
        for word in scam_keywords:
            if word in web_text:
                count = web_text.count(word)
                risk_score += (10 * count)
                # 為了畫文字雲，我們把發現的詞重複放進去
                found_text += (word + " ") * count 

        # 3. 輸出分數
        print(f"📊 最終風險評分: {risk_score} 分")

        # 4. 生成視覺化圖表 (功能 D)
        if found_text:
            generate_wordcloud(found_text)
        else:
            print("💡 網頁中沒有偵測到明顯的關鍵字，不生成文字雲。")

    except Exception as e:
        print(f"❌ 分析失敗: {e}")

if __name__ == "__main__":
    target_url = input("請輸入要檢測的網址: ")
    analyze_scam_site(target_url)