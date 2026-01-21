import streamlit as st
from brain import JarvisBrain

# 1. Page Configuration
st.set_page_config(page_title="Jarvis OS", page_icon="⚡", layout="wide")

# 2. Inject Custom CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("assets/style.css")

# 3. Sidebar for Settings & Status
with st.sidebar:
    st.image("https://img.icons8.com/clouds/200/iron-man.png", width=100)
    st.title("System Controls")
    st.markdown("---")
    
    # Model Status
    st.success("Core Engine: Phi-3 Mini (Online)")
    st.info("Vector DB: Pinecone (Connected)")
    
    # Clear Chat Button
    if st.button("Clear Memory", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    
    st.markdown("---")
    st.caption("Jarvis Enterprise OS v2.4")

# 4. Initialize Brain & History
if "jarvis" not in st.session_state:
    st.session_state.jarvis = JarvisBrain()

if "messages" not in st.session_state:
    st.session_state.messages = []

# 5. Chat Interface
st.title("⚡ Jarvis AI")
st.subheader("How can I assist you today, Sir?")

# Display messages with Material Icons
for msg in st.session_state.messages:
    # Use Material Icons for a futuristic look
    avatar = ":material/person:" if msg["role"] == "user" else ":material/smart_toy:"
    with st.chat_message(msg["role"], avatar=avatar):
        st.markdown(msg["content"])

# User Input with Spinner
if prompt := st.chat_input("Input command..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar=":material/person:"):
        st.markdown(prompt)

    with st.chat_message("assistant", avatar=":material/smart_toy:"):
        with st.status("Analyzing neural patterns...", expanded=True) as status:
            response = st.session_state.jarvis.ask_jarvis(prompt)
            status.update(label="Response generated!", state="complete", expanded=False)
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})