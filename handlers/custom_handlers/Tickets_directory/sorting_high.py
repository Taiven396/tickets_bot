from loader import dp
from aiogram import types
from FSM.FSM import UserTripInfo
from aiogram.dispatcher import FSMContext
from utils.next_previous_ticket import next_previous_ticket
from utils.tickets import search_ticket
from keyboards.inline.new_next_previous import kb_next_previous
from keyboards.inline.start import kb_start
from loguru import logger
from DataBase.Tickets_DB import add_to_db_tickets


@dp.callback_query_handler(state=UserTripInfo.sort_choice, text='high')
async def tickets_list_high(callback: types.CallbackQuery, state: FSMContext) -> None:
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
        await callback.message.answer(
            'Выполняю поиск билетов,\n'
            'пожалуйста, подождите...')
        await callback.message.answer_sticker(
            r'CAACAgIAAxkBAAEIXCVkI3g297l5AAE19fHmEquhl'
            r'MYIEcIAAq8lAAKbonBLuDnFfbteCGYvBA'
        )
        try:
            data["now_number_tickets"] = 0
            data['list_ticket'] = list(reversed(
                search_ticket(departure=data["departure"],
                              destination=data["destination"],
                              departure_at=data["departure_at"],
                              return_at=data["return_at"],
                              direct=data["direct"])
            ))
            if len(data['list_ticket']) > 0:
                await UserTripInfo.list_ticket_output.set()
                await callback.message.answer(
                    next_previous_ticket(number=0, data=data["list_ticket"]),
                    reply_markup=kb_next_previous(now_number=1, number_all=len(data))
                )
                return None
        except TypeError:
            await state.reset_state()
            logger.exception(
                f"\nПри поиске списка билетов, сортировка 'high', "
                f"у пользователя {callback.from_user.full_name}, "
                f"id: {callback.from_user.id}, разница даты вылета"
                f"и даты обратного вылета превысила 30 дней"
            )
            await state.reset_state()
            await callback.message.answer(
                'Разница в дате вылета и обратного рейса.\n'
                'не должна превышать 30 дней.\n'
                'Чем могу еще помочь?',
                reply_markup=kb_start()
            )
    await state.reset_state()
    await callback.message.answer(
        'Билеты не найдены.\nЕсли у вас возникли '
        'еще вопросы, я готов помочь!\n'
        'Выберите одну из доступных опций в меню ниже:',
        reply_markup=kb_start()
    )
