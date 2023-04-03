from loader import dp
from aiogram_calendar import dialog_cal_callback, DialogCalendar
from aiogram.dispatcher import FSMContext
from FSM.FSM import UserTripInfo
from aiogram.types import CallbackQuery
from utils.date_check import date_check
from keyboards.inline.yes_no import kb_yes_no


@dp.callback_query_handler(dialog_cal_callback.filter(),
                           state=UserTripInfo.departure_at)
async def dialog_calendar_departure_at(callback: CallbackQuery,
                                       callback_data,
                                       state: FSMContext) -> None:
    """
    Функция проверяет дату вылета на корректность,
    при прохождении проверки
    устанавливает в data два параметра departure_at
    для парсинга билетов и
    departure_at_datetime для базы данных
    :param callback: (CallbackQuery) объект после
    нажатия инлайн кнопки
    :param callback_data: словарь полученный
    из выбора даты вылета через DialogCalendar
    :param state: (FSMContex) машина состояний
    :return:
    """
    selected, date = await DialogCalendar().process_selection(callback,
                                                              callback_data)
    async with state.proxy() as user_data:
        if date_check(departure_date=date):
            user_data["departure_at"] = date.strftime("%Y-%m-%d")
            user_data["departure_at_datetime"] = date
            # user_data = await state.get_data()
            await callback.message.reply(f'Выбранная дата вылета: '
                                               f'{user_data["departure_at"]}')
            if user_data['cheapest'] == True:
                await UserTripInfo.one_way_or_not.set()
                await callback.message.answer(
                    'Пожалуйста, укажите, нужен ли вам обратный билет?',
                                              reply_markup=kb_yes_no()
                )
            else:
                await state.update_data(one_way=True)
                await UserTripInfo.return_at.set()
                await callback.message.\
                    answer("Выберите планируемую дату обратного рейса",
                           reply_markup=await DialogCalendar().start_calendar())
        else:
            await callback.message.\
                reply('Планируемая дата вылета указана неверно, '
                      'попробуйте еще раз.',
                      reply_markup=await DialogCalendar().start_calendar())
            return None
