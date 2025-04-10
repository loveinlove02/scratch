import streamlit as st

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import ChatMessage

from dotenv import load_dotenv
import os

load_dotenv(verbose=True)
key = os.getenv('OPENAI_API_KEY')

st.title('나만의 챗봇')


if 'messages' not in st.session_state:
    st.session_state['messages'] = []

st.session_state['messages'].append(
    ChatMessage(role='user', content='안녕?')
)

st.session_state['messages'].append(
    ChatMessage(role='assistant', content='무엇을 도와드릴까요?')
)

def print_messages():
    for chat_message in st.session_state['messages']:
        with st.chat_message(chat_message.role):
            st.write(chat_message.content)

print_messages()
