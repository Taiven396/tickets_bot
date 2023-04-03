from loader import dp
from FSM.FSM import UserTripInfo
from aiogram import types


@dp.callback_query_handler(state=UserTripInfo.destination, text='no')
async def city_name_departure_no(callback: types.CallbackQuery) -> None:
    """
    Функция вызывается, если пользователь
    нажмёт инлайн кнопку "Нет"
    при уточнении города назначения
    :param callback: (CallbackQuery) объект
    после нажатия инлайн кнопки
    """
    await callback.message.answer(
        'К сожалению, я могу ошибаться.\nПопробуйте '
        'написать название города полностью, '
        'без сокращений.'
    )