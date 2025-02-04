from floggit import flog
import streamlit as st
from gemini import generate_content

st.title("Rojbot")
st.write("Rojbot is a chatbot that can help you with your queries.")

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

@flog
def update_history():
    st.session_state.chat_history.append(st.session_state.chat_input)
    gemini_response = generate_content(st.session_state.chat_history)
    st.session_state.chat_history.append(gemini_response)

if st.session_state.chat_history:
    st.write(st.session_state.chat_history[-1])

st.chat_input(on_submit=update_history, key='chat_input')

# Inject custom CSS to change the background color to blue, the font, and the font color
st.markdown(
    """
    <style>
    .stApp {
        background-color: red;
        font-family: 'serif', sans-serif;
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)
