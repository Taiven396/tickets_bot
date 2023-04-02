from DataBase.DB import start_db
from logs.create_log import create_logs


def on_startup() -> None:
    """
    Функция инициализирует базу данных
    и создает лог файл, если его еще
    нет
    """
    start_db()
    create_logs()
