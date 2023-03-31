from FSM.FSM import UserTripInfo
from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.inline.yes_no import kb_yes_no
from loader import dp


@dp.callback_query_handler(state=UserTripInfo.one_way_or_not, text='no')
async def next_step_direct(callback: types.CallbackQuery,
                           state: FSMContext) -> None:
    """
    Функция срабатывает, когда пользователь нажимает Inline кнопку "Нет",
    добавляет в дату юзера параметр one_way False (рейс в одну сторону)
    :param callback: (CallbackQuery) объект от нажатия Inline кнопки
    :param state: (FSMContext) машина состояний
    """
    await state.update_data(one_way=False)
    await state.update_data(return_at='')
    await callback.message.answer('Рассматривать рейсы с пересадками?.',
                                  reply_markup=kb_yes_no())
    await UserTripInfo.direct.set()
