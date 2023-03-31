from loader import dp
from FSM.FSM import UserTripInfo
from aiogram import types
from aiogram_calendar import DialogCalendar


@dp.callback_query_handler(state=UserTripInfo.destination, text='yes')
async def city_name_destination_yes(callback: types.CallbackQuery) -> None:
    """
    Функция вызывается, если пользователь
    нажмёт инлайн кнопку
     "Да" при уточнении города назначения,
    переключает состояние на departure_at,
    выводит календарь для выбора даты вылета
    :param callback: (CallbackQuery) объект после
    нажатия инлайн кнопки
    """
    await UserTripInfo.departure_at.set()
    await callback.message.answer("Выберите планируемую дату вылета",
                                  reply_markup=await DialogCalendar().
                                  start_calendar())
