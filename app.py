import streamlit as st
from brain import JarvisBrain
import time

st.set_page_config(page_title="JARVIS v2.0", page_icon="🌐", layout="wide")

# Load our new Glassmorphism CSS
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Sidebar - System Diagnostics
with st.sidebar:
    st.markdown("<h1 style='color: #00f2fe;'>SYSTEM OS</h1>", unsafe_allow_html=True)
    st.divider()
    
    # Pulsing Status Indicator
    st.markdown("""
        <div style='display: flex; align-items: center;'>
            <div style='height: 10px; width: 10px; background-color: #00ff00; border-radius: 50%; margin-right: 10px; box-shadow: 0 0 10px #00ff00;'></div>
            <p style='margin: 0;'>Core: ONLINE</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.info("Memory: 3072-dim Vector Space")
    if st.button("🔄 Reset Neural Link"):
        st.session_state.messages = []
        st.rerun()

# Main UI
st.markdown("<h1 style='text-align: center; color: white; text-shadow: 0 0 20px #7000ff;'>J.A.R.V.I.S.</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; opacity: 0.6;'>Neural Network Interface • Phi-3 Mini Engine</p>", unsafe_allow_html=True)

if "jarvis" not in st.session_state:
    st.session_state.jarvis = JarvisBrain()

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Neural link established. How can I assist, sir?"}]

# Render Messages
for msg in st.session_state.messages:
    icon = "👤" if msg["role"] == "user" else "🤖"
    with st.chat_message(msg["role"], avatar=icon):
        st.markdown(msg["content"])

# Command Input
if prompt := st.chat_input("Enter command..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)

    with st.chat_message("assistant", avatar="🤖"):
        # Advanced "Processing" visual
        placeholder = st.empty()
        placeholder.markdown("🔍 *Scanning database...*")
        
        response = st.session_state.jarvis.ask_jarvis(prompt)
        
        # Typewriter effect for realism
        full_response = ""
        for char in response:
            full_response += char
            placeholder.markdown(full_response + "▌")
            time.sleep(0.01)
        placeholder.markdown(full_response)
        
    st.session_state.messages.append({"role": "assistant", "content": response})