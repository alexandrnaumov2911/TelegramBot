from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

button_yes = InlineKeyboardButton('Да', callback_data='Answer_Yes')
button_no = InlineKeyboardButton('Нет', callback_data='Answer_No')

KeyboardAnswer = InlineKeyboardMarkup().add(button_yes, button_no)

KeyboardClaim = InlineKeyboardMarkup()
KeyboardClaim.insert(InlineKeyboardButton('Оставить отзыв', switch_inline_query_current_chat='Жалоба: '))
