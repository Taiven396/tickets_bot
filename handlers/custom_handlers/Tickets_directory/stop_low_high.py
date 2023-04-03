from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from FSM.FSM import UserTripInfo
from keyboards.inline.after_tickets import kb_after_ticket
from DataBase.Tickets_DB import add_to_db_tickets


@dp.callback_query_handler(state=UserTripInfo.list_ticket_output,
                           text='stop')
async def next_showplace(callback: types.CallbackQuery,
                         state: FSMContext) -> None:
    """
    Функция останавливает выдачу достопримечательностей,
    ресетит машину состояний
    с предложением выбрать дальнейшее действие
    :param callback: (CallbackQuery) объект от
    нажатия инлайн кнопки
    :param state: (FSMContext) машина состояний
    """
    user_data = await state.get_data()
    await UserTripInfo.showplaces.set()
    await callback.message.answer(f'Хотите посмотреть достопримечательности\n'
                                  f'города {user_data["destination_city"]}?',
                                  reply_markup=kb_after_ticket())
