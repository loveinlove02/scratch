from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv
import os


load_dotenv(verbose=True)
key = os.getenv('OPENAI_API_KEY')

# 1. 프롬프트
prompt = PromptTemplate.from_template(
    """당신은 영어를 가르치는 10년차 영어 선생님입니다.
상황에 맞는 영어 회화를 작성해 주세요.
양식은 [FORMAT]을 참고하여 작성해 주세요.

#상황:
{question}

#FORMAT:
- 영어 회화:
- 한글 해석:
"""
)

# 2. LLM
llm = ChatOpenAI(
    api_key=key,
    model='gpt-4o-mini'
)

# 3. 출력 파서
output_parser = StrOutputParser()

# chain (실행기)
chain = prompt | llm | output_parser

user_input = input('질문: ')
answer = chain.invoke({'question': user_input})

print(answer)
