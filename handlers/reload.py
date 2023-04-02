from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from loguru import logger
from datetime import datetime


@dp.message_handler(commands='reload', state='*')
@dp.message_handler(Text(equals='reload',
                         ignore_case=True), state='*')
async def cmd_reload(message: types.Message,
                     state: FSMContext) -> None:
    """
    Функция ресетит машину состояний
    :param msg: Message сообщение пользователя
    :param state: FSMContext машина состояний
    """
    cur_state = await state.get_state()
    logger.info(
        f'\nПользователь: {message.from_user.full_name}, '
        f'id: {message.from_user.id}, выполнил перезагрузку,'
        f'пользователь был в состоянии {cur_state},'
        f'дата: {datetime.now()}'
    )
    await message.answer('Перезагрузка')
    await state.reset_state()
