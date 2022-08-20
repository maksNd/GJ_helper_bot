from telebot import types


def create_keybord_for_zones():
    """Create buttons for all zones with /start command"""
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    dict_with_buttons = {}
    for i in range(1, 9):
        dict_with_buttons[i] = types.KeyboardButton(f'F0{i}')
    keyboard.add(*dict_with_buttons.values(), types.KeyboardButton('/start'))
    return keyboard
