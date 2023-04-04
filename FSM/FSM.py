from aiogram.dispatcher.filters.state import StatesGroup, State


class UserTripInfo(StatesGroup):
    """
    Машина состояний, содержит список
    возможных состояний бота
    """
    departure = State()
    destination = State()
    departure_at = State()
    one_way_or_not = State()
    return_at = State()
    direct = State()
    list_ticket_output = State()
    sort_choice = State()
    showplaces = State()
    showplaces_output = State()
    game = State()
    history = State()
