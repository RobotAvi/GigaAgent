from langchain_gigachat import GigaChat
from config import GIGACHAT_CREDENTIALS
import atexit
import os

from langgraph.prebuilt import create_react_agent
from langchain_community.agent_toolkits import FileManagementToolkit
from langchain_experimental.tools import PythonREPLTool

llm = GigaChat(
    # Для авторизации запросов используйте ключ, полученный в проекте GigaChat API
    credentials=GIGACHAT_CREDENTIALS,
    verify_ssl_certs=False,
    model= ("GigaChat-2"),
    top_p=0
)

# Закрываем соединение при выходе
def cleanup():
    if hasattr(llm, '_client'):
        llm._client.close()

atexit.register(cleanup)


# Создаём рабочую директорию, например текущую или временную
root_dir = os.path.dirname(os.path.abspath(__file__))  # путь к директории скрипта

# Инициализируем toolkit
file_management_toolkit = FileManagementToolkit(root_dir=root_dir)

# Получаем инструменты (например, все доступные)
file_tools = file_management_toolkit.get_tools()

python_repl = PythonREPLTool()
tools = file_tools + [python_repl]

agent = create_react_agent(
    llm,
    tools=tools,
    prompt="""Ты ассистент для работы с файловой системой. При получении команды:
    1. Сначала напиши "План действий:" и перечисли шаги
    2. Добавь tools в шаги
    3. Если нужно создать или исправить Python скрипт:
       - Создай/отредактируй файл с помощью file tool
       - Прочитай содержимое файла
       - Проверь что код корректен и выведет 'Hello World'
       - Если есть ошибки, исправь их
       - Выполни скрипт через python_repl tool
       - Проверь что скрипт выполнился успешно
       - Если скрипт не выполнился, исправь ошибки и выполни его снова
    3. Сообщи об успешном выполнении"""
)

inputs = {"messages": [("user", "Создай папку hello_world_python и файл hello.py с выводом 'Hello World'")]}
messages = agent.invoke(inputs)["messages"]

# Print all messages to see the reasoning process
for msg in messages:
    print(f"\n{msg.type}: {msg.content}")