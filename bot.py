import telebot
from constants import TOKEN, DATA_SOURCE
from utils import create_keybord_for_zones, reading_json_file

dict_from_json = reading_json_file(DATA_SOURCE)

bot = telebot.TeleBot(TOKEN, parse_mode=None)


@bot.message_handler(commands=['start'])
def reply_for_start_command(message):
    bot.send_message(message.chat.id, 'Введите позицию для поиска IGMI\n(4х значное число)')


@bot.message_handler()
def show_buttons(message):
    if len(message.text) == 4 and message.text.isdigit():
        global position
        position = message.text
        bot.send_message(message.chat.id, "Выберите зону", reply_markup=create_keybord_for_zones())

    if message.text in ('F01', 'F02', 'F03', 'F04', 'F05', 'F06', 'F07', 'F08'):
        zone = message.text
        try:
            bot.send_message(message.chat.id, f"{zone}.{position} - {dict_from_json[zone][f'{zone}.{position}'][-4:]}")
        except KeyError:
            bot.send_message(message.chat.id, f'Не могу найти позицию - {zone}.{position}')
        except NameError:
            bot.send_message(message.chat.id, f'Для начала введите позицию\n(4х значное число)')


bot.infinity_polling()
