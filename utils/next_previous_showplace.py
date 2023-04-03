import requests
from config_data import config


def next_previous(number: int, data: dict) -> str:
    id = data[number]['properties']['xid']
    url = (f'https://api.opentripmap.com/0.1/ru/places/xid/{id}'
          f'?apikey={config.SHOWPLACES}')
    data = requests.get(url).json()
    small_info = data.get('wikipedia_extracts')
    if small_info is None:

        return (f"Название: {data['name']}\n"
               f"Ссылка: {data['otm']}")

    return (f"Название: {data['name']}\n"
           f"Ссылка: {data['otm']}\n"
           f"Краткое описание: {small_info['text']}")