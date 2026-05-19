import streamlit as st
from datetime import datetime

# 1. 網頁基本設定
st.set_page_config(
    page_title="2026 澳洲自駕隨身手冊", 
    page_icon="🦘", 
    layout="centered"
)

# 2. 核心 CSS 注入：加入絕美風景背景、毛玻璃卡片、加寬文字行距
custom_style = """
<style>
    /* 隱藏 Streamlit 預設的多餘元件 */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    div[data-testid="stConnectionStatus"] {display: none;}
    
    /* 🌄 高級感全域背景圖：使用雪梨歌劇院輕微霧化背景 */
    .stApp {
        background: linear-gradient(rgba(245, 247, 250, 0.88), rgba(245, 247, 250, 0.88)), 
                    url('https://images.unsplash.com/photo-1524820197278-540916411e20?q=80&w=1080') no-repeat center center fixed;
        background-size: cover;
    }
    
    /* 頂部高級深藍漸層卡片 */
    .hero-card {
        background: linear-gradient(135deg, #112233 0%, #1a365d 100%);
        padding: 28px 20px;
        border-radius: 20px;
        color: white;
        text-align: center;
        box-shadow: 0 10px 25px rgba(0,0,0,0.15);
        margin-bottom: 10px;
    }
    
    /* 📱 解決字體擁擠問題：大幅提升行距與段落高度 */
    p, li, span, div {
        line-height: 2.0 !important;
        font-size: 1.05rem !important;
        color: #2d3748 !important;
    }
    
    /* 讓展開摺疊面板 (Expander) 變成漂亮的現代毛玻璃字卡 */
    div[data-testid="stExpander"] {
        background: rgba(255, 255, 255, 0.65) !important;
        border-radius: 14px !important;
        border: 1px solid rgba(255, 255, 255, 0.5) !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03) !important;
        margin-bottom: 12px !important;
    }
    
    /* 🎨 行程標題微調 */
    .trip-day-header {
        font-size: 1.2rem !important;
        font-weight: 700 !important;
        color: #1a365d !important;
        margin-top: 5px;
        margin-bottom: 12px;
        border-left: 4px solid #3182ce;
        padding-left: 10px;
    }
    
    /* 🔗 超連結美化：藍色清晰帶下劃線 */
    .geo-link {
        color: #2b6cb0 !important;
        text-decoration: underline !important;
        font-weight: 700 !important;
    }
    .geo-link:hover {
        color: #c53030 !important;
    }
</style>
"""
st.markdown(custom_style, unsafe_allow_html=True)

# 3. ◀️ 左側邊欄（Sidebar）回歸與優化
with st.sidebar:
    st.markdown("### 🗺️ 澳洲旅程助手")
    target_date = datetime(2026, 7, 31)
    today = datetime.now()
    days_left = (target_date - today).days
    
    if days_left > 0:
        st.markdown(f"✈️ **距離澳洲出發還有：**")
        st.markdown(f"<h1 style='color:#e53e3e; margin-top:0;'>{days_left} 天</h1>", unsafe_allow_html=True)
    else:
        st.success("🎉 澳洲之旅順利進行中！")
        
    st.write("---")
    st.markdown("### 🕒 澳洲當地時間 (AEST)\n※ 墨爾本/雪梨/布里斯本比台灣快 2 小時！")
    st.write("---")
    st.markdown("### ❄️ 澳洲 8 月冬季氣候\n* **墨爾本**：8°C - 14°C (防風厚外套)\n* **雪梨**：10°C - 17°C (涼爽舒適)\n* **布里斯本**：11°C - 22°C (晴朗防曬)")

# 4. ▶️ 中央主畫面大標題
st.markdown("""
<div class="hero-card">
    <h1 style="margin:0; font-size:2.0rem; font-weight:700; color:#ffffff !important; letter-spacing:1px;">🇦🇺 2026 澳洲自駕隨身手冊</h1>
    <p style="margin:8px 0 0 0; opacity:0.85; color:#e2e8f0 !important; font-size:0.95rem !important;">專案代號：Antigravity 終極穩定版</p>
</div>
""", unsafe_allow_html=True)

# 5. 📱 手機版專屬：網頁原生級「左右滑動選單」切換組件
# 利用 Streamlit 的 query_params 來抓取獨立原生網頁元件點擊的選項，字體絕對看得見且極速流暢！
if "current_tab" not in st.session_state:
    st.session_state.current_tab = "📅 12天完整行程"

# 抓取頂部滑動列傳回來的點擊訊號
q_params = st.query_params
if "tab" in q_params:
    st.session_state.current_tab = q_params["tab"]

# 用極簡純網頁程式碼畫出「可左右滑動的漂亮膠囊按鈕」
tabs_html = f"""
<div style="overflow-x: auto; white-space: nowrap; padding: 10px 5px; -webkit-overflow-scrolling: touch; font-family: system-ui, -apple-system, sans-serif;">
    <a href="?tab=📅+12天完整行程" target="_self" style="display: inline-block; padding: 10px 22px; margin-right: 10px; border-radius: 25px; font-size: 15px; font-weight: bold; text-decoration: none; transition: all 0.2s;
       background: {'linear-gradient(135deg, #3182ce, #2b6cb0)' if st.session_state.current_tab == '📅 12天完整行程' else '#ffffff'};
       color: {'#ffffff' if st.session_state.current_tab == '📅 12天完整行程' else '#4a5568'};
       box-shadow: { '0 4px 10px rgba(49,130,206,0.3)' if st.session_state.current_tab == '📅 12天完整行程' else '0 2px 5px rgba(0,0,0,0.05)' };
       border: {'none' if st.session_state.current_tab == '📅 12天完整行程' else '1px solid #e2e8f0'};">📅 12天完整行程</a>
       
    <a href="?tab=🏨+住宿租車總覽" target="_self" style="display: inline-block; padding: 10px 22px; margin-right: 10px; border-radius: 25px; font-size: 15px; font-weight: bold; text-decoration: none; transition: all 0.2s;
       background: {'linear-gradient(135deg, #3182ce, #2b6cb0)' if st.session_state.current_tab == '🏨 住宿租車總覽' else '#ffffff'};
       color: {'#ffffff' if st.session_state.current_tab == '🏨 住宿租車總覽' else '#4a5568'};
       box-shadow: { '0 4px 10px rgba(49,130,206,0.3)' if st.session_state.current_tab == '🏨 住宿租車總覽' else '0 2px 5px rgba(0,0,0,0.05)' };
       border: {'none' if st.session_state.current_tab == '🏨 住宿租車總覽' else '1px solid #e2e8f0'};">🏨 住宿租車總覽</a>
       
    <a href="?tab=⚠️+貼心安全指南" target="_self" style="display: inline-block; padding: 10px 22px; margin-right: 10px; border-radius: 25px; font-size: 15px; font-weight: bold; text-decoration: none; transition: all 0.2s;
       background: {'linear-gradient(135deg, #3182ce, #2b6cb0)' if st.session_state.current_tab == '⚠️ 貼心安全指南' else '#ffffff'};
       color: {'#ffffff' if st.session_state.current_tab == '⚠️ 貼心安全指南' else '#4a5568'};
       box-shadow: { '0 4px 10px rgba(49,130,206,0.3)' if st.session_state.current_tab == '⚠️ 貼心安全指南' else '0 2px 5px rgba(0,0,0,0.05)' };
       border: {'none' if st.session_state.current_tab == '⚠️ 貼心安全指南' else '1px solid #e2e8f0'};">⚠️ 貼心安全指南</a>
</div>
"""
st.components.v1.html(tabs_html, height=65)
st.write("")

# 6. 行程與內容頁面
if st.session_state.current_tab == "📅 12天完整行程":
    st.subheader("🗺️ 12天完整自駕行程")
    st.caption("💡 點擊下方行程卡片展開，藍色帶底線字體可一鍵開啟地圖導航")
    
    with st.expander("📅 7/31 (五) Day 1：抵達墨爾本"):
        st.markdown("""
        <div class="trip-day-header">✈️ 抵達墨爾本機場 → 市區 → 入住飯店 Check in</div>
        • 🏠 <b>住宿飯店</b>：<a class="geo-link" href="https://maps.google.com/?q=Holiday+Inn+Express+Melbourne+Little+Collins" target="_blank">墨爾本小柯林斯智選假日酒店</a><br>
        • 🚗 <b>租車狀態</b>：❌ 本日不使用租車，搭乘市區大眾運輸工具。
        """, unsafe_allow_html=True)
        
    with st.expander("📅 8/1 (六) Day 2：墨爾本市區觀光"):
        st.markdown("""
        <div class="trip-day-header">📷 墨爾本復古英倫風市區大遊覽</div>
        • 🗺️ <b>景點導航</b>：<br>
        &nbsp;&nbsp;&nbsp;&nbsp;- 🚂 百年地標車站：<a class="geo-link" href="https://maps.google.com/?q=Flinders+Street+Station" target="_blank">弗林德斯街車站</a><br>
        &nbsp;&nbsp;&nbsp;&nbsp;- 🎨 繽紛街頭藝術：<a class="geo-link" href="https://maps.google.com/?q=Hosier+Lane" target="_blank">塗鴉巷 Hosier Lane</a><br>
        • 🏠 <b>住宿飯店</b>：<a class="geo-link" href="https://maps.google.com/?q=Holiday+Inn+Express+Melbourne+Little+Collins" target="_blank">墨爾本小柯林斯智選假日酒店</a>
        """, unsafe_allow_html=True)
        
    with st.expander("📅 8/2 (日) Day 3：彩虹小屋、蒸汽火車與企鵝歸巢 🚗"):
        st.markdown("""
        <div class="trip-day-header">🚗 啟動自駕小隊 → 蒸汽火車 → 來看神仙企鵝</div>
        • 🗺️ <b>景點導航</b>：<br>
        &nbsp;&nbsp;&nbsp;&nbsp;- 🏡 海灘打卡景點：<a class="geo-link" href="https://maps.google.com/?q=Brighton+Bathing+Boxes" target="_blank">布萊頓彩虹小屋</a><br>
        &nbsp;&nbsp;&nbsp;&nbsp;- 🚂 古董蒸汽火車：<a class="geo-link" href="https://maps.google.com/?q=Puffing+Billy+Railway" target="_blank">普芬比利蒸汽火車</a><br>
        &nbsp;&nbsp;&nbsp;&nbsp;- 🐧 超震撼自然奇景：<a class="geo-link" href="https://maps.google.com/?q=Phillip+Island+Nature+Parks" target="_blank">菲利普島企鵝歸巢</a><br>
        • 🚗 <b>租車狀態</b>：🟢 兩台自駕車今日取車出發！
        """, unsafe_allow_html=True)
        
    with st.expander("📅 8/3 (一) Day 4：世界最美大洋路壯遊 🚗"):
        st.markdown("""
        <div class="trip-day-header">🌊 退房出發 → Great Ocean Road 大洋路自駕 → 十二門徒石</div>
        • 🏠 <b>住宿飯店</b>：<a class="geo-link" href="https://maps.google.com/?q=Great+Ocean+Road+Tourist+Park" target="_blank">大洋路旅客公園飯店 (Tourist Park)</a><br>
        • 🚗 <b>租車狀態</b>：🟢 雙車自駕進行中
        """, unsafe_allow_html=True)

    with st.expander("💡 點擊展開查看更多後續天數..."):
        st.markdown("""
        * **Day 5 (8/4)**：大洋路開回機場還車 ✈️ 飛往雪梨，入住 <a class="geo-link" href="https://maps.google.com/?q=ibis+Styles+Sydney+Central" target="_blank">雪梨中央宜必思酒店</a>。
        * **Day 6 (8/5)**：深度探索 <a class="geo-link" href="https://maps.google.com/?q=Sydney+Opera+House" target="_blank">雪梨歌劇院</a>、暢玩 <a class="geo-link" href="https://maps.google.com/?q=Luna+Park+Sydney" target="_blank">月神樂園</a>。
        * **Day 7 (8/6)**：走訪絕美藍山國家公園（<a class="geo-link" href="https://www.kkday.com" target="_blank">KKday 藍山接駁專車一日遊</a>）。
        * **Day 8 (8/7)**：雪梨港出海賞鯨大體驗 🐋。
        * **Day 9 (8/8)**：✈️ 飛往黃金海岸，入住海灘風情 Airbnb。
        * **Day 10 (8/9)**：前往布里斯本，夜遊熱鬧的 <a class="geo-link" href="https://maps.google.com/?q=Eat+Street+Northshore" target="_blank">Eat Street 貨櫃市集</a>。
        * **Day 11 (8/10)**：親手抱無尾熊！<a class="geo-link" href="https://maps.google.com/?q=Lone+Pine+Koala+Sanctuary" target="_blank">龍校無尾熊保護區</a> 與 <a class="geo-link" href="https://maps.google.com/?q=Mount+Coot-tha+Summit+Lookout" target="_blank">庫薩山夕陽夜景</a> 🚗。
        * **Day 12 (8/11)**：市區採購伴手禮 → 前往 <a class="geo-link" href="https://maps.google.com/?q=Brisbane+Airport" target="_blank">布里斯本國際機場</a> 搭機回台。
        """, unsafe_allow_html=True)

elif st.session_state.current_tab == "🏨 住宿租車總覽":
    st.subheader("🏨 全程預訂與自駕日期總覽")
    
    # 解決之前破格與無法點選的問題
    st.markdown("""
    <div class="trip-day-header">🏢 飯店清單快速地圖導航</div>
    1. 📍 <b>墨爾本 (3晚)</b>：<a class="geo-link" href="https://maps.google.com/?q=Holiday+Inn+Express+Melbourne+Little+Collins" target="_blank">墨爾本小柯林斯智選假日酒店</a><br>
    2. 📍 <b>大洋路 (1晚)</b>：<a class="geo-link" href="https://maps.google.com/?q=Great+Ocean+Road+Tourist+Park" target="_blank">大洋路旅客公園飯店</a><br>
    3. 📍 <b>雪梨 (4晚)</b>：<a class="geo-link" href="https://maps.google.com/?q=ibis+Styles+Sydney+Central" target="_blank">雪梨中央宜必思酒店 (ibis Styles)</a><br>
    4. 📍 <b>黃金海岸 (1晚)</b>：<a class="geo-link" href="https://www.airbnb.com" target="_blank">陽光海岸 AirBnb 精選網頁</a><br>
    5. 📍 <b>布里斯本 (2晚)</b>：<a class="geo-link" href="https://maps.google.com/?q=The+George+Design+Hotel+Brisbane" target="_blank">布里斯本喬治飯店 (George Hotel)</a>
    """, unsafe_allow_html=True)
    
    st.write("---")
    st.markdown("### 🚗 自駕車出動天數提示")
    st.info("本次自駕遊在以下 **4天** 將會開啟 **2台租車** 同步出發，請正副駕駛打包好國際駕照：\n\n1. **8/2** (墨爾本近郊一日遊)\n2. **8/3 & 8/4** (大洋路壯遊與機場還車)\n3. **8/10** (布里斯本近郊動物園與山頂夜景)")

elif st.session_state.current_tab == "⚠️ 貼心安全指南":
    st.subheader("⚠️ 澳洲自駕與隨身安全須知")
    st.warning("🚗 <b>右駕核心口訣</b>：澳洲為右駕（靠左行駛），轉彎請默念「左小彎、右大彎」，進入圓環（Roundabout）請絕對停車禮讓右側來車！")
    st.info("🎒 <b>出國檢查清單</b>：台灣駕照正本 + 國際駕照（缺一不可！）、護照與澳洲 ETA 電子簽證、澳洲三腳規格轉接頭、保暖防風外套。")
