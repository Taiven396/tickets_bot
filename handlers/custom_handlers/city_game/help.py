from aiogram.dispatcher import FSMContext
from aiogram import types
from loader import dp
from FSM.FSM import UserTripInfo
from keyboards.inline.game import kb_game
from keyboards.inline.start import kb_start
from handlers.custom_handlers.city_game.bot_answer_with_help \
    import bot_answer_with_help


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
    async with state.proxy() as data:
        last_city_letter = data['city_out'][-1][-1]
        if last_city_letter == 'ъ' or last_city_letter == 'ь':
            last_city_letter = data['city_out'][-2][-2]
        cur_city = None
        for city in data['city_in_game']:
            if city.lower().startswith(last_city_letter):
                cur_city = city
                data['city_in_game'].remove(city)
                data['city_out'].append(city.title())
                break
        if not cur_city is None:
            await callback.message.answer(
                f'Спешу на помощь!\n'
                f'{city.title()}'
            )
            await bot_answer_with_help(
                getted_city=city,
                state=state,
                message=callback.message
            )
            return None
        else:
            await callback.message.answer(
                f'Городов на букву '
                f'{last_city_letter}'
                f'больше нет.\nИгра окончена!'
            )
            await state.reset_state()
            await callback.message.answer(
                'Чем еще могу помочь?',
                reply_markup=kb_start()
            )
