from enum import Enum, auto


class UnitSystem(Enum):
    IMPERIAL = auto()
    METRIC = auto()


class Polarity(Enum):
    DARK = auto()
    CLEAR = auto()
