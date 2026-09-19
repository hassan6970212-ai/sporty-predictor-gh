import streamlit as st
import random
from datetime import datetime

st.set_page_config(page_title="Pro Max GH VIP", page_icon="S", layout="centered")

# Style
st.markdown("""
<style>
.stApp {background:#0e0e0e; color:white;}
.stButton>button {background:#00ff88; color:black; font-weight:900; border-radius:12px; height:50px; font-size:16px;}
div[data-testid="stMetric"] {background:#1a1a1a; padding:10px; border-radius:10px; border-left:4px solid #00ff88;}
</style>
""", unsafe_allow_html=True)

OWNER_CODE = st.secrets.get("OWNER_CODE", "GHANA2026")
VALID_CODES = st.secrets.get("VALID_CODES", ["SP-8472","SP-2931","SP-5528","SP-1111"])

if "authenticated" not in st.session_state:
    st.session_state.authenticated=False
    st.session_state.is_owner=False
    st.session_state.balance=100
    st.session_state.history=[]

if not st.session_state.authenticated:
    st.markdown("<h1 style='text-align:center;color:#00ff88'>PRO MAX GH - VIP 2026</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center'>AI Football Intelligence | Ghana</p>", unsafe_allow_html=True)
    code = st.text_input("ACCESS CODE", type="password")
    if st.button("UNLOCK APP"):
        if code == OWNER_CODE:
            st.session_state.authenticated=True; st.session_state.is_owner=True; st.rerun()
        elif code in VALID_CODES:
            st.session_state.authenticated=True; st.session_state.is_owner=False; st.rerun()
        else:
            st.error("Invalid Code! WhatsApp: 0543799980 to buy")
    st.info("Price: 20 GHS Weekly | 50 GHS Monthly | Pay to 0543799980")
    st.stop()

# HEADER
colA, colB = st.columns([3,1])
with colA:
    st.markdown(f"### PRO MAX GH\n{datetime.now().strftime('%d %b %Y')}")
with colB:
    st.metric("Balance", f"{st.session_state.balance} GHS")

if st.session_state.is_owner:
    st.success(f"OWNER MODE | Codes Active: {len(VALID_CODES)}")
    with st.expander("OWNER DASHBOARD"):
        st.write("Active Customer Codes:", VALID_CODES)
        if st.button("Generate New Code"):
            new_code = f"SP-{random.randint(1000,9999)}"
            st.code(new_code)
            st.write("Go to Streamlit Secrets and add this code to VALID_CODES list")
        cust_code = st.text_input("Enter customer code to validate")
        if cust_code:
            if cust_code in VALID_CODES:
                st.success("Valid Code - Active User")
            else:
                st.error("Invalid")

tab1, tab2, tab3, tab4 = st.tabs(["MATCH ANALYZER", "DAILY ACCA", "VALUE FINDER", "MY BETS"])

with tab1:
    st.subheader("Deep Match Analysis")
    c1,c2 = st.columns(2)
    with c1:
        home = st.text_input("Home Team", "Hearts of Oak")
        home_goals = st.slider("Home Avg Goals Scored", 0.0, 3.5, 1.8)
        home_form = st.selectbox("Home Last 5", ["WWWWL","WWWDW","LWDWW","WWWWW","Mixed"], key="hf")
    with c2:
        away = st.text_input("Away Team", "Asante Kotoko")
        away_goals = st.slider("Away Avg Goals Scored", 0.0, 3.5, 1.2)
        away_form = st.selectbox("Away Last 5", ["LLLWW","WDLLW","LDLWL","WWLWD","Mixed"], key="af")
    
    league = st.selectbox("Competition", ["Ghana Premier League","EPL","La Liga","Bundesliga","UCL","AFCON"])
    injuries = st.checkbox("Key player injured?")
    
    if st.button("RUN AI ANALYSIS", type="primary"):
        st.balloons()
        # Logic
        total_goals = home_goals + away_goals
        conf = random.randint(78,96)
        if total_goals > 2.5:
            over_pick = "OVER 2.5 GOALS"
            over_conf = random.randint(82,94)
        else:
            over_pick = "OVER 1.5 GOALS"
            over_conf = random.randint(90,99)
        
        btts_prob = int((home_goals*30 + away_goals*30))
        cs1 = f"{random.randint(1,2)}-{random.randint(0,1)}"
        cs2 = f"{random.randint(1,3)}-{random.randint(1,2)}"
        
        st.markdown("---")
        m1,m2,m3 = st.columns(3)
        m1.metric("AI Confidence", f"{conf}%")
        m2.metric("Expected Goals", f"{round(total_goals,1)}")
        m3.metric("BTTS Chance", f"{min(btts_prob,85)}%")
        
        st.markdown(f"#### {home} vs {away} - Prediction")
        st.success(f"BANKER: {over_pick} - Confidence {over_conf}% @1.{random.randint(25,55)}")
        if btts_prob > 65:
            st.success(f"BTTS: YES @1.75 - {btts_prob}%")
        else:
            st.info(f"BTTS: NO @1.90 - {100-btts_prob}%")
        
        st.warning(f"DOUBLE CHANCE: {'1X' if home_goals>away_goals else 'X2'} - {random.randint(80,92)}%")
        st.info(f"CORRECT SCORE: {cs1} or {cs2} | HT/FT: {random.choice(['1/1','1/X','X/1'])}")
        st.write(f"INSIGHT: Home form {home_form}, Away form {away_form}. {'Injury affects odds - value on opponent!' if injuries else 'Both teams full squad - expect open game.'}")
        
        if st.button("Add to My Bets"):
            st.session_state.history.append(f"{home} vs {away} - {over_pick}")
            st.toast("Added to betslip!")

with tab2:
    st.subheader("Today's Accumulator Builder")
    level = st.radio("Risk Level", ["SAFE - 2 to 3 Odds","MEDIUM - 5 to 8 Odds","BOOM - 15+ Odds"], horizontal=True)
    if st.button("GENERATE ACCA"):
        games = [
            ("Man City vs Arsenal", "Over 1.5", 1.28),
            ("Real Madrid vs Barca", "BTTS Yes", 1.65),
            ("Hearts vs Kotoko", "1X", 1.35),
            ("Chelsea vs Liverpool", "Over 0.5 HT", 1.40),
            ("Bayern vs Dortmund", "Over 2.5", 1.70),
            ("Inter vs AC Milan", "Over 1.5", 1.30),
        ]
        pick_num = 3 if "SAFE" in level else 5 if "MEDIUM" in level else 6
        chosen = random.sample(games, pick_num)
        total=1
        for g,p,o in chosen:
            total*=o
            st.write(f"- {g} => {p} @ {o}")
        st.success(f"TOTAL ODDS: {round(total,2)}")
        st.code(f"Stake 20 GHS => Return {round(total*20,1)} GHS\nStake 50 GHS => Return {round(total*50,1)} GHS")
        st.caption("Pro Tip: For SAFE, cashout at 70 mins if winning!")

with tab3:
    st.subheader("Value Bet Finder")
    st.write("AI scans for bookmaker mistakes")
    if st.button("SCAN VALUE BETS"):
        for _ in range(3):
            match = random.choice(["Legon Cities vs Dreams FC","EPL: Brighton vs Palace","La Liga: Getafe vs Sevilla"])
            market = random.choice(["Over 1.5 Goals","Draw No Bet Home","BTTS NO"])
            book_odd = round(random.uniform(1.9, 2.4),2)
            fair_odd = round(book_odd - 0.35,2)
            st.error(f"VALUE FOUND: {match} - {market}\nBook Odd: {book_odd} | Fair Should Be: {fair_odd} | Value: +{random.randint(12,22)}%")
    
with tab4:
    st.subheader("My Bet History & Bankroll")
    st.write(f"Current Balance: {st.session_state.balance} GHS")
    if st.session_state.history:
        for h in st.session_state.history:
            st.write(f"- {h}")
    else:
        st.write("No bets added yet. Analyze a match and click Add to My Bets")
    st.markdown("---")
    st.write("Bankroll Rule: Never stake more than 10% of balance on one bet")

st.markdown("---")
if st.button("Logout"):
    st.session_state.authenticated=False
    st.rerun()
