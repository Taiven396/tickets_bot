from loader import dp
from utils.city_name_check import get_city_name
from keyboards.inline.yes_no import kb_yes_no
from aiogram import types
from aiogram.dispatcher import FSMContext
from FSM.FSM import UserTripInfo


@dp.message_handler(state=UserTripInfo.departure)
async def city_name_departure_check(message: types.Message,
                                    state: FSMContext) -> None:
    """
    Функция вызывает функцию в которой
    проверяется введённое название города,
    если проверка пройдена, парсится список
    с данными введённого города.
    :param message: (Message) сообщение пользователя
    :param state: (FSMContex) машина состояний
    """
    info = get_city_name(message.text)
    if info is None:
        await message.reply('Такой город не найден, попробуйте еще раз.')
        return
    else:
        await message.reply(f'В базе найден город {info["name"]}, '
                            f'вы имели ввиду его?',
                            reply_markup=kb_yes_no())
        await state.update_data(departure=info["code"])
        await state.update_data(departure_city=info["name"])
