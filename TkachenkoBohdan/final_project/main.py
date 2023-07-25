import telebot
import config
import time
from random import randint
from telebot import types
import json

#Параметр який вмикає підтримку проміжного програмного забезпечення
telebot.apihelper.ENABLE_MIDDLEWARE = True

# Ключ від телеграм бота
bot = telebot.TeleBot(config.bot_token)

#Файл у якому міститься імя користувача
USER_FILE = "users.json"

#Конструкція яка завантажує імя користувача з json файлу
try:
    with open(USER_FILE, "r") as f:
        users = json.load(f)
except FileNotFoundError:
    users = {}

#Функція яка зберігає данні користувача у json
def save_users():
    with open(USER_FILE, "w") as f:
        json.dump(users, f)

#Це пустий список який містить кількість спроб користувача
tries = []

# Функція яка додає кнопки від 1 до 10
def generate_number_buttons():
    markup = types.ReplyKeyboardMarkup(row_width=5)
    numbers = [str(i) for i in range(1, 11)]
    markup.add(*[types.KeyboardButton(number) for number in numbers])
    return markup

# Початкова функція, запитує ім'я користувача
@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    if user_id not in users:
        bot.send_message(message.chat.id, 'Привіт, незнайомець! Як тебе звати?')
        bot.register_next_step_handler(message, get_user_name)
    else:
        user_name = users[user_id]
        bot.send_message(message.chat.id, f'Привіт, {user_name}!')
        time.sleep(1)
        bot.send_message(message.chat.id, 'Пропоную тобі зіграти в гру, спробуй вгадати цифру від 1 до 10, в тебе буде 3 спроби',
                         reply_markup=generate_number_buttons())
        number = randint(1, 10)
        tries.clear()
        max_tries = 3
        bot.register_next_step_handler(message, handle_user_guess, number, max_tries)

# Функція для отримання імені користувача та початку гри
def get_user_name(message):
    user_id = message.from_user.id
    user_name = message.text.strip()

    if user_name:
        users[user_id] = user_name
        save_users()

    bot.send_message(message.chat.id, f'Привіт, {user_name}!')
    time.sleep(1)
    bot.send_message(message.chat.id, 'Пропоную тобі зіграти в гру, спробуй вгадати цифру від 1 до 10, в тебе буде 3 спроби',
                     reply_markup=generate_number_buttons())
    number = randint(1, 10)
    tries.clear()
    max_tries = 3
    bot.register_next_step_handler(message, handle_user_guess, number, max_tries)

# Функція, яка допомагає вгадати число та моніторить, якщо число було вгадане
def handle_user_guess(message, number, max_tries):
    if message.text.isdigit():
        tries.append(int(message.text))
        if int(message.text) > number:
            bot.send_message(message.chat.id, "Ви не вгадали число, дане число менше за ваше, спробуйте ще раз.")
            check_max_tries(message, number, max_tries)
        elif int(message.text) < number:
            bot.send_message(message.chat.id, "Ви не вгадали число, дане число більше за ваше, спробуйте ще раз.")
            check_max_tries(message, number, max_tries)
        else:
            bot.send_message(message.chat.id, "Ви вгадали число, вітаю. Якщо хочете зіграти ще раз, напишіть /start")
    else:
        bot.send_message(message.chat.id, "Будь ласка, введіть числове значення.")
        bot.register_next_step_handler(message, handle_user_guess, number, max_tries)

# Функція, яка перевіряє максимальну кількість спроб та зупиняє гру
def check_max_tries(message, number, max_tries):
    if len(tries) < max_tries:
        bot.send_message(message.chat.id, "Введіть будь ласка число від 1 до 10:")
        bot.register_next_step_handler(message, handle_user_guess, number, max_tries)
    else:
        bot.send_message(message.chat.id, "Нажаль, ви вичерпали всі спроби. Загадане число було: " + str(number))
        play_again(message)

# Функція, яка створює клавіші "Так", "Ні" та пропонує зіграти ще раз
def play_again(message):
    markup = types.InlineKeyboardMarkup()
    yes_btn = types.InlineKeyboardButton("Так", callback_data='play_again')
    no_btn = types.InlineKeyboardButton("Ні", callback_data='end_game')
    markup.add(yes_btn, no_btn)
    bot.send_message(message.chat.id, "Хочете спробувати ще раз?", reply_markup=markup)

# Функція, яка оброблює події після запуску гри через кнопу "Так"
@bot.callback_query_handler(func=lambda call: call.data == 'play_again')
def callback_play_again(call):
    bot.answer_callback_query(call.id)
    restart_game(call.message)

#Функція яка відповідає за перезапуск гри
def restart_game(message):
    bot.send_message(message.chat.id, "Гра розпочалась знову!")
    tries.clear()
    number = randint(1, 10)
    max_tries = 3
    bot.register_next_step_handler(message, handle_user_guess, number, max_tries)

# Функція, яка оброблює кнопку "Ні"
@bot.callback_query_handler(func=lambda call: call.data == 'end_game')
def callback_end_game(call):
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, "Дякую за гру. До зустрічі! Якщо хочете розпочати гру заново, напишіть /start")

# Метод, який запускає бота
bot.polling()
