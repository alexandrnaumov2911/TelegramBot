from aiogram import types

from telegram.loader import dp

import re
@dp.message_handler(
    regexp= re.compile(r'^/help$')
)
async def command_help(msg: types.Message):
    await msg.answer('Я ничего не умею')