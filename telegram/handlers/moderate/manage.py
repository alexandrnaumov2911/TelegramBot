import sqlite3

from aiogram import types

from telegram.loader import dp


@dp.message_handler(commands=['block'])
async def command_block(msg: types.Message):
    arg = msg.get_args().split(':')
    if len(arg) == 2:
        user_id_ban = arg[0]
        timestamp = msg.date.timestamp()
        reason = arg[1]

        with sqlite3.connect('database.db') as conn:
            cur = conn.cursor()
            cur.execute(
                """
                    insert into block_list(user_id, timestamp, reason) VALUES (?,?,?);
                """,
                (
                    user_id_ban,
                    timestamp,
                    reason,
                )
            )
            conn.commit()
        await msg.answer('Пользователь добавлен в бан!')

@dp.message_handler(commands=['/unblock'])
async def command_unblock(msg:types.Message):
    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()
        cur.execute(f"""
                        delete from block_list where user_id={msg.from_user.id}
                    """
                     )
        conn.commit()
        await msg.answer('Пользователь разблокирован')
