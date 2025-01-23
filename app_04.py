from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv(verbose=True)
goole_key = os.getenv('GOOGLE_API_KEY')


template = """
당신은 영어를 가르치는 영어 교사입니다. 상황에 맞는 영어 회화를 작성해주세요.
양식은 [FORMAT]를 참고하여 작성해주세요.

#상황:
{question}

#FORMAT:
- 영어회화
- 한글해석
"""

# 1. prompt 만들기
prompt = PromptTemplate.from_template(template)

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
answer = chain.invoke({'question':'음식점에서 주문을 하고 싶어요'})
print(answer)