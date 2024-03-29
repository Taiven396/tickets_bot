from loader import dp
from aiogram import types
import time
from DataBase.Showplaces_DB import history_showplace
from keyboards.inline.start import kb_start
from FSM.FSM import UserTripInfo
from aiogram.dispatcher import FSMContext
from loguru import logger
from datetime import datetime



@dp.callback_query_handler(state=UserTripInfo.history,
                           text='showplaces_history')
async def showplaces_history(callback: types.CallbackQuery,
                         state: FSMContext) -> None:
    """
    Функция вызывается при нажатии
    инлайн кнопки "История запросов",
    выводит последние 10 запросов пользователя
    :param callback: CallbackQuery объект
    после нажатия инлайн кнопки
    """
    logger.info(f'\nПользователь: {callback.from_user.full_name},id: {callback.from_user.id}, запросил '
                f'историю запросов достопримечательностей в {datetime.now()}')
    await callback.message.answer('Выполняю поиск ваших запросов в базе данных')
    for search in history_showplace(user_id=callback.from_user.id):
        time.sleep(1)
        await callback.message.answer(search)
    await state.reset_state()
    await callback.message.answer(
        'Если у вас возникли еще вопросы, я готов помочь!\n'
        'Выберите одну из доступных опций в меню ниже:',
        reply_markup=kb_start()
    )

