# https://gitlab.com/alexandrnaumov2911/linteh_28
"""
Реализовать эхо бота с использованием Telegram bot api. Бот должен не только принимать сообщения, но и изображения.
"""
import time

import requests

from config import TOKEN

BASE_URL = f'https://api.telegram.org/bot{TOKEN}'



def pulling():
    count_message = 0
    while True:
        time.sleep(1)
        response = requests.get(f'{BASE_URL}/getUpdates').json()
        if count_message != len(response['result']):
            count_message = len(response['result'])
            msg = response['result'][-1]['message']
            chat_id = msg['chat']['id']


            if msg.get('text'):
                text = msg['text']
                params = {
               'chat_id' : chat_id,
               'text' : text,
            }
                requests.post(f'{BASE_URL}/sendMessage', params=params)


            elif msg.get('photo') and msg.get('caption') is None:

                photo = msg['photo'][-1]['file_id']
                params = {
                    'chat_id': chat_id,
                    'photo' : photo,
                }
                requests.post(f'{BASE_URL}/sendPhoto', params=params)


            elif msg.get('photo') and msg.get('caption'):

                photo = msg['photo'][-1]['file_id']
                caption = msg['caption']
                params = {
                    'chat_id': chat_id,
                    'photo': photo,
                    'caption': caption
                }
                requests.post(f'{BASE_URL}/sendPhoto', params=params)

pulling()