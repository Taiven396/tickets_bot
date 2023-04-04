from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def kb_start() -> InlineKeyboardMarkup:
    """
    Функция создает инлайн кнопки "Самый дешёвый билет"
    "Список билетов" "История запросов"
    :return: InlineKeyboardMarkup инлайн клавиатура
    """
    inline_cheapest_button = InlineKeyboardButton(text='Самый дешевый билет',
                                                  callback_data='cheapest')
    inline_two_way_button = InlineKeyboardButton(text='Список билетов',
                                                 callback_data='list')
    inline_history = InlineKeyboardButton(text='История запросов',
                                          callback_data='history')
    inline_showplaces = InlineKeyboardButton(text='Достопримечательности',
                                             callback_data='showplaces')
    inline_game = InlineKeyboardButton(text='Игра города',
                                       callback_data='game')
    kb = InlineKeyboardMarkup(row_width=1).add(inline_cheapest_button,
                                               inline_two_way_button,
                                               inline_history,
                                               inline_showplaces,
                                               inline_game)
    return kb
