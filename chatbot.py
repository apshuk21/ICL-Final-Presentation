import streamlit as st # type: ignore
from helpers import agentic_chatbot, is_valid_json, json_to_dataframe

st.set_page_config(page_title="🧠 LangChain Chatbot", layout="centered")

st.title("Dhruva, AI Assistant")

# Initialize conversation
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi! I'm your chatbot. Ask me anything."}
    ]

# Display existing messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        content = msg["content"]

        # 🧾 If assistant message is JSON, try showing as DataFrame
        if msg["role"] == "assistant" and is_valid_json(content):
            df = json_to_dataframe(content)
            if not df.empty:
                st.dataframe(df, use_container_width=True)
            else:
                st.write("No trades found.")
        else:
            st.write(content)

# Handle user input
user_query = st.chat_input("Type your message...")

if user_query:
    st.chat_message("user").write(user_query)
    st.session_state.messages.append({"role": "user", "content": user_query})

    # 💬 Spinner and assistant message
    with st.chat_message("assistant"):
        with st.spinner("Thinking... 🤔"):
            bot_reply = agentic_chatbot(user_query)

            if is_valid_json(bot_reply):
                df = json_to_dataframe(bot_reply)
                if not df.empty:
                    # st.markdown("### 📊 Matched Trades:")
                    st.dataframe(df, use_container_width=True)
                else:
                    st.write("No trades found.")
            else:
                st.write("No trades found.")

    st.session_state.messages.append({"role": "assistant", "content": bot_reply})

