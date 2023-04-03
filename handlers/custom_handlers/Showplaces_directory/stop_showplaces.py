from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from FSM.FSM import UserTripInfo
from keyboards.inline.start import kb_start


@dp.callback_query_handler(state=UserTripInfo.showplaces_output,
                           text='stop')
async def next_showplace(callback: types.CallbackQuery,
                         state: FSMContext) -> None:
    """
    Функция останавливает выдачу достопримечательностей,
    ресетит машину состояний
    с предложением выбрать дальнейшее действие
    :param callback: CallbackQuery объект от нажатия инлайн кнопки
    :param state: FSMContext машина состояний
    """
    await state.reset_state()
    await callback.message.answer(
        'Если у вас возникли еще вопросы, я готов помочь!\n'
        'Выберите одну из доступных опций в меню ниже:',
        reply_markup=kb_start()
    )
