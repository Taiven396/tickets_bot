from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from FSM.FSM import UserTripInfo
import random
from keyboards.inline.game import kb_game
from loguru import logger
from datetime import datetime
import os


@dp.callback_query_handler(text='game')
async def lest_play(callback: types.CallbackQuery, state: FSMContext) -> None:
    """
    Функция выводит правила игры, называет рандомный
    город из списка, начинается
    игра
    :param callback: CallbackQuery объект от нажатия инлайн кнопки
    :param state: FSMContext машина состояний
    """
    logger.info(
        f'\nПользователь: {callback.from_user.full_name}, '
        f'id: {callback.from_user.id}, начал '
        f'игру "Города" в {datetime.now()}'
    )
    await callback.message.reply(
        'Давай сыграем в города\n'
        'правила просты, игра начинается с\n'
        'любого названия города\n'
        'вы должны назвать город,\n'
        'название которого начинается на букву\n'
        'которой заканчивается предыдущее название.\n'
        'Повторяться нельзя. Если город\n'
        'оканчивается на ь или ъ'
        ' знак, нужно назвать город\n'
        'на букву стоящую перед ь или ъ знаком.'
    )
    cities = list()
    path = os.path.abspath(os.path.join(
        'handlers', 'custom_handlers',
        'city_game', 'cities.txt'
    ))
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            cities.append(line.rstrip())

    random.shuffle(cities)

    async with state.proxy() as data:
        data['city_in_game'] = cities
        data['city_out'] = list()

    game_start = random.choice(cities)
    await callback.message.answer(f'Я начинаю:\n{game_start}\n')

    if game_start[-1] != 'ь' and game_start[-1] != 'ъ':
        await callback.message.answer(
            f'Вам на букву {game_start[-1]}',
            reply_markup=kb_game()
        )
    else:
        await callback.message.answer(
            f'Вам на букву {game_start[-2]}',
            reply_markup=kb_game()
        )

    async with state.proxy() as data:
        data['city_in_game'].remove(game_start)
        data['city_out'].append(game_start)
    await UserTripInfo.game.set()
