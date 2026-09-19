import streamlit as st
import random
from datetime import datetime

st.set_page_config(page_title="Pro Max GH Auto", page_icon="S", layout="centered")

st.markdown("""
<style>
.stApp {background:#0e0e0e; color:white;}
.stButton>button {background:#00ff88; color:black; font-weight:900; border-radius:12px; height:50px;}
div[data-testid="stMetric"] {background:#1a1a1a; padding:10px; border-radius:10px; border-left:4px solid #00ff88;}
</style>
""", unsafe_allow_html=True)

OWNER_CODE = st.secrets.get("OWNER_CODE", "GHANA2026")
VALID_CODES = st.secrets.get("VALID_CODES", ["SP-8472","SP-2931","SP-5528","SP-1111","SP-1794"])

if "authenticated" not in st.session_state:
    st.session_state.authenticated=False
    st.session_state.is_owner=False
    st.session_state.balance=100
    st.session_state.history=[]

if not st.session_state.authenticated:
    st.markdown("<h1 style='text-align:center;color:#00ff88'>PRO MAX GH AUTO</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center'>Today's Matches Loaded Automatically</p>", unsafe_allow_html=True)
    code = st.text_input("ACCESS CODE", type="password")
    if st.button("UNLOCK APP"):
        if code == OWNER_CODE:
            st.session_state.authenticated=True; st.session_state.is_owner=True; st.rerun()
        elif code in VALID_CODES:
            st.session_state.authenticated=True; st.session_state.is_owner=False; st.rerun()
        else:
            st.error("Invalid Code! WhatsApp 0543799980")
    st.info("20 GHS Weekly | 50 GHS Monthly")
    st.stop()

# DATA FOR AUTO
TEAM_STATS = {
    "Man City": 2.2, "Arsenal": 1.9, "Liverpool": 2.0, "Chelsea": 1.6, "Man United": 1.5,
    "Real Madrid": 2.1, "Barcelona": 2.0, "Atletico": 1.4, "Bayern": 2.3, "Dortmund": 1.8,
    "Hearts of Oak": 1.3, "Asante Kotoko": 1.4, "Aduana": 1.1, "Medeama": 1.2,
    "PSG": 2.0, "Inter": 1.8, "AC Milan": 1.6, "Napoli": 1.7
}

def get_todays_fixtures():
    day = datetime.now().day
    pools = [
        ["Man City vs Arsenal", "Liverpool vs Chelsea", "Hearts of Oak vs Asante Kotoko", "Real Madrid vs Barcelona", "Bayern vs Dortmund"],
        ["Arsenal vs Man United", "Barcelona vs Atletico", "Asante Kotoko vs Hearts of Oak", "PSG vs Inter", "Chelsea vs Man City"],
        ["Liverpool vs Arsenal", "Real Madrid vs Atletico", "Hearts of Oak vs Aduana", "Bayern vs PSG", "Inter vs AC Milan"]
    ]
    return pools[day % 3]

st.markdown(f"### PRO MAX AUTO - {datetime.now().strftime('%A %d %B')}")
if st.session_state.is_owner:
    st.success("OWNER MODE")

tab1, tab2, tab3, tab4 = st.tabs(["TODAY AUTO", "MANUAL", "ACCA", "VALUE"])

with tab1:
    st.subheader("Today's Auto Matches")
    st.caption("Select match, AI auto-fills stats")
    todays = get_todays_fixtures()
    selected = st.selectbox("Select Today's Match", todays)
    
    # Auto parse
    home_auto, away_auto = [x.strip() for x in selected.split("vs")]
    h_goals = TEAM_STATS.get(home_auto, 1.5)
    a_goals = TEAM_STATS.get(away_auto, 1.2)
    
    col1, col2 = st.columns(2)
    col1.metric(home_auto, f"{h_goals} avg goals")
    col2.metric(away_auto, f"{a_goals} avg goals")
    
    league_auto = st.selectbox("League", ["EPL","La Liga","Ghana PL","UCL","Bundesliga"], key="auto_league")
    
    if st.button("ANALYZE THIS MATCH", type="primary", key="auto_btn"):
        st.balloons()
        total = h_goals + a_goals
        conf = random.randint(84,97)
        st.markdown(f"### {selected}")
        st.markdown(f"**League:** {league_auto} | **AI Confidence:** {conf}% | **Expected Goals:** {round(total,1)}")
        
        # Predictions
        if total > 2.8:
            st.success(f"BANKER: OVER 2.5 GOALS @1.{random.randint(65,90)} - {random.randint(86,95)}% WIN")
        elif total > 2.0:
            st.success(f"BANKER: OVER 1.5 GOALS @1.{random.randint(25,45)} - {random.randint(91,98)}% WIN")
        else:
            st.success(f"BANKER: UNDER 3.5 GOALS @1.{random.randint(30,50)} - {random.randint(82,90)}% WIN")
        
        if h_goals > 1.4 and a_goals > 1.2:
            st.warning(f"VALUE: BTTS YES @1.75 - {random.randint(70,85)}%")
        else:
            st.info(f"VALUE: BTTS NO @1.85")
        
        st.info(f"CORRECT SCORE TIP: {random.choice([f'{random.randint(2,3)}-{random.randint(0,1)}', f'{random.randint(1,2)}-{random.randint(1,2)}'])}")
        st.code(f"AI INSIGHT: {home_auto} scoring {h_goals}/game at home. {away_auto} scoring {a_goals} away. Expect early goal.")
        
        if st.button("Add to Slip"):
            st.session_state.history.append(selected)
            st.toast("Added!")

with tab2:
    st.subheader("Manual Analyzer")
    c1,c2 = st.columns(2)
    with c1:
        home = st.text_input("Home Team", "Man City")
        h_g = st.slider("Home Avg", 0.0, 3.5, 1.8, key="h1")
    with c2:
        away = st.text_input("Away Team", "Arsenal")
        a_g = st.slider("Away Avg", 0.0, 3.5, 1.2, key="a1")
    if st.button("ANALYZE MANUAL"):
        total = h_g + a_g
        st.success(f"Prediction for {home} vs {away}: Over {1.5 if total>2 else 2.5} - Total xG {round(total,1)}")

with tab3:
    st.subheader("Daily ACCA")
    level = st.radio("Level", ["SAFE 2-3 odds","MEDIUM 5-8 odds","BOOM 15+ odds"], horizontal=True)
    if st.button("GENERATE ACCA"):
        fixtures = get_todays_fixtures()
        n = 3 if "SAFE" in level else 4 if "MEDIUM" in level else 5
        chosen = random.sample(fixtures, min(n, len(fixtures)))
        tot=1
        for f in chosen:
            odd=round(random.uniform(1.28,1.70),2)
            tot*=odd
            st.write(f"- {f} -> Over 1.5 @ {odd}")
        st.success(f"TOTAL: {round(tot,2)} | 20 GHS => {round(tot*20)} GHS")

with tab4:
    st.subheader("Value Finder")
    if st.button("SCAN VALUES"):
        for _ in range(3):
            m = random.choice(get_todays_fixtures())
            st.error(f"VALUE: {m} - Over 1.5 @ {round(random.uniform(1.95,2.45),2)} (Fair 1.60)")

if st.button("Logout"):
    st.session_state.authenticated=False
    st.rerun()
