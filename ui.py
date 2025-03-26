import streamlit as st
import requests

# Streamlit UI
st.set_page_config(page_title="SavarkarGPT UI", layout="centered")

st.title("SavarkarGPT Chatbot")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    if message["role"] == "user":
        with st.chat_message("user"):
            st.markdown(message["content"])
    else:
        with st.chat_message("assistant"):
            st.markdown(message["content"])

# Input box for user message
user_input = st.chat_input("Ask your question...")

if user_input:
    # Store user input
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)

    # Send query to API
    try:
        response = requests.post("http://127.0.0.1:5000/query", json={"query": user_input})
        response_data = response.json()
        bot_response = response_data.get("answer", "No response from the bot.")

        # Display bot response
        with st.chat_message("assistant"):
            st.markdown(bot_response)

        # Store bot response in session
        st.session_state.messages.append({"role": "assistant", "content": bot_response})

    except Exception as e:
        st.error(f"Error communicating with the API: {e}")
