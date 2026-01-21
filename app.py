import streamlit as st
from brain import JarvisBrain

st.set_page_config(page_title="JARVIS: NEURAL LINK", layout="wide")

with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- SIDEBAR: SYSTEM PULSE ---
with st.sidebar:
    st.markdown("### ⚡ SYSTEM PULSE")
    # Using the 'Synthesized Mint' for a healthy status look
    st.markdown("<p style='color: #3FFFB2;'>● Core Online</p>", unsafe_allow_html=True)
    st.progress(100)
    
    st.markdown("---")
    st.caption("Protocol: Y3K-GLASS")
    if st.button("Purge Neural Cache"):
        st.session_state.messages = []
        st.rerun()

# --- MAIN CHAT ---
st.title("J.A.R.V.I.S.")
st.write("Synthetic Intelligence Interface")

# Initialize brain...
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    # Custom avatars for the 2026 look
    avatar = "💎" if msg["role"] == "assistant" else "🔮"
    with st.chat_message(msg["role"], avatar=avatar):
        st.markdown(msg["content"])

# Input handling...
if prompt := st.chat_input("Transmit command..."):
    # (Existing logic to add message and get response)
    pass