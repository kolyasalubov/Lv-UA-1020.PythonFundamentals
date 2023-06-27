import json
import telebot
from flask import Flask, request
from config1 import KEY
from update_json import *

main = Flask(__name__)

bot = telebot.TeleBot(KEY)

@main.route("/", methods=["POST"])
def process():
    update = telebot.types.Update.de_json(request.get_json(force=True))
    bot.process_new_updates([update])
    return {"ok": True}
@bot.message_handler(commands=['start'])
def start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button = telebot.types.KeyboardButton('Add pills')
    keyboard.add(button)
    bot.send_message(message.chat.id, 'Hello! Click the button below:', reply_markup=keyboard)

@bot.message_handler(func=lambda message: True)
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
        bot.register_next_step_handler(message, add_name)


    elif message.text == 'Days':
        bot.send_message(message.chat.id, 'Please enter the number of days:')
        bot.register_next_step_handler(message, add_day)

    elif message.text == 'Time':
        bot.send_message(message.chat.id, 'Please enter the time:')
        bot.register_next_step_handler(message, add_time)



def add_name(message):
    chat_id = message.chat.id
    value = message.text
    update_json(chat_id, "name", value)

def add_day(message):
    chat_id = message.chat.id
    value = message.text
    update_json(chat_id, "day", value)

def add_time(message):
    chat_id = message.chat.id
    value = message.text
    update_json(chat_id, "time", value)

if __name__ == "__main__":
    main.run()

