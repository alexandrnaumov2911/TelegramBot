# @dp.message_handler(
#     content_types= types.ContentType.TEXT
# )
# async def echo(msg: types.Message):
#     with sqlite3.connect('database.db') as connection:
#         cur = connection.cursor()
#         user = cur.execute(f" SELECT * FROM user WHERE user_id={msg.from_user.id}").fetchone()
#         if not user:
#             logging.info(f'Создание нового пользователя: {msg.from_user.username} {msg.from_user.id}')
#
#             data = (msg.from_user.id, msg.chat.id, msg.from_user.username)
#             cur.execute(f"INSERT INTO user(user_id, chat_id, username) VALUES (?,?,?) ", data)
#             connection.commit()
#             await msg.answer('Вы добавлены в БД')
#         else:
#             await msg.answer('Вы уже в БД')
#     return webhook.SendMessage(msg.chat.id, msg.text)


# import logging
#
# from aiogram import Bot, Dispatcher, types
# from aiogram.contrib.middlewares.logging import LoggingMiddleware
# from aiogram.dispatcher import webhook
#
# from config import TOKEN, WEBHOOK_URL, WEBHOOK_PATH, WEBAPP_HOST, WEBAPP_PORT
#
# logging.basicConfig(level=logging.INFO)
# bot = Bot(
#     token=TOKEN,
#     parse_mode='HTML',
# )
# dp = Dispatcher(bot)
# dp.middleware.setup(LoggingMiddleware())
#
#
# async def on_startup(dp):
#     logging.info('Setting webhook :D')
#     await bot.set_webhook(WEBHOOK_URL)
#
#
# async def on_shutdown(dp):
#     logging.info('Shutting down..')
#     await bot.delete_webhook()
#     logging.info('Bye!')
#
#
# @dp.message_handler(commands=['start'])
# async def command_start(msg: types.Message):
#     return webhook.SendMessage(msg.chat.id, 'Добро пожаловать!')
#
#
# @dp.message_handler(commands=['help'])
# async def command_help(msg: types.Message):
#     return webhook.SendMessage(msg.chat.id, 'Вы обратились к справке бота')
#
#
# @dp.message_handler(commands=['myID'])
# async def get_id_user(msg: types.Message):
#     return webhook.SendMessage(msg.chat.id, f'ID: <code>{msg.chat.id}</code>')
#
#
# if __name__ == '__main__':
#     from aiogram import executor
#
#     executor.start_webhook(
#         dispatcher=dp,
#         skip_updates=True,
#         on_startup=on_startup,
#         on_shutdown=on_shutdown,
#         webhook_path=WEBHOOK_PATH,
#         host=WEBAPP_HOST,
#         port=WEBAPP_PORT,
#     )