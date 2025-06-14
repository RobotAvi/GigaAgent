from langchain_gigachat import GigaChat
from config import GIGACHAT_CREDENTIALS
import atexit

from langgraph.prebuilt import create_react_agent
from langchain_community.tools import DuckDuckGoSearchRun

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

agent = create_react_agent(llm, tools=[search_tool], prompt="Ты полезный ассистент")

inputs = {"messages": [("user", "Какие праздники отмечают завтра?")]}
messages = agent.invoke(inputs)["messages"]

print(messages[-1].content)