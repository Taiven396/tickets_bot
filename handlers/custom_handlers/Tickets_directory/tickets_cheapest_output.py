from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext
from keyboards.inline.after_tickets import kb_after_ticket
from DataBase.Tickets_DB import add_to_db_cheapest, add_to_db_cheapest_return
from FSM.FSM import UserTripInfo


async def cheapest_tickets_output(callback: CallbackQuery,
                                  state: FSMContext) -> None:
    """
    Функция срабатывает только когда пользователь ищет
    самые дешевые билеты, вводит в чат первый билет и
    если нужен обратный, выводит второй.
    :param callback: CallbackQuery объек от нажатия
    инлайн кнопки
    :param state: FSMContext машина состояний
    """
    async with state.proxy() as data:
        try:
            ticket = data['first_ticket'][0]
            await callback.message.answer(
                        f'Авиакомпания: {ticket["airline"]}\n' 
                        f'Город вылета: {ticket["origin"]}\n' 
                        f'Город прилёта: {ticket["destination"]}\n' 
                        f'Время в пути в минутах: {ticket["duration"]}\n' 
                        f'Вылет: {ticket["departure_at"][0:10]}  ' 
                        f'{ticket["departure_at"][12:18]}\n' 
                        f'Цена (руб): {ticket["price"]}\n' 
                        f'Ссылка: https://www.aviasales.ru{ticket["link"]}')
        except IndexError:
            await callback.message.answer(f'Билет из {data["departure_city"]}\n'
                                          f'в город {data["destination_city"]}\n'
                                          f'не найден.')
        try:
            ticket = data['second_ticket'][0]
            await callback.message.answer('Обратный билет:')
            await callback.message.answer(
                        f'Авиакомпания: {ticket["airline"]}\n' 
                        f'Город вылета: {ticket["origin"]}\n' 
                        f'Город прилёта: {ticket["destination"]}\n' 
                        f'Время в пути в минутах: {ticket["duration"]}\n' 
                        f'Вылет: {ticket["departure_at"][0:10]}  ' 
                        f'{ticket["departure_at"][12:18]}\n' 
                        f'Цена (руб): {ticket["price"]}\n' 
                        f'Ссылка: https://www.aviasales.ru{ticket["link"]}'
            )
            await add_to_db_cheapest_return(data=data, user_id=callback.from_user.id)
        except IndexError:
            await callback.message.answer(f'Билет из {data["destination_city"]}\n'
                                          f'в город {data["departure_city"]}\n'
                                          f'не найден.')
            await add_to_db_cheapest_return(data=data, user_id=callback.from_user.id)
        except KeyError:
            pass
        await add_to_db_cheapest(data=data, user_id=callback.from_user.id)
        await UserTripInfo.showplaces.set()
        await callback.message.answer(f'Хотите посмотреть достопримечательности\n'
                                      f'города {data["destination_city"]}?',
                                      reply_markup=kb_after_ticket())
