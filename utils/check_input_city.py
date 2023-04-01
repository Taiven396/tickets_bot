from aiogram.dispatcher import FSMContext
from aiogram import types


async def check_city_input(message: types.Message,state: FSMContext) -> bool:
    async with state.proxy() as data:
        last_city_letter = data['city_out'][-1][-1]
        if last_city_letter == 'ъ' or last_city_letter == 'ь':
            last_city_letter = data['city_out'][-2][-2]
        elif message.text.title() in data["city_out"]:
            await message.answer('Такой город уже был.')
            return False
        elif not message.text.title() in data["city_in_game"]:
            await message.answer('Такого города не существует.')
            return False
        elif not message.text.lower().startswith(last_city_letter):
            await message.answer(f'Вам нужно назвать город на букву'
                                 f' {last_city_letter}.')
            return False
        data['city_in_game'].remove(message.text.title())
        data['city_out'].append(message.text.title())
        return True