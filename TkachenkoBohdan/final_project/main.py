#Імпорт модулів
import telebot
import config
import time
from random import randint
from telebot import types


#Ключ від телеграм бота
bot = telebot.TeleBot(config.bot_token)


#Спроби юзера
tries = []



#Початкова функція, привітання після /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привіт, ' + message.from_user.first_name)
    time.sleep(1)
    bot.send_message(message.chat.id, 'Пропоную тобі зіграти в гру, спробуй вгадати цифру від 1 до 10, в тебе буде 3 спроби')
    number = randint(1, 10)
    tries.clear()
    max_tries = 3




#Функція, яка допомагає вгадати число, та моніторить якщо число було вгадане
    def handle_user_guess(message):
        if message.text.isdigit():
            tries.append(int(message.text))
            if int(message.text) > number:
                bot.send_message(message.chat.id, "Ви не вгадали число, дане число менше за ваше, спробуйте ще раз.")
                check_max_tries()
            elif int(message.text) < number:
                bot.send_message(message.chat.id, "Ви не вгадали число, дане число більше за ваше, спробуйте ще раз.")
                check_max_tries()
            else:
                bot.send_message(message.chat.id, "Ви вгадали число, вітаю. Якщо хочете зіграти ще раз, напишіть /start")
        else:
            bot.send_message(message.chat.id, "Будь ласка, введіть числове значення.")
            bot.register_next_step_handler(message, handle_user_guess)




#Функція, яка запускає процес вгадування та зупиняє у випадку вичерпання спроб.
    def check_max_tries():
        if len(tries) < max_tries:
            bot.send_message(message.chat.id, "Введіть будь ласка число від 1 до 10:")
            bot.register_next_step_handler(message, handle_user_guess)
        else:
            bot.send_message(message.chat.id, "Нажаль, ви вичерпали всі спроби. Загадане число було: " + str(number))
            play_again(message)

    time.sleep(2)
    bot.send_message(message.chat.id, "Введіть будь ласка число від 1 до 10:")
    bot.register_next_step_handler(message, handle_user_guess)



#Функція, яка створює клавіші "Так", "Ні" та пропонує зіграти ще раз.
    def play_again(message):
        markup = types.InlineKeyboardMarkup()
        yes_btn = types.InlineKeyboardButton("Так", callback_data='play_again')
        no_btn = types.InlineKeyboardButton("Ні", callback_data='end_game')
        markup.add(yes_btn, no_btn)
        bot.send_message(message.chat.id, "Хочете спробувати ще раз?", reply_markup=markup)





#Функції, які виконують перезапуск гри
@bot.callback_query_handler(func=lambda call: call.data == 'play_again')
def callback_play_again(call):
    bot.answer_callback_query(call.id)
    restart_game(call.message)

def restart_game(message):
    bot.send_message(message.chat.id, "Гра розпочалась знову!")
    tries.clear()
    start(message)




#Функція, яка завершує гру.
@bot.callback_query_handler(func=lambda call: call.data == 'end_game')
def callback_end_game(call):
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, "Дякую за гру. До зустрічі! Якщо хочете розпочати гру заново, напишіть /start")
#Метод який запускає бота.
bot.polling()
