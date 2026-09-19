import streamlit as st
import random

# --- SECRETS ---
OWNER_CODE = st.secrets.get("OWNER_CODE", "GHANA2026")
VALID_CODES = st.secrets.get("VALID_CODES", [])

# --- PAGE CONFIG ---
st.set_page_config(page_title="Pro Max GH", page_icon="⚽")

# --- LOGIN LOGIC ---
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
    st.session_state.is_owner = False

if not st.session_state.authenticated:
    st.title("⚽ Pro Max GH - Login")
    st.write("Enter your access code to continue")
    code = st.text_input("Access Code", type="password")
    
    if st.button("Unlock"):
        if code == OWNER_CODE:
            st.session_state.authenticated = True
            st.session_state.is_owner = True
            st.session_state.user_code = code
            st.rerun()
        elif code in VALID_CODES:
            st.session_state.authenticated = True
            st.session_state.is_owner = False
            st.session_state.user_code = code
            st.rerun()
        else:
            st.error("Invalid code! Contact 0543799980")
    st.stop()

# --- OWNER MODE ---
is_owner = st.session_state.is_owner

if is_owner:
    st.success(f"👑 OWNER MODE - {st.session_state.user_code}")
    if st.button("🎲 Generate NEW Customer Code"):
        new_code = f"SP-{random.randint(1000,9999)}"
        st.code(new_code)
        st.info("Copy this code and add it to Secrets VALID_CODES")

st.markdown("---")

# --- YOUR MAIN APP CONTENT HERE ---
st.title("⚽ Sporty Predictor GH")
st.write("Welcome! Your prediction app is live!")
# Add your prediction logic below this line

if st.button("Logout"):
    st.session_state.authenticated = False
    st.rerun()
