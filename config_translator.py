import json
import sys

from transformer import transform


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <output_file>")
        sys.exit(1)

    output_file = sys.argv[1]

    # Чтение входных данных из stdin
    json_input = sys.stdin.read()

    # Парсим json
    try:
        data = json.loads(json_input)
    except json.JSONDecodeError as e:
        print(f"Error in JSON input: {e}")
        sys.exit(1)

    # Преобразуем в учебный конфигурационный язык
    try:
        result = transform(data)
    except Exception as e:
        print(f"Error during transformation: {e}")
        sys.exit(1)

    # Записываем в файл
    with open(output_file, 'w') as f:
        f.write(result)


if __name__ == "__main__":
    main()

#python config_translator.py output.txt < examples/example4.json
#python -m unittest discover -s tests
