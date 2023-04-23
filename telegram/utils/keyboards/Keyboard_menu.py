from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from aiogram.utils.callback_data import CallbackData

from aiogram import types

multi_level_menu = CallbackData('menu', 'action')

close_btn = InlineKeyboardButton(text='Закрыть', callback_data=multi_level_menu.new(action='close'))

def action_from_general():
    return InlineKeyboardMarkup().add(
        InlineKeyboardButton(text='Далее', callback_data=multi_level_menu.new(action="next_from_general")),
        close_btn
    )

def action_from_second_section():
    return InlineKeyboardMarkup().add(
        InlineKeyboardButton(text='Далее', callback_data=multi_level_menu.new(action="next_from_second_section")),
        InlineKeyboardButton(text='Назад', callback_data=multi_level_menu.new(action='prev_from_second_section'))
    ).add(close_btn)

def action_from_final_section():
    return InlineKeyboardMarkup().add(
        InlineKeyboardButton(text='Назад', callback_data=multi_level_menu.new(action='prev_from_final_section')),
        close_btn
    ).add(InlineKeyboardButton(text='На главную', callback_data=multi_level_menu.new(action="to_general_from_final_section")))

