from aiogram import types

from telegram.loader import dp

from telegram.utils.keyboards.Keyboard_with_location import Keyboard_with_location

@dp.message_handler(commands=['location'])
async def command_location(msg: types.Message):
    await msg.answer('Вы можете отправить свою локацию нажав на кнопку', reply_markup= Keyboard_with_location)

@dp.message_handler(text = 'Отправить локацию')
async def locaton(msg: types.Message):
    await msg.answer('Вы отправили свою локацию')