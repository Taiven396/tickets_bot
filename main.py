from loader import dp, executor
from utils.on_start import on_startup


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup())
