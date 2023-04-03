from loader import dp
from aiogram import types
from FSM.FSM import UserTripInfo
from keyboards.inline.history_choice import kb_history


@dp.callback_query_handler(text='history')
async def history_select(callback: types.CallbackQuery) -> None:
    """
    Функция вызывается при нажатии инлайн
    кнопки "История запросов",
    выводит последние 10 запросов пользователя
    :param callback: CallbackQuery объект после
    нажатия инлайн кнопки
    """
    await UserTripInfo.history.set()
    await callback.message.answer('Пожалуйста, выберите, какую '
                                  'именно\nисторию вы хотите запросить:',
                                  reply_markup=kb_history())
