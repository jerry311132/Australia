import streamlit as st
from datetime import datetime
import pandas as pd

# 1. 網頁基本設定
st.set_page_config(
    page_title="2026 澳洲自駕隨身手冊", 
    page_icon="🦘", 
    layout="centered"
)

# 2. 定義清單與樣式
checklist_items = [
    "護照正本 (確認有效期限在 6 個月以上)",
    "澳洲 ETA 電子簽證 (建議列印或手機截圖)",
    "台灣駕照正本 + 國際駕照",
    "海外高回饋信用卡 + 少量澳幣現金",
    "澳洲規格轉接頭 + 延長線",
    "行動電源 (隨身攜帶)",
    "保暖防風外套 (澳洲8月是冬季)",
    "個人常備藥品",
    "手機網卡 / eSIM",
    "個人盥洗用品"
]

# 3. 核心 CSS 樣式 (把原本的精緻介面救回來)
st.markdown("""
<style>
    .hero-card {
        background: #1a365d;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        color: white;
        margin-bottom: 20px;
    }
    .trip-day-header {
        font-weight: 700; 
        color: #1a365d;
        border-left: 4px solid #3182ce;
        padding-left: 10px;
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

# 4. 側邊欄
with st.sidebar:
    st.markdown("### 🗺️ 澳洲旅程助手")
    target_date = datetime(2026, 7, 31)
    days_left = (target_date - datetime.now()).days
    st.metric("距離出發還有", f"{max(0, days_left)} 天")

# 5. 主畫面 (把原本的行程與清單功能補上)
st.markdown('<div class="hero-card"><h2>🇦🇺 2026 澳洲自駕隨身手冊</h2></div>', unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["📅 完整行程", "🏨 住宿租車", "🎒 行李清單"])

with tab1:
    st.markdown("### 🗺️ 每日詳細行程")
    with st.expander("📅 7/31 (五) Day 1：抵達墨爾本"):
        st.markdown('<div class="trip-day-header">✈️ 墨爾本機場 → 市區</div>', unsafe_allow_html=True)
    # (你可以把之前的所有行程內容繼續補在這裡...)

with tab3:
    st.subheader("🎒 澳洲自駕行李檢查清單")
    user_name = st.selectbox("👤 請選取你的名字：", ["駕駛老王", "副駕阿美", "隊員小明", "隊員小華"])
    
    st.write(f"請勾選 **{user_name}** 已準備的物品：")
    
    # 這裡顯示清單
    for item in checklist_items:
        st.checkbox(item, key=f"cb_{item}")
    
    if st.button("💾 儲存今日進度"):
        st.info("💡 系統提示：若要自動同步至 Google Sheets，請確保專案已配置正確的 GSheetsConnection。目前的狀態為純網頁展示，數據在重新整理後會重置。")
