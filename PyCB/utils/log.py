import enum


DEBUG = True


class Colors(enum.Enum):
    BLACK = "\x1b[30m"
    RED = "\x1b[31m"
    GREEN = "\x1b[32m"
    YELLOW = "\x1b[33m"
    BLUE = "\x1b[34m"
    MAGENTA = "\x1b[35m"
    CYAN = "\x1b[36m"
    WHITE = "\x1b[37m"


def color_print(color, msg):
    print(f"{color.value}{msg}")


def debug(name, msg):
    if DEBUG:
        color_print(Colors.BLUE, f"[DBG][{name.upper()}] {msg}")


def warning(name, msg):
    color_print(Colors.YELLOW, f"[WRN][{name.upper()}] {msg}")


def error(name, msg):
    color_print(Colors.RED, f"[ERR][{name.upper()}] {msg}")
