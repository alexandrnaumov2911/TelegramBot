from config import TOKEN

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
import logging

logging.basicConfig(level=logging.INFO)


bot = Bot(token = TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands= ['start'])
async def start(msg: types.Message):
    await msg.answer('Привет, это эхо бот')

@dp.message_handler(commands= ['help'])
async def start(msg: types.Message):
    await msg.answer('Я умею только повторять сообщения :(')

@dp.message_handler()
async def answer(msg: types.Message):
    await bot.send_message(msg.chat.id, msg.text)


if __name__ == '__main__':
    from aiogram import executor

    executor.start_polling(dp, skip_updates = True)