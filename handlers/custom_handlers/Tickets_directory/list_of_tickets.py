from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from FSM.FSM import UserTripInfo
from datetime import datetime
from loguru import logger


@dp.callback_query_handler(text='list')
async def ask_departure_city_list(callback: types.CallbackQuery,
                                  state: FSMContext) -> None:
    """
    Функция запрашивает город отправления, устанавливает
    параметр cheapest False в юзер дату, переключает
    состояние на departure
    :param callback: (CallbackQuery) объект от нажатия инлайн кнопки
    :param state: (FSMContext) машина состояний
    """
    logger.info(
        f'\nПользователь: {callback.from_user.full_name},id: '
        f'{callback.from_user.id}, начал поиск '
        f'списка билетов в {datetime.now()}'
    )
    await callback.message.answer('Пожалуйста, введите город отправления.')
    async with state.proxy() as data:
        data["cheapest"] = False
    await UserTripInfo.departure.set()
