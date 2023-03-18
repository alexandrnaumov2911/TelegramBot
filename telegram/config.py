import os

TOKEN = os.getenv("TOKEN")


ADMINS = (747184261,)

if not TOKEN:
    exit('Error: no token provided')

