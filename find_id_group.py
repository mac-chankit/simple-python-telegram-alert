# find_id_group.py

import requests

bot_token = 'YOUR_BOT_TOKEN'
url = f'https://api.telegram.org/bot{bot_token}/getUpdates'

response = requests.get(url)
print(response.json())
