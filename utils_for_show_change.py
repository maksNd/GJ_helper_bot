import datetime
from gj_changes import change_dict


def looks_like_date(text:str) -> bool:
    """Tries detect the text like date"""
    if len(text) in (3, 4, 5, 6) and '.' in text:
        return True


def conver_str_to_date(incoming_data: str, year=datetime.datetime.now().year):
    """Converts inputted text to data with current year"""
    incoming_data = incoming_data.replace(' ', '.')
    incoming_data = incoming_data.replace(',', '.')
    result = datetime.datetime.strptime(f"{incoming_data}.{year}", "%d.%m.%Y").date()
    return result


def calculate_change_for_date(date):
    """Returns what change for date"""
    for change, change_date in change_dict.items():
        if (change_date - date).days % 4 == 0:
            return change