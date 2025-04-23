from collections.abc import Callable

def process_data(data, operation: Callable, dict_mode: str = 'values'):
    try:
        if not callable(operation):
            raise TypeError("Аргумент 'operation' має бути функцією.")

        if isinstance(data, dict):
            if dict_mode == 'keys':
                return {operation(k): v for k, v in data.items()}
            elif dict_mode == 'values':
                return {k: operation(v) for k, v in data.items()}
            elif dict_mode == 'items':
                return {operation(k): operation(v) for k, v in data.items()}
            else:
                raise ValueError("dict_mode повинен бути 'keys', 'values' або 'items'.")

        elif isinstance(data, list):
            return [operation(x) for x in data]
        elif isinstance(data, tuple):
            return tuple(operation(x) for x in data)
        else:
            raise TypeError("Тип колекції не підтримується.")

    except Exception as e:
        return f"Помилка: {e}"

def filter_data(data, predicate: Callable):
    try:
        if not callable(predicate):
            raise TypeError("Аргумент 'predicate' має бути функцією.")

        if isinstance(data, dict):
            return {k: v for k, v in data.items() if predicate((k, v))}
        elif isinstance(data, list):
            return [x for x in data if predicate(x)]
        elif isinstance(data, tuple):
            return tuple(x for x in data if predicate(x))
        else:
            raise TypeError("Тип колекції не підтримується.")

    except Exception as e:
        return f"Помилка: {e}"

def combine_values(*args, separator: str = '', start=None):
    try:
        if not args:
            return None

        first_type = type(args[0])
        if all(isinstance(arg, (int, float)) for arg in args):
            result = start if start is not None else 0
            for arg in args:
                result += arg
            return result

        elif all(isinstance(arg, str) for arg in args):
            result = separator.join(args)
            return result
        else:
            raise TypeError("Усі аргументи повинні бути одного типу: або всі числа, або всі рядки.")

    except Exception as e:
        return f"Помилка: {e}"

if __name__ == "__main__":
    print(process_data([1, 2, 3], lambda x: x**2))
    print(process_data((1, 2, 3), lambda x: x + 1))
    print(process_data({"a": 1, "b": 2}, lambda x: x * 10, dict_mode='values'))

    print(filter_data([1, 2, 3, 4], lambda x: x % 2 == 0))
    print(filter_data({"a": 1, "b": 2}, lambda item: item[1] > 1))

    print(combine_values(1, 2, 3, start=10))
    print(combine_values("a", "b", "c", separator="-"))
