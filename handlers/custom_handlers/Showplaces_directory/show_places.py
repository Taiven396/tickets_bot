from loader import dp
from aiogram import types
from FSM.FSM import UserTripInfo


@dp.callback_query_handler(text='showplaces')
async def find_show_places(callback: types.CallbackQuery) -> None:
    """
    Функция срабатывает, когда пользователь
    нажимает кнопку "Достопримечательности"
    запрашивает город
    :param callback: (CallbackQuery) объект от
    нажатия инлайн кнопки
    """
    await UserTripInfo.showplaces.set()
    await callback.message.answer('Введите город для поиска '
                                  'достопримечательностей.')
