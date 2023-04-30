from telegram.loader import dp

from telegram.utils.keyboards.Keyboard_menu import multi_level_menu, action_from_general, action_from_second_section, action_from_final_section

from aiogram.utils.callback_data import CallbackData

from aiogram import types

@dp.message_handler(commands=['multi_menu'])
async def command_menu(msg: types.Message):
    await msg.answer("Вы перешли в главный раздел меню", reply_markup=action_from_general())

@dp.callback_query_handler(multi_level_menu.filter(action = ["to_general_from_final_section", "prev_from_second_section"]))
async def callback_main_menu(cb: types.CallbackQuery, callback_data: dict):
    from_section = 'из второго раздела' if callback_data["action"] == 'prev_from_second_section' else 'из последнего раздела'
    await cb.answer()
    await cb.message.edit_text(
        f"Вы перешли в главный раздел меню, {from_section}",
        reply_markup = action_from_general()
    )

@dp.callback_query_handler(multi_level_menu.filter(action = ["prev_from_final_section", "next_from_general"]))
async def callback_second_section(cb:types.CallbackQuery, callback_data: dict):
    from_section = "из главного раздела" if callback_data["action"] == "next_from_general" else "из третьего раздела"
    await cb.answer()
    await cb.message.edit_text(
        f"Вы перешли во второй раздел меню, {from_section}",
        reply_markup= action_from_second_section()
    )

@dp.callback_query_handler(multi_level_menu.filter(action = ["next_from_second_section"]))
async def callback_final_section(cb: types.CallbackQuery):
    await cb.answer()
    await cb.answer()
    await cb.message.edit_text(
        "Вы перешли в последний раздел меню, из второго раздела",
        reply_markup= action_from_final_section()
    )

@dp.callback_query_handler(multi_level_menu.filter(action = "close"))
async def callback_close(cb: types.CallbackQuery):
    await cb.answer()
    await cb.message.edit_reply_markup()
