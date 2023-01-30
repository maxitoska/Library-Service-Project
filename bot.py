import telebot
import config
from telebot import types

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=["start"])
def welcome(message):
    welcome_message = "Welcome, {0.first_name}!\nI am - <b>{1.first_name}</b>," \
                      " this bot created to help you get the more information about service borrowings"
    # open and send a sticker to user while command /start is written
    welcome_sticker = open("static/welcome_sticker.jpg", "rb")
    bot.send_sticker(message.chat.id, welcome_sticker)

    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Check my borrowings")
    item2 = types.KeyboardButton("Check my All borrowings")

    markup.add(item1, item2)

    bot.send_message(message.chat.id, welcome_message.format(message.from_user,
                                                             bot.get_me()),
                     parse_mode="html", reply_markup=markup)


@bot.message_handler(content_types=["text"])
def foo(message):
    if message.chat.type == "private":
        if message.text == "Check my borrowings":

            bot.send_message(message.chat.id, "Great, to look closer at your borrowings i need your data")
        elif message.text == "Check my All borrowings":

            bot.send_message(message.chat.id, "All Borrowings:")


# RUN
bot.polling(none_stop=True)
