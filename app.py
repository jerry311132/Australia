import streamlit as st
from datetime import datetime

# 1. 網頁基本設定
st.set_page_config(
    page_title="2026 澳洲自駕隨身手冊", 
    page_icon="🦘", 
    layout="centered"
)

# 2. 核心 CSS 注入：保留美觀的背景與字體，移除會造成錯誤的按鈕樣式
custom_style = """
<style>
    /* 隱藏預設元件 */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* 🌄 高級感全域背景圖：使用雪梨歌劇院輕微霧化背景 */
    .stApp {
        background: linear-gradient(rgba(245, 247, 250, 0.88), rgba(245, 247, 250, 0.88)), 
                    url('https://images.unsplash.com/photo-1524820197278-540916411e20?q=80&w=1080') no-repeat center center fixed;
        background-size: cover;
    }
    
    /* 頂部高級深藍漸層卡片 */
    .hero-card {
        background: linear-gradient(135deg, #112233 0%, #1a365d 100%);
        padding: 25px 20px;
        border-radius: 16px;
        color: white;
        text-align: center;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    
    /* 📱 解決字體擁擠問題：大幅提升行距與段落高度 */
    p, li, span {
        line-height: 1.9 !important;
        font-size: 1.05rem !important;
        color: #2d3748;
    }
    
    /* 讓展開摺疊面板 (Expander) 變成漂亮的現代毛玻璃字卡 */
    div[data-testid="stExpander"] {
        background: rgba(255, 255, 255, 0.75) !important;
        border-radius: 12px !important;
        border: 1px solid rgba(255, 255, 255, 0.6) !important;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05) !important;
        margin-bottom: 10px !important;
    }
    
    /* 🎨 行程標題微調 */
    .trip-day-header {
        font-size: 1.15rem !important;
        font-weight: 700 !important;
        color: #1a365d !important;
        margin-bottom: 10px;
        border-left: 4px solid #3182ce;
        padding-left: 10px;
    }
    
    /* 🔗 超連結美化：藍色清晰帶下劃線 */
    a {
        color: #2b6cb0 !important;
        text-decoration: underline !important;
        font-weight: 700 !important;
    }
    a:hover {
        color: #c53030 !important;
    }
    
    /* 美化官方 Tabs 頁籤字體大小 */
    button[data-baseweb="tab"] {
        font-size: 1.1rem !important;
        font-weight: 600 !important;
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
        st.markdown(f"<h1 style='color:#e53e3e; margin-top:0;'>{days_left} 天</h1>", unsafe_allow_html=True)
    else:
        st.success("🎉 澳洲之旅進行中！")
        
    st.write("---")
    st.markdown("### 🕒 澳洲當地時間 (AEST)\n※ 墨爾本/雪梨/布里斯本比台灣快 2 小時！")

# 4. ▶️ 中央主畫面大標題
st.markdown("""
<div class="hero-card">
    <h1 style="margin:0; font-size:1.8rem; font-weight:700; color:white;">🇦🇺 2026 澳洲自駕隨身手冊</h1>
</div>
""", unsafe_allow_html=True)

# 5. ⭐️ 核心修正：使用官方原生 Tabs，保證手機可滑動且絕對不會壞！
tab1, tab2, tab3 = st.tabs(["📅 12天完整行程", "🏨 住宿與租車", "⚠️ 安全指南"])

with tab1:
    st.caption("💡 點擊下方行程卡片展開，藍色帶底線字體可一鍵開啟地圖導航")
    
    with st.expander("📅 7/31 (五) Day 1：抵達墨爾本"):
        st.markdown("""
        <div class="trip-day-header">✈️ 抵達墨爾本機場 → 市區 → 入住飯店</div>
        • 🏠 **住宿**：<a href="https://maps.google.com/?q=Holiday+Inn+Express+Melbourne+Little+Collins" target="_blank">墨爾本小柯林斯智選假日酒店</a><br>
        • 🚗 **租車**：❌ 本日不租車
        """, unsafe_allow_html=True)
        
    with st.expander("📅 8/1 (六) Day 2：墨爾本市區觀光"):
        st.markdown("""
        <div class="trip-day-header">📷 墨爾本復古英倫風市區大遊覽</div>
        • 🗺️ **景點**：<a href="https://maps.google.com/?q=Flinders+Street+Station" target="_blank">弗林德斯街車站</a>、<a href="https://maps.google.com/?q=Hosier+Lane" target="_blank">塗鴉巷 Hosier Lane</a><br>
        • 🏠 **住宿**：<a href="https://maps.google.com/?q=Holiday+Inn+Express+Melbourne+Little+Collins" target="_blank">墨爾本小柯林斯智選假日酒店</a>
        """, unsafe_allow_html=True)
        
    with st.expander("📅 8/2 (日) Day 3：彩虹小屋與企鵝歸巢 🚗"):
        st.markdown("""
        <div class="trip-day-header">🚗 啟動自駕 → 蒸汽火車 → 神仙企鵝</div>
        • 🗺️ **景點**：<a href="https://maps.google.com/?q=Brighton+Bathing+Boxes" target="_blank">布萊頓彩虹小屋</a>、<a href="https://maps.google.com/?q=Puffing+Billy+Railway" target="_blank">蒸汽火車</a>、<a href="https://maps.google.com/?q=Phillip+Island+Nature+Parks" target="_blank">企鵝歸巢</a><br>
        • 🚗 **租車**：🟢 兩台自駕車今日取車出發！
        """, unsafe_allow_html=True)
        
    with st.expander("📅 8/3 (一) Day 4：大洋路壯遊 🚗"):
        st.markdown("""
        <div class="trip-day-header">🌊 Great Ocean Road 大洋路自駕 → 十二門徒石</div>
        • 🏠 **住宿**：<a href="https://maps.google.com/?q=Great+Ocean+Road+Tourist+Park" target="_blank">大洋路旅客公園飯店</a><br>
        • 🚗 **租車**：🟢 雙車自駕進行中
        """, unsafe_allow_html=True)

    with st.expander("📅 8/4 (二) Day 5：飛往雪梨 ✈️"):
        st.markdown("""
        <div class="trip-day-header">🌊 大洋路開回機場還車 → ✈️ 飛往雪梨</div>
        • 🏠 **住宿**：<a href="https://maps.google.com/?q=ibis+Styles+Sydney+Central" target="_blank">雪梨中央宜必思酒店</a><br>
        • 🚗 **租車**：🟢 機場還車
        """, unsafe_allow_html=True)

    with st.expander("📅 8/5 (三) Day 6：雪梨歌劇院與樂園"):
        st.markdown("""
        <div class="trip-day-header">🎭 深度探索雪梨市區與港灣</div>
        • 🗺️ **景點**：<a href="https://maps.google.com/?q=Sydney+Opera+House" target="_blank">雪梨歌劇院</a>、<a href="https://maps.google.com/?q=Luna+Park+Sydney" target="_blank">月神樂園</a><br>
        • 🏠 **住宿**：<a href="https://maps.google.com/?q=ibis+Styles+Sydney+Central" target="_blank">雪梨中央宜必思酒店</a>
        """, unsafe_allow_html=True)

    with st.expander("📅 8/6 (四) Day 7：藍山國家公園"):
        st.markdown("""
        <div class="trip-day-header">🏔️ 走訪絕美藍山國家公園</div>
        • 🎫 **行程**：<a href="https://www.kkday.com" target="_blank">KKday 藍山專車一日遊</a><br>
        • 🏠 **住宿**：<a href="https://maps.google.com/?q=ibis+Styles+Sydney+Central" target="_blank">雪梨中央宜必思酒店</a>
        """, unsafe_allow_html=True)

    with st.expander("📅 8/7 (五) Day 8：雪梨港賞鯨"):
        st.markdown("""
        <div class="trip-day-header">🐋 雪梨港出海賞鯨大體驗</div>
        • 🏠 **住宿**：<a href="https://maps.google.com/?q=ibis+Styles+Sydney+Central" target="_blank">雪梨中央宜必思酒店</a>
        """, unsafe_allow_html=True)

    with st.expander("📅 8/8 (六) Day 9：飛往黃金海岸 ✈️"):
        st.markdown("""
        <div class="trip-day-header">✈️ 飛往渡假天堂黃金海岸</div>
        • 🏠 **住宿**：<a href="https://www.airbnb.com" target="_blank">黃金海岸 AirBnb</a>
        """, unsafe_allow_html=True)

    with st.expander("📅 8/9 (日) Day 10：布里斯本市集"):
        st.markdown("""
        <div class="trip-day-header">🦘 前往布里斯本 → 夜遊熱鬧市集</div>
        • 🗺️ **景點**：<a href="https://maps.google.com/?q=Eat+Street+Northshore" target="_blank">Eat Street 貨櫃市集</a><br>
        • 🏠 **住宿**：<a href="https://maps.google.com/?q=The+George+Design+Hotel+Brisbane" target="_blank">布里斯本喬治飯店</a>
        """, unsafe_allow_html=True)

    with st.expander("📅 8/10 (一) Day 11：無尾熊與夜景 🚗"):
        st.markdown("""
        <div class="trip-day-header">🐨 親手抱無尾熊！市郊自駕遊</div>
        • 🗺️ **景點**：<a href="https://maps.google.com/?q=Lone+Pine+Koala+Sanctuary" target="_blank">龍柏無尾熊保護區</a>、<a href="https://maps.google.com/?q=Mount+Coot-tha+Summit+Lookout" target="_blank">庫薩山夕陽夜景</a><br>
        • 🚗 **租車**：🟢 布里斯本單日租車
        """, unsafe_allow_html=True)

    with st.expander("📅 8/11 (二) Day 12：準備回台 ✈️"):
        st.markdown("""
        <div class="trip-day-header">🛍️ 市區採購伴手禮 → 前往機場搭機</div>
        • 🗺️ **景點**：<a href="https://maps.google.com/?q=Brisbane+Airport" target="_blank">布里斯本國際機場</a>
        """, unsafe_allow_html=True)

with tab2:
    st.markdown("""
    <div class="trip-day-header">🏢 飯店清單快速地圖導航</div>
    1. 📍 **墨爾本 (3晚)**：<a href="https://maps.google.com/?q=Holiday+Inn+Express+Melbourne+Little+Collins" target="_blank">墨爾本小柯林斯智選假日酒店</a><br>
    2. 📍 **大洋路 (1晚)**：<a href="https://maps.google.com/?q=Great+Ocean+Road+Tourist+Park" target="_blank">大洋路旅客公園飯店</a><br>
    3. 📍 **雪梨 (4晚)**：<a href="https://maps.google.com/?q=ibis+Styles+Sydney+Central" target="_blank">雪梨中央宜必思酒店</a><br>
    4. 📍 **黃金海岸 (1晚)**：<a href="https://www.airbnb.com" target="_blank">黃金海岸 AirBnb</a><br>
    5. 📍 **布里斯本 (2晚)**：<a href="https://maps.google.com/?q=The+George+Design+Hotel+Brisbane" target="_blank">布里斯本喬治飯店</a>
    """, unsafe_allow_html=True)
    
    st.write("---")
    st.info("🚗 **租車提醒**：本次行程共有 **4天** 需使用租車 (8/2, 8/3, 8/4, 8/10)。")

with tab3:
    st.warning("🚗 **右駕核心口訣**：澳洲為右駕（靠左行駛），轉彎請默念「左小彎、右大彎」，進入圓環請絕對停車禮讓右側來車！")
    st.info("🎒 **出國檢查清單**：台灣駕照正本 + 國際駕照、護照與澳洲 ETA 電子簽證、澳洲三腳規格轉接頭。")
