# send_alert.py

import requests

bot_token = 'YOUR_BOT_TOKEN'
chat_id = 'YOUR_GROUP_CHAT_ID'  # เช่น -123456789
message = 'สวัสดีครับ นี่คือข้อความแจ้งเตือนจาก Python'

url = f'https://api.telegram.org/bot{bot_token}/sendMessage'

payload = {
    'chat_id': chat_id,
    'text': message
}

response = requests.post(url, data=payload)

if response.status_code == 200:
    print('ส่งข้อความสำเร็จ')
else:
    print('ส่งข้อความไม่สำเร็จ', response.text)
