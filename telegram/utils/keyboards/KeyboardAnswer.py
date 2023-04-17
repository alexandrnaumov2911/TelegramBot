from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

KeyboardAnswer = ReplyKeyboardMarkup(resize_keyboard=True)

buttons = [
    'Да',
    'Нет'
]

KeyboardAnswer.add(*buttons)
