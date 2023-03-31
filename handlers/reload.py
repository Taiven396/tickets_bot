from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text


@dp.message_handler(commands='reload', state='*')
@dp.message_handler(Text(equals='reload', ignore_case=True), state='*')
async def cmd_reload(message: types.Message, state: FSMContext) -> None:
    """
    Функция ресетит машину состояний
    :param msg: Message сообщение пользователя
    :param state: FSMContext машина состояний
    """
    await message.answer('Перезагрузка')
    await state.reset_state()
