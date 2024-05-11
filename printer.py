from Color import paint


def format_dict(dict_: dict, indent: int = 0, key_color: str = None, value_color: str = None) -> None:
    result = ""
    max_len = max(len(str(key)) for key in dict_)
    for key, value in dict_.items():
        connector = "└─"
        if isinstance(value, dict):
            result += " " * indent + connector + f"{paint(key, key_color)}:\n"
            result += format_dict(value, indent + 4, key_color=key_color, value_color=value_color)
        elif isinstance(value, list):
            result += " " * indent + connector + f"{paint(key.ljust(max_len), key_color)}:\n"
            for item in value:
                result += " " * (indent + 4) + connector + f"{paint(item, value_color)}\n"
        else:
            result += " " * indent + connector + f"{paint(key.ljust(max_len), key_color)}: {paint(value, value_color)}\n"
    print(result)


def format_list(array: list, indent: int = 0) -> None:
    result = ''
    for index, item in enumerate(array):
        if isinstance(item, list):
            result += ' ' * indent + f'{index}: '
            result += format_list(item, indent + indent)
        elif isinstance(item, dict):
            result += ' ' * indent + f'{index}: '
            result += format_dict(item, indent + indent)
        else:
            result += ' ' * indent + f"{index}: {item}\n"
    print(result)


def _find_max(array: list[list]) -> list:
    return [max(map(len, map(str, column))) for column in zip(*array)]


def list_to_table(array: list[list], names: list = None) -> None:
    if names is not None:
        array.insert(0, names)
    max_lengths = _find_max(array)
    border = '+' + '+'.join(['-' * (length + 2) for length in max_lengths]) + '+'
    for item in array:
        print(border)
        string_ = ' | '.join([f"{str(element):<{max_length}}" for element, max_length in zip(item, max_lengths)])
        print('| ' + string_ + ' | ')
    print(border)


if __name__ == '__main__':
    list_ = [['John', 'Doe', '23', 'New York', 'Designer'], ['Klaus', 'Shnaider', '23', 'New York', 'Code']]
    list_to_table(list_, ['name', 'surname', 'age', 'city', 'job'])
