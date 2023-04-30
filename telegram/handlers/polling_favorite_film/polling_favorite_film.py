import sqlite3

from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ReplyKeyboardRemove, CallbackQuery
from aiogram.dispatcher.filters.state import State, StatesGroup

from telegram.loader import dp

class CallbackOnStart(StatesGroup):
    Q1 = State()
    Q2 = State()

def genre():
    list_button_genre = (
        ("Комедия", "Фантастика", "Драма", "Ужасы"),
        ("Детектив", "Триллер", "Научная фантастика", "Боевик")
    )

    buttons_list = []
    for item in list_button_genre:
        list1 = []
        for i in item:
            list1.append(
                InlineKeyboardButton(
                    text = i,
                    callback_data = i,
                )
            )
        buttons_list.append(list1)

    keyboard_inline_buttons = InlineKeyboardMarkup(inline_keyboard=buttons_list)

    return keyboard_inline_buttons

@dp.message_handler(commands='start_polling', state = '*')
async def on_start_polling(msg: Message, state: FSMContext):
    user_id = msg.from_user.id
    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()
        user_id_obj = cur.execute(
            f"""
                select user_id from polling_favorite_film where user_id={user_id} and vote is 1
            """
        ).fetchone()
        if user_id_obj is None:
            await msg.answer('Описание опросника')
            await msg.answer(
                (
                    "Вопрос №1\n"
                    "Как вас зовут?"
                ),
                reply_markup = ReplyKeyboardRemove(),
            )
            await state.set_state(CallbackOnStart.Q1.state)
        else:
            await msg.answer("Вы уже проходили тест")

@dp.message_handler(state=CallbackOnStart.Q1)
async def genre_film(msg:Message, state: FSMContext):
    await state.update_data(name = msg.text)
    await msg.answer(
        (
            "Вопрос №2\n"
            "Какой фаш любимый жанр фильмов?\n"
            "Выберите ответ из предложенных"
        ),
        reply_markup=genre(),
    )
    await state.set_state(CallbackOnStart.Q2.state)

@dp.callback_query_handler(state = CallbackOnStart.Q2)
async def end(cb: CallbackQuery, state: FSMContext):
    await state.update_data(
        genre = cb.data,
    )

    data = await state.get_data()
    line_break = '\n\n'
    await cb.message.answer(text=(
        f'Ваши ответы: \n\n'
        f'{line_break.join(data.values())}'),
        reply_markup=ReplyKeyboardRemove()
    )

    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()
        cur.execute("""
                        insert into polling_favorite_film(user_id, vote, data) VALUES (?,?,?)
                    """,
                    (
                        cb.from_user.id,
                        1,
                        str(data)
                    ),
                )
        await state.finish()

@dp.message_handler(commands=['/repeat_polling'])
async def command_repeat_polling(msg: Message):
    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()
        cur.execute(f"""
                        delete from polling_favorite_film where user_id={msg.from_user.id}
                    """
                     )
        conn.commit()
        await msg.answer('Вы можете пройти опрос ещё раз')
