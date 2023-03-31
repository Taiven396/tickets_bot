from loader import dp
from FSM.FSM import UserTripInfo
from aiogram import types


@dp.callback_query_handler(state=UserTripInfo.departure, text='yes')
async def city_name_departure_yes(callback: types.CallbackQuery) -> None:
    """
    Функция вызывается, если пользователь нажмёт
    инлайн кнопку "Да" при уточнении города вылета,
    переключает состояние на destination, выводит
    сообщение о городе назначения
    :param callback: (CallbackQuery) объект после
    нажатия инлайн кнопки
    """
    await UserTripInfo.destination.set()
    await callback.message.answer("Введите город назначения.")
