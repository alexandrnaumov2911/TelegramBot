import logging

from aiogram import Bot, types, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(
    token= TOKEN,
    # parse_mode=
)

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
