from telebot import types
def create_keyboard(categories):
    keyboard1 = types.InlineKeyboardMarkup()
    keyboard2 = types.InlineKeyboardMarkup()
    keyboard3 = types.InlineKeyboardMarkup()
    keyboard4 = types.InlineKeyboardMarkup()
    buttons = []
    for i in categories:
        buttons.append(types.InlineKeyboardButton(text=categories[i][0], callback_data=i))
    for i in range(0, 12, 3):
        keyboard1.row(buttons[i], buttons[i+1], buttons[i+2])
    keyboard1.row(types.InlineKeyboardButton(text='1', callback_data='1'),
                  types.InlineKeyboardButton(text='2', callback_data='2'))
    keyboard1.row(types.InlineKeyboardButton(text='Назад', callback_data='back'))
    for i in range(12, 24, 3):
        keyboard2.row(buttons[i], buttons[i+1], buttons[i+2])
    keyboard2.row(types.InlineKeyboardButton(text='1', callback_data='1'),
                  types.InlineKeyboardButton(text='2', callback_data='2'))
    keyboard2.row(types.InlineKeyboardButton(text='Назад', callback_data='back'))
    keyboard3.row(types.InlineKeyboardButton(text='Случайный анегдот', callback_data='random'))
    keyboard3.row(types.InlineKeyboardButton(text='Категории', callback_data='category'))
    keyboard3.row(types.InlineKeyboardButton(text='Смешная картинка', callback_data='image'))
    keyboard4.row(types.InlineKeyboardButton(text='Ещё', callback_data='more'),
                  types.InlineKeyboardButton(text='Назад', callback_data='delete'))
    return keyboard1, keyboard2, keyboard3, keyboard4