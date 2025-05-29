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

def create_chain():
    prompt = load_prompt('prompts/summary.yaml', encoding='utf-8')



print_message()

user_input = st.chat_input('궁금한 내용을 입력하세요')
