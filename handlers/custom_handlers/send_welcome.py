from loader import dp
from keyboards.inline.start import kb_start
from aiogram import types
import emoji
from loguru import logger
from datetime import datetime


@dp.message_handler()
async def send_welcome(message: types.Message) -> None:
    """
    Функция отправляет в чат приветственное сообщение,
    с возможностью выбрать действие в виде Inline кнопок
    :param message: Message сообщение от пользователя
    """
    logger.info(
        f'\nПользователь: {message.from_user.full_name} ,'
        f'id: {message.from_user.id}, начал работу '
        f'с ботом в {datetime.now()}, '
        f'написав сообщение {message.text}'
    )
    await message.answer(
        f"{emoji.emojize(':waving_hand:')} "
        f"Здравствуй, {message.from_user.full_name}! "
        f"Рад видеть тебя!\nЯ здесь, чтобы помочь тебе с:\n\n"
        f"{emoji.emojize(':airplane:')} "
        f"Поиском билетов в обе стороны (с ограничением в 30 дней между рейсами)\n\n"
        f"{emoji.emojize(':airplane:')} Нахождением самых дешевых билетов в одну или обе стороны без ограничений по датам\n\n"
        f"{emoji.emojize(':classical_building:')} "
        f"Поиском достопримечательностей в городе\n\n"
        f"{emoji.emojize(':closed_book:')} "
        f"Просмотром истории запросов.\n\n"
        f"{emoji.emojize(':video_game:')}"
        f"И даже предложить сыграть в игру!\n\n"
        f"Если возникнут проблемы, просто напиши 'reload'",
        reply_markup=kb_start()
    )