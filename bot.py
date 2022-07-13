import telebot
from telebot import types
from reading_json import reading_json_file

filepath = r'data_for_all_zones1.json'

dict_from_json = reading_json_file(filepath)

token = '5471219208:AAFIjOrKvPFINV3NykFhKC74rrGT0Ea0-ic'
bot = telebot.TeleBot(token, parse_mode=None)


keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
button_f01 = types.KeyboardButton('F01')
button_f02 = types.KeyboardButton('F02')
button_f03 = types.KeyboardButton('F03')
button_f04 = types.KeyboardButton('F04')
button_f05 = types.KeyboardButton('F05')
button_f06 = types.KeyboardButton('F06')
button_f07 = types.KeyboardButton('F07')
button_f08 = types.KeyboardButton('F08')
button_start = types.KeyboardButton('/start')

keyboard.add(button_f01, button_f02, button_f03, button_f04, button_f05, button_f06, button_f07, button_f08,
             button_start)


@bot.message_handler(commands=['start'])
def reply_for_start_command(message):
    bot.send_message(message.chat.id, 'Введите позицию для поиска \n(4х значное число)')


@bot.message_handler()
def show_buttons(message):
    if len(message.text) == 4 and not message.text.isalpha():
        global position
        position = message.text
        bot.send_message(message.chat.id, "Выберите зону", reply_markup=keyboard)

    if message.text in ('F01', 'F02', 'F03', 'F04', 'F05', 'F06', 'F07', 'F08'):
        zone = message.text
        try:
            bot.send_message(message.chat.id, f"{zone}.{position} - {dict_from_json[zone][f'{zone}.{position}'][-4:]}")
        except KeyError:
            bot.send_message(message.chat.id, f'Не могу найти позицию - {zone}.{position}')


bot.infinity_polling()
