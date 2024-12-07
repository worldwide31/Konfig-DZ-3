def transform(data):
    result = []

    def process_value(value):
        if isinstance(value, int):
            return str(value)
        elif isinstance(value, dict):
            return transform(value)
        elif isinstance(value, list):
            return process_expression(value)
        else:
            raise ValueError(f"Unsupported value: {value}")

    def process_expression(expr):
        if len(expr) == 0:
            return ""

        # Сложение
        if len(expr) == 3 and expr[1] == '+':
            return f"{process_value(expr[0])} + {process_value(expr[2])}"

        # Функция max()
        if len(expr) > 1 and expr[0] == "max":
            return f"max({', '.join(process_value(arg) for arg in expr[1:])})"

        # Функция sqrt()
        if len(expr) == 2 and expr[0] == "sqrt":
            return f"sqrt({process_value(expr[1])})"

        raise ValueError("Invalid expression format")

    for key, value in data.items():
        result.append(f"{key} -> {process_value(value)}")

    return "\n".join(result)
