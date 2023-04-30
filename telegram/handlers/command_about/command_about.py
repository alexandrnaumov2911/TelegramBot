from aiogram import types

from telegram.loader import dp

@dp.message_handler(commands= ['about'])
async def command_about(msg: types.Message):
    await msg.answer('Я эхо бот. Я способен повторить вам текст или фото, которое вы отправили.')