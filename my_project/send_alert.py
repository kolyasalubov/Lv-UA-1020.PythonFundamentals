import telebot
from config1 import KEY
import json
import datetime

def send_alert(chat_id, message):
    bot = telebot.TeleBot(KEY)
    bot.send_message(chat_id, message)

def parse_json():
    file_path = 'pills_library.json'
    current_time = datetime.datetime.now().strftime('%H:%M')

    with open(file_path, 'r') as file:
        json_data = file.read()
    data = json.loads(json_data)

    alert_list = []

    for item in data:
        item_time = item['time']
        item_day = int(item['day'])


        if current_time in item_time:

            if item_day > 0:
                alert_item = {
                    'chat_id': item['chat_id'],
                    'name': item['name'],
                    'current_time': current_time
                }
                alert_list.append(alert_item)
                item['day'] = item_day - 1  # Minus 1 from day


    with open(file_path, 'w') as file:
        file.write(json.dumps(data))

    print(alert_list)

    for alert in alert_list:
        chat_id = alert['chat_id']
        pill_name = alert['name']
        time = alert['current_time']
        message = f"Hello! You need to take the pills {pill_name} at {time}"
        send_alert(chat_id, message)

parse_json()