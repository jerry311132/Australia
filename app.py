import streamlit as st

# 1. 網頁基本設定
st.set_page_config(
    page_title="2026 澳洲自駕隨身手冊", 
    page_icon="🦘", 
    layout="centered"
)

# 隱藏 Streamlit 預設網頁元件
hide_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    div[data-testid="stConnectionStatus"] {display: none;}
    </style>
"""
st.markdown(hide_style, unsafe_allow_html=True)

st.title("🇦🇺 2026 澳洲行程總表")
st.caption("📱 手機隨身優化版（超連結修正版）")

page = st.radio(
    "請選擇查看項目：", 
    ["📅 每日詳細行程", "🏨 住宿與租車", "⚠️ 貼心提醒事項"], 
    horizontal=True
)

st.write("---")

if page == "📅 每日詳細行程":
    st.subheader("🗺️ 12天完整行程安排")
    
    with st.expander("📅 7/31 (五) Day 1：抵達墨爾本"):
        st.markdown("""
        * **行程重點**：✈️ 抵達墨爾本機場 → 市區 → 入住
        * **🏠 住宿**：[墨爾本小柯林斯智選假日酒店](https://www.google.com/maps/search/?api=1&query=Holiday+Inn+Express+Melbourne+Little+Collins) 📍
        * **🚗 租車**：❌ 不租車
        """)
        
    with st.expander("📅 8/1 (六) Day 2：墨爾本市區"):
        st.markdown("""
        * **行程重點**：📷 墨爾本市區景點觀光
        * **景點導航**：
            * ☕ [弗林德斯街車站](https://www.google.com/maps/search/?api=1&query=Flinders+Street+Station)
            * 🎨 [彩虹巷 Hosier Lane](https://www.google.com/maps/search/?api=1&query=Hosier+Lane)
        * **🏠 住宿**：[墨爾本小柯林斯智選假日酒店](https://www.google.com/maps/search/?api=1&query=Holiday+Inn+Express+Melbourne+Little+Collins)
        """)
        
    with st.expander("📅 8/2 (日) Day 3：彩虹小屋與企鵝歸巢 🚗"):
        st.markdown("""
        * **行程重點**：🚗 租車 → 彩虹小屋 → 🚂 蒸汽火車 → 🐧 企鵝歸巢
        * **景點導航**：
            * 🏡 [布萊頓彩虹小屋](https://www.google.com/maps/search/?api=1&query=Brighton+Bathing+Boxes)
            * 🚂 [普芬比利蒸汽火車](https://www.google.com/maps/search/?api=1&query=Puffing+Billy+Railway)
            * 🐧 [菲利普島企鵝歸巢](https://www.google.com/maps/search/?api=1&query=Phillip+Island+Nature+Parks)
        * **🏠 住宿**：墨爾本小柯林斯智選假日酒店
        * **🚗 租車**：🟢 租車 (2台)
        """)
        
    with st.expander("📅 8/3 (一) Day 4：大洋路之旅 🚗"):
        st.markdown("""
        * **行程重點**：🌊 退房 → Great Ocean Road (大洋路) → 入住
        * **🏠 住宿**：[大洋路旅客公園飯店](https://www.google.com/maps/search/?api=1&query=Great+Ocean+Road+Tourist+Park) 📍
        * **🚗 租車**：🟢 租車 (2台)
        """)
        
    with st.expander("📅 8/4 (二) Day 5：前進雪梨 ✈️"):
        st.markdown("""
        * **行程重點**：🌊 大洋路 → 還車 → ✈️ 飛 Sydney (16:40~18:10) → 入住
        * **🏠 住宿**：[雪梨宜必思酒店](https://www.google.com/maps/search/?api=1&query=ibis+Styles+Sydney+Central) 📍
        * **🚗 租車**：🟢 租車 (2台)
        """)
        
    with st.expander("📅 8/5 (三) Day 6：雪梨歌劇院與月神樂園"):
        st.markdown("""
        * **行程重點**：🗺️ [雪梨歌劇院導覽](https://www.google.com/maps/search/?api=1&query=Sydney+Opera+House) → 🎡 [月神樂園 Luna Park](https://www.google.com/maps/search/?api=1&query=Luna+Park+Sydney)
        * **🏠 住宿**：雪梨宜必思 (ibis Styles Sydney Central)
        """)
        
    with st.expander("📅 8/6 (四) Day 7：藍山國家公園"):
        st.markdown("""
        * **行程重點**：🏔️ [KKday 藍山國家公園一日遊](https://www.kkday.com/) （可自行替換成你的行程預訂連結）
        * **🏠 住宿**：雪梨宜必思 (ibis Styles Sydney Central)
        """)
        
    with st.expander("📅 8/7 (五) Day 8：雪梨賞鯨"):
        st.markdown("""
        * **行程重點**：🐋 賞鯨 → 雪梨市區自由活動
        * **🏠 住宿**：雪梨宜必思 (ibis Styles Sydney Central)
        """)
        
    with st.expander("📅 8/8 (六) Day 9：飛往黃金海岸 ✈️"):
        st.markdown("""
        * **行程重點**：✈️ 雪梨飛黃金海岸 (12:20~13:40) → check in → 🌊 玩海水
        * **🏠 住宿**：[陽光海岸 Airbnb 導航](https://www.google.com/maps) （可替換成你實際的 Airbnb 地址網址）
        """)
        
    with st.expander("📅 8/9 (日) Day 10：前進布里斯本"):
        st.markdown("""
        * **行程重點**：🦘 黃金海岸 → 搭火車到 Brisbane → 市區 → check in → 🍱 [Eat Street 貨櫃市集](https://www.google.com/maps/search/?api=1&query=Eat+Street+Northshore)
        * **🏠 住宿**：[布里斯本喬治飯店](https://www.google.com/maps/search/?api=1&query=George+Hotel+Brisbane) 📍
        """)
        
    with st.expander("📅 8/10 (一) Day 11：看無尾熊 🚗"):
        st.markdown("""
        * **行程重點**：臨近動物園 🐨 [龍柏無尾熊保護區](https://www.google.com/maps/search/?api=1&query=Lone+Pine+Koala+Sanctuary) → 🏔️ [庫薩山觀景台](https://www.google.com/maps/search/?api=1&query=Mount+Coot-tha+Summit+Lookout)
        * **🏠 住宿**：布里斯本喬治飯店 (George Hotel Brisbane)
        * **🚗 租車**：🟢 租車 (2台)
        """)
        
    with st.expander("📅 8/11 (二) Day 12：布里斯本市區 / 回台 ✈️"):
        st.markdown("""
        * **行程重點**：🏢 布里斯本市區逛逛 → ✈️ [布里斯本機場](https://www.google.com/maps/search/?api=1&query=Brisbane+Airport) → 回台
        * **航班時間**：⏳ 8/11 22:15 ~ 8/12 05:10
        * **🏠 住宿**：無住宿（夜宿機上）
        """)

elif page == "🏨 住宿與租車":
    st.subheader("📌 住宿預訂與租車分配清單")
    
    st.markdown("### 🏢 全程飯店快速導航（點擊直接開地圖）")
    st.info("""
    1. 📍 [墨爾本小柯林斯智選假日酒店](https://www.google.com/maps/search/?api=1&query=Holiday+Inn+Express+Melbourne+Little+Collins)
    2. 📍 [大洋路旅客公園飯店 (Great Ocean Road Tourist Park)](https://www.google.com/maps/search/?api=1&query=Great+Ocean+Road+Tourist+Park)
    3. 📍 [雪梨宜必思 (ibis Styles Sydney Central)](https://www.google.com/maps/search/?api=1&query=ibis+Styles+Sydney+Central)
    4. 📍 [布里斯本喬治飯店 (George Hotel Brisbane)](https://www.google.com/maps/search/?api=1&query=George+Hotel+Brisbane)
    """)

elif page == "⚠️ 貼心提醒事項":
    st.subheader("💡 澳洲之行注意事項")
    st.warning("**🚗 💡 連結小提示：** 行程表內藍色帶底線的文字（如飯店、景點名稱）現在都可以直接點選！點擊後會自動彈出網頁或 Google 地圖幫你導航喔！")
