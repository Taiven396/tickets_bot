import datetime
from DataBase.DB import Search
from typing import Dict


def history(user_id: int) -> str:
    """
    Функция запрашивает из базы данных список последних 10 строк,
    поиск осуществляется по user_id
    :param user_id: (int) айди пользователя
    :return: str смоделированную строку с информацией о запросе
    """
    search_param = Search.select().limit(10).where(
        Search.user_id == user_id).order_by(Search.search_date.desc())
    all_search = search_param.dicts().execute()
    if len(all_search) == 0:
        yield 'Данных о запросах не найдено.'
    else:
        for request in all_search:
            yield (f'Дата поиска: {request["search_date"].strftime("%Y-%m-%d")}\n'
                  f'Город отправления: {request["departure"]}\n'
                  f'Город назначения: {request["destination"]}\n'
                  f'Дата вылета: {request["departure_at"]}\n'
                  f'Дата обратного вылета: {request["return_at"]}\n'
                  f'Тип запроса: {request["type_of_search"]}')

async def add_to_db_tickets(data: Dict, user_id: int) -> None:
    """
    Функция добавляет в базу данных строку с
    информацией о запросе
    :param data: (Dict) словарь в котором сохранена
     информация о запросе пользователя
    :param user_id: (int) айди пользователя
    """
    Search(
        search_date=datetime.datetime.now(),
        user_id=user_id,
        departure=data["departure_city"],
        destination=data["destination_city"],
        departure_at=data["departure_at"],
        return_at=data["return_at"],
        type_of_search='Список билетов'
    ).save()

async def add_to_db_cheapest(data: Dict, user_id: int) -> None:
    """
    Функция добавляет в базу данных строку с
    информацией о запросе
    :param data: (Dict) словарь в котором сохранена
     информация о запросе пользователя
    :param user_id: (int) айди пользователя
    """
    Search(
        search_date=datetime.datetime.now(),
        user_id=user_id,
        departure=data["departure_city"],
        destination=data["destination_city"],
        departure_at=data["departure_at"],
        return_at='',
        type_of_search='Самый дешёвый билет'
    ).save()

async def add_to_db_cheapest_return(data: Dict, user_id: int) -> None:
    """
    Функция добавляет в базу данных строку с
    информацией о запросе
    :param data: (Dict) словарь в котором сохранена
     информация о запросе пользователя
    :param user_id: (int) айди пользователя
    """
    Search(
        search_date=datetime.datetime.now(),
        user_id=user_id,
        departure=data["destination_city"],
        destination=data["departure_city"],
        departure_at=data["return_at"],
        return_at='',
        type_of_search='Самый дешёвый билет'
    ).save()
