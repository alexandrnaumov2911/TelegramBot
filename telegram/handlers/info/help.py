from aiogram import types

from telegram.loader import dp

@dp.message_handler(commands= ['help', ])
async def command_help(msg: types.Message):
    await msg.answer('Я ничего не умею :(')
