from telebot import types


def create_keybord_for_zones():
    """Create buttons for all zones with /cancel command"""
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    dict_with_buttons = {}
    for i in range(1, 9):
        dict_with_buttons[i] = types.KeyboardButton(f'F0{i}')
    keyboard.add(*dict_with_buttons.values(), types.KeyboardButton('Cancel'))
    return keyboard


def create_keyboard_for_change():
    """Create buttons for choice change"""
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    cancel_button = types.KeyboardButton('Cancel')
    button_1 = types.KeyboardButton('Yesterday')
    button_2 = types.KeyboardButton('Today')
    button_3 = types.KeyboardButton('Tomorrow')
    keyboard.add(button_1, button_2, button_3, cancel_button)
    return keyboard
