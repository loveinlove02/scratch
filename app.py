import streamlit as st

from langchain_core.messages import ChatMessage
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_teddynote.prompts import load_prompt

from dotenv import load_dotenv
import os

load_dotenv()
key = os.getenv('OPENAI_API_KEY')

st.title('챗봇')


if 'messages' not in st.session_state:
    st.session_state['messages'] = []

def print_message():
    for chat_message in st.session_state['messages']:
        with st.chat_message(chat_message.role):
            st.write(chat_message.content)

def add_message(role, message):
    st.session_state['messages'].append(ChatMessage(role=role, content=message))

add_message(role='user', message='안녕?')
add_message(role='assistant', message='무엇을 도와드릴까요?')

print_message()
