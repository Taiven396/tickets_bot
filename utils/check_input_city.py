from aiogram.dispatcher import FSMContext
from aiogram import types
import emoji


async def check_city_input(message: types.Message,state: FSMContext) -> bool:
    async with state.proxy() as data:

        last_city_letter = data['city_out'][-1][-1]
        if last_city_letter == 'ъ' or last_city_letter == 'ь':
            last_city_letter = data['city_out'][-2][-2]
        elif not message.text.lower().startswith(last_city_letter):
            await message.answer(
                f'Ой, вы ошиблись начальной буквой. Назовите город на букву'
                f' {last_city_letter}, пожалуйста. {emoji.emojize(":smiling_face:")}'
            )
            return False
        elif message.text.title() in data["city_out"]:
            await message.answer(
                f'{emoji.emojize(":no_entry:")} '
                f'Этот город уже был использован. Попробуйте другой!'
            )
            return False
        elif not message.text.title() in data["city_in_game"]:
            await message.answer(
                f"{emoji.emojize(':no_entry:')} "
                "Такого города не существует. Попробуйте еще раз."
            )
            return False
        data['city_in_game'].remove(message.text.title())
        data['city_out'].append(message.text.title())
        return True