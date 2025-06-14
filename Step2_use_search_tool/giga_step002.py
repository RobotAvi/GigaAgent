from langchain_gigachat import GigaChat
from config import GIGACHAT_CREDENTIALS
import atexit
from colorama import init, Fore, Style

from langgraph.prebuilt import create_react_agent
from langchain_community.tools import DuckDuckGoSearchRun

# Initialize colorama
init()

llm = GigaChat(
    # Для авторизации запросов используйте ключ, полученный в проекте GigaChat API
    credentials=GIGACHAT_CREDENTIALS,
    verify_ssl_certs=False,
    model= ("GigaChat-2-Max"),
    top_p=0
)

# Закрываем соединение при выходе
def cleanup():
    if hasattr(llm, '_client'):
        llm._client.close()

atexit.register(cleanup)

search_tool = DuckDuckGoSearchRun()

agent = create_react_agent(
    llm, 
    tools=[search_tool], 
    prompt="""Ты полезный ассистент. При ответе на вопросы:
    1. Сначала напиши "Рассуждаю:" и объясни:
       - Что нужно узнать
       - Почему тебе нужен или не нужен поиск
       - Какие факты ты ищешь
    2. Только потом используй инструменты или отвечай
    3. В конце объясни, как ты пришел к ответу"""
)

inputs = {"messages": [("user", "Кто такой Авенир Воронов?")]}
messages = agent.invoke(inputs)["messages"]

# Print all messages to see the reasoning process
for msg in messages:
    color = Fore.GREEN if msg.type == "user" else Fore.BLUE if msg.type == "assistant" else Fore.YELLOW
    print(f"\n{color}{msg.type}{Style.RESET_ALL}: {msg.content}")