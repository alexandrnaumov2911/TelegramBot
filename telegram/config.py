import os

TOKEN = os.getenv("TOKEN")


ADMINS = (747184261,)
NGROK = 'https://98b8-178-141-16-81.eu.ngrok.io'

WEBHOOK_PATH = ''
WEBHOOK_URL = f'{NGROK}{WEBHOOK_PATH}'

# настройки веб сервера
WEBAPP_HOST = '127.0.0.1'  # or ip
WEBAPP_PORT = 8000

if not TOKEN:
    exit('Error: no token provided')

