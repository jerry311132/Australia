import streamlit as st
import datetime

# ==========================================
# 1. 網頁基本設定（澳洲手機瀏覽極致優化）
# ==========================================
st.set_page_config(
    page_title="2026 澳洲自駕隨身手冊 🦘", 
    page_icon="🦘", 
    layout="centered"
)

# ==========================================
# 2. 注入澳洲冒險風 CSS 視覺設計
# ==========================================
custom_css = """
<style>
/* 載入 Google Fonts 設計中文字體 */
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@300;400;500;700&family=Outfit:wght@300;400;500;600;700&display=swap');

/* 全域字體與背景美化 (修正 class 選擇器以避免渲染空白) */
html, body, .stApp {
    font-family: 'Outfit', 'Noto Sans TC', -apple-system, BlinkMacSystemFont, sans-serif !important;
    background-color: #f7f9fa !important;
    color: #232d37 !important;
}

/* 隱藏 Streamlit 預設網頁多餘元件，營造原生 App 感 */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
div[data-testid="stConnectionStatus"] {display: none;}

/* 澳洲大自然探險風格大 Banner (海岸深綠藍到內陸土紅金) */
.hero-banner {
    background: linear-gradient(135deg, #005f73 0%, #0a9396 45%, #ee9b00 85%, #ca6702 100%);
    color: white;
    padding: 30px 25px;
    border-radius: 20px;
    margin-bottom: 25px;
    box-shadow: 0 10px 25px rgba(10, 147, 150, 0.15);
    text-align: center;
    position: relative;
    overflow: hidden;
}
.hero-banner h1 {
    font-size: 2.1rem !important;
    font-weight: 700 !important;
    margin: 0 !important;
    color: white !important;
    text-shadow: 0 2px 4px rgba(0,0,0,0.15);
}
.hero-banner p {
    font-size: 0.95rem !important;
    margin: 8px 0 0 0 !important;
    opacity: 0.95;
    font-weight: 500;
}

/* 玻璃透光質感卡片 (Glassmorphism Travel Card) */
.travel-card {
    background: rgba(255, 255, 255, 0.95) !important;
    border-radius: 16px !important;
    padding: 22px !important;
    margin-bottom: 18px !important;
    border: 1px solid rgba(10, 147, 150, 0.15) !important;
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.04) !important;
    transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
}
.travel-card:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 12px 25px rgba(10, 147, 150, 0.08) !important;
    border-color: rgba(238, 155, 0, 0.35) !important;
}

/* 精美分期時間軸 (Timeline Style) */
.timeline-container {
    padding-left: 5px;
    margin-top: 10px;
}
.timeline-item {
    position: relative;
    padding-left: 28px;
    padding-bottom: 22px;
    border-left: 2.5px solid rgba(10, 147, 150, 0.3);
}
.timeline-item:last-child {
    border-left: 2.5px solid transparent;
    padding-bottom: 5px;
}
.timeline-item::before {
    content: '';
    position: absolute;
    left: -8px;
    top: 5px;
    width: 14px;
    height: 14px;
    background-color: #0a9396;
    border: 3px solid white;
    border-radius: 50%;
    box-shadow: 0 0 0 3px rgba(10, 147, 150, 0.25);
    transition: all 0.2s ease;
}
.timeline-item:hover::before {
    background-color: #ee9b00;
    box-shadow: 0 0 0 5px rgba(238, 155, 0, 0.25);
}
.timeline-time {
    display: inline-block;
    background: linear-gradient(135deg, rgba(10, 147, 150, 0.15) 0%, rgba(0, 95, 115, 0.15) 100%);
    color: #005f73;
    font-weight: 700;
    font-size: 0.82rem;
    padding: 3px 10px;
    border-radius: 20px;
    margin-bottom: 6px;
}
.timeline-title {
    font-weight: 700;
    color: #1a202c;
    font-size: 1.05rem;
}
.timeline-desc {
    color: #4a5568;
    font-size: 0.92rem;
    margin-top: 5px;
    line-height: 1.45;
}

/* 時間軸住宿與租車標籤 */
.timeline-tag-hotel {
    display: inline-block;
    background-color: rgba(10, 147, 150, 0.08);
    color: #005f73;
    font-size: 0.78rem;
    padding: 2px 8px;
    border-radius: 6px;
    margin-right: 6px;
    font-weight: bold;
}
.timeline-tag-car-yes {
    display: inline-block;
    background-color: rgba(56, 161, 105, 0.08);
    color: #38a169;
    font-size: 0.78rem;
    padding: 2px 8px;
    border-radius: 6px;
    font-weight: bold;
}
.timeline-tag-car-no {
    display: inline-block;
    background-color: rgba(229, 62, 62, 0.08);
    color: #e53e3e;
    font-size: 0.78rem;
    padding: 2px 8px;
    border-radius: 6px;
    font-weight: bold;
}

/* 點擊複製卡片欄位 */
.copyable-field {
    background-color: #f7fafc;
    border: 1px dashed #0a9396;
    border-radius: 10px;
    padding: 10px 14px;
    font-family: monospace;
    font-size: 0.95rem;
    color: #2d3748;
    margin: 8px 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
    cursor: pointer;
    transition: all 0.2s;
}
.copyable-field:hover {
    background-color: #edf2f7;
    border-color: #005f73;
}
.copy-badge {
    background-color: rgba(10, 147, 150, 0.1);
    color: #0a9396;
    padding: 2px 8px;
    border-radius: 6px;
    font-size: 0.75rem;
    font-weight: bold;
}

/* 警示與資訊徽章 */
.alert-card-info {
    background: linear-gradient(135deg, rgba(10, 147, 150, 0.08) 0%, rgba(0, 95, 115, 0.08) 100%);
    border-left: 5px solid #0a9396;
    color: #005f73;
    padding: 15px;
    border-radius: 12px;
    margin-bottom: 15px;
}
.alert-card-success {
    background: linear-gradient(135deg, rgba(56, 161, 105, 0.08) 0%, rgba(47, 133, 90, 0.08) 100%);
    border-left: 5px solid #38a169;
    color: #22543d;
    padding: 15px;
    border-radius: 12px;
    margin-bottom: 15px;
}
.alert-card-warning {
    background: linear-gradient(135deg, rgba(238, 155, 0, 0.08) 0%, rgba(202, 103, 2, 0.08) 100%);
    border-left: 5px solid #ee9b00;
    color: #744210;
    padding: 15px;
    border-radius: 12px;
    margin-bottom: 15px;
}
.alert-card-danger {
    background: linear-gradient(135deg, rgba(229, 62, 62, 0.08) 0%, rgba(155, 44, 44, 0.08) 100%);
    border-left: 5px solid #e53e3e;
    color: #742a2a;
    padding: 15px;
    border-radius: 12px;
    margin-bottom: 15px;
}

/* 地圖導航小按鈕 */
.map-btn {
    display: inline-flex;
    align-items: center;
    background-color: #ffffff;
    color: #ca6702;
    border: 1px solid #ca6702;
    border-radius: 20px;
    padding: 3px 12px;
    font-size: 0.8rem;
    font-weight: bold;
    text-decoration: none;
    margin-top: 8px;
    transition: all 0.2s;
}
.map-btn:hover {
    background-color: #ca6702;
    color: white !important;
}

/* Streamlit 原生 Tab 按鈕美化 */
button[role="tab"] {
    font-size: 0.95rem !important;
    font-weight: 600 !important;
    border-radius: 10px !important;
    padding: 10px 16px !important;
    transition: all 0.25s ease !important;
}
button[role="tab"][aria-selected="true"] {
    background-color: rgba(10, 147, 150, 0.12) !important;
    color: #005f73 !important;
    box-shadow: inset 0 -2px 0 #0a9396 !important;
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# ==========================================
# 3. 頂部大標題（澳洲冒險風 Banner）
# ==========================================
st.markdown(
    """
    <div class="hero-banner">
        <h1>🇦🇺 2026 澳洲自駕隨身手冊</h1>
        <p>📱 手機隨身優化版（專案代號：Antigravity）</p>
    </div>
    """, 
    unsafe_allow_html=True
)

# ==========================================
# 4. 側邊欄：倒數計時與即時天氣
# ==========================================
with st.sidebar:
    st.markdown("### 🦘 澳洲旅程助手")
    
    # 旅程倒數計時 (2026-07-31)
    departure_date = datetime.date(2026, 7, 31)
    today = datetime.date.today()
    days_left = (departure_date - today).days
    
    if days_left > 0:
        st.metric(label="✈️ 距離澳洲出發還有", value=f"{days_left} 天")
    elif days_left == 0:
        st.success("🎉 今天就是出發日！澳洲神仙之旅啟航！")
    else:
        st.info("✈️ 澳洲自駕歡樂進行中 / 已回國")
        
    st.write("---")
    
    # 即時澳洲東部時間 (AEST 比台灣快2小時)
    now_utc = datetime.datetime.now(datetime.timezone.utc)
    aest_time = now_utc + datetime.timedelta(hours=10)
    st.markdown(f"🕒 **澳洲當地時間 (AEST)**: `{aest_time.strftime('%H:%M:%S')}`")
    st.caption("※ 墨爾本/雪梨/布里斯本比台灣快 2 小時！")
    
    st.write("---")
    
    # 澳洲冬天 (8月份) 各城市即時氣溫與防裝穿搭
    st.markdown("""
    ❄️ **澳洲 8 月冬季氣候預測**
    - **墨爾本 (Melbourne)**：8°C - 14°C 🌧️ (濕冷多雨，務必帶防風厚外套與雨傘)
    - **雪梨 (Sydney)**：10°C - 17°C ⛅ (氣候舒適，涼爽，早晚偏冷)
    - **布里斯本 (Brisbane)**：11°C - 22°C ☀️ (溫暖晴朗，非常舒適，防曬必備)
    """)

# ==========================================
# 5. 主分頁導覽列（使用 Streamlit 進階 Tabs）
# ==========================================
tabs = st.tabs(["📅 每日詳細行程", "🏨 住宿與租車", "🚗 自駕安全指南", "👥 旅客與清單"])

# ==========================================
# 分頁 1：📅 每日詳細行程
# ==========================================
with tabs[0]:
    st.subheader("🗺️ 12天完整行程安排")
    st.caption("💡 點擊下方日期可展開查看細節、住宿與租車狀況")
    
    # 精緻區域選單，方便手機操作與防內容過長
    area_sel = st.segmented_control(
        "快速跳轉區域：",
        options=["全部天數", "墨爾本段 (D1-D5)", "雪梨段 (D5-D9)", "昆士蘭段 (D9-D12)"],
        default="全部天數"
    )
    
    # Day 1
    if area_sel in ["全部天數", "墨爾本段 (D1-D5)"]:
        with st.expander("📅 7/31 (五) Day 1：啟程與抵達墨爾本 ✈️", expanded=True):
            st.markdown(
                """
                <div class="timeline-container">
                    <span class="timeline-tag-hotel">🏠 墨爾本小柯林斯智選假日酒店</span>
                    <span class="timeline-tag-car-no">❌ 本日不租車</span>
                    <div class="timeline-item">
                        <div class="timeline-time">上午 - 下午</div>
                        <div class="timeline-title">🛫 搭機啟程前返澳洲</div>
                        <div class="timeline-desc">提早抵達桃園機場辦理登機。確認澳洲電子簽證 (ETA) 及國際駕照已備妥在隨身行李中。</div>
                    </div>
                    <div class="timeline-item">
                        <div class="timeline-time">晚上</div>
                        <div class="timeline-title">✈️ 抵達墨爾本機場 (MEL)</div>
                        <div class="timeline-desc">出關後，搭乘機場 SkyBus 巴士或 Uber/計程車前往市區飯店。</div>
                        <a href="https://maps.app.goo.gl/FzB3C4H9LzQeN1c7A" target="_blank" class="map-btn">📍 墨爾本機場導航</a>
                    </div>
                    <div class="timeline-item">
                        <div class="timeline-time">21:00</div>
                        <div class="timeline-title">🏨 入住飯店休息</div>
                        <div class="timeline-desc">入住「墨爾本小柯林斯智選假日酒店」，調整時差與休息。</div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

    # Day 2
    if area_sel in ["全部天數", "墨爾本段 (D1-D5)"]:
        with st.expander("📅 8/1 (六) Day 2：墨爾本優雅英倫風市區觀光 📷", expanded=False):
            st.markdown(
                """
                <div class="timeline-container">
                    <span class="timeline-tag-hotel">🏠 墨爾本小柯林斯智選假日酒店</span>
                    <span class="timeline-tag-car-no">❌ 本日不租車</span>
                    <div class="timeline-item">
                        <div class="timeline-time">09:30</div>
                        <div class="timeline-title">☕ 塗鴉牆與弗林德斯街車站</div>
                        <div class="timeline-desc">漫步霍西爾巷 (Hosier Lane) 欣賞前衛塗鴉，朝聖百年文藝地標「Flinders Street Station」。</div>
                        <a href="https://maps.app.goo.gl/3rGgM7y2s4wYVz9J8" target="_blank" class="map-btn">📍 弗林德斯街車站導航</a>
                    </div>
                    <div class="timeline-item">
                        <div class="timeline-time">13:00</div>
                        <div class="timeline-title">☕ 墨爾本咖啡文化體驗</div>
                        <div class="timeline-desc">前往著名的墨爾本拱廊與小巷，點一杯道地 Flat White，享受悠閒下午。</div>
                    </div>
                    <div class="timeline-item">
                        <div class="timeline-time">16:00</div>
                        <div class="timeline-title">⛪ 聖保羅大教堂 & 尤利卡觀景台</div>
                        <div class="timeline-desc">參觀新哥德式大教堂，傍晚可登上尤利卡觀景台俯瞰市區美麗夜景。</div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

    # Day 3
    if area_sel in ["全部天數", "墨爾本段 (D1-D5)"]:
        with st.expander("📅 8/2 (日) Day 3：彩虹小屋、蒸汽火車與企鵝歸巢 🚗", expanded=False):
            st.markdown(
                """
                <div class="timeline-container">
                    <span class="timeline-tag-hotel">🏠 墨爾本小柯林斯智選假日酒店</span>
                    <span class="timeline-tag-car-yes">🟢 租車 (2台)</span>
                    <div class="timeline-item">
                        <div class="timeline-time">08:30</div>
                        <div class="timeline-title">🚗 市區取車與出發</div>
                        <div class="timeline-desc">兩位指定駕駛前往租車點辦理取車手續，熟悉右駕操作後，開車前往 Brighton Beach。</div>
                    </div>
                    <div class="timeline-item">
                        <div class="timeline-time">09:30</div>
                        <div class="timeline-title">🌈 布萊頓彩虹小屋 (Brighton Bathing Boxes)</div>
                        <div class="timeline-desc">五彩繽紛的沙灘更衣小屋，是墨爾本必拍的海岸地標。</div>
                        <a href="https://maps.app.goo.gl/q6y3C4H9LzQeN1c8A" target="_blank" class="map-btn">📍 彩虹小屋導航</a>
                    </div>
                    <div class="timeline-item">
                        <div class="timeline-time">12:00</div>
                        <div class="timeline-title">🚂 普芬比利蒸汽火車 (Puffing Billy)</div>
                        <div class="timeline-desc">體驗古老的復古森林蒸汽火車，把腳掛在窗外欣賞丹頓農山脈山林美景！</div>
                        <a href="https://maps.app.goo.gl/2F8yN4k9LzQeR1m7B" target="_blank" class="map-btn">📍 蒸汽火車站導航</a>
                    </div>
                    <div class="timeline-item">
                        <div class="timeline-time">17:00</div>
                        <div class="timeline-title">🐧 菲利普島企鵝歸巢 (Penguin Parade)</div>
                        <div class="timeline-desc">看世界最小的藍色小企鵝成群結隊從海灘走回沙丘，超級療癒！(晚間氣溫低，請加強防寒)</div>
                        <a href="https://maps.app.goo.gl/s9Y3C4H9LzQeT1p8C" target="_blank" class="map-btn">📍 企鵝歸巢中心導航</a>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

    # Day 4
    if area_sel in ["全部天數", "墨爾本段 (D1-D5)"]:
        with st.expander("📅 8/3 (一) Day 4：世界最美海岸公路大洋路之旅 🚗", expanded=False):
            st.markdown(
                """
                <div class="timeline-container">
                    <span class="timeline-tag-hotel">🏠 大洋路旅客公園飯店</span>
                    <span class="timeline-tag-car-yes">🟢 租車 (2台)</span>
                    <div class="timeline-item">
                        <div class="timeline-time">08:00</div>
                        <div class="timeline-title">🔑 退房與壯遊啟程</div>
                        <div class="timeline-desc">辦理退房，行李上車。正式開往世界級奇景公路——大洋路 (Great Ocean Road)。</div>
                    </div>
                    <div class="timeline-item">
                        <div class="timeline-time">11:00</div>
                        <div class="timeline-title">🌊 大洋路紀念牌樓 & 奧特威角</div>
                        <div class="timeline-desc">在 Memorial Arch 牌樓拍照留念。一路上海岸線波瀾壯闊，駕駛請注意休息。</div>
                    </div>
                    <div class="timeline-item">
                        <div class="timeline-time">15:00</div>
                        <div class="timeline-title">🪨 十二門徒石 (Twelve Apostles)</div>
                        <div class="timeline-desc">大自然鬼斧神工的巨石聳立在海浪中，順便參觀洛克阿德峽谷 (Loch Ard Gorge)。</div>
                        <a href="https://maps.app.goo.gl/4B7yN4k9LzQeW1v9D" target="_blank" class="map-btn">📍 十二門徒石導航</a>
                    </div>
                    <div class="timeline-item">
                        <div class="timeline-time">18:00</div>
                        <div class="timeline-title">🏕️ 入住大洋路營地公園</div>
                        <div class="timeline-desc">抵達並入住「大洋路旅客公園飯店」，享受大自然環繞的悠閒夜晚。</div>
                        <a href="https://maps.app.goo.gl/z9Y3C4H9LzQeM1k7E" target="_blank" class="map-btn">📍 營地公園飯店導航</a>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

    # Day 5
    if area_sel in ["全部天數", "墨爾本段 (D1-D5)", "雪梨段 (D5-D9)"]:
        with st.expander("📅 8/4 (二) Day 5：大洋路回程、還車與飛往雪梨 ✈️", expanded=False):
            st.markdown(
                """
                <div class="timeline-container">
                    <span class="timeline-tag-hotel">🏠 雪梨宜必思 (ibis Styles Central)</span>
                    <span class="timeline-tag-car-yes">🟢 租車還車 & 機場移動</span>
                    <div class="timeline-item">
                        <div class="timeline-time">09:00</div>
                        <div class="timeline-title">🌊 享受早晨海岸與返程</div>
                        <div class="timeline-desc">退房後，開車經由內陸線返回墨爾本市區/機場（內陸線路程較平坦好開）。</div>
                    </div>
                    <div class="timeline-item">
                        <div class="timeline-time">14:00</div>
                        <div class="timeline-title">⛽ 滿油還車 (墨爾本機場)</div>
                        <div class="timeline-desc">還車前請在機場附近的加油站將油加滿，並前往指定還車點完成還車。</div>
                    </div>
                    <div class="timeline-item">
                        <div class="timeline-time">16:40</div>
                        <div class="timeline-title">✈️ 國內線航班：墨爾本飛雪梨</div>
                        <div class="timeline-desc">搭乘國內線航班 (16:40 - 18:10) 前往澳洲第一大城雪梨。</div>
                    </div>
                    <div class="timeline-item">
                        <div class="timeline-time">19:30</div>
                        <div class="timeline-title">🏨 入住雪梨飯店</div>
                        <div class="timeline-desc">搭乘雪梨機場快線火車抵達市區，辦理「雪梨宜必思」入住登記並用晚餐。</div>
                        <a href="https://maps.app.goo.gl/d9Y3C4H9LzQeK1f6F" target="_blank" class="map-btn">📍 雪梨宜必思導航</a>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

    # Day 6
    if area_sel in ["全部天數", "雪梨段 (D5-D9)"]:
        with st.expander("📅 8/5 (三) Day 6：雪梨歌劇院與復古月神樂園 🎡", expanded=False):
            st.markdown(
                """
                <div class="timeline-container">
                    <span class="timeline-tag-hotel">🏠 雪梨宜必思 (ibis Styles Central)</span>
                    <span class="timeline-tag-car-no">❌ 本日不租車</span>
                    <div class="timeline-item">
                        <div class="timeline-time">09:30</div>
                        <div class="timeline-title">🏛️ 雪梨歌劇院導覽 (Opera House)</div>
                        <div class="timeline-desc">參加官方中文導覽，深入了解這座世界文化遺產的建築傳奇與音樂廳內部。</div>
                        <a href="https://maps.app.goo.gl/x9Y3C4H9LzQeG1r5G" target="_blank" class="map-btn">📍 雪梨歌劇院導航</a>
                    </div>
                    <div class="timeline-item">
                        <div class="timeline-time">13:00</div>
                        <div class="timeline-title">🌉 雪梨港灣大橋與岩石區</div>
                        <div class="timeline-desc">在岩石區 (The Rocks) 用午餐，欣賞歷史老街，並從橋下漫步拍攝大橋壯麗全景。</div>
                    </div>
                    <div class="timeline-item">
                        <div class="timeline-time">15:30</div>
                        <div class="timeline-title">🎡 雪梨月神樂園 (Luna Park)</div>
                        <div class="timeline-desc">搭乘渡輪前往對岸的經典懷舊樂園，門口的標誌性大笑臉是經典打卡地標！</div>
                        <a href="https://maps.app.goo.gl/y9Y3C4H9LzQeH1k7H" target="_blank" class="map-btn">📍 月神樂園導航</a>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

    # Day 7
    if area_sel in ["全部天數", "雪梨段 (D5-D9)"]:
        with st.expander("📅 8/6 (四) Day 7：藍山國家公園一日遊 🏔️", expanded=False):
            st.markdown(
                """
                <div class="timeline-container">
                    <span class="timeline-tag-hotel">🏠 雪梨宜必思 (ibis Styles Central)</span>
                    <span class="timeline-tag-car-no">❌ 本日不租車 (KKday 包車行程)</span>
                    <div class="timeline-item">
                        <div class="timeline-time">08:00</div>
                        <div class="timeline-title">🚐 KKday 一日遊集合出發</div>
                        <div class="timeline-desc">於指定地點集合，搭乘舒適觀光巴士直達世界遺產藍山國家公園。</div>
                    </div>
                    <div class="timeline-item">
                        <div class="timeline-time">10:00</div>
                        <div class="timeline-title">🏔️ 藍山三姊妹岩與景觀世界</div>
                        <div class="timeline-desc">眺望著名的三姊妹岩。搭乘森林纜車、世界上最陡的紅木森林鐵道與高空玻璃纜車。</div>
                        <a href="https://maps.app.goo.gl/t9Y3C4H9LzQeJ1m6I" target="_blank" class="map-btn">📍 藍山景觀世界導航</a>
                    </div>
                    <div class="timeline-item">
                        <div class="timeline-time">15:00</div>
                        <div class="timeline-title">🦘 蘿拉小鎮文青散策</div>
                        <div class="timeline-desc">英式風情滿滿的 Leura 小鎮，逛逛手工藝品店、享受下午茶。傍晚返回雪梨市區。</div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

    # Day 8
    if area_sel in ["全部天數", "雪梨段 (D5-D9)"]:
        with st.expander("📅 8/7 (五) Day 8：震撼雪梨賞鯨與市區悠閒漫步 🐋", expanded=False):
            st.markdown(
                """
                <div class="timeline-container">
                    <span class="timeline-tag-hotel">🏠 雪梨宜必思 (ibis Styles Central)</span>
                    <span class="timeline-tag-car-no">❌ 本日不租車</span>
                    <div class="timeline-item">
                        <div class="timeline-time">09:00</div>
                        <div class="timeline-title">🐋 環形碼頭登船賞鯨 (Whale Watching)</div>
                        <div class="timeline-desc">冬季是座頭鯨遷徙期！搭乘大型遊艇駛出雪梨港，親眼看座頭鯨躍出海面的震撼畫面！</div>
                        <a href="https://maps.app.goo.gl/w9Y3C4H9LzQeP1k7J" target="_blank" class="map-btn">📍 環形碼頭導航</a>
                    </div>
                    <div class="timeline-item">
                        <div class="timeline-time">13:30</div>
                        <div class="timeline-title">🛍️ 雪梨塔與維多利亞女王大廈 (QVB)</div>
                        <div class="timeline-desc">前往世界上最美麗的購物中心 QVB 欣賞古老機械鐘，並可在皮特街血拚採購伴手禮。</div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

    # Day 9
    if area_sel in ["全部天數", "雪梨段 (D5-D9)", "昆士蘭段 (D9-D12)"]:
        with st.expander("📅 8/8 (六) Day 9：飛往昆士蘭陽光黃金海岸 ✈️", expanded=False):
            st.markdown(
                """
                <div class="timeline-container">
                    <span class="timeline-tag-hotel">🏠 陽光海岸 Airbnb</span>
                    <span class="timeline-tag-car-no">❌ 本日不租車</span>
                    <div class="timeline-item">
                        <div class="timeline-time">09:30</div>
                        <div class="timeline-title">🔑 退房前往雪梨機場</div>
                        <div class="timeline-desc">雪梨宜必思退房，搭乘火車前往雪梨國內機場。</div>
                    </div>
                    <div class="timeline-item">
                        <div class="timeline-time">12:20</div>
                        <div class="timeline-title">✈️ 航班：雪梨飛黃金海岸</div>
                        <div class="timeline-desc">搭乘飛機 (12:20 - 13:40) 飛抵昆士蘭度假天堂黃金海岸。</div>
                    </div>
                    <div class="timeline-item">
                        <div class="timeline-time">15:00</div>
                        <div class="timeline-title">🌊 陽光海灘與 Airbnb 入住</div>
                        <div class="timeline-desc">前往陽光海岸的奢華 Airbnb 辦理入住，隨後步行至沙灘，漫步在著名的衝浪者天堂。</div>
                        <a href="https://maps.app.goo.gl/v9Y3C4H9LzQeL1m7K" target="_blank" class="map-btn">📍 衝浪者天堂沙灘導航</a>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

    # Day 10
    if area_sel in ["全部天數", "昆士蘭段 (D9-D12)"]:
        with st.expander("📅 8/9 (日) Day 10：火車前進布里斯本與美食街狂歡 🦘", expanded=False):
            st.markdown(
                """
                <div class="timeline-container">
                    <span class="timeline-tag-hotel">🏠 布里斯本喬治飯店</span>
                    <span class="timeline-tag-car-no">❌ 本日不租車</span>
                    <div class="timeline-item">
                        <div class="timeline-time">10:00</div>
                        <div class="timeline-title">🚂 搭乘火車前往布里斯本</div>
                        <div class="timeline-desc">退房後，搭乘昆士蘭鐵路火車前往布里斯本市區，沿途欣賞陽光州的鄉野景致。</div>
                    </div>
                    <div class="timeline-item">
                        <div class="timeline-time">13:00</div>
                        <div class="timeline-title">🏢 布里斯本市區 & 喬治飯店入住</div>
                        <div class="timeline-desc">抵達並入住「布里斯本喬治飯店 (George Hotel Brisbane)」放置行李，並在皇后街商業區漫步。</div>
                        <a href="https://maps.app.goo.gl/u9Y3C4H9LzQeS1k7L" target="_blank" class="map-btn">📍 布里斯本喬治飯店導航</a>
                    </div>
                    <div class="timeline-item">
                        <div class="timeline-time">17:30</div>
                        <div class="timeline-title">🍱 北岸集裝箱美食街 (Eat Street Northshore)</div>
                        <div class="timeline-desc">必訪人氣美食貨櫃市集！無數現場樂團演奏與多國特色小吃，節慶氛圍滿點！</div>
                        <a href="https://maps.app.goo.gl/p9Y3C4H9LzQeT1m7M" target="_blank" class="map-btn">📍 Eat Street 美食街導航</a>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

    # Day 11
    if area_sel in ["全部天數", "昆士蘭段 (D9-D12)"]:
        with st.expander("📅 8/10 (一) Day 11：近距離親近無尾熊與夕陽展望 🚗", expanded=False):
            st.markdown(
                """
                <div class="timeline-container">
                    <span class="timeline-tag-hotel">🏠 布里斯本喬治飯店</span>
                    <span class="timeline-tag-car-yes">🟢 租車 (2台)</span>
                    <div class="timeline-item">
                        <div class="timeline-time">08:30</div>
                        <div class="timeline-title">🚗 布里斯本租車手續</div>
                        <div class="timeline-desc">兩位指定駕駛前往取車點，辦理租車手續（2台車）。這是在澳洲的最後一次自駕！</div>
                    </div>
                    <div class="timeline-item">
                        <div class="timeline-time">09:30</div>
                        <div class="timeline-title">🐨 龍柏無尾熊動物園 (Lone Pine Koala Sanctuary)</div>
                        <div class="timeline-desc">世界最大最古老的無尾熊動物園！在這裡可以親眼看超萌無尾熊、親手餵食袋鼠！</div>
                        <a href="https://maps.app.goo.gl/r9Y3C4H9LzQV1n7N" target="_blank" class="map-btn">📍 龍柏無尾熊動物園導航</a>
                    </div>
                    <div class="timeline-item">
                        <div class="timeline-time">15:30</div>
                        <div class="timeline-title">🏔️ 庫薩山觀景台 (Mount Coot-tha)</div>
                        <div class="timeline-desc">開車登上庫薩山，在山頂觀景台眺望布里斯本全市高樓大廈與蜿蜒河流的絕美全景。</div>
                        <a href="https://maps.app.goo.gl/s9Y3C4H9LzQeW1k7O" target="_blank" class="map-btn">📍 庫薩山觀景台導航</a>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

    # Day 12
    if area_sel in ["全部天數", "昆士蘭段 (D9-D12)"]:
        with st.expander("📅 8/11 (二) Day 12：布里斯本市區最後巡禮、平安回台 ✈️", expanded=False):
            st.markdown(
                """
                <div class="timeline-container">
                    <span class="timeline-tag-hotel">🏠 夜宿機上</span>
                    <span class="timeline-tag-car-no">❌ 本日不租車</span>
                    <div class="timeline-item">
                        <div class="timeline-time">10:00</div>
                        <div class="timeline-title">🏢 南岸公園 (South Bank Parklands)</div>
                        <div class="timeline-desc">退房寄存行李。前往南岸公園漫步，欣賞全澳洲唯一的市區人造沙灘與摩天輪。</div>
                    </div>
                    <div class="timeline-item">
                        <div class="timeline-time">17:00</div>
                        <div class="timeline-title">🍴 告別晚餐與領取行李</div>
                        <div class="timeline-desc">享用在澳洲的最後一頓奢華晚餐，回飯店提領行李，搭乘 Uber 或機場快線前往機場。</div>
                    </div>
                    <div class="timeline-item">
                        <div class="timeline-time">19:00</div>
                        <div class="timeline-title">🛫 抵達布里斯本機場 (BNE)</div>
                        <div class="timeline-desc">前往布里斯本國際航廈辦理行李託運、退稅手續，在免稅店做最後的黃金鴯鶓油或綿羊油採購。</div>
                        <a href="https://maps.app.goo.gl/q9Y3C4H9LzQeX1m7P" target="_blank" class="map-btn">📍 布里斯本機場導航</a>
                    </div>
                    <div class="timeline-item">
                        <div class="timeline-time">22:15</div>
                        <div class="timeline-title">✈️ 航班返航回台 (⏳ 22:15 - 次日 05:10)</div>
                        <div class="timeline-desc">飛機準時起飛，夜宿機上。將於明晨 (8/12) 05:10 平安抵達桃園國際機場，結束精彩的12天澳洲自駕旅程！</div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

# ==========================================
# 分頁 2：🏨 住宿與租車
# ==========================================
with tabs[1]:
    st.subheader("📌 住宿與租車詳情")
    
    st.markdown("### 🏢 全程 5 大精選飯店清單")
    st.caption("💡 點擊下方卡片中的地址即可快速複製，用於手機地圖或導航輸入！")
    
    # 飯店 1
    st.markdown(
        """
        <div class="travel-card">
            <div class="alert-card-info">
                <strong>🏨 住宿 1：墨爾本小柯林斯智選假日酒店 (Holiday Inn Express Little Collins)</strong>
            </div>
            <ul>
                <li><strong>住退日期</strong>：7/31 (五) 入住 ～ 8/3 (一) 退房 (3晚)</li>
                <li><strong>電話</strong>：+61-3-9111-8888</li>
            </ul>
            <p><strong>📍 飯店地址</strong> (點擊複製)：</p>
            <div class="copyable-field" onclick="navigator.clipboard.writeText('589 Little Collins St, Melbourne VIC 3000'); alert('已複製墨爾本飯店地址！')">
                <span>589 Little Collins St, Melbourne VIC 3000</span>
                <span class="copy-badge">點擊複製 📋</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # 飯店 2
    st.markdown(
        """
        <div class="travel-card">
            <div class="alert-card-info">
                <strong>🏨 住宿 2：大洋路旅客公園飯店 (Great Ocean Road Tourist Park)</strong>
            </div>
            <ul>
                <li><strong>住退日期</strong>：8/3 (一) 入住 ～ 8/4 (二) 退房 (1晚)</li>
                <li><strong>電話</strong>：+61-3-5598-8123</li>
            </ul>
            <p><strong>📍 飯店地址</strong> (點擊複製)：</p>
            <div class="copyable-field" onclick="navigator.clipboard.writeText('Irving St, Peterborough VIC 3270'); alert('已複製大洋路營地地址！')">
                <span>Irving St, Peterborough VIC 3270</span>
                <span class="copy-badge">點擊複製 📋</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # 飯店 3
    st.markdown(
        """
        <div class="travel-card">
            <div class="alert-card-info">
                <strong>🏨 住宿 3：雪梨中央宜必思樣式酒店 (ibis Styles Sydney Central)</strong>
            </div>
            <ul>
                <li><strong>住退日期</strong>：8/4 (二) 入住 ～ 8/8 (六) 退房 (4晚)</li>
                <li><strong>電話</strong>：+61-2-9289-0000</li>
            </ul>
            <p><strong>📍 飯店地址</strong> (點擊複製)：</p>
            <div class="copyable-field" onclick="navigator.clipboard.writeText('272-282 Pitt St, Sydney NSW 2000'); alert('已複製雪梨飯店地址！')">
                <span>272-282 Pitt St, Sydney NSW 2000</span>
                <span class="copy-badge">點擊複製 📋</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # 飯店 4
    st.markdown(
        """
        <div class="travel-card">
            <div class="alert-card-info">
                <strong>🏨 住宿 4：黃金海岸度假 Airbnb (陽光海岸段)</strong>
            </div>
            <ul>
                <li><strong>住退日期</strong>：8/8 (六) 入住 ～ 8/9 (日) 退房 (1晚)</li>
                <li><strong>備註</strong>：靠海景觀、有廚房，附近有超市</li>
            </ul>
            <p><strong>📍 民宿地址</strong> (點擊複製)：</p>
            <div class="copyable-field" onclick="navigator.clipboard.writeText('Surfers Paradise Blvd, Surfers Paradise QLD 4217'); alert('已複製 Airbnb 地址！')">
                <span>Surfers Paradise Blvd, Surfers Paradise QLD 4217</span>
                <span class="copy-badge">點擊複製 📋</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # 飯店 5
    st.markdown(
        """
        <div class="travel-card">
            <div class="alert-card-info">
                <strong>🏨 住宿 5：布里斯本喬治飯店 (George Hotel Brisbane)</strong>
            </div>
            <ul>
                <li><strong>住退日期</strong>：8/9 (日) 入住 ～ 8/11 (二) 退房 (2晚)</li>
                <li><strong>電話</strong>：+61-7-3221-1111</li>
            </ul>
            <p><strong>📍 飯店地址</strong> (點擊複製)：</p>
            <div class="copyable-field" onclick="navigator.clipboard.writeText('345 George St, Brisbane City QLD 4000'); alert('已複製布里斯本飯店地址！')">
                <span>345 George St, Brisbane City QLD 4000</span>
                <span class="copy-badge">點擊複製 📋</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.write("---")
    st.markdown("### 🚗 租車自駕日程與車輛分配")
    
    st.markdown(
        """
        <div class="travel-card">
            <div class="alert-card-success">
                <strong>🚗 澳洲用車清單（全程共需準備 2 台中大型休旅車）</strong>
            </div>
            <p><strong>第一段用車：墨爾本 (彩虹小屋、蒸汽火車、菲利普島、大洋路)</strong></p>
            <ul>
                <li><strong>用車時間</strong>：8/2 (日) 早上 08:30 ～ 8/4 (二) 下午 14:00 還車 (共 3 天)</li>
                <li><strong>取還車點</strong>：墨爾本市區取車 / 墨爾本機場 (MEL) 還車</li>
                <li><strong>車輛配置</strong>：2 台 5-7人座 SUV (中大型行李箱空間)</li>
            </ul>
            <p><strong>第二段用車：布里斯本 (龍柏無尾熊動物園、庫薩山觀景)</strong></p>
            <ul>
                <li><strong>用車時間</strong>：8/10 (一) 早上 08:30 ～ 8/10 (一) 傍晚 18:30 當日還車</li>
                <li><strong>取還車點</strong>：布里斯本市區營業所同點取還</li>
                <li><strong>車輛配置</strong>：2 台中型 SUV</li>
            </ul>
            <p><strong>⚠️ 重要自駕必備文件</strong>：</p>
            <ul>
                <li><strong>台灣駕照正本</strong> (日本譯本在澳洲無效，請勿攜帶錯誤)</li>
                <li><strong>英文版國際駕照正本</strong> (需在台灣監理所提前辦妥，效期內)</li>
                <li><strong>主駕駛人信用卡</strong> (擔保取車押金使用)</li>
                <li><strong>護照正本</strong> (取車時需核對個人身份)</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

# ==========================================
# 分頁 3：🚗 自駕安全指南
# ==========================================
with tabs[2]:
    st.subheader("⚠️ 澳洲自駕注意事項與貼心提醒")
    
    st.markdown(
        """
        <div class="travel-card">
            <div class="alert-card-danger">
                <strong>🚨 澳洲自駕黃金安全守則：靠左行駛！</strong>
            </div>
            <p>澳洲是<strong>右駕左行</strong>國家，對台灣駕駛是全新挑戰，請注意以下幾點：</p>
            <ol>
                <li><strong>轉彎口訣</strong>：隨時默念「靠左行駛，右轉大彎，左轉小彎，雨刷與方向燈通常相反」。</li>
                <li><strong>圓環 (Roundabout) 規則</strong>：澳洲圓環極多。進入圓環前必須完全停下，<strong>禮讓右側已在圓環內的車輛</strong>，順時針繞行。</li>
                <li><strong>防逆向提醒</strong>：副駕駛請扮演最佳導航員，特別在轉彎後，提醒駕駛開入左側正確車道，切勿逆向！</li>
            </ol>
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(
            """
            <div class="travel-card" style="height: 100%;">
                <h4 style="color:#ee9b00; margin-top:0;">🛣️ 澳洲電子收費 (Tolls)</h4>
                <p>墨爾本、雪梨與布里斯本市區有許多收費高速公路 (如 Linkt)：</p>
                <ul>
                    <li><strong>無收費站</strong>：所有路段均為感應收費，沒有人工收費亭。</li>
                    <li><strong>租車處理</strong>：取車時確認車上是否已安裝 E-Tag，若無，須在過路後 3 天內上網繳費，或由租車公司代扣（通常有小額手續費）。</li>
                </ul>
            </div>
            """, 
            unsafe_allow_html=True
        )
        
    with col2:
        st.markdown(
            """
            <div class="travel-card" style="height: 100%;">
                <h4 style="color:#0a9396; margin-top:0;">🦘 野生動物與夜間行車</h4>
                <p>澳洲大自然生態極佳，但也帶來行車隱憂：</p>
                <ul>
                    <li><strong>黃昏與夜間</strong>：袋鼠、袋熊等野生動物極易在此時衝出路面（尤其在大洋路或菲利普島郊區路段）。</li>
                    <li><strong>安全對策</strong>：盡量<strong>避免在黃昏後與夜間駕駛郊區公路</strong>。若遇動物衝出，請握緊方向盤並減速，切勿猛打方向盤導致翻車！</li>
                </ul>
            </div>
            """, 
            unsafe_allow_html=True
        )
        
    st.write("---")
    
    st.markdown(
        """
        <div class="travel-card">
            <h4 style="color:#ca6702; margin-top:0;">⛽ 澳洲加油與超速重罰</h4>
            <ul>
                <li><strong>油品選擇</strong>：租車一般加 <strong>Unleaded 91</strong> 汽油。請勿加錯柴油 (Diesel)。</li>
                <li><strong>超速零容忍</strong>：澳洲測速照相非常嚴格，有些州超速 1-2 公里就會被重罰數百澳幣，請務必嚴格遵守速限標誌！</li>
                <li><strong>緊急電話</strong>：若遇到緊急事故需要警車或救護車，請直撥澳洲緊急電話 <strong>「000」 (Triple Zero)</strong>。</li>
            </ul>
        </div>
        """, 
        unsafe_allow_html=True
    )

# ==========================================
# 分頁 4：👥 旅客與清單
# ==========================================
with tabs[3]:
    st.subheader("👥 旅客名單與行李打包清單")
    
    # 待辦與行李打包
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("##### 📌 出發前確認 (必備證件)")
        p_passport = st.checkbox("護照正本 (效期 > 6個月)", value=True, key="au_passport")
        p_eta = st.checkbox("澳洲電子簽證 (ETA Visa) 已核准", value=True, key="au_eta")
        p_license = st.checkbox("台灣駕照正本 + 英文版國際駕照 🪪", value=True, key="au_license")
        p_cash = st.checkbox("澳幣現金與雙幣信用卡 💳", value=False, key="au_cash")
        
    with col2:
        st.markdown("##### 🎒 行李與個人裝備")
        p_coat = st.checkbox("保暖外套與禦寒衣物 🧥 (澳洲 8月為冬季)", value=True, key="au_coat")
        p_adaptor = st.checkbox("澳洲八字插頭轉接器 + 延長線 🔌", value=False, key="au_adaptor")
        p_sim = st.checkbox("澳洲上網 SIM 卡 / eSIM 📶", value=True, key="au_sim")
        p_sunglass = st.checkbox("太陽眼鏡與防曬乳 🕶️ (澳洲紫外線強)", value=False, key="au_sunglass")
        
    # 計算準備進度
    total_items = 8
    checked_items = sum([p_passport, p_eta, p_license, p_cash, p_coat, p_adaptor, p_sim, p_sunglass])
    progress = checked_items / total_items
    
    st.write("---")
    st.markdown(f"**🎒 行李打包進度：{checked_items} / {total_items}**")
    st.progress(progress)
    if progress == 1.0:
        st.balloons()
        st.success("🎉 太棒了！澳洲冒險所有裝備已備齊，隨時準備出發！")

    st.write("---")
    
    # 旅客與駕駛人名單
    st.markdown("##### 👥 旅客名單與車輛駕駛分配")
    st.markdown(
        """
        <div class="travel-card" style="background-color:#fcfcfc !important;">
            <table style="width:100%; border-collapse: collapse; text-align: left;">
                <thead>
                    <tr style="border-bottom: 2px solid #e2e8f0; color: #005f73;">
                        <th style="padding: 10px 5px;">姓名 / 分配角色</th>
                        <th style="padding: 10px 5px;">證件狀態</th>
                        <th style="padding: 10px 5px;">旅平險單號</th>
                    </tr>
                </thead>
                <tbody>
                    <tr style="border-bottom: 1px solid #edf2f7;">
                        <td style="padding: 10px 5px; font-weight:bold;">1. 🚗 駕駛 A (主開車 1)</td>
                        <td style="padding: 10px 5px;"><span style="color:#38a169; font-weight:bold;">🪪 國際照已備</span></td>
                        <td style="padding: 10px 5px;"><code>INS-AU-001</code></td>
                    </tr>
                    <tr style="border-bottom: 1px solid #edf2f7;">
                        <td style="padding: 10px 5px; font-weight:bold;">2. 🚗 駕駛 B (主開車 2)</td>
                        <td style="padding: 10px 5px;"><span style="color:#38a169; font-weight:bold;">🪪 國際照已備</span></td>
                        <td style="padding: 10px 5px;"><code>INS-AU-002</code></td>
                    </tr>
                    <tr style="border-bottom: 1px solid #edf2f7;">
                        <td style="padding: 10px 5px;">3. 👤 乘客 C</td>
                        <td style="padding: 10px 5px; color:#a0aec0;">無駕照</td>
                        <td style="padding: 10px 5px;"><code>INS-AU-003</code></td>
                    </tr>
                    <tr>
                        <td style="padding: 10px 5px;">4. 👤 乘客 D</td>
                        <td style="padding: 10px 5px; color:#a0aec0;">無駕照</td>
                        <td style="padding: 10px 5px;"><code>INS-AU-004</code></td>
                    </tr>
                </tbody>
            </table>
        </div>
        """,
        unsafe_allow_html=True
    )
