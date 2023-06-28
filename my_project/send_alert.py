import telebot
from config1 import KEY
import json
import datetime
from datetime import datetime

def send_alert(chat_id, message):#відправляє повідомлення з вказаним текстом на вказаний chat_id
    bot = telebot.TeleBot(KEY)
    bot.send_message(chat_id, message)

def parse_json():# функція яка вичитує json для подальшого педавання інф в message. повертає
    # словничок конкретного id якщо поточна година
    file_path = 'pills_library.json'
    current_time = datetime.now().strftime('%H:%M')

    with open(file_path, 'r') as file:
        json_data = file.read()
    data = json.loads(json_data)

    alert_list = []# конкретний ліст поточної дати

    for item in data:
        item_time = item['time']
        item_day = int(item['day'])
        creation_date = datetime.strptime(item['creation_date'], '%Y-%m-%d').date()
        current_date = datetime.now().date()
        date_difference = current_date - creation_date # різниця між датою коли був створений запис та поточною датою

        if current_time in item_time:

            if item_day >= date_difference.days:
                alert_item = {
                    'chat_id': item['chat_id'],
                    'name': item['name'],
                    'current_time': current_time
                }
                alert_list.append(alert_item)


    with open(file_path, 'w') as file:
        file.write(json.dumps(data))

    print(alert_list)

    for alert in alert_list:
        chat_id = alert['chat_id']
        pill_name = alert['name']
        time = alert['current_time']
        message = f"Hello! You need to take the pills {pill_name} at {time}"# повідомлення юзеру
        send_alert(chat_id, message)

parse_json()