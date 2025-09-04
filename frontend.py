import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/chat"

st.set_page_config(page_title="Gemini Chatbot", page_icon="🤖", layout="centered")
st.title("🤖 AI Chatbot ")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Show chat history
for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input box
if prompt := st.chat_input("Type your message..."):
    st.session_state["messages"].append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        response = requests.post(API_URL, json={"message": prompt})
        if response.status_code == 200:
            bot_reply = response.json().get("reply", "⚠️ No reply")
        else:
            bot_reply = f"⚠️ Error {response.status_code}: {response.text}"
    except Exception as e:
        bot_reply = f"⚠️ Exception: {str(e)}"

    with st.chat_message("assistant"):
        st.markdown(bot_reply)

    st.session_state["messages"].append({"role": "assistant", "content": bot_reply})
