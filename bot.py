import telebot
from reading_json import reading_json_file

filepath = r'data_for_all_zones1.json'

dict_from_json = reading_json_file(filepath)

token = '5471219208:AAFIjOrKvPFINV3NykFhKC74rrGT0Ea0-ic'
bot = telebot.TeleBot(token, parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler()
def find_IGME_position(message):
    if message.text[:3] in dict_from_json:
        zone_name = message.text[:3]
        position = message.text
        # print(f'{zone_name}.{position}')
        bot.reply_to(message, f'IGME - {dict_from_json[zone_name][position]}')


bot.infinity_polling()
