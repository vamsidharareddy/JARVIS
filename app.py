import streamlit as st
import time
from brain import JarvisBrain

st.set_page_config(page_title="JARVIS OS", page_icon="💠", layout="wide")

# Injecting the new Cyber-Industrial CSS
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- SIDEBAR: SYSTEM DIAGNOSTICS ---
with st.sidebar:
    st.markdown("<h1 style='color: #00f2fe; font-family: monospace;'>OS INTERFACE</h1>", unsafe_allow_html=True)
    st.write("---")
    
    # Real-time Status Simulator
    st.write("📡 **Neural Link:** `ESTABLISHED`")
    st.write("🧠 **Model:** `Phi-3 Mini`")
    st.write("🛡️ **Security:** `ENCRYPTED`")
    
    st.divider()
    if st.button("🔄 REBOOT SYSTEM", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# --- MAIN INTERFACE ---
st.markdown("<h2 style='text-align: center; letter-spacing: 5px; color: white;'>J.A.R.V.I.S.</h2>", unsafe_allow_html=True)

if "jarvis" not in st.session_state:
    st.session_state.jarvis = JarvisBrain()

if "messages" not in st.session_state:
    st.session_state.messages = []

# Displaying chat with "Glass" styling
for message in st.session_state.messages:
    icon = "🤖" if message["role"] == "assistant" else "👤"
    with st.chat_message(message["role"], avatar=icon):
        st.markdown(message["content"])

# User Command Input
if prompt := st.chat_input("Input command..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)

    with st.chat_message("assistant", avatar="🤖"):
        # Typewriter effect for premium UX
        response_box = st.empty()
        full_response = st.session_state.jarvis.ask_jarvis(prompt)
        
        typed_text = ""
        for char in full_response:
            typed_text += char
            response_box.markdown(typed_text + "▌")
            time.sleep(0.01) # Simulated typing speed
        response_box.markdown(typed_text)

    st.session_state.messages.append({"role": "assistant", "content": full_response})