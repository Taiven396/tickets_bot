import datetime
from DataBase.DB import Showplaces


def history_showplace(user_id: int) -> str:
    """
    Функция запрашивает из базы данных список последних 10 строк,
    поиск осуществляется по user_id
    :param user_id: int айди пользователя
    :return: str смоделированную строку с информацией о запросе
    """
    search_param = Showplaces.select().limit(10).where(
        Showplaces.user_id == user_id).order_by(Showplaces.search_date.desc()
                                                )
    all_search = search_param.dicts().execute()
    if len(all_search) == 0:
        yield 'Данных о запросах не найдено.'
    else:
        for request in all_search:
            yield (f'Дата поиска: {request["search_date"].strftime("%Y-%m-%d")}\n'
                  f'Город поиска: {request["city"]}\n')

async def add_to_db_showplaces(city: str, user_id: int) -> None:
    """
    Функция добавляет в базу данных строку с
    информацией о запросе
    :param city: (str) название города
    :param user_id: (int) айди пользователя
    """
    Showplaces(
        search_date=datetime.datetime.now(),
        user_id=user_id,
        city=city
    ).save()
