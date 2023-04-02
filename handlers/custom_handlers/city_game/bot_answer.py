from loader import dp
from FSM.FSM import UserTripInfo
from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.inline.game import kb_game
from keyboards.inline.start import kb_start
from utils.check_input_city import check_city_input


@dp.message_handler(state=UserTripInfo.game)
async def bot_answer(message: types.Message,
                     state: FSMContext) -> None:
    """
    Функция проверяет было ли использовано
    название города в игре и вообще существует
    ли такой город, если проверки проходят,
    игра продолжается
    :param message: (Message) сообщение от пользователя
    :param state: (FSMContext) машина состояний
    """
    if await check_city_input(message=message, state=state):
        async with state.proxy() as data:
            if message.text[-1] == 'ь' or message.text[-1] == 'ъ':
                await message.answer(
                    f'Мне на букву {message.text[-2]}'
                )
                new_letter = message.text[-2]
            else:
                await message.answer(
                    f'Мне на букву {message.text[-1]}'
                )
                new_letter = message.text[-1]
            cur_city = None
            for city in data['city_in_game']:
                if city.lower().startswith(new_letter):
                    cur_city = city
                    break
            if not cur_city is None:
                await message.answer(f'{city.title()}')
                if city[-1] == 'ь' or city[-1] == 'ъ':
                    await message.answer(
                        f'Вам на букву {city[-2]}',
                        reply_markup=kb_game()
                    )
                    data['city_in_game'].remove(city)
                    data['city_out'].append(city)
                    return None
                else:
                    await message.answer(
                        f'Вам на букву {city[-1]}',
                        reply_markup=kb_game()
                    )
                    data['city_in_game'].remove(city)
                    data['city_out'].append(city)
                    return None
            await message.answer(
                f'Городов на букву {new_letter}'
                f'больше нет.\nИгра окончена!'
            )
            await state.reset_state()
            await message.answer(
                'Чем еще могу помочь?',
                reply_markup=kb_start()
            )
    return None
