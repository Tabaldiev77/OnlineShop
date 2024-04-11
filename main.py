import telebot

bot = telebot.TeleBot('7035871779:AAE8efBWqtRYHN-RGTiFLGLISWp8a4I0KJA')

categories = {
    'Фрукты': ['Яблоко', 'Банан', 'Апельсин', 'Груша'],
    'Канцелярские товары': ['Ручка', 'Карандаш', 'Блокнот', 'Ластик'],
    'Напитки': ['Вода', 'Чай', 'Кофе', 'Сок'],
    'Мороженое': ['Ванильное', 'Шоколадное', 'Клубничное', 'Пломбир']
}

def get_categories_markup():
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
    for category in categories:
        markup.add(telebot.types.KeyboardButton(category))
    return markup

def get_categories():
    return list(categories.keys())

products_info = {
    "Яблоко": {"description": "Яблоко — это сладкий съедобный фрукт, произрастающий на яблоне.", "price": 50},
    "Банан": {"description": "Банан — это продолговатый съедобный фрукт, производимый растениями рода Musa.", "price": 70},
    "Апельсин": {"description": "Апельсин — это плод различных видов цитрусовых семейства Рутовые.", "price": 60},
    "Груша": {"description": "Груша — это съедобный плод растений рода груша.", "price": 55},
    "Ручка": {"description": "Ручка — это обычный пишущий инструмент, используемый для нанесения чернил на поверхность.", "price": 30},
    "Карандаш": {"description": "Карандаш — это инструмент для письма или рисования, состоящий из твердого пигментного стержня.", "price": 25},
    "Блокнот": {"description": "Блокнот — это стопка бумажных страниц, используемых для записи заметок или других письменных работ.", "price": 40},
    "Ластик": {"description": "Ластик — это приспособление для стирания надписей или рисунков на бумаге.", "price": 15},
    "Вода": {"description": "Вода — прозрачное химическое вещество, основной компонент рек, озер и океанов Земли.", "price": 20},
    "Чай": {"description": "Чай — это напиток, приготовленный из высушенных листьев чайного куста.", "price": 35},
    "Кофе": {"description": "Кофе — это напиток, приготовленный из обжаренных кофейных зерен.", "price": 45},
    "Сок": {"description": "Сок — это напиток, приготовленный из сока фруктов или овощей.", "price": 50},
    "Ванильное": {"description": "Ванильное мороженое — это мороженое с ванильным вкусом.", "price": 60},
    "Шоколадное": {"description": "Шоколадное мороженое — это мороженое с шоколадным вкусом.", "price": 65},
    "Клубничное": {"description": "Клубничное мороженое — это мороженое с клубничным вкусом.", "price": 70},
    "Пломбир": {"description": "Пломбир — это мороженое с кремовым вкусом и высоким содержанием жира.", "price": 75}
}

user_data = {}

@bot.message_handler(commands=['start'])
def start(message):
    user_data[message.chat.id] = {}
    user_data[message.chat.id]['category'] = ''
    bot.reply_to(message, 'Добро пожаловать! Пожалуйста, выберите категорию:', reply_markup=get_categories_markup())

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    chat_id = message.chat.id
    if chat_id in user_data and 'category' in user_data[chat_id]:
        category = user_data[chat_id]['category']
        if category:
            product = message.text.strip()
            if product in categories[category]:
                bot.send_message(chat_id, f"{products_info[product]['description']}\nЦена: {products_info[product]['price']} сом")
            else:
                bot.send_message(chat_id, 'Неверный выбор продукта.')
            user_data[chat_id]['category'] = ''
            bot.send_message(chat_id, 'Пожалуйста, выберите другую категорию:', reply_markup=get_categories_markup())
            return  # Добавляем return, чтобы прервать выполнение функции после обработки сообщения
    else:
        bot.send_message(chat_id, 'Неверная команда. Пожалуйста, используйте кнопки для взаимодействия.')

    # Если сообщение не соответствует ожидаемым условиям, ничего не делаем
    # Это важно, чтобы сообщения, не относящиеся к выбору категории или продукта, не вызывали лишних ответов от бота

# Добавляем обработчик для ожидания выбора продукта после выбора категории
@bot.message_handler(func=lambda message: message.text.strip() in sum(categories.values(), []))
def handle_product_selection(message):
    chat_id = message.chat.id
    category = user_data[chat_id]['category']
    product = message.text.strip()
    bot.send_message(chat_id, f"{products_info[product]['description']}\nЦена: {products_info[product]['price']} сом")
    user_data[chat_id]['category'] = ''
    bot.send_message(chat_id, 'Пожалуйста, выберите другую категорию:', reply_markup=get_categories_markup())

bot.polling()






# import telebot
#
# bot = telebot.TeleBot('7035871779:AAE8efBWqtRYHN-RGTiFLGLISWp8a4I0KJA')
#
# categories = {
#     'Фрукты': ['Яблоко', 'Банан', 'Апельсин', 'Груша'],
#     'Канцелярские товары': ['Ручка', 'Карандаш', 'Блокнот', 'Ластик'],
#     'Напитки': ['Вода', 'Чай', 'Кофе', 'Сок'],
#     'Мороженое': ['Ванильное', 'Шоколадное', 'Клубничное', 'Пломбир']
# }
#
# products_info = {
#     "Яблоко": "Яблоко — это сладкий съедобный фрукт, произрастающий на яблоне.",
#     "Банан": "Банан — это продолговатый съедобный фрукт, производимый растениями рода Musa.",
#     "Апельсин": "Апельсин — это плод различных видов цитрусовых семейства Рутовые.",
#     "Груша": "Груша — это съедобный плод растений рода груша.",
#     "Ручка": "Ручка — это обычный пишущий инструмент, используемый для нанесения чернил на поверхность.",
#     "Карандаш": "Карандаш — это инструмент для письма или рисования, состоящий из твердого пигментного стержня.",
#     "Блокнот": "Блокнот — это стопка бумажных страниц, используемых для записи заметок или других письменных работ.",
#     "Ластик": "Ластик — это приспособление для стирания надписей или рисунков на бумаге.",
#     "Вода": "Вода — прозрачное химическое вещество, основной компонент рек, озер и океанов Земли.",
#     "Чай": "Чай — это напиток, приготовленный из высушенных листьев чайного куста.",
#     "Кофе": "Кофе — это напиток, приготовленный из обжаренных кофейных зерен.",
#     "Сок": "Сок — это напиток, приготовленный из сока фруктов или овощей.",
#     "Ванильное": "Ванильное мороженое — это мороженое с ванильным вкусом.",
#     "Шоколадное": "Шоколадное мороженое — это мороженое с шоколадным вкусом.",
#     "Клубничное": "Клубничное мороженое — это мороженое с клубничным вкусом.",
#     "Пломбир": "Пломбир — это мороженое с кремовым вкусом и высоким содержанием жира."
# }
#
# user_data = {}
#
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     user_data[message.chat.id] = {}
#     user_data[message.chat.id]['category'] = ''
#     bot.reply_to(message, 'Добро пожаловать! Пожалуйста, выберите категорию:', reply_markup=get_categories_markup())
#
#
# @bot.message_handler(func=lambda message: True)
# def handle_message(message):
#     chat_id = message.chat.id
#     if chat_id in user_data and 'category' in user_data[chat_id]:
#         category = user_data[chat_id]['category']
#         if category:
#             product = message.text.strip()
#             if product in categories[category]:
#                 bot.send_message(chat_id, products_info[product])
#             else:
#                 bot.send_message(chat_id, 'Неверный выбор продукта.')
#             user_data[chat_id]['category'] = ''
#             bot.send_message(chat_id, 'Пожалуйста, выберите другую категорию:', reply_markup=get_categories_markup())
#     else:
#         bot.send_message(chat_id, 'Неверная команда. Пожалуйста, используйте кнопки для взаимодействия.')
#
#
# def get_categories_markup():
#     markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
#     for category in categories:
#         markup.add(telebot.types.KeyboardButton(category))
#     return markup
#
#
# @bot.message_handler(func=lambda message: message.text.lower() in categories.keys())
# def handle_category_selection(message):
#     chat_id = message.chat.id
#     category = message.text.lower()
#     user_data[chat_id]['category'] = category
#     bot.send_message(chat_id, f'Вы выбрали категорию "{category}". Пожалуйста, выберите продукт:',
#                      reply_markup=get_products_markup(category.capitalize()))
#
#
# def get_products_markup(category):
#     markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
#     for product in categories[category.lower()]:
#         markup.add(telebot.types.KeyboardButton(product))
#     return markup
#
#
# bot.polling()
