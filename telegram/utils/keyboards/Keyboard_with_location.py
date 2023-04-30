from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

Keyboard_with_location = ReplyKeyboardMarkup(resize_keyboard=True)
Keyboard_with_location.add(KeyboardButton('Отправить локацию',request_location= True))