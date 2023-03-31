from loader import dp
from FSM.FSM import UserTripInfo
from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext
from utils.next_previous_showplace import next_previous
from keyboards.inline.new_next_previous import kb_next_previous
from loader import bot

@dp.callback_query_handler(text='next',
                           state=UserTripInfo.showplaces_output)
async def next_showplace(callback: CallbackQuery,
                        state: FSMContext) -> None:
    """
    Функция срабатывает, когда пользователь
    нажимает инлайн кнопку "->" при выводе
    достопримечательностей, изменяет последнее
    сообщение бота на новое
    :param callback: (CallbackQuery) объект от
    нажатия инлайн кнопки
    :param state: (FSMContext) машина состояний
    """
    async with state.proxy() as data:
        data['now_number'] += 1
        if data['now_number'] == len(data["showplaces_data"]):
            data['now_number'] = 0
        await bot.edit_message_text(chat_id=callback.from_user.id,
                                    message_id=callback.message.message_id,
                                    text=next_previous(number=data['now_number'],
                                                       data=data["showplaces_data"]),
                                    reply_markup=kb_next_previous(
                                                        now_number=data["now_number"] + 1,
                                                        number_all=len(data["showplaces_data"])))
