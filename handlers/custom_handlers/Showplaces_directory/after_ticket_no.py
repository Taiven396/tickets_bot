from loader import dp
from FSM.FSM import UserTripInfo
from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext
from keyboards.inline.start import kb_start


@dp.callback_query_handler(text='after_ticket_no',
                           state=UserTripInfo.showplaces)
async def after_ticket_no(callback: CallbackQuery,
                           state: FSMContext):
    """
    Функция срабатывает если пользователь
    нажимет кнопку нет при предложении показать
    достопримечательности после вывода билетов
    :param callback: (CallbackQuery) объек после
    нажаитя инлайн кнопки
    :param state: (FSMContext) машина состояний
    :return:
    """
    await state.reset_state()
    await callback.message.answer('Чем могу еще помочь?',
                                  reply_markup=kb_start())
