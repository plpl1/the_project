import csv
import telebot

bot = telebot.TeleBot("1582698434:AAEEvRxFR-85UpFfr7DBUficSAZBOffoo_Q")
password = "12345"

@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

    item1 = telebot.types.KeyboardButton("Учитель")
    item2 = telebot.types.KeyboardButton("Ученик")
    markup.add(item1, item2)
    bot.send_message(message.chat.id, 'Кто вы?', reply_markup=markup)




# if message.text == "Учитель":
#	bot.send_message(message.chat.id, "Введите пароль")
#	bot.register_next_step_handler(message, teacher)
@bot.message_handler(content_types=['text'])
def working(message):
    if message.text == "Погнали!":
        bot.send_message(message.chat.id, "Кто вы?")
        bot.register_next_step_handler(message, get_person)
    else:
        bot.send_message(message.chat.id, "Напиши 'Погнали!'")


def get_person(message):
    global name
    name = message.text
    if name == "Учитель":
        bot.send_message(message.chat.id, "Напиши пароль")
    else:
        bot.send_message(message.chat.id, "OK")



bot.polling(none_stop=True)

