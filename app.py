import streamlit as st
import time
from brain import JarvisBrain

st.set_page_config(page_title="JARVIS OS", page_icon="💠", layout="wide")

# Injecting the new CSS
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- SIDEBAR: SYSTEM DIAGNOSTICS ---
with st.sidebar:
    st.markdown("<h2 style='color: #00d2ff; letter-spacing: 2px;'>SYSTEM CORE</h2>", unsafe_allow_html=True)
    st.write("---")
    
    # Status Indicators
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Uptime", value="99.9%")
    with col2:
        st.metric(label="Latency", value="24ms")
        
    st.write("---")
    if st.button("🗑️ Wipe Memory Cache", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# --- MAIN INTERFACE ---
st.markdown("<h1 style='text-align: center; font-family: monospace; color: white;'>J.A.R.V.I.S. INTERFACE</h1>", unsafe_allow_html=True)

if "jarvis" not in st.session_state:
    st.session_state.jarvis = JarvisBrain()

if "messages" not in st.session_state:
    st.session_state.messages = []

# Displaying chat with custom icons
for message in st.session_state.messages:
    avatar = "🛰️" if message["role"] == "assistant" else "👨‍🚀"
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

# User Input Logic
if prompt := st.chat_input("Input Command..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="👨‍🚀"):
        st.markdown(prompt)

    with st.chat_message("assistant", avatar="🛰️"):
        # Simulated Typewriter Response
        response_placeholder = st.empty()
        full_response = st.session_state.jarvis.ask_jarvis(prompt)
        
        current_text = ""
        for char in full_response:
            current_text += char
            response_placeholder.markdown(current_text + "▌")
            time.sleep(0.01) # Speed of typing
        response_placeholder.markdown(current_text)

    st.session_state.messages.append({"role": "assistant", "content": full_response})