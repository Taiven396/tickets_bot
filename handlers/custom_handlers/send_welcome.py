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
        f"{emoji.emojize(':waving_hand:')}  "
        f"Привет, {message.from_user.full_name},"
        f"я могу помочь тебе найти:\n\n"
        f"{emoji.emojize(':airplane:')}  "
        f"Билеты в обе стороны,\n"
        f"но есть ограничение, разница между датой\n"
        f"вылета и обратным рейсом не должна "
        f"превышать 30 дней\n\n"
        f"{emoji.emojize(':airplane:')}  Самый дешевый"
        f" билет в одну или обе стороны\n"
        f"без ограничений по датам\n\n"
        f"{emoji.emojize(':classical_building:')} "
        f"Достопримечательности в городе\n\n"
        f"{emoji.emojize(':closed_book:')} "
        f"Показать историю запросов.\n\n"
        f"{emoji.emojize(':video_game:')}"
        f"Или можем сыграть в игру!\n\n"
        f"В любой непонятной ситуации, напиши reload",
        reply_markup=kb_start()
    )
