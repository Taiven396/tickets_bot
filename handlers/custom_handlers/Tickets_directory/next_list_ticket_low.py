from loader import dp
from FSM.FSM import UserTripInfo
from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext
from utils.next_previous_ticket import next_previous_ticket
from keyboards.inline.new_next_previous import kb_next_previous
from loader import bot


@dp.callback_query_handler(text='next',
                           state=UserTripInfo.list_ticket_output)
async def next_ticket_low(callback: CallbackQuery,
                        state: FSMContext) -> None:
    """
    Функция срабатывает, когда пользователь
    нажимает кнопку "->" при просмотре билетов
    изменяет последнее сообщение бота на новое
    :param callback: (CallbackQuery) объект от
    нажатия инлайн кнопки
    :param state: (FSMContext) машина состояний
    """
    async with state.proxy() as data:
        data['now_number_tickets'] += 1
        if data['now_number_tickets'] == len(data["list_ticket"]):
            data['now_number_tickets'] = 0
        await bot.edit_message_text(
            chat_id=callback.from_user.id,
            message_id=callback.message.message_id,
            text=next_previous_ticket(number=data['now_number_tickets'],
                                      data=data["list_ticket"]),
                                      reply_markup=kb_next_previous(
                                                    now_number=data["now_number_tickets"] + 1,
                                                    number_all=len(data["list_ticket"]))
        )
