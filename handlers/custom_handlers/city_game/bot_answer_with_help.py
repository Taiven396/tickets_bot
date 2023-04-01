from loader import dp
from FSM.FSM import UserTripInfo
from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.inline.game import kb_game
from keyboards.inline.start import kb_start


@dp.message_handler(state=UserTripInfo.game)
async def bot_answer_with_help(getted_city: str, message,
                     state: FSMContext) -> None:
    """
    Функция проверяет было ли использовано
    название города в игре и вообще существует
    ли такой город, если проверки проходят,
    игра продолжается
    :param message: (Message) сообщение от пользователя
    :param state: (FSMContext) машина состояний
    """
    async with state.proxy() as data:
        if getted_city[-1] == 'ь' or getted_city[-1] == 'ъ':
            await message.answer(f'Мне на букву {getted_city[-2]}')
            new_letter = getted_city[-2]
        else:
            await message.answer(f'Мне на букву {getted_city[-1]}')
            new_letter = getted_city[-1]
        cur_city = None
        for city in data['city_in_game']:
            if city.lower().startswith(new_letter):
                cur_city = city
                break
        if not cur_city is None:
            await message.answer(f'{city.title()}')
            if city[-1] == 'ь' or city[-1] == 'ъ':
                await message.answer(f'Вам на букву {city[-2]}',
                                         reply_markup=kb_game())
                data['city_in_game'].remove(city)
                data['city_out'].append(city)
                return None
            else:
                await message.answer(f'Вам на букву {city[-1]}',
                                         reply_markup=kb_game())
                data['city_in_game'].remove(city)
                data['city_out'].append(city)
                return None
        await message.answer(f'Городов на букву {new_letter}'
                             f'больше нет.\nИгра окончена!')
        await state.reset_state()
        await message.answer('Чем еще могу помочь?',
                             reply_markup=kb_start())
        return None
