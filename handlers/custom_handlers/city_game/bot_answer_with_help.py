from loader import dp
from FSM.FSM import UserTripInfo
from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.inline.game import kb_game
from keyboards.inline.start import kb_start
import emoji
import time


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
            await message.answer(
                f'Теперь мой ход, пытаюсь вспомнить '
                f'город на букву {getted_city[-2].upper()} '
                f'{emoji.emojize(":thinking_face:")}'
            )
            new_letter = getted_city[-2]
        else:
            await message.answer(
                f'Теперь мой ход, пытаюсь вспомнить '
                f'город на букву {getted_city[-1].upper()} '
                f'{emoji.emojize(":thinking_face:")}'
            )
            new_letter = getted_city[-1]
        cur_city = None
        for city in data['city_in_game']:
            if city.lower().startswith(new_letter):
                cur_city = city
                data['city_in_game'].remove(cur_city)
                data['city_out'].append(cur_city)
                time.sleep(2)
                break
        if not cur_city is None:
            await message.answer(
                f'{emoji.emojize(":grinning_face_with_smiling_eyes:")} '
                f'Вспомнил!\n{city.title()}'
            )
            if cur_city[-1] == 'ь' or cur_city[-1] == 'ъ':
                await message.answer(
                    f"{emoji.emojize(':face_with_monocle:')} "
                    f"Теперь ваш ход!\n"
                    f"Назовите город на букву {cur_city[-2].upper()}",
                    reply_markup=kb_game()
                )
                return None
            else:
                await message.answer(
                    f"{emoji.emojize(':face_with_monocle:')} "
                    f"Теперь ваш ход!\n"
                    f"Назовите город на букву {cur_city[-1].upper()}",
                    reply_markup=kb_game()
                )
                return None
        await message.answer(
            f'Я не могу найти город на букву "{new_letter.upper()}".\n'
            f'Кажется, игра окончена!'
        )
        await state.reset_state()
        await message.answer(
            'Если у вас возникли еще вопросы, я готов помочь!\n'
            'Выберите одну из доступных опций в меню ниже:',
            reply_markup=kb_start()
        )

        return None
