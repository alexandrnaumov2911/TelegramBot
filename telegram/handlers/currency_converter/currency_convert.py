from telegram.loader import dp

import requests
from aiogram import types
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext

class CallbackOnStart(StatesGroup):
    Rub = State()
@dp.message_handler(commands= 'currency_convert', state='*')
async def currency_convert(msg: types.Message, state: FSMContext):
    await msg.answer('Введите количество рублей, которе хотите посчитать в юанях')
    await state.set_state(CallbackOnStart.Rub.state)

@dp.message_handler(state= CallbackOnStart.Rub)
async def end(msg:types.Message, state: FSMContext):
    response = requests.get("https://www.cbr-xml-daily.ru/daily_json.js").json()['Valute']['CNY']['Value']
    if msg.text.isdigit():
        await state.update_data(
            answer = msg.text
        )
        await msg.answer(
            "Итог:\n"
            f"{msg.text} RUB ---> {int(msg.text) * response} CNY"
        )
        await state.finish()
    else:
        await msg.answer('Введите количество рублей корректно')
