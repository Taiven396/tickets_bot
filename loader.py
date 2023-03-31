from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config_data import config
from aiogram import Bot, Dispatcher, executor, types


bot = Bot(token=config.BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
