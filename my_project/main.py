import json
import telebot
from flask import Flask, request
from config1 import KEY
from update_json import *

main = Flask(__name__)

bot = telebot.TeleBot(KEY)

@main.route("/", methods=["POST"])
#функція є обробником HTTP POST-запитів, які надсилаються на кореневий шлях ("/") веб-сервера Flask.
def process():
    # Оновлення отримані з JSON даних перетворюються у відповідний об'єкт Update за допомогою telebot.types.Update.de_json().
    update = telebot.types.Update.de_json(request.get_json(force=True))#force - гарантує, що функція спробує розпізнати
    # JSON-дані незалежно від заголовків запиту
    bot.process_new_updates([update])# обробка нових оновлень
    return {"ok": True}
@bot.message_handler(commands=['start'])
#обробника повідомлень, який відповідає на команду '/start' в Telegram боті.
def start(message):
    #створює новий об'єкт клавіатури з налаштуваннями, де кнопки будуть розташовані у один рядок і масштабуватись під розмір екрану.
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)# resize_keyboard - маштабування під розмір екрану
    button = telebot.types.KeyboardButton('Add pills')#ми створюємо кнопку з підписом "Add pills", яка буде додана до клавіатури.
    keyboard.add(button)
    bot.send_message(message.chat.id, 'Hello! Click the button below:', reply_markup=keyboard)#це метод бота, який
    # використовується для відправки повідомлень користувачам.          #Користувач може вибирати кнопки з клавіатури

@bot.message_handler(func=lambda message: True)#буде викликатись для будь-якого повідомлення, отриманого ботом. завжди повертає True.
def handle_button_click(message):
    if message.text == 'Add pills':
        keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        name_button = telebot.types.KeyboardButton('Name')
        days_button = telebot.types.KeyboardButton('Days')
        time_button = telebot.types.KeyboardButton('Time')
        keyboard.add(name_button, days_button, time_button)
        bot.send_message(message.chat.id, 'Please enter info:', reply_markup=keyboard)

    elif message.text == 'Name':
        bot.send_message(message.chat.id, 'Please enter the name of the pill:')
        bot.register_next_step_handler(message, add_name)#отримання повідомлення (об'єкта) від користувача, виклик функції


    elif message.text == 'Days':
        bot.send_message(message.chat.id, 'Please enter the number of days:')
        bot.register_next_step_handler(message, add_day)

    elif message.text == 'Time':
        bot.send_message(message.chat.id, 'Please enter the time:')
        bot.register_next_step_handler(message, add_time)



def add_name(message):
    chat_id = message.chat.id # id usera
    value = message.text # повідомлення від юзера, саме текст
    update_json(chat_id, "name", value)# викликаю функцю update_json з файлу update_json

def add_day(message):
    chat_id = message.chat.id
    value = message.text
    update_json(chat_id, "day", int(value))

def add_time(message):
    chat_id = message.chat.id
    value = message.text
    update_json(chat_id, "time", value)

if __name__ == "__main__":
    main.run()

