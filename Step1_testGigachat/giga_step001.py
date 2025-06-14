from langchain_gigachat import GigaChat
from config import GIGACHAT_CREDENTIALS
import atexit

llm = GigaChat(
    # Для авторизации запросов используйте ключ, полученный в проекте GigaChat API
    credentials=GIGACHAT_CREDENTIALS,
    verify_ssl_certs=False,
    model= ("GigaChat-2-Max"),
)

# Закрываем соединение при выходе
def cleanup():
    if hasattr(llm, '_client'):
        llm._client.close()

atexit.register(cleanup)

print(llm.invoke("Кто тебя создал?").content)