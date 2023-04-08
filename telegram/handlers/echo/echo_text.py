from aiogram import types

from telegram.loader import dp

@dp.message_handler(
    content_types=types.ContentType.TEXT,
)

async def echo_text(msg: types.Message, ):
    await msg.answer(msg.text)
