from loader import dp
from aiogram_calendar import dialog_cal_callback, DialogCalendar
from keyboards.inline.yes_no import kb_yes_no
from utils.date_check import date_check
from FSM.FSM import UserTripInfo
from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext



@dp.callback_query_handler(dialog_cal_callback.filter(),
                           state=UserTripInfo.return_at)
async def dialog_calendar_return_at(callback_query: CallbackQuery,
                                    callback_data,
                                    state: FSMContext) -> None:
    """
    Функция проверяет выбранную дату пользователем,
    если проверка успешная, добавляет дату обратного
    рейса в дату параметр return_at, переключает
    состояние на direct,
     если дата обратного рейса не прошла проверку,
     предлагает выбрать дату еще раз.
    :param callback: CallbackQuery объект после
    нажатия инлайн кнопки
    :param callback_data: (Dict) словарь полученный
    из выбора даты вылета через DialogCalendar
    :param state: (FSMContext) машина состояний
    """
    selected, date = await DialogCalendar().process_selection(callback_query,
                                                              callback_data)
    async with state.proxy() as data:
        if date_check(departure_date=data['departure_at_datetime'],
                      return_date=date):
            await state.update_data(return_at=date.strftime("%Y-%m-%d"))
            user_data = await state.get_data()
            await callback_query.message.\
                answer(f'Выбранная дата обратного рейса:\n'
                      f'{user_data["return_at"]}')
            await callback_query.message.\
                answer('Рассматривать рейсы с пересадками?.',
                      reply_markup=kb_yes_no())
            await UserTripInfo.direct.set()
        else:
            await callback_query.message.\
                answer('Планируемая дата обратного '
                      'рейса\nуказана неверно, '
                      'попробуйте еще раз.',
                      reply_markup=await DialogCalendar().start_calendar())
            return None
