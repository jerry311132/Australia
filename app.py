import streamlit as st
from datetime import datetime
import pandas as pd
import requests
import os

# 1. 網頁基本設定
st.set_page_config(
    page_title="2026 澳洲自駕隨身手冊", 
    page_icon="🦘", 
    layout="centered"
)

# 2. 共用行李清單項目
checklist_items = [
    "護照正本 (確認有效期限在 6 個月以上)",
    "澳洲 ETA 電子簽證 (建議列印或手機截圖核准畫面)",
    "台灣駕照正本 + 國際駕照 (自駕小隊駕駛人必備，缺一不可！)",
    "海外高回饋信用卡 (建議帶2張以上備用) + 少量澳幣現金",
    "澳洲規格八字三腳轉接頭 + 延長線 (飯店插座通常不夠用)",
    "行動電源 (注意！必須放在隨身行李登機，不可托運)",
    "保暖防風外套 / 輕量羽絨衣 (澳洲 8 月是冬季，早晚非常涼)",
    "個人常備藥品 (感冒藥、腸胃藥、暈車藥，入境記得申報)",
    "手機網卡 / eSIM (確認在出發前已完成開通設定)",
    "個人盥洗用品 (牙刷、牙膏，澳洲許多環保飯店不主動提供)"
]

# 你的 Google 試算表 CSV 導出與讀取連結
CSV_URL = "https://docs.google.com/spreadsheets/d/1fQVv508Y4aQYYUJL5bOczni58UV7L8Tgs_nyljg6Nxo/export?format=csv&gid=0"
LOCAL_BACKUP_FILE = "travel_backup.csv"

# 3. 雲端/本地資料庫與天氣 API 核心
def load_cloud_data():
    try:
        if os.path.exists(LOCAL_BACKUP_FILE):
            df = pd.read_csv(LOCAL_BACKUP_FILE)
        else:
            df = pd.read_csv(f"{CSV_URL}&nocache={datetime.now().timestamp()}")
            
        cloud_dict = {}
        if df is not None and not df.empty:
            for _, row in df.iterrows():
                user = str(row['User']).strip()
                item = str(row['Item']).strip()
                status = str(row['Status']).strip().upper() == "TRUE"
                if user not in cloud_dict:
                    cloud_dict[user] = {}
                cloud_dict[user][item] = status
        return cloud_dict
    except:
        return {}

def save_cloud_data(user_name, user_answers):
    try:
        current_cloud = load_cloud_data()
        if user_name not in current_cloud:
            current_cloud[user_name] = {}
            
        current_cloud[user_name].update(user_answers)
        
        rows = []
        for user, items in current_cloud.items():
            for item, status in items.items():
                rows.append({"User": user, "Item": item, "Status": str(status).upper()})
        
        df_new = pd.DataFrame(rows)
        df_new.to_csv(LOCAL_BACKUP_FILE, index=False)
        
        st.session_state.cloud_data = current_cloud
        st.session_state.local_backup[user_name] = user_answers
        
        return True
    except Exception as e:
        return False

const App: React.FC = () => {
  const [activeTab, setActiveTab] = useState<TabType>('flight');
  const [selectedDate, setSelectedDate] = useState<string>('1/26');
  const [weather, setWeather] = useState<{ temp: number; code: number } | null>(null);
  const [locationName, setLocationName] = useState<string>('定位中...');

  const getWeatherIcon = (code: number) => {
    if (code === 0) return '☀️';
    if (code <= 3) return '🌤️';
    if (code <= 48) return '🌫️';
    if (code <= 67) return '🌧️';
    if (code <= 77) return '❄️';
    if (code <= 82) return '🌦️';
    if (code <= 86) return '🌨️';
    return '🌩️';
  };

  useEffect(() => {
    if ("geolocation" in navigator) {
      const fetchLocationAndWeather = async (lat: number, lon: number) => {
        try {
          const weatherPromise = fetch(`https://api.open-meteo.com/v1/forecast?latitude=${lat}&longitude=${lon}&current_weather=true`).then(res => res.json());
          const geoPromise = fetch(`https://nominatim.openstreetmap.org/reverse?lat=${lat}&lon=${lon}&format=json&accept-language=zh-TW`).then(res => res.json());

          const [weatherData, geoData] = await Promise.all([weatherPromise, geoPromise]);
          setWeather({
            temp: Math.round(weatherData.current_weather.temperature),
            code: weatherData.current_weather.weathercode
          });
          const city = geoData.address.city || geoData.address.town || geoData.address.suburb || geoData.address.district || geoData.address.state || '未知地點';
          setLocationName(city);
        } catch (error) {
          setLocationName('載入失敗');
        }
      };

      navigator.geolocation.getCurrentPosition(
        (position) => fetchLocationAndWeather(position.coords.latitude, position.coords.longitude),
        () => setLocationName('定位權限關閉')
      );
    }
  }, []);

  const WeatherCard = () => (
    <div className="mx-6 mb-4">
      <div className="bg-soft-white rounded-2xl shadow-journal border-2 border-forest-green/10 p-5 flex items-center justify-between">
        <div className="flex items-center gap-3">
          <div className="bg-forest-green/10 p-2 rounded-xl text-forest-green">
            <Navigation size={22} className="fill-forest-green/20" />
          </div>
          <div>
            <p className="text-xs font-medium text-earth-brown/50 uppercase tracking-widest leading-none mb-1">目前城市</p>
            <p className="text-lg font-bold text-earth-brown">{locationName}</p>
          </div>
        </div>
        {weather && (
          <div className="flex items-center gap-2 bg-snow-beige/50 px-4 py-2 rounded-xl border border-forest-green/5">
            <span className="text-xl font-bold text-forest-green">{weather.temp}°C</span>
            <span className="text-2xl leading-none">{getWeatherIcon(weather.code)}</span>
          </div>
        )}
      </div>
    </div>
  );

# 4. 核心 CSS 注入
custom_style = """
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    div[data-testid="stMarkdownContainer"] p:contains("滑動切換選單"),
    div[data-testid="stMarkdownContainer"]:contains("滑動切換選單") {
        display: none !important;
        visibility: hidden !important;
        height: 0px !important;
        margin: 0 !important;
        padding: 0 !important;
    }
    
    div.element-container:has(iframe), .stAlert + div { border: none !important; }
    
    .stApp {
        background: linear-gradient(rgba(245, 247, 250, 0.95), rgba(245, 247, 250, 0.95)), 
                    url('https://images.unsplash.com/photo-1524820197278-540916411e20?q=80&w=1080') no-repeat center center fixed;
        background-size: cover;
    }
    
    .hero-card {
        background: #1a365d; padding: 30px 20px; border-radius: 12px;
        text-align: center; box-shadow: 0 10px 25px rgba(0,0,0,0.15); margin-bottom: 20px;
    }
    .hero-title { color: #ffffff !important; font-size: 1.6rem !important; font-weight: 700 !important; margin-bottom: 8px !important; }
    .hero-subtitle { color: #90cdf4 !important; font-size: 1.05rem !important; font-weight: 500 !important; }
    
    /* 儀表板自訂樣式 */
    div[data-testid="metric-container"] {
        background: white; border-radius: 10px; padding: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05); text-align: center;
        border: 1px solid #e2e8f0;
    }
    
    p, li, span { line-height: 1.9 !important; font-size: 1.05rem !important; color: #2d3748; }
    
    div[data-testid="stExpander"] {
        background: rgba(255, 255, 255, 0.9) !important; border-radius: 12px !important;
        border: 1px solid rgba(0, 0, 0, 0.05) !important; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03) !important;
        margin-bottom: 12px !important;
    }
    
    .trip-day-header {
        font-size: 1.15rem !important; font-weight: 700 !important; color: #1a365d !important;
        margin-bottom: 10px; border-left: 4px solid #3182ce; padding-left: 10px;
    }
    
    a { color: #2b6cb0 !important; text-decoration: underline !important; font-weight: 700 !important; }
    button[data-baseweb="tab"] { font-size: 1.1rem !important; font-weight: 600 !important; }
</style>
"""
st.markdown(custom_style, unsafe_allow_html=True)

# 初始化緩衝記憶體
if "cloud_data" not in st.session_state:
    st.session_state.cloud_data = load_cloud_data()
if "local_backup" not in st.session_state:
    st.session_state.local_backup = {}

# 5. 側邊欄助理 (僅保留雲端同步按鈕)
with st.sidebar:
    st.markdown("### ⚙️ 系統設定")
    if st.button("🔄 同步最新雲端進度", use_container_width=True):
        st.session_state.cloud_data = load_cloud_data()
        st.toast("✅ 已成功從資料庫即時抓取最新進度！")

# 6. 中央主畫面大標題
st.markdown("""
<div class="hero-card">
    <div class="hero-title">🐨 2026 澳洲自駕隨身手冊</div>
    <div class="hero-subtitle">專案代號：Antigravity 全自動無感閃聯版</div>
</div>
""", unsafe_allow_html=True)

# 7. 頂部儀表板：日期、天氣、倒數
today = datetime.now()
target_date = datetime(2026, 7, 31)
days_left = (target_date - today).days

city, weather_desc = get_location_and_weather()

# 使用 3 個 Column 排列儀表板
col1, col2, col3 = st.columns(3)
col1.metric("📅 今日日期", today.strftime("%Y-%m-%d"))
col2.metric(f"📍 {city}", weather_desc)
col3.metric("⏳ 距離澳洲出發", f"{max(0, days_left)} 天")

st.markdown("<br>", unsafe_allow_html=True)

# 8. 核心頁籤
tab1, tab2, tab3 = st.tabs(["📅 12天完整行程", "🏨 住宿與租車", "🎒 行李清單與安全"])

with tab1:
    st.markdown("### 📍 每日詳細行程安排")
    st.caption("💡 點擊下方行程卡片展開，藍色帶底線字體可一鍵開啟地圖導航")
    
    with st.expander("✈️ 7/31 (五) Day 1：抵達墨爾本"):
        st.markdown('<div class="trip-day-header">🛬 抵達墨爾本機場 → 市區 → 入住飯店</div>• 🏨 **住宿**：<a href="https://maps.google.com/?q=Holiday+Inn+Express+Melbourne+Little+Collins" target="_blank">墨爾本小柯林斯智選假日酒店</a><br>• 🚗 **租車**： 本日不租車', unsafe_allow_html=True)
    with st.expander("☕ 8/1 (六) Day 2：墨爾本市區觀光"):
        st.markdown('<div class="trip-day-header">🏙️ 墨爾本復古英倫風市區大遊覽</div>• 📸 **景點**：<a href="https://maps.google.com/?q=Flinders+Street+Station" target="_blank">弗林德斯街車站</a>、<a href="https://maps.google.com/?q=Hosier+Lane" target="_blank">塗鴉巷 Hosier Lane</a>', unsafe_allow_html=True)
    with st.expander("🐧 8/2 (日) Day 3：彩虹小屋、蒸汽火車與企鵝歸巢"):
        st.markdown('<div class="trip-day-header">🚂 啟動自駕 → 蒸汽火車 → 神仙企鵝</div>• 📸 **景點**：<a href="https://maps.google.com/?q=Brighton+Bathing+Boxes" target="_blank">布萊頓彩虹小屋</a>、<a href="https://maps.google.com/?q=Puffing+Billy+Railway" target="_blank">蒸汽火車</a>、<a href="https://maps.google.com/?q=Phillip+Island+Nature+Parks" target="_blank">企鵝歸巢</a><br>• 🚗 **租車**： 兩台自駕車今日取車出發！', unsafe_allow_html=True)
    with st.expander("🌊 8/3 (一) Day 4：世界最美大洋路壯遊"):
        st.markdown('<div class="trip-day-header">🛣️ Great Ocean Road 大洋路自駕 → 十二門徒石</div>• 🏨 **住宿**：<a href="https://maps.google.com/?q=Great+Ocean+Road+Tourist+Park" target="_blank">大洋路旅客公園飯店</a><br>• 🚗 **租車**： 雙車自駕進行中', unsafe_allow_html=True)
    with st.expander("✈️ 8/4 (二) Day 5：飛往雪梨"):
        st.markdown('<div class="trip-day-header">🚙 大洋路開回機場還車 → 🛫 飛往雪梨</div>• 🏨 **住宿**：<a href="https://maps.google.com/?q=ibis+Styles+Sydney+Central" target="_blank">雪梨中央宜秘思酒店</a>', unsafe_allow_html=True)
    with st.expander("🎢 8/5 (三) Day 6：雪梨歌劇院與樂園"):
        st.markdown('<div class="trip-day-header">🎭 深度探索雪梨市區與港灣</div>• 📸 **景點**：<a href="https://maps.google.com/?q=Sydney+Opera+House" target="_blank">雪梨歌劇院</a>、<a href="https://maps.google.com/?q=Luna+Park+Sydney" target="_blank">月神樂園</a>', unsafe_allow_html=True)
    with st.expander("⛰️ 8/6 (四) Day 7：藍山國家公園"):
        st.markdown('<div class="trip-day-header">🚠 走訪絕美藍山國家公園</div>• 🚌 **行程**：<a href="https://www.kkday.com" target="_blank">KKday 藍山專車一日遊</a>', unsafe_allow_html=True)
    with st.expander("🐋 8/7 (五) Day 8：雪梨港賞鯨"):
        st.markdown('<div class="trip-day-header">🚢 雪梨港出海賞鯨大體驗</div>• 🏨 **住宿**：<a href="https://maps.google.com/?q=ibis+Styles+Sydney+Central" target="_blank">雪梨中央宜秘思酒店</a>', unsafe_allow_html=True)
    with st.expander("🏖️ 8/8 (六) Day 9：飛往黃金海岸"):
        st.markdown('<div class="trip-day-header">🏄 飛往渡假天堂黃金海岸</div>• 🏨 **住宿**：<a href="https://www.airbnb.com" target="_blank">黃金海岸 AirBnb</a>', unsafe_allow_html=True)
    with st.expander("🍔 8/9 (日) Day 10：布里斯本市集"):
        st.markdown('<div class="trip-day-header">🚗 前往布里斯本 → 夜遊熱鬧市集</div>• 📸 **景點**：<a href="https://maps.google.com/?q=Eat+Street+Northshore" target="_blank">Eat Street 貨櫃市集</a>', unsafe_allow_html=True)
    with st.expander("🐨 8/10 (一) Day 11：無尾熊與夜景"):
        st.markdown('<div class="trip-day-header">🌿 親手抱無尾熊！市郊自駕遊</div>• 📸 **景點**：<a href="https://maps.google.com/?q=Lone+Pine+Koala+Sanctuary" target="_blank">龍柏無尾熊保護區</a>、<a href="https://maps.google.com/?q=Mount+Coot-tha+Summit+Lookout" target="_blank">庫薩山夕陽夜景</a><br>• 🚗 **租車**： 布里斯本單日租車', unsafe_allow_html=True)
    with st.expander("🛍️ 8/11 (二) Day 12：準備回台"):
        st.markdown('<div class="trip-day-header">🎁 市區採購伴手禮 → 前往機場搭機</div>• 📸 **景點**：<a href="https://maps.google.com/?q=Brisbane+Airport" target="_blank">布里斯本國際機場</a>', unsafe_allow_html=True)

with tab2:
    st.markdown('<div class="trip-day-header">📍 飯店清單快速地圖導航</div>1. 🏨 **墨爾本 (3晚)**：<a href="https://maps.google.com/?q=Holiday+Inn+Express+Melbourne+Little+Collins" target="_blank">墨爾本小柯林斯智選假日酒店</a><br>2. 🏨 **大洋路 (1晚)**：<a href="https://maps.google.com/?q=Great+Ocean+Road+Tourist+Park" target="_blank">大洋路旅客公園飯店</a><br>3. 🏨 **雪梨 (4晚)**：<a href="https://maps.google.com/?q=ibis+Styles+Sydney+Central" target="_blank">雪梨中央宜秘思酒店</a><br>4. 🏠 **黃金海岸 (1晚)**：<a href="https://www.airbnb.com" target="_blank">黃金海岸 AirBnb</a><br>5. 🏨 **布里斯本 (2晚)**：<a href="https://maps.google.com/?q=The+George+Design+Hotel+Brisbane" target="_blank">布里斯本喬治飯店</a>', unsafe_allow_html=True)
    st.write("---")
    st.info("🚗 **租車提醒**：本次行程共有 **4天** 需使用租車 (8/2, 8/3, 8/4, 8/10)。")

with tab3:
    st.warning("⚠️ **右駕核心口訣**：澳洲為右駕（靠左行駛），轉彎請默念「左小彎、右大彎」，進入圓環請絕對停車禮讓右側來車！")
    st.write("---")
    
    st.subheader("📋 澳洲自駕行李檢查清單")
    
    user_name = st.selectbox("👤 請選取你的名字：", ["駕駛老王", "副駕阿美", "隊員小明", "隊員小華"])
    
    user_records = st.session_state.local_backup.get(user_name, st.session_state.cloud_data.get(user_name, {}))
    
    st.write(f"請勾選 **{user_name}** 已放進行李的物品：")
    
    current_answers = {}
    completed_count = 0
    
    for item in checklist_items:
        default_checked = user_records.get(item, False)
        is_checked = st.checkbox(item, value=default_checked, key=f"cb_{user_name}_{item}")
        current_answers[item] = is_checked
        if is_checked:
            completed_count += 1
            
    total_count = len(checklist_items)
    progress_percentage = completed_count / total_count
    
    st.write("")
    st.progress(progress_percentage)
    st.markdown(f"🎯 **{user_name} 的準備進度：{completed_count} / {total_count} ({int(progress_percentage * 100)}%)**")
    
    if st.button("💾 儲存今日進度", type="primary", use_container_width=True):
        with st.spinner("正在安全鎖定數據並同步..."):
            success = save_cloud_data(user_name, current_answers)
            if success:
                st.success(f"✅ 儲存成功！{user_name} 的數據已鎖定。App 關閉後進度也絕對不會遺失！")
                st.balloons()
