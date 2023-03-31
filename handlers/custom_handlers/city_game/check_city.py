from loader import dp
from FSM.FSM import UserTripInfo
from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.inline.game import kb_game
from keyboards.inline.start import kb_start


@dp.message_handler(state=UserTripInfo.game)
async def check_city(message: types.Message, state: FSMContext):
    """
    Функция проверяет было ли использовано
    название города в игре и вообще существует
    ли такой город, если проверки проходят,
    игра продолжается
    :param message: (Message) сообщение от пользователя
    :param state: (FSMContext) машина состояний
    """
    async with state.proxy() as data:
        last_city_letter = data['city_out'][-1][-1]
        if last_city_letter == 'ъ' or last_city_letter == 'ь':
            last_city_letter = data['city_out'][-2][-2]
        else:
            pass
        if message.text.title() in data["city_out"]:
            await message.answer('Такой город уже был.')
            return
        if not message.text.title() in data["city_in_game"]:
            await message.answer('Такого города не существует.')
            return
        if not message.text.lower().startswith(last_city_letter):
            await message.answer(f'Вам нужно назвать город на букву'
                                 f' {last_city_letter}.')
            return
        data['city_in_game'].remove(message.text.title())
        data['city_out'].append(message.text.title())
        if message.text[-1] == 'ь' or message.text[-1] == 'ъ':
            await message.answer(f'Мне на букву {message.text[-2]}')
            new_letter = message.text[-2]
        else:
            await message.answer(f'Мне на букву {message.text[-1]}')
            new_letter = message.text[-1]

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
                return
            else:
                await message.answer(f'Вам на букву {city[-1]}',
                                         reply_markup=kb_game())
                data['city_in_game'].remove(city)
                data['city_out'].append(city)
                return
        await message.answer(f'Городов на букву {new_letter}'
                             f'больше нет.\nИгра окончена!')
        await state.reset_state()
        await message.answer('Чем еще могу помочь?',
                             reply_markup=kb_start())
