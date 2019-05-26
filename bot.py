import telebot
import datetime
import traceback
from telebot import types
import misc
import os


bot = telebot.TeleBot(misc.token)


@bot.message_handler(content_types=['text'])
def message(message):
    global path
    keyboard = types.ReplyKeyboardRemove()

    if message.text.split()[0] == '/dir':
        if len(message.text.split()) > 2:
            keyboard_width = message.text.split()[2]
        else:
            keyboard_width = misc.keyboard_width

        path = message.text.split()[1]
        files = os.listdir(path)
        keyboard = types.InlineKeyboardMarkup()
        if keyboard_width == 2:
            for file in range(1, len(files)//2*2):
                button1 = types.InlineKeyboardButton(text=files[file-1], callback_data=files[file-1])
                button2 = types.InlineKeyboardButton(text=files[file], callback_data=files[file])
                keyboard.add(button1, button2)
            if len(files)//2 != 0:
                keyboard.add(types.InlineKeyboardButton(text=files[-1], callback_data=files[-1]))
        elif keyboard_width == 1:
            for file in files: keyboard.add(types.InlineKeyboardButton(text=file, callback_data=file))
        bot.send_message(message.chat.id, 'Найдено файлов: {}'.format(len(files)), reply_markup=keyboard)


bot.polling()
