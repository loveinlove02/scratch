
from langchain_core.messages import ChatMessage

session_state = {}

if 'messages' not in session_state:
    session_state['messages'] = []


def add_messages(role, message):
    session_state['messages'].append(ChatMessage(role=role, content=message))

def print_message():
    for chat_message in session_state['messages']:
        print(chat_message.role, chat_message.content)

# 대화 내용 추가
add_messages('user', '안녕?')
add_messages('assistant', '무엇을 도와드릴까요?')

# 대화 내용 출력
print_message()

