from pars import *
from telebot import types
import telebot
from keyboard import create_keyboard


bot = telebot.TeleBot('985536359:AAH16l6cvdEZDlfvt8IIROwEzpJPzvS3bm4')
# Поиск всех категорий и количества максиальных страниц
categories = get_category()
# Создание клавиатур
keyboard1, keyboard2, keyboard3, keyboard4 = create_keyboard(categories)
keyboard = keyboard1

# Обработчик сообщений
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # Если написали «/start»
    if message.text == "/start":
        bot.send_message(message.from_user.id, text='Меню: ', reply_markup=keyboard3)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, 'Напиши /start и откроеться главное меню')
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


# Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global keyboard
    text = 'Меню: '
    if call.data == '1':
        keyboard = keyboard1
        text = 'Страница 1'
    elif call.data == '2':
        keyboard = keyboard2
        text = 'Страница 2'
    elif call.data == 'back':
        text = 'Меню: '
        keyboard = keyboard3
    elif call.data == 'category':
        keyboard = keyboard1
        text = 'Страница 1'
    elif call.data == 'random':
        keyboard = keyboard3
        text = get_random_anegdot()
    elif call.data == 'image':
        photo = get_random_image(categories)
        keyboard = keyboard3
        bot.send_photo(chat_id=call.message.chat.id, photo=photo, reply_markup=keyboard4)
    elif call.data == 'more':
        photo = get_random_image(categories)
        bot.edit_message_media(media=types.InputMedia(type='photo', media=photo), chat_id=call.message.chat.id,
                               message_id=call.message.message_id, reply_markup=keyboard4)
    elif call.data == 'delete':
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    else:
        text = get_random_from_category(call.data, categories)
    if call.data != 'image' and call.data != 'delete' and call.data != 'more':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                          text=text, reply_markup=keyboard)


bot.polling(none_stop=True, interval=0)

