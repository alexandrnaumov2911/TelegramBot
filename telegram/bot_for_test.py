"""
Доп дз
"""
from config import TOKEN

from aiogram import types, Bot
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardMarkup
from asyncio import sleep
from random import choice


bot = Bot(token=TOKEN)

dp = Dispatcher(bot)

values = ['ножницы', 'бумага', 'камень']

list_win = [
    ['ножницы', 'бумага'],
    ['бумага', 'камень'],
    ['камень', 'ножницы']
]

@dp.message_handler(commands= ['start'])
async def command_start(msg: types.Message):
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard= True,
        one_time_keyboard= True
    )

    buttons = [
        "Начать",
    ]


    keyboard.add(*buttons)

    await msg.answer("""Привет, это бот для игры камень, ножницы бумага. 
Для того чтобы начать игру, нажмите кнопку.""", reply_markup=keyboard)


@dp.message_handler(Text(equals="Начать"))
async def start(msg: types.Message):
    await msg.answer("Отлично! Напишите свой вариант (ножницы, бумага или камень)")

@dp.message_handler(Text(equals=["камень", "ножницы", "бумага",], ignore_case= True))
async def result(msg: types.Message):
    res = list()
    res.append(choice(values))
    res.append(msg.text)
    await sleep(1)
    await msg.answer(f'Выбор бота: {res[0]}')
    await msg.answer('Бот победил' if res in list_win else 'Ничья' if res[0] == res[1] else 'Вы победили')


if __name__ == '__main__':
    from aiogram import executor

    executor.start_polling(
        dispatcher=dp,
        skip_updates=True,
    )
