# from aiogram.dispatcher import FSMContext
# from utils.tickets import search_ticket
# from utils.iterators import Tickets_iterator
# from FSM.FSM import UserTripInfo
# from keyboards.inline.next import kb_next
# from keyboards.inline.low_high import kb_low_high
#
#
# async def set_direct(message, state: FSMContext) -> None:
#     """
#     Функция срабатывает только тогда, когда
#     пользователь ищет самые дешевые билеты,
#     в зависимости от выбора нужен ли обратный билет,
#     создает 1 или 2 итератора которые будут выводить билеты,
#     переключает состояние на search_tickets_one_way
#     :param message: Message предыдущее сообщение
#     пользователя (в моём случае это CallbackQuery)
#     :param state: FSMContext машина состояний
#     """
#     user_data = await state.get_data()
#     if user_data['cheapest']:
#         await message.message.answer('Выполняю поиск.')
#         await message.message.answer_sticker(r'CAACAgIAAxkBAAEIXCVkI3g'
#                                              r'297l5AAE19fHmEquhlMYIEcI'
#                                              r'AAq8lAAKbonBLuDnFfbteCGYvBA')
#         if not user_data.get('one_way'):
#             async with state.proxy() as data:
#                 data['tickets_first'] = Tickets_iterator(
#                     search_ticket(departure=data["departure"],
#                                   destination=data["destination"],
#                                   departure_at=data["departure_at"],
#                                   return_at='',
#                                   direct=data["direct"]))
#
#                 await message.message.answer('Нажми следующий билет'
#                                              '\nдля отображения билета',
#                                              reply_markup=kb_next())
#
#             await UserTripInfo.search_tickets_one_way.set()
#             return
#         else:
#             async with state.proxy() as data:
#                 await message.message.answer('Выполняю поиск.')
#                 await message.message.answer_sticker(r'CAACAgIAAxkBAAEIXCVkI3g'
#                                                      r'297l5AAE19fHmEquhlMYIEcI'
#                                                      r'AAq8lAAKbonBLuDnFfbteCGYvBA')
#                 data['tickets_first'] = Tickets_iterator(
#                     search_ticket(departure=data["departure"],
#                                   destination=data["destination"],
#                                   departure_at=data["departure_at"],
#                                   return_at='',
#                                   direct=data["direct"]))
#
#                 data['tickets_second'] = Tickets_iterator(
#                     search_ticket(departure=data["destination"],
#                                   destination=data["departure"],
#                                   departure_at=data["return_at"],
#                                   return_at='',
#                                   direct=data["direct"]))
#
#                 await message.message.answer('Нажми следующий билет'
#                                              '\nдля отображения билета',
#                                              reply_markup=kb_next())
#
#             await UserTripInfo.search_tickets_one_way.set()
#             return
#     else:
#         await UserTripInfo.sort_choice.set()
#         await message.message.reply('Как отсортировать список,\n',
#                                     reply_markup=kb_low_high())
