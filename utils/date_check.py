import datetime
from typing import Optional


def date_check(departure_date: datetime,
               return_date: Optional[datetime] = None) -> bool:
    """
    Функция получает на вход только дату
    вылета или дату вылета и обратного рейса,
    проверяет даты на корректность, если
    проверка пройдена возвращает True, в
    противном случае False
    :param departure_date: datetime дата вылета
    :param return_date: Optional[None, datetime]
    дата обратного рейса или None
    :return:
    """
    if return_date is None:
        cur_date = datetime.datetime.now()
        if departure_date <= cur_date:
            return False
        return True
    else:
        if return_date >= departure_date:
            return True
        return False
