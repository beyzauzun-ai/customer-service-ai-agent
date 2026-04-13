import streamlit as st
import requests

API_URL = "https://customer-service-ai-agent-264345805986.europe-west1.run.app"

st.set_page_config(
    page_title="Customer Service AI Agent",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Customer Service AI Agent")
st.caption("Talk to the AI-powered customer service backend.")

if "messages" not in st.session_state:
    st.session_state.messages = []

st.markdown("### Quick Actions")
col1, col2, col3, col4 = st.columns([1, 1, 1, 1])

quick_prompt = None

if col1.button("💸 Refund", use_container_width=True):
    quick_prompt = "I want a refund"

if col2.button("📦 Track Order", use_container_width=True):
    quick_prompt = "Where is my order?"

if col3.button("⚠️ Damaged Product", use_container_width=True):
    quick_prompt = "My product arrived damaged"

if col4.button("🗑️ Clear", use_container_width=True):
    st.session_state.messages = []
    st.rerun()

st.markdown("---")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("Type your message here...")

if quick_prompt:
    user_input = quick_prompt

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    try:
        response = requests.post(
            f"{API_URL}/chat",
            json={"message": user_input},
            timeout=20
        )
        response.raise_for_status()
        data = response.json()
        reply = data.get("reply", "No response received.")
    except requests.exceptions.RequestException as e:
        reply = f"Connection error: {e}"
    except Exception as e:
        reply = f"Error: {e}"

    st.session_state.messages.append({"role": "assistant", "content": reply})

    with st.chat_message("assistant"):
        st.markdown(reply)