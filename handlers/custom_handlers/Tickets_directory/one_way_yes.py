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
    await UserTripInfo.return_at.set()
    await callback.message.answer("Выберите планируемую дату обратного рейса",
                                  reply_markup=await DialogCalendar()
                                  .start_calendar())
    await state.update_data(one_way=True)
