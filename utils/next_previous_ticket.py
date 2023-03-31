def next_previous_ticket(number: int, data: list) -> str:
    ticket = data[number]
    return f'Авиакомпания: {ticket["airline"]}\n' \
           f'Город вылета: {ticket["origin"]}\n' \
           f'Город прилёта: {ticket["destination"]}\n' \
           f'Время в пути в минутах: {ticket["duration"]}\n' \
           f'Вылет: {ticket["departure_at"][0:10]}  ' \
           f'{ticket["departure_at"][12:18]}\n' \
           f'Цена (руб): {ticket["price"]}\n' \
           f'Ссылка: https://www.aviasales.ru{ticket["link"]}'
