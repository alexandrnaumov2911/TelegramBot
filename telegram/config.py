import os

TOKEN = os.getenv("TOKEN")


ADMINS = (747184261,)
NGROK = os.getenv("NGROK")


WEBHOOK_PATH = ''
WEBHOOK_URL = f'{NGROK}{WEBHOOK_PATH}'

WEBAPP_HOST = '127.0.0.1'  # or ip
WEBAPP_PORT = 8000

if not TOKEN:
    exit('Error: no token provided')

