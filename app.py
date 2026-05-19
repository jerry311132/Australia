import streamlit as st
from datetime import datetime

# 1. 網頁基本設定
st.set_page_config(
    page_title="2026 澳洲自駕隨身手冊", 
    page_icon="🦘", 
    layout="centered"
)

# 2. 注入自訂高級 CSS：加入風景背景圖、增加行距、打造手機左右滑動導覽列
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
    
    /* 📱 修正字體太擠：調大行高 (line-height) 與段落間距 */
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
    
    /* 狀態標籤 */
    .badge-no-car {
        background-color: #fee2e2;
        color: #dc2626;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.85rem !important;
        font-weight: 600;
        display: inline-block;
    }
    .badge-need-car {
        background-color: #dcfce7;
        color: #16a34a;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.85rem !important;
        font-weight: 600;
        display: inline-block;
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
    
    /* 🛝 讓單選鈕群組在手機上變成「可以左右水平滑動」的精美膠囊 */
    div[data-testid="stRadio"] > div {
        flex-direction: row !important;
        overflow-x: auto !important;
        white-space: nowrap !important;
        flex-wrap: nowrap !important;
        padding-bottom: 10px;
        -webkit-overflow-scrolling: touch;
    }
    div[data-testid="stRadio"] label {
        background: rgba(255, 255, 255, 0.7);
        padding: 8px 16px !important;
        border-radius: 20px !important;
        border: 1px solid #e2e8f0 !important;
        margin-right: 8px !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
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
    st.write("---")
    st.markdown("### ❄️ 澳洲 8 月冬季氣候預測\n* **墨爾本**：8°C - 14°C (濕冷多雨)\n* **雪梨**：10°C - 17°C (舒適偏涼)\n* **布里斯本**：11°C - 22°C (晴朗暖和)")

# 4. ▶️ 中央主畫面
st.markdown("""
<div class="hero-card">
    <h1 style="margin:0; font-size:1.9rem; letter-spacing:1px;">🇦🇺 2026 澳洲自駕隨身手冊</h1>
    <p style="margin:6px 0 0 0; opacity:0.85; font-size:0.9rem !important;">專案代號：Antigravity 視覺重塑版</p>
</div>
""", unsafe_allow_html=True)

# 導覽選單（手機上可左右滑動）
page = st.radio(
    "滑動切換選單：", 
    ["📅 12天完整行程", "🏨 住宿租車總覽", "⚠️ 貼心安全指南"], 
    horizontal=True
)

st.write("---")

# 5. 分頁內容實作
if page == "📅 12天完整行程":
    st.subheader("🗺️ 每日詳細行程安排")
    st.caption("💡 藍色帶底線的景點名稱都可以直接點擊開啟導航")
    st.write("")

    with st.expander("📅 7/31 (五) Day 1：抵達墨爾本"):
        st.markdown("""
        <div class="trip-day-header">✈️ 抵達墨爾本機場 → 市區 → 入住飯店</div>
        🏠 住宿飯店：<a href="https://maps.google.com/?q=Holiday+Inn+Express+Melbourne+Little+Collins" target="_blank">墨爾本小柯林斯智選假日酒店</a><br>
        🚗 租車狀態：<span class="badge-no-car">❌ 本日不租車</span>
        """, unsafe_allow_html=True)
        
    with st.expander("📅 8/1 (六) Day 2：墨爾本英倫風市區觀光"):
        st.markdown("""
        <div class="trip-day-header">📷 墨爾本經典市區景點打卡</div>
        🗺️ 景點導航：<br>
        • 🚂 歷史地標：<a href="https://maps.google.com/?q=Flinders+Street+Station" target="_blank">弗林德斯街車站</a><br>
        • 🎨 街頭藝術：<a href="https://maps.google.com/?q=Hosier+Lane" target="_blank">塗鴉巷 Hosier Lane</a><br><br>
        🏠 住宿飯店：<a href="https://maps.google.com/?q=Holiday+Inn+Express+Melbourne+Little+Collins" target="_blank">墨爾本小柯林斯智選假日酒店</a><br>
        🚗 租車狀態：<span class="badge-no-car">❌ 本日不租車</span>
        """, unsafe_allow_html=True)
        
    with st.expander("📅 8/2 (日) Day 3：彩虹小屋、蒸汽火車與企鵝歸巢 🚗"):
        st.markdown("""
        <div class="trip-day-header">🚗 啟動自駕 → 繽紛彩虹屋 → 復古火車 → 神仙企鵝</div>
        🗺️ 景點導航：<br>
        • 🏡 超萌必拍：<a href="https://maps.google.com/?q=Brighton+Bathing+Boxes" target="_blank">布萊頓彩虹小屋</a><br>
        • 🚂 森林鐵道：<a href="https://maps.google.com/?q=Puffing+Billy+Railway" target="_blank">普芬比利蒸汽火車</a><br>
        • 🐧 震撼奇景：<a href="https://maps.google.com/?q=Phillip+Island+Nature+Parks" target="_blank">菲利普島企鵝歸巢</a><br><br>
        🏠 住宿飯店：<a href="https://maps.google.com/?q=Holiday+Inn+Express+Melbourne+Little+Collins" target="_blank">墨爾本小柯林斯智選假日酒店</a><br>
        🚗 租車狀態：<span class="badge-need-car">🟢 需取租車 (2台)</span>
        """, unsafe_allow_html=True)
        
    with st.expander("📅 8/3 (一) Day 4：世界最美公路大洋路之旅 🚗"):
        st.markdown("""
        <div class="trip-day-header">🌊 退房出發 → Great Ocean Road (大洋路) → 看十二門徒</div>
        🏠 住宿飯店：<a href="https://maps.google.com/?q=Great+Ocean+Road+Tourist+Park" target="_blank">大洋路旅客公園飯店</a><br>
        🚗 租車狀態：<span class="badge-need-car">🟢 隨身自駕中 (2台)</span>
        """, unsafe_allow_html=True)
        
    with st.expander("📅 8/4 (二) Day 5：告別墨爾本，飛往雪梨 ✈️"):
        st.markdown("""
        <div class="trip-day-header">🌊 大洋路晨曦 → 機場還車 → 飛往雪梨 → 飯店 Check in</div>
        ✈️ 航班資訊：國內線航班 (16:40 墨爾本起飛 ~ 18:10 抵達雪梨)<br>
        🏠 住宿飯店：<a href="https://maps.google.com/?q=ibis+Styles+Sydney+Central" target="_blank">雪梨中央宜必思酒店</a><br>
        🚗 租車狀態：<span class="badge-need-car">🟢 機場還車前需用車 (2台)</span>
        """, unsafe_allow_html=True)
        
    with st.expander("📅 8/5 (三) Day 6：雪梨歌劇院與復古樂園"):
        st.markdown("""
        <div class="trip-day-header">⛪ 深入歌劇院內部導覽 → 🎡 繽紛港畔月神樂園</div>
        🗺️ 景點導航：<br>
        • 🎭 世界地標：<a href="https://maps.google.com/?q=Sydney+Opera+House" target="_blank">雪梨歌劇院導覽</a><br>
        • 🎡 拍照聖地：<a href="https://maps.google.com/?q=Luna+Park+Sydney" target="_blank">雪梨月神樂園</a><br><br>
        🏠 住宿飯店：<a href="https://maps.google.com/?q=ibis+Styles+Sydney+Central" target="_blank">雪梨中央宜必思酒店</a><br>
        🚗 租車狀態：<span class="badge-no-car">❌ 本日不租車</span>
        """, unsafe_allow_html=True)
        
    with st.expander("📅 8/6 (四) Day 7：藍山國家公園壯麗一日遊"):
        st.markdown("""
        <div class="trip-day-header">🏔️ 走訪三姐妹岩、搭乘經典景觀纜車</div>
        🎫 預訂平台：<a href="https://www.kkday.com" target="_blank">KKday 藍山專屬一日遊行程連結</a><br>
        🏠 住宿飯店：<a href="https://maps.google.com/?q=ibis+Styles+Sydney+Central" target="_blank">雪梨中央宜必思酒店</a><br>
        🚗 租車狀態：<span class="badge-no-car">❌ 本日不租車 (搭專車)</span>
        """, unsafe_allow_html=True)
        
    with st.expander("📅 8/7 (五) Day 8：南半球極致賞鯨體驗"):
        st.markdown("""
        <div class="trip-day-header">🐋 搭乘賞鯨船出海 → 雪梨市區自由購物</div>
        🏠 住宿飯店：<a href="https://maps.google.com/?q=ibis+Styles+Sydney+Central" target="_blank">雪梨中央宜必思酒店</a><br>
        🚗 租車狀態：<span class="badge-no-car">❌ 本日不租車</span>
        """, unsafe_allow_html=True)
        
    with st.expander("📅 8/8 (六) Day 9：飛往度假天堂黃金海岸 ✈️"):
        st.markdown("""
        <div class="trip-day-header">✈️ 雪梨飛黃金海岸 → 抵達陽光海岸 Airbnb → 衝向海灘</div>
        🏠 住宿飯店：<a href="https://www.airbnb.com" target="_blank">陽光海岸精選 Airbnb 網站</a><br>
        🚗 租車狀態：<span class="badge-no-car">❌ 本日不租車</span>
        """, unsafe_allow_html=True)
        
    with st.expander("📅 8/9 (日) Day 10：火車前進布里斯本"):
        st.markdown("""
        <div class="trip-day-header">🦘 黃金海岸搭火車 → Brisbane 市區巡禮 → 🍱 貨櫃市集</div>
        🗺️ 景點導航：<a href="https://maps.google.com/?q=Eat+Street+Northshore" target="_blank">Eat Street 貨櫃市集</a><br>
        🏠 住宿飯店：<a href="https://maps.google.com/?q=The+George+Design+Hotel+Brisbane" target="_blank">布里斯本喬治飯店</a><br>
        🚗 租車狀態：<span class="badge-no-car">❌ 本日不租車</span>
        """, unsafe_allow_html=True)
        
    with st.expander("📅 8/10 (一) Day 11：抱無尾熊與頂級夜景 🚗"):
        st.markdown("""
        <div class="trip-day-header">🐨 龍柏無尾熊動物園 → 🏔️ 庫薩山看全景落日</div>
        🗺️ 景點導航：<br>
        • 🐨 無尾熊聖地：<a href="https://maps.google.com/?q=Lone+Pine+Koala+Sanctuary" target="_blank">龍柏無尾熊保護區</a><br>
        • 🏔️ 俯瞰市區：<a href="https://maps.google.com/?q=Mount+Coot-tha+Summit+Lookout" target="_blank">庫薩山觀景台</a><br><br>
        🏠 住宿飯店：<a href="https://maps.google.com/?q=The+George+Design+Hotel+Brisbane" target="_blank">布里斯本喬治飯店</a><br>
        🚗 租車狀態：<span class="badge-need-car">🟢 需取租車 (2台)</span>
        """, unsafe_allow_html=True)
        
    with st.expander("📅 8/11 (二) Day 12：布里斯本市區漫步 / 回台 ✈️"):
        st.markdown("""
        <div class="trip-day-header">🏢 市區最後採買伴手禮 → ✈️ 機場還車辦登機</div>
        ✈️ 航班時間：⏳ 8/11 22:15 布里斯本起飛 ~ 8/12 05:10 抵達台灣<br>
        🗺️ 機場導航：<a href="https://maps.google.com/?q=Brisbane+Airport" target="_blank">布里斯本國際機場</a><br>
        🏠 住宿狀態：無住宿（夜宿機上）
        """, unsafe_allow_html=True)

elif page == "🏨 住宿租車總覽":
    st.subheader("📌 住宿預訂與自駕總覽")
    
    # 修正：加上 unsafe_allow_html=True，讓住宿網址連結能正常點選且完美呈現
    st.markdown("""
    ### 🏢 全程飯店快速導航（點擊直接開地圖）
    1. 📍 7/31 - 8/2 (3晚) 墨爾本：<a href="https://maps.google.com/?q=Holiday+Inn+Express+Melbourne+Little+Collins" target="_blank">墨爾本小柯林斯智選假日酒店</a>
    2. 📍 8/3 (1晚) 大洋路：<a href="https://maps.google.com/?q=Great+Ocean+Road+Tourist+Park" target="_blank">大洋路旅客公園飯店</a>
    3. 📍 8/4 - 8/7 (4晚) 雪梨：<a href="https://maps.google.com/?q=ibis+Styles+Sydney+Central" target="_blank">雪梨中央宜必思酒店</a>
    4. 📍 8/8 (1晚) 黃金海岸：<a href="https://www.airbnb.com" target="_blank">陽光海岸 AirBnb 專屬網頁</a>
    5. 📍 8/9 - 8/10 (2晚) 布里斯本：<a href="https://maps.google.com/?q=The+George+Design+Hotel+Brisbane" target="_blank">布里斯本喬治飯店</a>
    """, unsafe_allow_html=True)
    
    st.write("---")
    st.markdown("### 🚗 雙車自駕天數提醒")
    st.success("這次行程共有 **4天** 需要使用 **2台租車**：\n* 8/2：墨爾本周邊\n* 8/3：大洋路過夜自駕\n* 8/4：大洋路開回機場還車\n* 8/10：布里斯本近郊")

elif page == "⚠️ 貼心安全指南":
    st.subheader("💡 澳洲旅遊隨身注意事項")
    st.warning("🚗 駕車提醒：澳洲為右駕（靠左行駛），轉彎請默念「左小彎、右大彎」，進入圓環請務必禮讓右側來車！")
    st.info("🎒 隨身必備：台灣駕照正本 + 國際駕照、澳洲電子簽證 (ETA)、行動電源、禦寒衣服、八月防曬用品。")
