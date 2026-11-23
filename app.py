
import streamlit as st
from openai import OpenAI

st.set_page_config(
    page_title="My AI Coder",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 My AI Coder")
st.write("Your Personal AI Coding Assistant")

# API Key
try:
    client = OpenAI(
        api_key=st.secrets["OPENAI_API_KEY"]
    )
except Exception:
    st.error("API Key not configured. Please check Streamlit Secrets.")
    st.stop()

# Name
name = st.text_input("Enter your name")

if name:
    st.success(f"Welcome {name}!")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
prompt = st.chat_input("Ask me to write or fix code...")

if prompt:
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("AI is thinking..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-4.1-mini",
                    messages=[
                        {
                            "role": "system",
                            "content": "You are My AI Coder, a helpful coding assistant. Explain code in simple Hindi or English."
                        }
                    ] + st.session_state.messages
                )

                answer = response.choices[0].message.content
                st.markdown(answer)

                st.session_state.messages.append(
                    {"role": "assistant", "content": answer}
                )

            except Exception as e:
                st.error(f"Error: {e}")

if st.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()
    
