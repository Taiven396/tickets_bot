from loader import dp
from utils.city_name_check import get_city_name
from keyboards.inline.yes_no import kb_yes_no
from aiogram import types
from aiogram.dispatcher import FSMContext
from FSM.FSM import UserTripInfo


@dp.message_handler(state=UserTripInfo.showplaces)
async def city_name_showplaces_check(message: types.Message,
                                     state: FSMContext) -> None:
    """
    Функция вызывает функцию в которой проверяется
     введённое название города
    :param message: (Message) сообщение пользователя
    :param state: (FSMContex) машина состояний
    """
    info = get_city_name(message.text)
    if info is None:
        await message.answer(
            'К сожалению, я не смог найти такой город. '
            'Пожалуйста, убедитесь, что вы правильно ввели название города '
            'без опечаток и сокращений, и попробуйте снова.'
        )
        return None
    else:
        await message.answer(
            f'Найден город {info["name"]}.\n'
            f'Это тот, который вы имели ввиду?',
            reply_markup=kb_yes_no()
        )
        await state.update_data(showplaces_city=info["name"])
