from telebot import types
import json
from constants import JSON_FROM_GITHUB
import requests


def looks_like_conveyor_position(text: str) -> bool:
    """Tries detect the text like conveyor position"""
    if len(text) == 4 and text.isdigit():
        return True


def load_from_local_json_file(path) -> dict:
    """Load data from local json file"""
    with open(path, 'r') as file:
        dict_from_file = json.load(file)
        return dict_from_file


def load_from_gitHub_json_file(gitHub_path=JSON_FROM_GITHUB) -> dict:
    """Load data from json file from GitHub"""
    response = requests.get(gitHub_path)
    return response.json()
