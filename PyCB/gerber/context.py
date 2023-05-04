from dataclasses import dataclass, field

from PyCB.adt import Vector
from .enums import UnitSystem, Polarity
from .shapes import Shape


@dataclass
class Context:
    global_unit_system: UnitSystem = UnitSystem.IMPERIAL
    unit_system: UnitSystem = UnitSystem.IMPERIAL
    polarity: Polarity = Polarity.CLEAR
    apertures: dict = field(default_factory=dict)
    draw_queue: list[Shape] = field(default_factory=list)
    aperture: str = "10"
    position: Vector = field(default_factory=Vector)
    polygon_mode: bool = False
