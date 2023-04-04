from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def kb_after_ticket():
    inline_yes = InlineKeyboardButton(text='Да', callback_data='after_ticket_yes')
    inline_no = InlineKeyboardButton(text='Нет', callback_data='after_ticket_no')
    kb = InlineKeyboardMarkup(row_width=1).add(inline_yes, inline_no)
    return kb