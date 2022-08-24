import datetime
from telebot import telebot, types
from constants import TOKEN
from utils_for_igme_positions import load_from_gitHub_json_file, looks_like_conveyor_position
from utils_for_show_change import conver_str_to_date, calculate_change_for_date, looks_like_date
from utils_for_bot import create_keybord_for_zones, create_keyboard_for_change
import logging
from logger import get_and_set_logger, new_log

get_and_set_logger()
logger = logging.getLogger('basic')

bot = telebot.TeleBot(TOKEN, parse_mode=None)


@bot.message_handler(commands=['test'])
def reply_for_test(message):
    logger.info(f'{message.from_user.id} :'
                f' {message.from_user.first_name}'
                f' {message.from_user.last_name} :'
                f' {message.text}')


@bot.message_handler(commands=['log'])
def reply_for_log_command(message):
    with open('log.log', encoding='utf-8') as file:
        data_from_log = file.read()
    bot.send_message(message.chat.id, data_from_log)


@bot.message_handler(commands=['start', 'cancel'])
def reply_for_start_command(message):
    start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton('Find IGME position')
    button_2 = types.KeyboardButton('Change')
    start_keyboard.add(button_1, button_2)
    bot.send_message(message.chat.id, 'ok', reply_markup=start_keyboard)


position_to_find = {'position': '0000'}  # инициализируем переменную для хранения позиции для поиска


@bot.message_handler()
def main_message_handler(message):  # перехватчик всех сообщений



    logger.info(f'{message.from_user.id} :'
                f' {message.from_user.first_name}'
                f' {message.from_user.last_name} :'
                f' {message.text}')

    if message.text == 'Cancel':
        start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_1 = types.KeyboardButton('Find IGME position')
        button_2 = types.KeyboardButton('Change')
        start_keyboard.add(button_1, button_2)
        bot.send_message(message.chat.id, 'ok', reply_markup=start_keyboard)

    if looks_like_date(message.text):  # если введен текст похожий на дату
        try:
            date_for_calculate = conver_str_to_date(message.text)
        except ValueError:
            return
        change_for_date = calculate_change_for_date(date_for_calculate)
        new_log(logger, message.from_user.first_name, message.text)
        bot.send_message(message.chat.id, f'{date_for_calculate.strftime("%d.%m.%y")}:\n{change_for_date}')

    if message.text == 'Change':  # нажата кнопка "Change"
        keyboard = create_keyboard_for_change()
        bot.send_message(message.chat.id, f'Choice the day',
                         reply_markup=keyboard)

    if message.text == 'Today':  # нажата кнопка "Today"
        date_for_calculate = datetime.datetime.now().date()
        change_for_date = calculate_change_for_date(date_for_calculate)
        keyboard = create_keyboard_for_change()
        new_log(logger, message.from_user.first_name, message.text)
        bot.send_message(message.chat.id, f'{date_for_calculate.strftime("%d.%m.%y")}:\n{change_for_date}',
                         reply_markup=keyboard)

    if message.text == 'Yesterday':  # нажата кнопка "Yesterday"
        date_for_calculate = datetime.datetime.now().date() - datetime.timedelta(days=1)
        change_for_date = calculate_change_for_date(date_for_calculate)
        keyboard = create_keyboard_for_change()
        new_log(logger, message.from_user.first_name, message.text)
        bot.send_message(message.chat.id, f'{date_for_calculate.strftime("%d.%m.%y")}:\n{change_for_date}',
                         reply_markup=keyboard)

    if message.text == 'Tomorrow':  # нажата кнопка "Yesterday"
        date_for_calculate = datetime.datetime.now().date() + datetime.timedelta(days=1)
        change_for_date = calculate_change_for_date(date_for_calculate)
        keyboard = create_keyboard_for_change()
        new_log(logger, message.from_user.first_name, message.text)
        bot.send_message(message.chat.id, f'{date_for_calculate.strftime("%d.%m.%y")}:\n{change_for_date}',
                         reply_markup=keyboard)

    if looks_like_conveyor_position(message.text):  # введен текст похожий на позицию конвейера
        position_to_find['position'] = message.text  # переопределим переменную
        keyboard = create_keybord_for_zones()
        bot.send_message(message.chat.id, "Choice zone", reply_markup=keyboard)

    position = position_to_find['position']

    if message.text == 'Find IGME position':  # нажата кнопка "Find IGME position"
        # remote_keyboard = types.ReplyKeyboardRemove()  # удалит клавиатуру
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        cancel_button = types.KeyboardButton('Cancel')
        keyboard.add(cancel_button)
        bot.send_message(message.chat.id, "Write conveyor position\n(4 signs)", reply_markup=keyboard)

    if message.text in ('F01', 'F02', 'F03', 'F04', 'F05', 'F06', 'F07', 'F08'):  # нажата кнопка зоны"
        zone = message.text
        try:
            dict_from_json = load_from_gitHub_json_file()
            bot.send_message(message.chat.id, f"{zone}.{position} - {dict_from_json[zone][f'{zone}.{position}']}")
        except KeyError:
            bot.send_message(message.chat.id, f"Can't find position - {zone}.{position}")
        except NameError:
            bot.send_message(message.chat.id, f'Write the number at first\n(4 signs)')
        finally:
            logger.info(f'{message.from_user.id} - get reply for {message.text}')


bot.infinity_polling()
