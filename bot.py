from telebot import telebot, types
from constants import TOKEN
from utils_for_igme_positions import load_from_gitHub_json_file, looks_like_conveyor_position
from utils_for_show_change import conver_str_to_date, calculate_change_for_date, looks_like_date
from utils_for_bot import create_keybord_for_zones

bot = telebot.TeleBot(TOKEN, parse_mode=None)


# todo добавить логирование
# todo вынести в функции

@bot.message_handler(commands=['start'])
def reply_for_start_command(message):
    bot.send_message(message.chat.id, 'Введите позицию для поиска EGMI\n(4х значное число)')


position_to_find = {'position': '0000'}  # инициализируем переменную для хранения позиции для поиска


@bot.message_handler()
def main_message_handler(message):  # перехватчик всех сообщений
    if looks_like_date(message.text):
        try:
            date_for_calculate = conver_str_to_date(message.text)
            change_for_date = calculate_change_for_date(date_for_calculate)
            bot.send_message(message.chat.id, f'{date_for_calculate.strftime("%d.%m.%y")}:\n{change_for_date}')
        except ValueError:
            return

    if looks_like_conveyor_position(message.text):
        position_to_find['position'] = message.text  # если ввод похож на позицию для поиска - переопределим переменную
        keyboard = create_keybord_for_zones()
        bot.send_message(message.chat.id, "Выберите зону", reply_markup=keyboard)

    position = position_to_find['position']

    if message.text in ('F01', 'F02', 'F03', 'F04', 'F05', 'F06', 'F07', 'F08'):
        zone = message.text
        try:
            dict_from_json = load_from_gitHub_json_file()
            bot.send_message(message.chat.id, f"{zone}.{position} - {dict_from_json[zone][f'{zone}.{position}']}")
        except KeyError:
            # keyboard = types.ReplyKeyboardRemove()  # удалит клавиатуру
            bot.send_message(message.chat.id, f'Не могу найти позицию - {zone}.{position}')
        except NameError:
            bot.send_message(message.chat.id, f'Для начала введите позицию\n(4х значное число)')


bot.infinity_polling()
