from aiogram.dispatcher import FSMContext
from aiogram import types
from loader import dp
from FSM.FSM import UserTripInfo
from keyboards.inline.game import kb_game
from keyboards.inline.start import kb_start


@dp.callback_query_handler(text='help', state=UserTripInfo.game)
async def help(callback: types.CallbackQuery,
               state: FSMContext) -> None:
    """
    Функция вызывается, когда пользователь просит помочь
    найти город, находит город, выводит его, потом
    выводит город на последнюю букву найденного города
    если в каком-либо месте не удалось найти город,
    выводит соответсвующее сообщение
    :param callback: CallbackQuery объект от нажатия
    инлайн кнопки
    :param state: FSMContext машина состояний
    """
    new_letter = ''
    async with state.proxy() as data:
        last_city_letter = data['city_out'][-1][-1]
        if last_city_letter == 'ъ' or last_city_letter == 'ь':
            last_city_letter = data['city_out'][-2][-2]
        else:
            pass
        cur_city = None
        for city in data['city_in_game']:
            if city.lower().startswith(last_city_letter):
                cur_city = city
                data['city_in_game'].remove(city)
                data['city_out'].append(city.title())
                break
        if not cur_city is None:
            await callback.message.answer(f'Спешу на помощь!\n'
                                              f'{city.title()}')
            if city[-1] == 'ь' or city[-1] == 'ъ':
                await callback.message.answer(f'Мне на букву {city[-2]}')
                new_letter = city[-2]
            else:
                await callback.message.answer(f'Мне на букву {city[-1]}')
                new_letter = city[-1]
        else:
            await callback.message.answer(f'Городов на букву '
                                          f'{last_city_letter}\n'
                                          f'больше нет. Игра окончена!')
            await state.reset_state()
            await callback.message.answer('Чем еще могу помочь?',
                                  reply_markup=kb_start())
        cur_city = None
        for city in data['city_in_game']:
            if city.lower().startswith(new_letter):
                cur_city = city
                break
        if not cur_city is None:
            await callback.message.answer(f'{city.title()}')
            if city[-1] == 'ь' or city[-1] == 'ъ':
                await callback.message.answer(f'Вам на букву {city[-2]}',
                                                  reply_markup=kb_game())
            else:
                await callback.message.answer(f'Вам на букву {city[-1]}',
                                                  reply_markup=kb_game())
                data['city_in_game'].remove(city)
                data['city_out'].append(city)
                return
        await callback.message.answer(f'Городов на букву {new_letter}\n'
                                      f'больше нет. Игра окончена!')
        await state.reset_state()
        await callback.message.answer('Чем еще могу помочь?',
                                      reply_markup=kb_start())

