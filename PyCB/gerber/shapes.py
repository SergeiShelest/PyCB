from enum import Enum, auto
from dataclasses import dataclass

from PyCB.adt import Vector


class ShapeType(Enum):
    APERTURE = auto()
    POLYGON = auto()
    LINE = auto()
    ARC = auto()


@dataclass(slots=True)
class Shape:
    type: ShapeType
    aperture: int
    positions: [Vector]
