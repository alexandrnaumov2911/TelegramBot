# https://gitlab.com/alexandrnaumov2911/linteh_28


import random
from config import TOKEN
from expressions import answer

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor



bot = Bot(token = TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def answer_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, random.choice(answer))



if __name__ == '__main__':
    executor.start_polling(dp)