import json
import os


def load_transactions(file_path):
    if not os.path.exists(file_path):
        return []

    with open(file_path, 'r') as file:
        try:
            data = json.load(file)
            if isinstance(data, list):
                return data
            else:
                return []
        except json.JSONDecodeError:
            return []


from logger import utils_logger

def another_function():
    utils_logger.error("Это сообщение об ошибке из utils.")