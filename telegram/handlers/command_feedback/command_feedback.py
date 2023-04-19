import re
import sqlite3

from aiogram import types
from telegram.loader import dp

from telegram.utils.keyboards.KeyboardAnswer import KeyboardAnswer
from aiogram.types import ReplyKeyboardRemove
@dp.message_handler(commands=['feedback'])
async def command_feedback(msg:types.Message):
    await msg.answer("""Рады что вы хотите оставить отзыв. Вам нравиться бот? Над вашей клавиатурой предложены кнопки для выбора""", reply_markup=KeyboardAnswer)

@dp.message_handler(text = 'Да',)
async def the_answer_is_yes(msg:types.Message):
    await msg.answer(f"Спасибо! Мы рады, что вам всё нравиться", reply_markup=ReplyKeyboardRemove())

@dp.message_handler(text = 'Нет')
async def the_answer_is_not(msg:types.Message):
    await msg.answer(f"""Очень жаль:(, но если вы оставите причину, мы попробуем исправиться
(оставьте причину в формате  --*Причина: ... *--)""", reply_markup=ReplyKeyboardRemove(), parse_mode="Markdown")

@dp.message_handler(regexp=re.compile(r'^Причина:'))
async def Reason(msg: types.Message):
    arg = msg.text.split(':')
    if len(arg) == 2:
        user_id = msg.from_user.id
        timestamp = msg.date.timestamp()
        username = msg.from_user.username
        reason = arg[1]
        with sqlite3.connect('database.db') as conn:
            cur = conn.cursor()
            cur.execute(f"""
                            insert into complaint_book(user_id, timestamp, username, reason) VALUES (?,?,?,?);
                        """,
                        (
                            user_id,
                            timestamp,
                            username,
                            reason
                        )
                    )
    await msg.answer('Спасибо! Ваши жалобы будут рассмотрены.')