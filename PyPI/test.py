import requests

url = 'https://pypi.org/project/requests/'
response = requests.get(url = url)
print(response.status_code)
