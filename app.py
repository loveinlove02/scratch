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
