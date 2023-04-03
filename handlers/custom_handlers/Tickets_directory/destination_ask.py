from loader import dp
from FSM.FSM import UserTripInfo
from utils.city_name_check import get_city_name
from aiogram import types
from keyboards.inline.yes_no import kb_yes_no
from aiogram.dispatcher import FSMContext


@dp.message_handler(state=UserTripInfo.destination)
async def city_name_destination_check(message: types.Message,
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
    user_data = await state.get_data()
    if info is None:
        await message.answer(
            'К сожалению, я не смог найти такой город. '
            'Пожалуйста, убедитесь, что вы правильно ввели название города '
            'без опечаток и сокращений, и попробуйте снова.'
        )
        return None
    elif info["name"] == user_data["departure_city"]:
        await message.answer(
            'Кажется, вы ввели один и тот же город дважды.\n'
            'Пожалуйста, укажите разные города отправления и назначения.'
        )
        return None
    else:
        await message.answer(
            f'Найден город {info["name"]}.\n'
            f'Это тот, который вы имели ввиду?',
            reply_markup=kb_yes_no()
        )
        await state.update_data(destination=info["code"])
        await state.update_data(destination_city=info["name"])
        await state.update_data(showplaces_city=info["name"])
