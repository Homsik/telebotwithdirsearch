import telebot
import misc
import func
import os

bot = telebot.TeleBot(misc.token)
global dir_search
dir_search = False

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет.')

@bot.message_handler(content_types=['text'])
def get_command(message):
    if message.text.split()[0] == '/dir': #Исполнение команды
        dir = message.text.split()[1]
        dir_search = True #Режим проверки папок
        dir_data = func.create_list(dir)
        bot.send_message(message.chat.id, f'Найдено объектов: {dir_data[1]}.\nПуть: {dir_data[2]}/', reply_markup=dir_data[0])
    if message.text == '[Выйти]' and dir_search: #Выключение
        dir_search = False
        bot.send_message(message.chat.id, 'Режим проверки директорий выключен.')
    if message.text == '[Назад]' and dir_search: #Уровень вверх
        dir = dir.split('//')[:-1]
        print(dir)


bot.polling()
