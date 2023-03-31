from loader import dp, executor
from DataBase.DB import start_db
import handlers


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=start_db())
