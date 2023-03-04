

import asyncio
from random import randrange
from config import TOKEN


from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

answer = {1 : 'Я не хочу разговаривать',
          2 : 'Отстань, у меня нет настроения',
          3 : 'Поговорим в другой раз',
          4 : 'Мне кажется, наша коммуникация достигла своего предела. Далее предлагаю пойти каждому своей дорогой.',
          5 : 'Мне кажется, что наше общение недостаточно приятно для меня, поэтому предлагаю прекратить его.',
          6 : 'Прошу простить меня, но продолжать эту беседу желания нет.',
          7 : 'Я не могу продолжать общение, потому что у меня нет на это никакого желания.',
          8 : 'Мне кажется, что наше общение уже исчерпало весь свой потенциал.',
          9 : 'Я не могу продолжать эту беседу, я ухожу.',
          10 : 'Знаешь, я не хочу с тобой общаться!'
}

BASE_URL = 'https://api.telegram.org/bot'
bot = Bot(token = TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def answer_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, answer.get(randrange(1, 10, 1)))



if __name__ == '__main__':
    executor.start_polling(dp)