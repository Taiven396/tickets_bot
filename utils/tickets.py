import requests
from config_data import config
from typing import List
import pprint


def search_ticket(departure: str, destination: str,
				  departure_at: str, return_at: str,
				  direct: str) -> List[dict]:
    """
    Функция на вход получает данные введённые пользователем: город вылета,
    город назначения, дату вылета и дату обратного вылета,
    рейс с пересадками или без,
    возвращает список со словарями с информацией о рейсах
	:param departure: str город вылета
	:param destination: str город назначения
	:param departure_at: str дата вылета
	:param return_at: str дата обратного рейса
	:param direct: str пересадки
	:return:
	"""
    url = (f"https://api.travelpayouts.com/aviasales/v3/prices_for_dates"
	      f"?origin={departure}&destination={destination}&"
		  f"departure_at={departure_at}&return_at={return_at}&sorting="
		  f"price&direct={direct}&currency=rub&limit=30&token={config.TICKETS}")

    response = requests.get(url)
    return response.json()['data']
