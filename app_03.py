from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv(verbose=True)
goole_key = os.getenv('GOOGLE_API_KEY')

# 1. prompt 만들기
prompt = PromptTemplate.from_template(
    '{product}는 어느 회사에서 개발한 제품인가요?'
)

# 2. LLM 생성
llm = ChatGoogleGenerativeAI(
    api_key=goole_key,
    model='gemini-1.5-pro-latest'
)

# 3. 출력 파서
output_parer = StrOutputParser()

# 4. chain 생성
chain = prompt | llm | output_parer

# 5. 실행
answer = chain.invoke({'product':'겔럭시폰'})
print(answer)