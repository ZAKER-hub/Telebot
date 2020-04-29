import random
from telebot import types

import telebot
import datetime

from bs4 import BeautifulSoup
import requests


#Парсинг текста и фото для знака зодиака
def get_zodiac(sign):
    page = requests.get(f'https://1001goroskop.ru/?znak={sign}')
    b = BeautifulSoup(page.text, "html.parser")
    return b.find('p').text


def get_photo(sign):
    page = requests.get(f'https://1001goroskop.ru/?znak={sign}')
    b = BeautifulSoup(page.text, "html.parser")
    a = b.find('img', class_='img_left')
    return 'https://1001goroskop.ru/' + a['src']


bot = telebot.TeleBot('985536359:AAH16l6cvdEZDlfvt8IIROwEzpJPzvS3bm4')
signs = ['aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra', 'scorpio',
         'sagittarius', 'capricorn', 'aquarius', 'pisces']

keyboard = types.InlineKeyboardMarkup()
key_oven = types.InlineKeyboardButton(text='Овен', callback_data=signs[0])
keyboard.add(key_oven)
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # Если написали «Гороскоп»
    global id1, id2, id3
    if message.text == "Гороскоп":
        # Готовим кнопки


        id1 = message.from_user.id
        bot.send_photo(message.from_user.id, caption='картинка 1', reply_markup=keyboard, photo='https://nekdo.ru/images/all/nekdo_1587128409.jpg')
        id3 = message.message_id
    elif message.text == "/help":
        bot.send_message(message.from_user.id, 'Напиши "Гороскоп"')
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


# Обработчик нажатий на кнопки

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    # Если нажали на одну из 12 кнопок — выводим гороскоп
    if call.data in signs:
        # Формируем гороскоп
        #bot.edit_message_media(media=types.InputMedia(type='photo', media='https://nekdo.ru/images/all/nekdo_1587142807.jpg'), chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=keyboard)
        #bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=keyboard, text='Я хаебаляся', )
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption='картинка 2')
        bot.send_photo(chat_id=call.message.chat.id, photo='https://nekdo.ru/images/all/nekdo_1587142807.jpg', )
bot.polling(none_stop=True, interval=0)
