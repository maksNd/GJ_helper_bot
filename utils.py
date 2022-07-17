from telebot import types
import json


def reading_json_file(path):
    with open(path, 'r') as file:
        dict_from_file = json.load(file)
        return dict_from_file


def create_keybord_for_zones():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    dict_with_buttons = {}
    for i in range(1, 9):
        dict_with_buttons[i] = types.KeyboardButton(f'F0{i}')
    keyboard.add(*dict_with_buttons.values(), types.KeyboardButton('/start'))
    return keyboard
