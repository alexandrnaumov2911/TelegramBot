from telegram.loader import dp

from aiogram import types

from telegram.utils.keyboards.Keyboard_favorite_film import Keyboard_fv_film
@dp.message_handler(commands= ['favorite_film'])
async def fv_film(msg: types.Message):
    await msg.answer('Посмотреть мой любимый фильм можно, нажав на кнопку', reply_markup = Keyboard_fv_film())

