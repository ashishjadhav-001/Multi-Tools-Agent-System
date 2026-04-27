import streamlit as st
import requests
import uuid

API_URL = "http://127.0.0.1:8000/chat"

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="City Intelligence AI",
    page_icon="🌍",
    layout="centered"
)

# ------------------ HEADER ------------------
st.markdown("""
    <h1 style='text-align: center;'>🌍 City Intelligence AI</h1>
    <p style='text-align: center; color: gray;'>
        Weather • News • Calculator • Wikipedia
    </p>
""", unsafe_allow_html=True)

# ------------------ SESSION ------------------
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

if "messages" not in st.session_state:
    st.session_state.messages = []

# ------------------ SIDEBAR ------------------
with st.sidebar:
    st.header("⚙️ Controls")

    # 🔥 Clear Chat Button
    if st.button("🧹 Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.divider()

    st.subheader("ℹ️ Info")
    st.write("Multi-tool AI Agent")
    st.caption(f"Session: {st.session_state.session_id[:8]}")

# ------------------ CHAT DISPLAY ------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ------------------ INPUT ------------------
user_input = st.chat_input("Ask about weather, news, math, or anything...")

if user_input:
    # Display user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    # Call backend
    try:
        with st.chat_message("assistant"):
            with st.spinner("🤖 Thinking..."):
                response = requests.post(
                    API_URL,
                    json={
                        "question": user_input,
                        "session_id": st.session_state.session_id
                    },
                    timeout=15
                )

                data = response.json()
                bot_reply = data.get("response", "⚠️ No response")

                st.markdown(bot_reply)

    except Exception as e:
        bot_reply = f"❌ Error: {str(e)}"
        with st.chat_message("assistant"):
            st.error(bot_reply)

    # Save response
    st.session_state.messages.append({
        "role": "assistant",
        "content": bot_reply
    })

# ------------------ FOOTER ------------------
st.markdown("""
---
<p style='text-align: center; font-size: 12px; color: gray;'>
Built with ❤️ using FastAPI + Streamlit
</p>
""", unsafe_allow_html=True)