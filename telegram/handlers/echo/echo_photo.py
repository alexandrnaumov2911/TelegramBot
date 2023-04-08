from aiogram import types

from telegram.loader import dp

@dp.message_handler(
    content_types=types.ContentType.PHOTO,
)

async def echo_photo(msg: types.Message):
    photo = msg.photo[-1]
    caption = 'Вот ваша фотография'
    await msg.answer_photo(
        photo= photo.file_id,
        caption = msg.caption if msg.caption else caption
    )