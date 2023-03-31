from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from FSM.FSM import UserTripInfo


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
    await callback.message.answer('Введите город отправления.')
    async with state.proxy() as data:
        data["cheapest"] = False
    await UserTripInfo.departure.set()
