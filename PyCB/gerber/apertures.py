from dataclasses import dataclass


@dataclass(slots=True)
class Aperture:
    hole_diameter: float = 0.0


@dataclass(slots=True)
class CircleAperture(Aperture):
    diameter: float = 0.0


@dataclass(slots=True)
class RectangleAperture(Aperture):
    x_size: float = 0.0
    y_size: float = 0.0


@dataclass(slots=True)
class ObroundAperture(Aperture):
    x_size: float = 0.0
    y_size: float = 0.0


@dataclass(slots=True)
class PolygonAperture(Aperture):
    outer_diameter: float = 0.0
    vertices: int = 0
    rotation: float = 0.0
