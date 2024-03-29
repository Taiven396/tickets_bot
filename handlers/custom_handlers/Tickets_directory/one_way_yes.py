from loader import dp
from FSM.FSM import UserTripInfo
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram_calendar import DialogCalendar


@dp.callback_query_handler(state=UserTripInfo.one_way_or_not, text='yes')
async def return_ticket(callback: types.CallbackQuery,
                        state: FSMContext) -> None:
    """
    Функция срабатывает, когда пользователь
    нажимает Inline кнопку "Да",
    добавляет в дату юзера параметр
    one_way True (нужен обратный рейс),
    запрашивает планируемую дату обратного рейса,
    переключает состояние
    на return_at
    :param callback: CallbackQuery объект от нажатия Inline кнопки
    :param state: FSMContext машина состояний
    """
    user_data = await state.get_data()
    await UserTripInfo.return_at.set()
    await callback.message.answer(
        "Для поиска подходящих рейсов,\n"
        "пожалуйста, выберите дату обратного вылета.\n"
        f"Она должна быть не ранее {user_data['departure_at']}",
        reply_markup=await DialogCalendar().start_calendar()
    )
    await state.update_data(one_way=True)
