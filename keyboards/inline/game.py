from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def kb_game():
    inline_help = InlineKeyboardButton(text='Подсказка',
                                       callback_data='help')
    inline_stop = InlineKeyboardButton(text='Остановить игру',
                                       callback_data='stop')
    kb = InlineKeyboardMarkup(row_width=1).add(inline_help,
                                               inline_stop)
    return kb
