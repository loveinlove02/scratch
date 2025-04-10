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


def print_messages():
    for chat_message in st.session_state['messages']:
        with st.chat_message(chat_message.role):
            st.write(chat_message.content)


def add_message(role, message):
    st.session_state['messages'].append(
        ChatMessage(role=role, content=message)
    )



print_messages()
