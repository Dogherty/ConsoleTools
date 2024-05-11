RESET = '\033[0m'

COLORS = {
    'PURPLE': '\033[95m',
    'CYAN': '\033[96m',
    'DARKCYAN': '\033[36m',
    'BLUE': '\033[94m',
    'GREEN': '\033[92m',
    'YELLOW': '\033[93m',
    'RED': '\033[91m',
    'BOLD': '\033[1m',
    'UNDERLINE': '\033[4m'
}

RAINBOW_COLORS = {
    'RED': '\033[91m',
    'ORANGE': '\033[38;5;208m',
    'YELLOW': '\033[93m',
    'GREEN': '\033[92m',
    'BLUE': '\033[94m',
    'INDIGO': '\033[38;5;69m',
    'VIOLET': '\033[95m',
}


def paint(text: str, color: str = None) -> str:
    if color is None:
        return text
    color_code = COLORS.get(color.upper())
    if color_code is None:
        raise ValueError('Unknown color. Use rgb(text, r, g, b) for different colors.')
    return color_code + text + RESET


def paint_rgb(text: str, red: int, green: int, blue: int) -> str:
    if not all(0 <= value <= 250 for value in (red, green, blue)):
        raise ValueError('RGB values must be between 0 and 250.')
    return "\033[38;2;{r};{g};{b}m{text}{reset}".format(
        r=red, g=green, b=blue, text=text, reset=RESET
    )


def paint_rainbow(text: str, paint_individual_chars: bool = False) -> str:
    if paint_individual_chars:
        return ''.join([list(RAINBOW_COLORS.values())[i % 7] + char for i, char in enumerate(text)] + ['\033[0m'])
    else:
        return ' '.join(
            [list(RAINBOW_COLORS.values())[i % 7] + word for i, word in enumerate(text.split())] + ['\033[0m'])
