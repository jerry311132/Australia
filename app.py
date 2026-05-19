import streamlit as st
from datetime import datetime

# 1. 網頁基本設定與標題
st.set_page_config(
    page_title="2026 澳洲自駕隨身手冊", 
    page_icon="🦘", 
    layout="wide"  # 使用寬版排版，在手機和電腦上看都很舒適
)

# 2. 注入自訂 CSS 樣式：打造極致精美的極簡現代風、毛玻璃字卡與進階配色
custom_css = """
<style>
    /* 隱藏預設元件 */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    div[data-testid="stConnectionStatus"] {display: none;}
    
    /* 漸層大標題卡片 */
    .hero-card {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        padding: 30px;
        border-radius: 20px;
        color: white;
        text-align: center;
        box-shadow: 0 10px 20px rgba(0,0,0,0.15);
        margin-bottom: 25px;
    }
    
    /* 行程彩色字卡設計 */
    .trip-day-header {
        font-size: 1.2rem;
        font-weight: bold;
        color: #1e3c72;
        margin-top: 10px;
    }
    
    /* 狀態標籤 */
    .badge-no-car {
        background-color: #ffeef0;
        color: #e41749;
        padding: 3px 10px;
        border-radius: 12px;
        font-size: 0.85rem;
        font-weight: bold;
    }
    .badge-need-car {
        background-color: #e6f7ed;
        color: #1f9353;
        padding: 3px 10px;
        border-radius: 12px;
        font-size: 0.85rem;
        font-weight: bold;
    }
    
    /* 超連結美化 */
    a {
        color: #2a5298 !important;
        text-decoration: none !important;
        font-weight: bold;
    }
    a:hover {
        color: #ff6b6b !important;
        text-decoration: underline !important;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# 3. ◀️ 側邊欄（Sidebar）資訊全面回歸與擴充
with st.sidebar:
    st.markdown("### 🗺️ 澳洲旅程助手")
    
    # 倒數計時功能 (目標設定為 2026/07/31)
    target_date = datetime(2026, 7, 31)
    today = datetime.now()
    days_left = (target_date - today).days
    
    if days_left > 0:
        st.markdown(f"✈️ **距離澳洲出發還有：**")
        st.markdown(f"<h1 style='color:#e41749; margin-top:0;'>{days_left} 天</h1>", unsafe_allow_html=True)
    else:
        st.success("🎉 澳洲之旅進行中！")
        
    st.write("---")
    
    # 時差提醒
    st.markdown("### 🕒 澳洲當地時間 (AEST)")
    st.caption("※ 墨爾本/雪梨/布里斯本比台灣快 2 小時！")
    
    st.write("---")
    
    # 冬季氣候預測
    st.markdown("### ❄️ 澳洲 8 月冬季氣候預測")
    st.markdown("""
    * **墨爾本 (Melbourne)**：8°C - 14°C  
      🌦️ *濕冷多雨，務必帶防風厚外套與雨傘！*
    * **雪梨 (Sydney)**：10°C - 17°C  
      🌤️ *氣候舒適，涼爽，早晚偏冷。*
    * **布里斯本 (Brisbane)**：11°C - 22°C  
      ☀️ *溫暖晴朗，非常舒適，防曬必備！*
    """)

# 4. ▶️ 中央主畫面（Main Content）
# 頂部大漸層字卡
st.markdown("""
<div class="hero-card">
    <h1 style="margin:0; font-size:2.2rem;">AU 2026 澳洲自駕隨身手冊</h1>
    <p style="margin:10px 0 0 0; opacity:0.85;">📱 手機隨身優化視覺版（專案代號：Antigravity 完全體）</p>
</div>
""", unsafe_allow_html=True)

# 頁籤選單美化
page = st.radio(
    "請選擇查看項目：", 
    ["📅 12天完整行程", "🏨 住宿與租車總覽", "⚠️ 貼心安全指南"], 
    horizontal=True
)

st.write("---")

# 5. 各頁面精美內容實作
if page == "📅 12天完整行程":
    st.subheader("🗺️ 12天詳細行程安排")
    st.caption("💡 點擊下方藍色字體可以直接開地圖或網站導航喔！")
    
    # 快速跳轉按鈕組（示意）
    st.markdown("**快速跳轉區域：** `全部天數` | `墨爾本段 (D1-D5)` | `雪梨段 (D5-D9)` | `昆士蘭段 (D9-D12)`")
    st.write("")

    with st.expander("📅 7/31 (五) Day 1：抵達墨爾本"):
        st.markdown("""
        <div class="trip-day-header">✈️ 抵達墨爾本機場 → 市區 → 入住飯店</div>
        * **🏠 住宿飯店**：👉 <a href="https://maps.google.com/?q=Holiday+Inn+Express+Melbourne+Little+Collins" target="_blank">墨爾本小柯林斯智選假日酒店</a>
        * **🚗 租車狀態**：<span class="badge-no-car">❌ 本日不租車</span>
        """, unsafe_allow_html=True)
        
    with st.expander("📅 8/1 (六) Day 2：墨爾本英倫風市區觀光"):
        st.markdown("""
        <div class="trip-day-header">📷 墨爾本經典市區景點打卡</div>
        * **景點導航**：
            * 🚂 歷史地標：<a href="https://maps.google.com/?q=Flinders+Street+Station" target="_blank">弗林德斯街車站</a>
            * 🎨 街頭藝術：<a href="https://maps.google.com/?q=Hosier+Lane" target="_blank">塗鴉巷 Hosier Lane</a>
        * **🏠 住宿飯店**：👉 <a href="https://maps.google.com/?q=Holiday+Inn+Express+Melbourne+Little+Collins" target="_blank">墨爾本小柯林斯智選假日酒店</a>
        * **🚗 租車狀態**：<span class="badge-no-car">❌ 本日不租車</span>
        """, unsafe_allow_html=True)
        
    with st.expander("📅 8/2 (日) Day 3：彩虹小屋、蒸汽火車與企鵝歸巢 🚗"):
        st.markdown("""
        <div class="trip-day-header">🚗 啟動自駕 → 繽紛彩虹屋 → 復古火車 → 神仙企鵝</div>
        * **景點導航**：
            * 🏡 超萌必拍：<a href="https://maps.google.com/?q=Brighton+Bathing+Boxes" target="_blank">布萊頓彩虹小屋</a>
            * 🚂 森林鐵道：<a href="https://maps.google.com/?q=Puffing+Billy+Railway" target="_blank">普芬比利蒸汽火車</a>
            * 🐧 震撼奇景：<a href="https://maps.google.com/?q=Phillip+Island+Nature+Parks" target="_blank">菲利普島企鵝歸巢</a>
        * **🏠 住宿飯店**：👉 <a href="https://maps.google.com/?q=Holiday+Inn+Express+Melbourne+Little+Collins" target="_blank">墨爾本小柯林斯智選假日酒店</a>
        * **🚗 租車狀態**：<span class="badge-need-car">🟢 需取租車 (2台)</span>
        """, unsafe_allow_html=True)
        
    with st.expander("📅 8/3 (一) Day 4：世界最美公路大洋路之旅 🚗"):
        st.markdown("""
        <div class="trip-day-header">🌊 退房出發 → Great Ocean Road (大洋路) → 看十二門徒</div>
        * **🏠 住宿飯店**：👉 <a href="https://maps.google.com/?q=Great+Ocean+Road+Tourist+Park" target="_blank">大洋路旅客公園飯店 (Great Ocean Road Tourist Park)</a>
        * **🚗 租車狀態**：<span class="badge-need-car">🟢 隨身自駕中 (2台)</span>
        """, unsafe_allow_html=True)
        
    with st.expander("📅 8/4 (二) Day 5：告別墨爾本，飛往雪梨 ✈️"):
        st.markdown("""
        <div class="trip-day-header">🌊 大洋路晨曦 → 機場還車 → 飛往雪梨 → 飯店 Check in</div>
        * **✈️ 航班資訊**：國內線航班 (16:40 墨爾本起飛 ~ 18:10 抵達雪梨)
        * **🏠 住宿飯店**：👉 <a href="https://maps.google.com/?q=ibis+Styles+Sydney+Central" target="_blank">雪梨中央宜必思酒店 (ibis Styles)</a>
        * **🚗 租車狀態**：<span class="badge-need-car">🟢 機場還車前需用車 (2台)</span>
        """, unsafe_allow_html=True)
        
    with st.expander("📅 8/5 (三) Day 6：雪梨歌劇院與復古樂園"):
        st.markdown("""
        <div class="trip-day-header">⛪ 深入歌劇院內部導覽 → 🎡 繽紛港畔月神樂園</div>
        * **景點導航**：
            * 🎭 世界地標：<a href="https://maps.google.com/?q=Sydney+Opera+House" target="_blank">雪梨歌劇院導覽</a>
            * 🎡 拍照聖地：<a href="https://maps.google.com/?q=Luna+Park+Sydney" target="_blank">雪梨月神樂園</a>
        * **🏠 住宿飯店**：👉 <a href="https://maps.google.com/?q=ibis+Styles+Sydney+Central" target="_blank">雪梨中央宜必思酒店</a>
        * **🚗 租車狀態**：<span class="badge-no-car">❌ 本日不租車</span>
        """, unsafe_allow_html=True)
        
    with st.expander("📅 8/6 (四) Day 7：藍山國家公園壯麗一日遊"):
        st.markdown("""
        <div class="trip-day-header">🏔️ 走訪三姐妹岩、搭乘經典景觀纜車</div>
        * **預訂平台**：👉 <a href="https://www.kkday.com" target="_blank">KKday 藍山專屬一日遊行程</a>
        * **🏠 住宿飯店**：👉 <a href="https://maps.google.com/?q=ibis+Styles+Sydney+Central" target="_blank">雪梨中央宜必思酒店</a>
        * **🚗 租車狀態**：<span class="badge-no-car">❌ 本日不租車 (搭專車)</span>
        """, unsafe_allow_html=True)
        
    with st.expander("📅 8/7 (五) Day 8：南半球極致賞鯨體驗"):
        st.markdown("""
        <div class="trip-day-header">🐋 搭乘賞鯨船出海 → 雪梨市區自由購物</div>
        * **🏠 住宿飯店**：👉 <a href="https://maps.google.com/?q=ibis+Styles+Sydney+Central" target="_blank">雪梨中央宜必思酒店</a>
        * **🚗 租車狀態**：<span class="badge-no-car">❌ 本日不租車</span>
        """, unsafe_allow_html=True)
        
    with st.expander("📅 8/8 (六) Day 9：飛往度假天堂黃金海岸 ✈️"):
        st.markdown("""
        * **行程重點**：✈️ 雪梨飛黃金海岸 (12:20~13:40) → 抵達陽光海岸 Airbnb → 衝向海灘
        * **🏠 住宿飯店**：👉 <a href="https://www.airbnb.com" target="_blank">陽光海岸精選 Airbnb 網站</a>
        * **🚗 租車狀態**：<span class="badge-no-car">❌ 本日不租車</span>
        """, unsafe_allow_html=True)
        
    with st.expander("📅 8/9 (日) Day 10：火車前進布里斯本、越夜越美"):
        st.markdown("""
        <div class="trip-day-header">🦘 黃金海岸搭火車 → Brisbane 市區巡禮 → 🍱 網美 Eat Street 貨櫃市集</div>
        * **景點導航**：
            * 🍱 美食夜市：<a href="https://maps.google.com/?q=Eat+Street+Northshore" target="_blank">Eat Street 貨櫃市集</a>
        * **🏠 住宿飯店**：👉 <a href="https://maps.google.com/?q=The+George+Design+Hotel+Brisbane" target="_blank">布里斯本喬治飯店 (George Hotel)</a>
        * **🚗 租車狀態**：<span class="badge-no-car">❌ 本日不租車</span>
        """, unsafe_allow_html=True)
        
    with st.expander("📅 8/10 (一) Day 11：抱無尾熊與頂級夜景 🚗"):
        st.markdown("""
        <div class="trip-day-header">🐨 龍柏無尾熊動物園 (近距離親密接觸) → 🏔️ 庫薩山看全景落日</div>
        * **景點導航**：
            * 🐨 無尾熊聖地：<a href="https://maps.google.com/?q=Lone+Pine+Koala+Sanctuary" target="_blank">龍柏無尾熊保護區</a>
            * 🏔️ 俯瞰市區：<a href="https://maps.google.com/?q=Mount+Coot-tha+Summit+Lookout" target="_blank">庫薩山觀景台</a>
        * **🏠 住宿飯店**：👉 <a href="https://maps.google.com/?q=The+George+Design+Hotel+Brisbane" target="_blank">布里斯本喬治飯店 (George Hotel)</a>
        * **🚗 租車狀態**：<span class="badge-need-car">🟢 需取租車 (2台)</span>
        """, unsafe_allow_html=True)
        
    with st.expander("📅 8/11 (二) Day 12：布里斯本市區漫步 / 依依不捨回台 ✈️"):
        st.markdown("""
        <div class="trip-day-header">🏢 市區最後採買伴手禮 → ✈️ 機場還車辦登機 → 歸途</div>
        * **✈️ 航班時間**：⏳ 8/11 22:15 布里斯本起飛 ~ 8/12 05:10 抵達台灣
        * **景點導航**：👉 <a href="https://maps.google.com/?q=Brisbane+Airport" target="_blank">布里斯本國際機場</a>
        * **🏠 住宿**：無住宿（夜宿機上）
        * **🚗 租車狀態**：<span class="badge-no-car">❌ 本日不租車</span>
        """, unsafe_allow_html=True)

elif page == "🏨 住宿與租車總覽":
    st.subheader("📌 飯店預訂與自駕日期一覽")
    
    st.markdown("### 🏢 全程精美飯店卡片（點擊即刻地圖導航）")
    st.info("""
    1. 📍 7/31 - 8/2 (3晚) 墨爾本：<a href="https://maps.google.com/?q=Holiday+Inn+Express+Melbourne+Little+Collins" target="_blank">墨爾本小柯林斯智選假日酒店</a>
    2. 📍 8/3 (1晚) 大洋路：<a href="https://maps.google.com/?q=Great+Ocean+Road+Tourist+Park" target="_blank">大洋路旅客公園飯店 (Great Ocean Road Tourist Park)</a>
    3. 📍 8/4 - 8/7 (4晚) 雪梨：<a href="https://maps.google.com/?q=ibis+Styles+Sydney+Central" target="_blank">雪梨中央宜必思酒店 (ibis Styles)</a>
    4. 📍 8/8 (1晚) 黃金海岸：<a href="https://www.airbnb.com" target="_blank">陽光海岸 AirBnb 專屬網頁</a>
    5. 📍 8/9 - 8/10 (2晚) 布里斯本：<a href="https://maps.google.com/?q=The+George+Design+Hotel+Brisbane" target="_blank">布里斯本喬治飯店 (George Hotel)</a>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🚗 雙車自駕天數清單")
    st.success("""
    這次行程共有 **4天** 需要動用到 **2台租車**，請駕駛人注意右駕習慣：
    * **8/2 (日)**：墨爾本周邊（彩虹小屋、蒸汽火車、企鵝歸巢）
    * **8/3 (一)**：大洋路過夜自駕
    * **8/4 (二)**：大洋路開回墨爾本機場還車
    * **8/10 (一)**：布里斯本近郊（無尾熊動物園、庫薩山夜景）
    """)

elif page == "⚠️ 貼心安全指南":
    st.subheader("💡 澳洲旅遊隨身注意事項")
    st.warning("🚗 **右駕注意事項：** 澳洲為右駕（靠左行駛），轉彎時請默念「左小彎、右大彎」，特別是圓環請務必禮讓右側來車！")
    st.info("🎒 **個人隨身必備：** 台灣駕照正本 + 國際駕照、澳洲電子簽證 (ETA)、行動電源、禦寒長袖、澳洲規格三腳插頭。")
