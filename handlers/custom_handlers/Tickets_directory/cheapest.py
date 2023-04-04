from loader import dp
from aiogram import types
from FSM.FSM import UserTripInfo
from aiogram.dispatcher import FSMContext
from datetime import datetime
from loguru import logger


@dp.callback_query_handler(text=['cheapest'])
async def ask_departure_city_cheapest(callback: types.CallbackQuery,
                                      state: FSMContext) -> None:
    """
    Функция отлавливает нажатие инлайн
    кнопки "Самый дешевый билет".
    Переключает состояние на departure,
    запрашивает город отправления,
    в data устанавливает параметр cheapest=True
    :param callback: (CallbackQuery) объект после
    нажатия инлайн кнопки
    :param state: (FSMContex) машина состояний
    """
    logger.info(
        f'\nПользователь: {callback.from_user.full_name}, '
        f'id: {callback.from_user.id}, начал поиск '
        f'самых дешёвых билетов в {datetime.now()}'
    )
    await callback.message.answer('Пожалуйста, введите город отправления.')
    await state.update_data(cheapest=True)
    await UserTripInfo.departure.set()

