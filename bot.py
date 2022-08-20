import datetime
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
    start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton('Find IGME position')
    button_2 = types.KeyboardButton('Change today')
    start_keyboard.add(button_1, button_2)
    # bot.send_message(message.chat.id, 'Введите позицию для поиска EGMI\n(4х значное число)')

    bot.send_message(message.chat.id, 'ok', reply_markup=start_keyboard)


position_to_find = {'position': '0000'}  # инициализируем переменную для хранения позиции для поиска


@bot.message_handler()
def main_message_handler(message):  # перехватчик всех сообщений
    if looks_like_date(message.text):  # если введен текст похожий на дату
        try:
            date_for_calculate = conver_str_to_date(message.text)
        except ValueError:
            return
        change_for_date = calculate_change_for_date(date_for_calculate)
        bot.send_message(message.chat.id, f'{date_for_calculate.strftime("%d.%m.%y")}:\n{change_for_date}')

    if message.text == 'Change today':  # нажата кнопка "Change today"
        date_for_calculate = datetime.datetime.now().date()
        change_for_date = calculate_change_for_date(date_for_calculate)
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        start_button = types.KeyboardButton('/start')
        keyboard.add(start_button)
        bot.send_message(message.chat.id, f'{date_for_calculate.strftime("%d.%m.%y")}:\n{change_for_date}',
                         reply_markup=keyboard)

    if looks_like_conveyor_position(message.text):  # введен текст похожий на позицию конвейера
        position_to_find['position'] = message.text  # если ввод похож на позицию для поиска - переопределим переменную
        keyboard = create_keybord_for_zones()
        bot.send_message(message.chat.id, "Change zone", reply_markup=keyboard)

    position = position_to_find['position']

    if message.text == 'Find IGME position':  # нажата кнопка "Find IGME position"
        remote_keyboard = types.ReplyKeyboardRemove()  # удалит клавиатуру
        bot.send_message(message.chat.id, "Write conveyor position\n(4 signs)", reply_markup=remote_keyboard)

    if message.text in ('F01', 'F02', 'F03', 'F04', 'F05', 'F06', 'F07', 'F08'):  # нажата кнопка зоны"
        zone = message.text
        try:
            dict_from_json = load_from_gitHub_json_file()
            bot.send_message(message.chat.id, f"{zone}.{position} - {dict_from_json[zone][f'{zone}.{position}']}")
        except KeyError:
            bot.send_message(message.chat.id, f"Can't find position - {zone}.{position}")
        except NameError:
            bot.send_message(message.chat.id, f'Write the number at first\n(4 signs)')


bot.infinity_polling()
