import logging
import sqlite3

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware

from config import TOKEN


logging.basicConfig(level=logging.INFO)
bot = Bot(
    token=TOKEN,
)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

@dp.message_handler(
    content_types= types.ContentType.TEXT
)
async def echo(msg: types.Message):
    with sqlite3.connect('database.db') as connection:
        cur = connection.cursor()
        user = cur.execute(f" SELECT * FROM user WHERE user_id={msg.from_user.id}").fetchone()
        if not user:
            logging.info(f'Создание нового пользователя: {msg.from_user.username} {msg.from_user.id}')

            data = (msg.from_user.id, msg.chat.id, msg.from_user.username)
            cur.execute(f"INSERT INTO user(user_id, chat_id, username) VALUES (?,?,?) ", data)
            connection.commit()
            await msg.answer('Вы добавлены в БД')
        else:
            await msg.answer('Вы уже в БД')
    await msg.answer(msg.text)


if __name__ == '__main__':
    from aiogram import executor
    from database import create_table

    create_table()

    executor.start_polling(

        dispatcher=dp,
        skip_updates=True,
    )