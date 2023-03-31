class Tickets_iterator:
    """
    Класс итератор, возвращает смоделированную строку из списка с билетами
    """
    def __init__(self, tickets: list) -> None:
        self.__tickets = tickets
        self.__count = 0

    def __iter__(self):
        self.__count = 0
        return self

    def __next__(self):
        if self.__tickets is None:
            raise StopIteration
        if self.__count < len(self.__tickets):
            ticket = self.__tickets[self.__count]
            self.__count += 1
            return f'Авиакомпания: {ticket["airline"]}\n' \
                   f'Город вылета: {ticket["origin"]}\n' \
                   f'Город прилёта: {ticket["destination"]}\n' \
                   f'Время в пути в минутах: {ticket["duration"]}\n' \
                   f'Вылет: {ticket["departure_at"][0:10]}  ' \
                   f'{ticket["departure_at"][12:18]}\n' \
                   f'Цена (руб): {ticket["price"]}\n' \
                   f'Ссылка: https://www.aviasales.ru{ticket["link"]}'
        raise StopIteration


class Tickets_iterator_High:
    """
    Класс итератор, возвращает смоделированную строку из списка с билетами,
    начинает с самых дорогих билетов
    """
    def __init__(self, tickets: list) -> None:
        self.__tickets = tickets
        self.__count = -1

    def __iter__(self):
        self.__count = -1
        return self

    def __next__(self):
        if self.__tickets is None:
            raise StopIteration
        if self.__count > -len(self.__tickets):
            ticket = self.__tickets[self.__count]
            self.__count -= 1
            return f'Авиакомпания: {ticket["airline"]}\n' \
                   f'Город вылета: {ticket["origin"]}\n' \
                   f'Город прилёта: {ticket["destination"]}\n' \
                   f'Время в пути в минутах: {ticket["duration"]}\n' \
                   f'Вылет: {ticket["departure_at"][0:10]}  ' \
                   f'{ticket["departure_at"][12:18]}\n' \
                   f'Обратный рейс: {ticket["return_at"][0:10]}  ' \
                   f'{ticket["return_at"][12:18]}\n' \
                   f'Цена (руб): {ticket["price"]}\n' \
                   f'Ссылка: https://www.aviasales.ru{ticket["link"]}'
        raise StopIteration


class Tickets_iterator_Low:
    """
    Класс итератор, возвращает смоделированную строку из списка с билетами,
    начинает с самых дешевых билетов
    """
    def __init__(self, tickets: list) -> None:
        self.__tickets = tickets
        self.__count = 0

    def __iter__(self):
        self.__count = 0
        return self

    def __next__(self):
        if self.__tickets is None:
            raise StopIteration
        if self.__count < len(self.__tickets):
            ticket = self.__tickets[self.__count]
            self.__count += 1
            return f'Авиакомпания: {ticket["airline"]}\n' \
                   f'Город вылета: {ticket["origin"]}\n' \
                   f'Город прилёта: {ticket["destination"]}\n' \
                   f'Время в пути в минутах: {ticket["duration"]}\n' \
                   f'Вылет: {ticket["departure_at"][0:10]}  ' \
                   f'{ticket["departure_at"][12:18]}\n' \
                   f'Обратный рейс: {ticket["return_at"][0:10]}  ' \
                   f'{ticket["return_at"][12:18]}\n' \
                   f'Цена (руб): {ticket["price"]}\n' \
                   f'Ссылка: https://www.aviasales.ru{ticket["link"]}'
        raise StopIteration
