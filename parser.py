import re

def parse_json(data):
    # Проверка на соответствие требованиям
    for key, value in data.items():
        if not re.match(r'^[a-z_]+$', key):
            raise ValueError(f"Invalid name: {key}")

        if isinstance(value, dict):
            parse_json(value)  # Рекурсивно проверяем вложенные словари

        # Проверка значений: числа, списки, или словари
        if not isinstance(value, (int, dict, list)):
            raise ValueError(f"Invalid value for {key}: {value}")
    return data
