from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def kb_history():
    inline_tickets = InlineKeyboardButton(text='Запросы билетов',
                                          callback_data='tickets_history')
    inline_showplaces = InlineKeyboardButton(text='Запросы достопримечательностей',
                                             callback_data='showplaces_history')
    kb = InlineKeyboardMarkup(row_width=1).add(inline_tickets, inline_showplaces)
    return kb