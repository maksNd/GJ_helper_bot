from telebot import types
import json
from constants import JSON_FROM_GITHUB
import requests


def create_keybord_for_zones():
    """Create buttons for all zones with /start command"""
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    dict_with_buttons = {}
    for i in range(1, 9):
        dict_with_buttons[i] = types.KeyboardButton(f'F0{i}')
    keyboard.add(*dict_with_buttons.values(), types.KeyboardButton('/start'))
    return keyboard


def load_from_local_json_file(path) -> dict:
    """Load data from local json file"""
    with open(path, 'r') as file:
        dict_from_file = json.load(file)
        return dict_from_file


def load_from_gitHub_json_file(gitHup_path=JSON_FROM_GITHUB) -> dict:
    """Load data from json file from GitHub"""
    response = requests.get(gitHup_path)
    return response.json()
