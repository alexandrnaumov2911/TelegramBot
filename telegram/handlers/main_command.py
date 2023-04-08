from aiogram import types

from telegram.loader import dp

@dp.message_handler(
    commands= ['start', ]
)
async def command_start(msg: types.Message):
    await msg.answer('Привет, я эхо бот')
