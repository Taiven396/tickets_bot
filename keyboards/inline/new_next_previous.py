from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def kb_next_previous(now_number: int,number_all: int) -> InlineKeyboardMarkup:
    inline_next = InlineKeyboardButton(text='->', callback_data='next')

    inline_number = InlineKeyboardButton(f'{now_number}/{number_all}', callback_data='page')
    inline_previous = InlineKeyboardButton(text='<-', callback_data='previous')
    inline_stop = InlineKeyboardButton(text='Закончить', callback_data='stop')
    kb = InlineKeyboardMarkup().add(inline_previous, inline_number,inline_next)
    kb.add(inline_stop)
    return kb