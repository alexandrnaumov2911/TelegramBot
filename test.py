import requests
from pprint import pprint

response = requests.get("https://www.cbr-xml-daily.ru/daily_json.js").json()['Valute']['CNY']['Value']
