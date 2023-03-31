from loader import dp
from FSM.FSM import UserTripInfo
from aiogram import types
from aiogram.dispatcher import FSMContext
from handlers.custom_handlers.Tickets_directory.iterator_creation_cheapest import set_direct


@dp.callback_query_handler(state=UserTripInfo.direct, text='yes')
async def set_direct_yes(callback: types.CallbackQuery,
                         state: FSMContext) -> None:
    """
    Функция добавляет в дату параметр direct(false), рейсы с пересадками,
    запускает функцию set_direct
    :param callback: CallbackQuery объект от нажатия Inline кнопки
    :param state: FSMContext машина состояний
    """
    await state.update_data(direct='false')
    await set_direct(callback, state)
