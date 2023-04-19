import re
import sqlite3

from aiogram import types
from telegram.loader import dp

from telegram.utils.keyboards.KeyboardAnswer import KeyboardClaim, KeyboardAnswer
from aiogram.types import ReplyKeyboardRemove
@dp.message_handler(commands=['feedback'])
async def command_feedback(msg:types.Message):
    await msg.answer("""Рады что вы хотите оставить отзыв. Вам нравиться бот? Над вашей клавиатурой предложены кнопки для выбора""", reply_markup=KeyboardAnswer)

@dp.callback_query_handler(text = 'Answer_Yes')
async def inline_answer_yes(cb: types.CallbackQuery):
    await cb.answer()
    await cb.message.answer('Спасибо за ваш отзыв, мы рады, что вам всё нравиться')

@dp.callback_query_handler(text = 'Answer_No')
async def inline_answer_no(cb: types.CallbackQuery):
    await cb.answer()
    await cb.message.answer("Очень жаль, но если вы оставите причину, мы попробуем исправиться", reply_markup= KeyboardClaim)

@dp.message_handler(regexp=re.compile(r'Жалоба:'))
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