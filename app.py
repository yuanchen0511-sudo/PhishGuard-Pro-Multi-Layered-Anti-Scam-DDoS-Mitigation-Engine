import streamlit as st
import time
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# 設定網頁標題
st.set_page_config(page_title="打詐資安探測器", layout="wide")


# 使用 Markdown 呈現 h1 標題
st.markdown("# 🛡️ 打詐資安探測器")
st.markdown("### 多層次網頁威脅分析與 DDoS 主動防禦系統")
st.divider()

# --- 側邊欄：使用者輸入 ---
st.sidebar.header("模擬操作區")
target_url = st.sidebar.text_input("輸入要偵測的網址", "http://127.0.0.1:8080/login.php")
start_btn = st.sidebar.button("開始分析與壓力測試")

if start_btn:
    # --- 1. 偵測層 (Scoring Engine) ---
    st.header("⚡ 第一階段：偵測層 (Scoring Engine)")
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("📝 風險評分說明")
        st.write("""
        我們的評分機制分為三部分：
        1. **協議檢查**：非 HTTPS 網站先扣 30 分。
        2. **語意分析**：偵測「飆股」、「加LINE」等關鍵字。
        3. **詞彙密度**：同一個詐騙詞彙出現次數越多，加權分數越高。
        """)
        st.metric(label="最終風險分數", value="85 分", delta="極高風險", delta_color="inverse")
    
    with col2:
        st.subheader("🎨 風險關鍵字視覺化")
        # 這裡模擬文字雲
        wc_text = "飆股 投資 獲利 加LINE 領取 財富 中獎 " * 5
        wc = WordCloud(font_path="C:/Windows/Fonts/msjh.ttc", width=800, height=400, background_color='white', colormap='Reds').generate(wc_text)
        st.image(wc.to_array())

    st.divider()

    # --- 2. 數據層 (Data Layer) ---
    st.header("📊 第二階段：數據層 (Data Layer)")
    st.write("當偵測系統運作時，伺服器資源的使用狀況如下：")
    
    # 模擬數據延遲
    chart_data = pd.DataFrame({
        '請求序號': range(1, 21),
        '延遲秒數(s)': [0.02, 0.03, 0.025, 0.04, 0.035, 0.05, 0.08, 0.09, 0.12, 0.15, 0.2, 0.22, 0.18, 0.15, 0.05, 0.04, 0.03, 0.03, 0.02, 0.02]
    })
    st.line_chart(chart_data.set_index('請求序號'))
    
    st.info("""
    **節點解釋：**
    * **1-10 筆**：系統處於正常處理狀態，延遲極低。
    * **11-15 筆**：系統開始執行 IP 寫入與比對，導致排隊效應，時間大幅飆升。
    * **15 筆後**：防禦機制全面啟動，直接拒絕請求，系統壓力瞬間釋放而下降。
    """)

    st.divider()

    # --- 3. 防禦層 (Defense Layer) ---
    st.header("🧱 第三階段：防禦層 (Defense Layer)")
    st.subheader("🛡️ 網站如何擋住攻擊？")
    
    with st.expander("點擊查看防禦邏輯詳解"):
        st.write("""
        當系統收到請求時，會執行以下防禦步驟：
        1. **IP 識別**：紀錄發起者的 IP 位置。
        2. **次數判定**：讀取 `ip_counter.txt`，確認該 IP 是否在 1 分鐘內超過 5 次請求。
        3. **強制阻斷**：一旦超過門檻，PHP 會直接下達 `http_response_code(429)`。
        4. **資源保護**：不進入後端資料庫查詢，節省伺服器 CPU 消耗。
        """)
        
    st.code("""
    // 防禦代碼核心
    if ($counts[$ip] > 5) {
        http_response_code(429); // 回傳 429 Too Many Requests
        exit;
    }
    """, language="php")

    st.success("✅ 實驗模擬完成！該網址已被列入黑名單，成功保護使用者資料。")

else:
    st.write("👈 請在左側輸入網址並點擊按鈕，開始多層次防禦模擬測試。")