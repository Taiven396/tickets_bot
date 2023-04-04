import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()

BOT_TOKEN = os.getenv("bot_token")
TICKETS = os.getenv('tickets_api_key')
SHOWPLACES = os.getenv('showplaces')
