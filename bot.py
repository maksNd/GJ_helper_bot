import telebot
from telebot import types
from reading_json import reading_json_file

filepath = r'data_for_all_zones1.json'

dict_from_json = reading_json_file(filepath)

token = '5471219208:AAFIjOrKvPFINV3NykFhKC74rrGT0Ea0-ic'
bot = telebot.TeleBot(token, parse_mode=None)


# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
#     bot.reply_to(message, "Howdy, how are you doing?")

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
button_f01 = types.KeyboardButton('F01')
button_f02 = types.KeyboardButton('F02')
button_f03 = types.KeyboardButton('F03')
button_f04 = types.KeyboardButton('F04')
button_f05 = types.KeyboardButton('F05')
button_f06 = types.KeyboardButton('F06')
button_f07 = types.KeyboardButton('F07')
button_f08 = types.KeyboardButton('F08')

keyboard.add(button_f01, button_f02, button_f03, button_f04, button_f05, button_f06, button_f07, button_f08)

@bot.message_handler()
def show_buttons(message):
    if len(message.text) == 4 and not message.text.isalpha():
        global position
        position = message.text
        bot.send_message(message.chat.id, "ok, change zone", reply_markup=keyboard)

    if message.text in ('F01', 'F02', 'F03', 'F04', 'F05', 'F06', 'F07', 'F08'):
        print('ok')
        bot.send_message(message.chat.id, "finally")

bot.infinity_polling()

