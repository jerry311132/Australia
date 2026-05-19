import streamlit as st
from datetime import datetime

# 1. 網頁基本設定
st.set_page_config(
    page_title="2026 澳洲自駕隨身手冊", 
    page_icon="🦘", 
    layout="centered"
)

# 2. 定義共用行李清單
checklist_items = [
    "護照正本 (確認有效期限在 6 個月以上)",
    "澳洲 ETA 電子簽證 (建議列印或手機截圖核準畫面)",
    "台灣駕照正本 + 國際駕照 (自駕小隊駕駛人必備，缺一不可！)",
    "海外高回饋信用卡 (建議帶2張以上備用) + 少量澳幣現金",
    "澳洲規格八字三腳轉接頭 + 延長線 (飯店插座通常不夠用)",
    "行動電源 (注意！必須放在隨身行李登機，不可托運)",
    "保暖防風外套 / 輕量羽絨衣 (澳洲 8 月是冬季，早晚非常涼)",
    "個人常備藥品 (感冒藥、腸胃藥、暈車藥，入境記得申報)",
    "手機網卡 / eSIM (確認在出發前已完成開通設定)",
    "個人盥洗用品 (牙刷、牙膏，澳洲許多環保飯店不主動提供)"
]

# 3. 核心 CSS 注入（保持淺色舒適介面與毛玻璃字卡）
custom_style = """
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    .stApp {
        background: linear-gradient(rgba(245, 247, 250, 0.88), rgba(245, 247, 250, 0.88)), 
                    url('https://images.unsplash.com/photo-1524820197278-540916411e20?q=80&w=1080') no-repeat center center fixed;
        background-size: cover;
    }
    
    .hero-card {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.75) 0%, rgba(219, 234, 254, 0.85) 100%);
        padding: 25px 20px;
        border-radius: 16px;
        text-align: center;
        box-shadow: 0 8px 16px rgba(0,0,0,0.04);
        margin-bottom: 20px;
        border: 1px solid rgba(255, 255, 255, 0.6);
    }
    
    p, li, span {
        line-height: 1.9 !important;
        font-size: 1.05rem !important;
        color: #2d3748;
    }
    
    div[data-testid="stExpander"] {
        background: rgba(255, 255, 255, 0.75) !important;
        border-radius: 12px !important;
        border: 1px solid rgba(255, 255, 255, 0.6) !important;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05) !important;
        margin-bottom: 10px !important;
    }
    
    .trip-day-header {
        font-size: 1.15rem !important;
        font-weight: 700 !important;
        color: #1a365d !important;
        margin-bottom: 10px;
        border-left: 4px solid #3182ce;
        padding-left: 10px;
    }
    
    a {
        color: #2b6cb0 !important;
        text-decoration: underline !important;
        font-weight: 700 !important;
    }
    
    button[data-baseweb="tab"] {
        font-size: 1.1rem !important;
        font-weight: 600 !important;
    }
</style>
"""
st.markdown(custom_style, unsafe_allow_html=True)

# 4. JavaScript 瀏覽器本地記憶體（LocalStorage）橋接器
# 這個隱藏的自訂組件可以讓 Streamlit 讀取和存入使用者手機的 LocalStorage，達成關閉網頁不遺失的功能
def st_local_storage(key, value=None):
    import json
    # 建立一個唯一的金鑰名稱
    js_key = f"au_trip_{key}"
    
    if f"ls_{js_key}" not in st.session_state:
        st.session_state[f"ls_{js_key}"] = "{}"

    # 如果有傳入新值，同步更新到 Session 與發送 JS 到前端存檔
    if value is not None:
        v_str = json.dumps(value)
        st.session_state[f"ls_{js_key}"] = v_str
        js_code = f"""
        <script>
            localStorage.setItem("{js_key}", '{v_str}');
        </script>
        """
        st.components.v1.html(js_code, height=0, width=0)
        return value

    # 讀取邏輯：透過一個簡單的 HTML 密道把手機本地資料傳回 st.query_params
    q_params = st.query_params
    param_key = f"load_{js_key}"
    
    if param_key in q_params:
        try:
            return json.loads(q_params[param_key])
        except:
            return {}
            
    # 網頁剛載入時，呼叫前端去把手機資料捞出來放進網址裡讓 Python 讀取
    fetch_js = f"""
    <script>
        const val = localStorage.getItem("{js_key}") || "{{}}";
        const url = new URL(window.location.href);
        if (url.searchParams.get("{param_key}") !== val) {{
            url.searchParams.set("{param_key}", val);
            window.location.href = url.href;
        }}
    </script>
    """
    st.components.v1.html(fetch_js, height=0, width=0)
    try:
        return json.loads(st.session_state[f"ls_{js_key}"])
    except:
        return {}

# 5. ◀️ 側邊欄助理
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
    st.markdown("### 🕒 澳洲當地時間 (AEST)\n※ 比台灣快 2 小時！")

# 6. ▶️ 中央主畫面大標題
st.markdown("""
<div class="hero-card">
    <h1 style="margin:0; font-size:1.8rem; font-weight:700; color:#1a365d !important;">🇦🇺 2026 澳洲自駕隨身手冊</h1>
</div>
""", unsafe_allow_html=True)

# 7. 核心頁籤元件
tab1, tab2, tab3 = st.tabs(["📅 12天完整行程", "🏨 住宿與租車", "⚠️ 安全指南"])

with tab1:
    st.caption("💡 點擊下方行程卡片展開，藍色帶底線字體可一鍵開啟地圖導航")
    
    with st.expander("📅 7/31 (五) Day 1：抵達墨爾本"):
        st.markdown("""
        <div class="trip-day-header">✈️ 抵達墨爾本機場 → 市區 → 入住飯店</div>
        • 🏠 **住宿**：<a href="https://maps.google.com/?q=Holiday+Inn+Express+Melbourne+Little+Collins" target="_blank">墨爾本小柯林斯智選假日酒店</a><br>
        • 🚗 **租車**：❌ 本日不租車
        """, unsafe_allow_html=True)
        
    with st.expander("📅 8/1 (六) Day 2：墨爾本市觀光"):
        st.markdown("""
        <div class="trip-day-header">📷 墨爾本復古英倫風市區大遊覽</div>
        • 🗺️ **景點**：<a href="https://maps.google.com/?q=Flinders+Street+Station" target="_blank">弗林德斯街車站</a>、<a href="https://maps.google.com/?q=Hosier+Lane" target="_blank">塗鴉巷 Hosier Lane</a>
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
        • 🏠 **住宿**：<a href="https://maps.google.com/?q=ibis+Styles+Sydney+Central" target="_blank">雪梨中央宜必思酒店</a>
        """, unsafe_allow_html=True)

    with st.expander("📅 8/5 (三) Day 6：雪梨歌劇院與樂園"):
        st.markdown("""
        <div class="trip-day-header">🎭 深度探索雪梨市區與港灣</div>
        • 🗺️ **景點**：<a href="https://maps.google.com/?q=Sydney+Opera+House" target="_blank">雪梨歌劇院</a>、<a href="https://maps.google.com/?q=Luna+Park+Sydney" target="_blank">月神樂園</a>
        """, unsafe_allow_html=True)

    with st.expander("📅 8/6 (四) Day 7：藍山國家公園"):
        st.markdown("""
        <div class="trip-day-header">🏔️ 走訪絕美藍山國家公園</div>
        • 🎫 **行程**：<a href="https://www.kkday.com" target="_blank">KKday 藍山專車一日遊</a>
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
        • 🗺️ **景點**：<a href="https://maps.google.com/?q=Eat+Street+Northshore" target="_blank">Eat Street 貨櫃市集</a>
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
    st.write("---")
    
    st.subheader("🎒 澳洲自駕行李檢查清單")
    
    # 🌟 重點：讓每個人選擇自己的名字，切換時會自動加載對應的 LocalStorage 數據
    user_name = st.selectbox("👤 請選取你的名字（進度將自動綁定並儲存在你的手機裡）：", ["駕駛 A", "副駕駛 B", "隊員 C", "隊員 D"])
    
    # 從該使用者的手機儲存空間中讀取歷史紀錄
    saved_data = st_local_storage(user_name)
    
    st.write(f"請勾選 **{user_name}** 已經確認放入隨身包或行李箱的物品：")
    
    # 渲染複選框並記錄更改
    new_data = {}
    completed_count = 0
    
    for item in checklist_items:
        # 預設值讀取歷史紀錄，如果沒有就設為 False
        default_val = saved_data.get(item, False)
        
        # 為了防止切換使用者時元件打架，加上 user_name 作為 key 的一部分
        is_checked = st.checkbox(item, value=default_val, key=f"item_{user_name}_{item}")
        new_data[item] = is_checked
        if is_checked:
            completed_count += 1
            
    # 如果使用者動手勾選了，立刻觸發 JavaScript 將新狀態存入手機 LocalStorage 裡
    if new_data != saved_data:
        st_local_storage(user_name, new_data)
        st.rerun() # 立即刷新，確保畫面進度條同步反應

    # 計算百分比並顯示進度條
    total_count = len(checklist_items)
    progress_percentage = completed_count / total_count
    
    st.write("")
    st.progress(progress_percentage)
    st.markdown(f"📊 **{user_name} 的準備進度：{completed_count} / {total_count} ({int(progress_percentage * 100)}%)**")
    
    if completed_count == total_count:
        st.balloons()
        st.success(f"🎉 太棒了！{user_name} 的行李全部準備齊全，可以出發囉！")
