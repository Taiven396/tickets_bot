from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def kb_yes_no() -> InlineKeyboardMarkup:
    """
    Функция создает инлайн кнопки "Да" "Нет"
    :return: InlineKeyboardMarkup инлайн клавиатура
    """
    inline_yes_button = InlineKeyboardButton(text='Да', callback_data='yes')
    inline_no_button = InlineKeyboardButton(text='Нет', callback_data='no')
    kb = InlineKeyboardMarkup().add(inline_yes_button, inline_no_button)
    return kb
