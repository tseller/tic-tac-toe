import os
from floggit import flog
import streamlit as st
from gemini import generate_content, generate_image

st.title("Rojbot")
st.write("Rojbot is a chatbot that can help you with your queries.")

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

@flog
def update_history():
    st.session_state.chat_history.append(st.session_state.chat_input)
    image_filename = generate_image(st.session_state.chat_history[-1])
    st.image(image_filename)
    os.remove(image_filename)
    #st.session_state.chat_history.append(gemini_response)

if st.session_state.chat_history:
    st.write(st.session_state.chat_history[-1])

st.chat_input(on_submit=update_history, key='chat_input')
