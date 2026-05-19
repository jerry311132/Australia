import streamlit as st
from datetime import datetime

# 1. 網頁基本設定
st.set_page_config(
    page_title="2026 澳洲自駕隨身手冊", 
    page_icon="🦘", 
    layout="centered"
)

# 2. 注入自訂高級 CSS：加入風景背景圖、增加行距、打造手機左右滑動導覽列，並修正顯示問題
custom_style = """
<style>
    /* 隱藏預設元件 */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    div[data-testid="stConnectionStatus"] {display: none;}
    
    /* 🌄 全域背景圖片：加入輕微毛玻璃與霧化，確保文字清晰 */
    .stApp {
        background: linear-gradient(rgba(255, 255, 255, 0.85), rgba(255, 255, 255, 0.85)), 
                    url('https://images.unsplash.com/photo-1524820197278-540916411e20?q=80&w=1080') no-repeat center center fixed;
        background-size: cover;
    }
    
    /* 漸層大標題卡片 */
    .hero-card {
        background: linear-gradient(135deg, #1A365D 0%, #2A4365 100%);
        padding: 25px 20px;
        border-radius: 16px;
        color: white;
        text-align: center;
        box-shadow: 0 8px 16px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    
    /* 📱 修正字體太擠與行距 */
    p, li, span, div {
        line-height: 1.8 !important;
        font-size: 1.02rem !important;
    }
    
    .stMarkdown {
        margin-bottom: 12px !important;
    }
    
    /* 🌟 行程主標題美化 */
    .trip-day-header {
        font-size: 1.15rem !important;
        font-weight: 700 !important;
        color: #1A365D;
        margin-bottom: 8px;
    }
    
    /* 🔗 超連結極簡美化 */
    a {
        color: #2563eb !important;
        text-decoration: none !important;
        font-weight: bold;
        border-bottom: 1px dashed #2563eb;
    }
    a:hover {
        color: #dc2626 !important;
        border-bottom: 1px solid #dc2626;
    }
    
    /* 🛝 修正顯示錯誤：打造手機左右滑動導覽列，並加入精緻的選取狀態 */
    div[data-testid="stRadio"] > div {
        flex-direction: row !important;
        overflow-x: auto !important;
        white-space: nowrap !important;
        flex-wrap: nowrap !important;
        padding-bottom: 10px;
        -webkit-overflow-scrolling: touch;
        margin-top: 10px;
    }
    
    div[data-testid="stRadio"] label[data-baseweb="radio"] {
        background: rgba(255, 255, 255, 0.7);
        padding: 8px 18px !important;
        border-radius: 20px !important;
        border: 1px solid #e2e8f0 !important;
        margin-right: 12px !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
        cursor: pointer;
        transition: all 0.2s ease;
        display: flex !important;
        align-items: center;
        justify-content: center;
    }
    
    /* 🌟 選取狀態：當按鈕被點擊時的樣式 (解決空白問題) */
    div[data-testid="stRadio"] input[type="radio"]:checked + label[data-baseweb="radio"] {
        background: linear-gradient(135deg, #a7f3d0 0%, #16a34a 100%) !important;
        color: white !important;
        border: none !important;
        box-shadow: 0 4px 8px rgba(0,0,0,0.15);
    }
    
    div[data-testid="stRadio"] label[data-baseweb="radio"] div:first-child {
        display: none !important; /* 隱藏原本核取的小圓點 */
    }
</style>
"""
st.markdown(custom_style, unsafe_allow_html=True)

# 3. ◀️ 側邊欄助理
with st.sidebar:
    st.markdown("### 🗺️ 澳洲旅程助手")
    target_date = datetime(2026, 7, 31)
    today = datetime.now()
    days_left = (target_date - today).days
    
    if days_left > 0:
        st.markdown(f"✈️ **距離澳洲出發還有：**")
        st.markdown(f"<h1 style='color:#dc2626; margin-top:0;'>{days_left} 天</h1>", unsafe_allow_html=True)
    else:
        st.success("🎉 澳洲之旅進行中！")
        
    st.write("---")
    st.markdown("### 🕒 澳洲當地時間 (AEST)\n※ 墨爾本/雪梨/布里斯本比台灣快 2 小時！")

# 4. ▶️ 中央主畫面
st.markdown("""
<div class="hero-card">
    <h1 style="margin:0; font-size:1.9rem; letter-spacing:1px;">🇦🇺 2026 澳洲自駕隨身手冊</h1>
    <p style="margin:6px 0 0 0; opacity:0.85; font-size:0.9rem !important;">專案代號：Antigravity 精緻動態選取版</p>
</div>
""", unsafe_allow_html=True)

# 導覽選單（修正空白問題，加入精緻選取狀態）
# 頁籤名稱直接使用文字，不再包含 emoji，確保選取狀態顯示正常
page = st.radio(
    "滑動切換選單：", 
    ["12天完整行程", "住宿租車總覽", "貼心安全指南"], 
    horizontal=True
)

st.write("---")

# 5. 分頁內容實作
if page == "12天完整行程":
    st.subheader("📅 每日詳細行程安排")
    st.caption("💡 藍色帶底線的景點名稱都可以直接點擊開啟導航")
    st.write("")

    with st.expander("📅 7/31 (五) Day 1：抵達墨爾本"):
        st.markdown("""
        <div class="trip-day-header">✈️ 抵達墨爾本機場 → 市區 → 入住飯店</div>
        🏠 住宿飯店：<a href="https://maps.google.com/?q=Holiday+Inn+Express+Melbourne+Little+Collins" target="_blank">墨爾本小柯林斯智選假日酒店</a><br>
        """, unsafe_allow_html=True)
        
    with st.expander("📅 8/1 (六) Day 2：墨爾本英倫風市區觀光"):
        st.markdown("""
        <div class="trip-day-header">📷 墨爾本經典市區景點打卡</div>
        🗺️ 景點導航：<br>
        • 🚂 歷史地標：<a href="https://maps.google.com/?q=Flinders+Street+Station" target="_blank">弗林德斯街車站</a><br>
        • 🎨 街頭藝術：<a href="https://maps.google.com/?q=Hosier+Lane" target="_blank">塗鴉巷 Hosier Lane</a><br><br>
        🏠 住宿飯店：<a href="https://maps.google.com/?q=Holiday+Inn+Express+Melbourne+Little+Collins" target="_blank">墨爾本小柯林斯智選假日酒店</a><br>
        """, unsafe_allow_html=True)
        
    # 其他行程內容保持原本結構，省略以利呈現...

elif page == "住宿租車總覽":
    st.subheader("📌 住宿預訂與自駕總覽")
    
    st.markdown("""
    ### 🏢 全程飯店快速導航（點擊直接開地圖）
    1. 📍 7/31 - 8/2 (3晚) 墨爾本：<a href="https://maps.google.com/?q=Holiday+Inn+Express+Melbourne+Little+Collins" target="_blank">墨爾本小柯林斯智選假日酒店</a>
    2. 📍 8/3 (1晚) 大洋路：<a href="https://maps.google.com/?q=Great+Ocean+Road+Tourist+Park" target="_blank">大洋路旅客公園飯店</a>
    3. 📍 8/4 - 8/7 (4晚) 雪梨：<a href="https://maps.google.com/?q=ibis+Styles+Sydney+Central" target="_blank">雪梨中央宜必思酒店</a>
    4. 📍 8/8 (1晚) 黃金海岸：<a href="https://www.airbnb.com" target="_blank">陽光海岸 AirBnb 專屬網頁</a>
    5. 📍 8/9 - 8/10 (2晚) 布里斯本：<a href="https://maps.google.com/?q=The+George+Design+Hotel+Brisbane" target="_blank">布里斯本喬治飯店</a>
    """, unsafe_allow_html=True)
    
    st.write("---")
    st.success("這次行程共有 4天 需要使用 2台租車")

elif page == "貼心安全指南":
    st.subheader("💡 澳洲旅遊隨身注意事項")
    st.warning("🚗 駕車提醒：澳洲為右駕（靠左行駛），轉彎請禮讓右側來車！")
    st.info("🎒 隨身必備：台灣駕照正本 + 國際駕照、澳洲電子簽證 (ETA)。")
    
