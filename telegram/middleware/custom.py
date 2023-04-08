import logging
import sqlite3

from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware


class SomeMiddleware(BaseMiddleware):

    async def on_process_message(self, message: types.Message, data: dict):
        pass
    #     with sqlite3.connect('database.db') as conn:
    #         cur = conn.cursor()

    # TODO: Этот код не работает по причине что нет такой таблицы в БД. Ты ее не создаешь.

    #         cur.execute(
    #             f"""
    #             INSERT INTO chat_message(user_id, chat_id, message) VALUES (?,?,?)
    #         """,
    #             (
    #                 message.from_user.id,
    #                 message.chat.id,
    #                 message.text
    #             )
    #         )
    #         conn.commit()
