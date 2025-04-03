from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

from dotenv import load_dotenv
import os

load_dotenv(verbose=True)
key = os.getenv('OPENAI_API_KEY')

# 1. 프롬프트
prompt = PromptTemplate.from_template(
    "{product}는 어는 회사에서 만든 제품인가요?"
)

# 2. LLM
llm = ChatOpenAI(api_key=key,model='gpt-4o-mini')

# 체인 만들기(실행기)
chain = prompt | llm

answer = chain.invoke({'product': '겔럭시폰'})
print(answer)