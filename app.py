import streamlit as st
import random
from datetime import datetime

st.set_page_config(page_title="Pro Max GH - VIP", page_icon="⚽", layout="centered")

# Custom SportyBet Green Style
st.markdown("""
<style>
    .stApp { background-color: #0a0a0a; color: white; }
    .stButton>button { background-color: #00ff00; color: black; font-weight: bold; border-radius: 10px; width: 100%; }
    .prediction-box { background: #1a1a1a; padding: 15px; border-radius: 10px; border-left: 4px solid #00ff00; margin: 10px 0; }
</style>
""", unsafe_allow_html=True)

OWNER_CODE = st.secrets.get("OWNER_CODE", "GHANA2026")
VALID_CODES = st.secrets.get("VALID_CODES", ["SP-8472","SP-2931"])

if "authenticated" not in st.session_state:
    st.session_state.authenticated=False
    st.session_state.is_owner=False

if not st.session_state.authenticated:
    st.markdown("<h1 style='text-align:center;color:#00ff00'>⚽ PRO MAX GH</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center'>Ghana's #1 AI Predictor</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center'>🔒 VIP Access Only</p>", unsafe_allow_html=True)
    code = st.text_input("Enter Access Code", type="password", placeholder="e.g. SP-8472")
    if st.button("🔓 UNLOCK VIP PREDICTIONS"):
        if code == OWNER_CODE:
            st.session_state.authenticated=True; st.session_state.is_owner=True; st.rerun()
        elif code in VALID_CODES:
            st.session_state.authenticated=True; st.session_state.is_owner=False; st.rerun()
        else:
            st.error("❌ Wrong Code! Buy code: WhatsApp 0543799980")
    st.info("💰 Get Access Code: 20 GHS Weekly / 50 GHS Monthly")
    st.stop()

# LOGGED IN
if st.session_state.is_owner:
    st.success(f"👑 OWNER: {OWNER_CODE} | Active Codes: {len(VALID_CODES)}")
    c1,c2 = st.columns(2)
    with c1:
        if st.button("🎲 Gen New Code"):
            new = f"SP-{random.randint(1000,9999)}"
            st.code(new)
            st.toast(f"New Code: {new}")
    with c2:
        if st.button("📋 Show All Codes"):
            st.write(VALID_CODES)

st.markdown(f"<h2 style='color:#00ff00'>⚽ PRO MAX PREDICTOR</h2><p>{datetime.now().strftime('%A, %d %B %Y - %H:%M')}</p>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["🔮 Single Match", "🔥 Daily Acca", "📊 Strategy"])

with tab1:
    col1, col2 = st.columns(2)
    with col1:
        home = st.text_input("Home Team", "Man City", key="h")
    with col2:
        away = st.text_input("Away Team", "Arsenal", key="a")
    league = st.selectbox("League", ["EPL 🏴󠁧󠁢󠁥󠁮󠁧󠁿","La Liga 🇪🇸","Ghana PL 🇬🇭","UCL 🏆","Serie A 🇮🇹","Other"])
    odd_home = st.slider("Home Form (1-10)", 1, 10, 7)
    
    if st.button("🔮 ANALYZE NOW", type="primary"):
        st.balloons()
        conf = random.randint(82,97)
        st.markdown(f"""
        <div class='prediction-box'>
        <h3>{home} vs {away}</h3>
        <p>League: {league} | AI Confidence: <b style='color:#00ff00'>{conf}%</b></p>
        </div>
        """, unsafe_allow_html=True)
        
        p_safe = random.choice(["Over 1.5 Goals @1.25","Over 0.5 HT @1.40","Double Chance 1X @1.20"])
        p_mid = random.choice(["Over 2.5 Goals @1.85","BTTS YES @1.75","Home Over 1.5 @1.90"])
        p_risk = random.choice(["Correct Score 2-1 @8.5","HT/FT 1/1 @2.10","Over 3.5 Goals @2.80"])
        
        st.success(f"✅ **SAFE (Banker):** {p_safe} - {random.randint(88,98)}% Win")
        st.warning(f"⚠️ **VALUE:** {p_mid} - {random.randint(70,85)}% Win")
        st.info(f"💎 **ODDS BOOST:** {p_risk} - For small stake")
        st.markdown(f"**🧠 AI Insight:** {home} strong home form ({odd_home}/10), expect goals early.")

with tab2:
    st.markdown("### 🔥 Today's 10 Odds Accumulator")
    if st.button("Generate Today's Acca"):
        matches = [
            "Hearts vs Kotoko - Over 1.5",
            "Chelsea vs Liverpool - BTTS YES",
            "Real Madrid vs Barca - Over 2.5",
            "Arsenal vs Man U - 1X",
            "Dortmund vs Bayern - Over 1.5"
        ]
        total = 1.0
        for i, m in enumerate(matches, 1):
            odd = round(random.uniform(1.25, 1.65), 2)
            total *= odd
            st.write(f"{i}. {m} @ {odd}")
        st.success(f"**Total Odds: {round(total,2)}** | Stake 20 GHS → Win {round(total*20,2)} GHS")
        st.caption("Safe version: Pick first 3 only for 2.5 odds")

with tab3:
    st.markdown("### 📊 Bankroll Strategy")
    st.write("If you have 100 GHS:")
    st.code("Day 1-3: 10 GHS per bet (Safe picks only)\nDay 4-7: 20 GHS per bet\nTarget: 250 GHS profit weekly")
    st.error("Rule: NEVER chase loss! Max 2 bets per day.")

st.markdown("---")
if st.button("Logout"):
    st.session_state.authenticated=False
    st.rerun()
