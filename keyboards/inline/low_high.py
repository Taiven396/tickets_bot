from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def kb_low_high() -> InlineKeyboardMarkup:
    """
     Функция создает инлайн кнопки "По увеличению цены" "По уменьшению цены"
     :return: InlineKeyboardMarkup инлайн клавиатура
     """
    inline_low_button = InlineKeyboardButton(text='По увеличению цены',
                                             callback_data='low')
    inline_high_button = InlineKeyboardButton(text='По уменьшению цены',
                                              callback_data='high')
    kb = InlineKeyboardMarkup(row_width=1).add(inline_low_button,
                                               inline_high_button)
    return kb
