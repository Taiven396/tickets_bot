import requests
from typing import Optional, List


def get_city_name(city: str) -> Optional[List]:
    """
    Функция получает на вход название города,
    проверяет строку на содержание ненужных символов
    если проверка пройдена, парсится список с информацией о городе
    :param city: str Название города
    :return: List список с информацией о городе
    """
    if city.replace('-', '').isalpha():
        iata_request = requests.get('https://autocomplete.'
                                    'travelpayouts.com/places2?'
                                    'locale=en&types[]=airport&'
                                    'types[]=city&term=' + city)
        iata_list = iata_request.json()
        if len(iata_list):
            return iata_list[0]
        return None
    else:
        return None


if __name__ == "__main__":
    pass
