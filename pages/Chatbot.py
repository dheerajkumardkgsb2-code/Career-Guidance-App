import streamlit as st
import streamlit.components.v1 as components

def chatbot():
    st.set_page_config(page_title="Career Guidance Chatbot", layout="wide")
    st.title("💬 Career Guidance Chatbot")

    st.markdown("""
        Welcome to your personal career assistant!  
        Ask me anything about **career options**, **skills**, **education paths**, and more.
    """)

    # Embedding Chatbase chatbot via iframe
    components.html(
        """
        <iframe
            src="https://www.chatbase.co/chatbot-iframe/xEwaLQuHJptgC1qj1HS4r"
            width="100%"
            style="height: 100%; min-height: 700px;"
            frameborder="0"
            allow="microphone"
        ></iframe>
        """,
        height=700,
        scrolling=True
    )

if __name__ == "__main__":
    chatbot()
