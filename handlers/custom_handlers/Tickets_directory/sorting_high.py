from loader import dp
from aiogram import types
from FSM.FSM import UserTripInfo
from aiogram.dispatcher import FSMContext
from utils.next_previous_ticket import next_previous_ticket
from utils.tickets import search_ticket
from keyboards.inline.new_next_previous import kb_next_previous
from keyboards.inline.start import kb_start


@dp.callback_query_handler(state=UserTripInfo.sort_choice, text='high')
async def tickets_list_high(callback: types.CallbackQuery,
                           state: FSMContext) -> None:
    """
    Функция срабатывает только тогда, когда
    пользователь ищет билеты списком,
    парсит список билетов
    в порядке уменьшения цены за билет,
    срабатывает, когда пользователь выбирает
    сортировку high, переключает состояние на
    list_ticket_output
    :param callback: CallbackQuery объект от нажатия Inline кнопки
    :param state: FSMContext машина состояний
    """
    async with state.proxy() as data:
        await callback.message.answer('Выполняю поиск.')
        await callback.message.answer_sticker(r'CAACAgIAAxkBAAEIXCVkI3g'
                                              r'297l5AAE19fHmEquhlMYIEcI'
                                              r'AAq8lAAKbonBLuDnFfbteCGYvBA')
        data["now_number_tickets"] = 0
        data['list_ticket'] = list(reversed(
                              search_ticket(departure=data["departure"],
                                            destination=data["destination"],
                                            departure_at=data["departure_at"],
                                            return_at=data["return_at"],
                                            direct=data["direct"])))

    if len(data['list_ticket']) > 0:
        await UserTripInfo.list_ticket_output.set()
        await callback.message.answer(next_previous_ticket(number=0, data=data["list_ticket"]),
                                      reply_markup=kb_next_previous(now_number=1,
                                                                    number_all=len(data)))
        return
    await state.reset_state()
    await callback.message.answer('Билеты не найдены.\n'
                                  'Чем могу еще помочь?', reply_markup=kb_start())


