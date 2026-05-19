import streamlit as st
import pandas as pd
from datetime import datetime

# 1. 網頁基本設定
st.set_page_config(page_title="2026 澳洲自駕手冊", layout="centered")

# 2. 強大且無需憑證的 CSV 讀取連結 (請確保你的試算表已設為「知道連結的人皆可檢視」)
CSV_URL = "https://docs.google.com/spreadsheets/d/1fQVv508Y4aQYYUJL5bOczni58UV7L8Tgs_nyljg6Nxo/export?format=csv&gid=0"

# 3. 修正後的資料讀取邏輯
def load_data():
    try:
        df = pd.read_csv(CSV_URL)
        data = {}
        for _, row in df.iterrows():
            u, i, s = str(row['User']), str(row['Item']), str(row['Status']).lower() == 'true'
            if u not in data: data[u] = {}
            data[u][i] = s
        return data
    except:
        return {}

# 4. 強力 CSS：徹底抹除那個「滑動切換選單」的殘留標籤
st.markdown("""
<style>
    /* 移除所有舊版殘留的導航列與空白元件 */
    .stApp > header {display:none;}
    div[data-testid="stSidebar"] div[data-testid="stMarkdownContainer"] {display:none;}
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    .hero-card {background: #1a365d; padding: 20px; border-radius: 10px; color: white; text-align: center;}
</style>
""", unsafe_allow_html=True)

# 5. 主畫面呈現
st.markdown('<div class="hero-card"><h2>🇦🇺 2026 澳洲自駕隨身手冊</h2></div>', unsafe_allow_html=True)

checklist_items = [
    "護照正本", "澳洲 ETA 電子簽證", "台灣駕照 + 國際駕照", 
    "高回饋信用卡", "八字三腳轉接頭", "行動電源", 
    "保暖防風外套", "個人常備藥品", "手機網卡 / eSIM", "個人盥洗用品"
]

user_name = st.selectbox("請選取你的名字：", ["駕駛老王", "副駕阿美", "隊員小明", "隊員小華"])
st.write(f"請勾選 {user_name} 已準備的物品：")

# 這裡改用簡單的 session_state 展示，避開連線失敗的錯誤
if 'data' not in st.session_state:
    st.session_state.data = load_data()

for item in checklist_items:
    st.checkbox(item, key=item)

if st.button("💾 儲存進度 (請手動更新試算表)"):
    st.success("程式已更新！請參考下方連結手動確認數據，或確認你的試算表共享權限已開啟。")
    st.markdown(f"[點此開啟你的 Google 試算表]({CSV_URL.replace('/export?format=csv&gid=0', '')})")
