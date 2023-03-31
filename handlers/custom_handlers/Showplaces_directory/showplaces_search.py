from loader import dp
from aiogram.dispatcher import FSMContext
from aiogram import types
import requests
from FSM.FSM import UserTripInfo
from config_data import config
from utils.next_previous_showplace import next_previous
from keyboards.inline.new_next_previous import kb_next_previous
from keyboards.inline.start import kb_start
from DataBase.Showplaces_DB import add_to_db_showplaces


@dp.callback_query_handler(text=['after_ticket_yes', 'yes'],
                           state=UserTripInfo.showplaces)
async def showplaces_search(callback: types.CallbackQuery,
                            state: FSMContext) -> None:
    """
    Функция парсит координаты города, далее парсит
    список достопримечательностей
    по координатам и радиусу, создает класс итератор,
    устанавливает в юзер дату параметр data
    :param callback: CallbackQuery объект от нажатия инлайн кнопки
    :param state: FSMContex машина состояний
    """
    await callback.message.answer('Выполняю поиск достопримечательностей.')
    await callback.message.answer_sticker(r'CAACAgIAAxkBAAEIXCVk'
                                          r'I3g297l5AAE19fHmEquhl'
                                          r'MYIEcIAAq8lAAKbonBLuDnFfbteCGYvBA')
    user_data = await state.get_data()
    await add_to_db_showplaces(city=user_data["showplaces_city"],
                               user_id=callback.from_user.id)
    url = f'https://api.opentripmap.com/0.1/ru/places' \
          f'/geoname?name={user_data["showplaces_city"]}' \
          f'&apikey={config.SHOWPLACES}'
    data = requests.get(url).json()

    url = f'https://api.opentripmap.com/0.1/ru/places/' \
          f'radius?radius=20000&lon={data["lon"]}&lat=' \
          f'{data["lat"]}&rate=3&apikey=' \
          f'{config.SHOWPLACES}'
    data = requests.get(url).json()['features']
    await state.update_data(showplaces_data=data)
    await state.update_data(now_number=0)
    if len(data) > 0:
        await UserTripInfo.showplaces_output.set()
        await callback.message.answer(next_previous(number=0, data=data),
                                      reply_markup=kb_next_previous(now_number=1,
                                                                    number_all=len(data)))
        return
    await callback.message.answer('Достопримечательности не найдены.\n'
                                  'Чем могу еще помочь?', reply_markup=kb_start())

