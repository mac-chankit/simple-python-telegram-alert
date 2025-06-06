# Telegram Bot Python Scripts

โปรเจกต์นี้ประกอบด้วยสคริปต์ Python สำหรับใช้งาน Telegram Bot API เพื่อดึงข้อมูลการอัปเดตและส่งข้อความแจ้งเตือนในกลุ่ม Telegram

---

## ไฟล์ในโปรเจกต์

### 1. find_id_group.py
ใช้สำหรับดึงข้อมูลอัปเดต (updates) จากบอท Telegram ของคุณ เพื่อดู `chat_id` ของกลุ่มหรือแชทที่บอทอยู่

**การใช้งาน**  
- แก้ไขตัวแปร `bot_token` โดยใส่ Token ของบอทคุณ  
- รันสคริปต์นี้จะได้ผลลัพธ์ JSON ที่มีข้อมูลต่าง ๆ รวมถึง `chat_id` ของกลุ่มหรือแชท

```python
import requests

bot_token = 'YOUR_BOT_TOKEN'
url = f'https://api.telegram.org/bot{bot_token}/getUpdates'

response = requests.get(url)
print(response.json())
```

---

### 2. send_alert.py
ใช้สำหรับส่งข้อความแจ้งเตือนไปยังกลุ่ม Telegram ที่ระบุ

**การใช้งาน**  
- แก้ไขตัวแปร `bot_token` โดยใส่ Token ของบอทคุณ  
- แก้ไขตัวแปร `chat_id` ใส่ ID ของกลุ่มหรือแชทที่ต้องการส่งข้อความ (เช่น `-123456789`)  
- แก้ไขข้อความในตัวแปร `message` ตามต้องการ  
- รันสคริปต์เพื่อส่งข้อความ

```python
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
```

---

## วิธีเตรียมใช้งาน

1. สร้างบอท Telegram ผ่าน BotFather  
2. รับ `bot_token` จาก BotFather  
3. เพิ่มบอทเข้าไปในกลุ่ม Telegram ที่ต้องการใช้  
4. ใช้สคริปต์ `find_id_group.py` เพื่อดู `chat_id` ของกลุ่ม  
5. ใช้สคริปต์ `send_alert.py` เพื่อส่งข้อความแจ้งเตือน  

---

## หมายเหตุ

- โปรดระวังไม่เปิดเผย Token ของบอทให้ผู้อื่นทราบ  
- การใช้บอทในกลุ่มต้องให้สิทธิ์บอทส่งข้อความในกลุ่มด้วย  

---

ถ้ามีข้อสงสัยหรือต้องการความช่วยเหลือ สามารถติดต่อได้เลย!
