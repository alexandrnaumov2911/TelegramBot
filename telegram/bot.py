# https://gitlab.com/alexandrnaumov2911/linteh_28


"""
Реализовать запрос на отправку копии сообщения пользователю, который отправил его боту.
"""

from config import TOKEN

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor



bot = Bot(token = TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def answer_message(msg: types.Message):
    await msg.reply(msg.text)



if __name__ == '__main__':
    executor.start_polling(dp)