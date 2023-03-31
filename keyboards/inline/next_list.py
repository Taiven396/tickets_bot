from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def kb_next_list() -> InlineKeyboardMarkup:
    """
     Функция создает инлайн кнопки "Следующий билет"
     "Остановиться на этом билете"
     :return: InlineKeyboardMarkup инлайн клавиатура
     """
    inline_next_button = InlineKeyboardButton(text='Следующий билет',
                                              callback_data='next_list')
    inline_stop = InlineKeyboardButton(text='Остановиться на этом билете',
                                       callback_data='stop')
    kb = InlineKeyboardMarkup(row_width=1).add(inline_next_button, inline_stop)
    return kb
