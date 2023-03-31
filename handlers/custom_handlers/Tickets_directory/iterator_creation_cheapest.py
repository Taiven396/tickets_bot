from aiogram.dispatcher import FSMContext
from utils.tickets import search_ticket
from FSM.FSM import UserTripInfo
from keyboards.inline.low_high import kb_low_high
from loader import dp
from aiogram.types import CallbackQuery
from handlers.custom_handlers.Tickets_directory.tickets_cheapest_output \
    import cheapest_tickets_output


@dp.message_handler(state=UserTripInfo.direct)
async def set_direct(callback: CallbackQuery, state: FSMContext) -> None:
    """
    Функция проверяет параметр 'cheapest', если True
    в зависимости от выбора нужен ли обратный билет,
    парсит 1 или 2 списка с билетами, запускает
    функцию await cheapest_tickets_output,
    если False то запрашивает сортировку,
    переключает состояние на sort_choice
    :param message: (CallbackQuery) предыдущее
    сообщение пользователя
    :param state: (FSMContext) машина состояний
    """
    user_data = await state.get_data()
    if user_data['cheapest'] == True:
        await callback.message.answer('Выполняю поиск.')
        await callback.message.answer_sticker(r'CAACAgIAAxkBAAEIXCVkI3g'
                                              r'297l5AAE19fHmEquhlMYIEcI'
                                              r'AAq8lAAKbonBLuDnFfbteCGYvBA')
        if not user_data.get('one_way'):
            async with state.proxy() as data:
                await state.update_data(first_ticket=search_ticket(
                                  departure=data["departure"],
                                  destination=data["destination"],
                                  departure_at=data["departure_at"],
                                  return_at='',
                                  direct=data["direct"]
                                  ))
            await cheapest_tickets_output(callback=callback, state=state)
        else:
            async with state.proxy() as data:
                await state.update_data(first_ticket=search_ticket(
                                        departure=data["departure"],
                                        destination=data["destination"],
                                        departure_at=data["departure_at"],
                                        return_at='',
                                        direct=data["direct"]
                                        ))
                await state.update_data(second_ticket=search_ticket(
                                        departure=data["destination"],
                                        destination=data["departure"],
                                        departure_at=data["return_at"],
                                        return_at='',
                                        direct=data["direct"]
                                        ))
                await cheapest_tickets_output(callback=callback, state=state)
    else:
        await UserTripInfo.sort_choice.set()
        await callback.message.reply('Как отсортировать список,\n',
                                    reply_markup=kb_low_high())
