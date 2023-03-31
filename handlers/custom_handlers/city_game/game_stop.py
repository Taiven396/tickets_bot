from aiogram.dispatcher import FSMContext
from aiogram import types
from loader import dp
from FSM.FSM import UserTripInfo
from keyboards.inline.start import kb_start


@dp.callback_query_handler(text='stop', state=UserTripInfo.game)
async def help(callback: types.CallbackQuery, state: FSMContext) -> None:
    """
    Функция срабатывает, когда пользователь
    нажимает кнопку "Остановить игру", ресетит
    машину состояний
    :param callback: (CallbackQuery) объект от
    нажатия инлайн кнопки
    :param state: (FSMContext) машина состояний
    """
    await state.reset_state()
    await callback.message.answer('Спасибо за игру!')
    await callback.message.answer('Чем могу еще помочь?',
                                  reply_markup=kb_start())
