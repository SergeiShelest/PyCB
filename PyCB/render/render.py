import math

from PyCB.adt import Vector
from PyCB.gerber import CommandsProcessor
from PyCB.gerber.shapes import ShapeType
from PyCB.gerber.apertures import CircleAperture, RectangleAperture, ObroundAperture, PolygonAperture

from .painters.interface import IPainter


class Render:
    def __init__(self, processor: CommandsProcessor, painter: IPainter, scale: int, start_pos: Vector, end_pos: Vector):
        self.cmd_proc = processor
        self.cmd_proc.start()

        self.scale = scale
        self.start_pos = start_pos
        self.end_pos = end_pos

        image_size = abs(self.end_pos - self.start_pos) * self.scale
        image_size = image_size.floor()

        self.painter = painter
        self.painter.init(image_size)

    def transform_positions(self, positions):
        new_positions = []

        for p in positions:
            p = self.start_pos - p

            if self.start_pos.x < 0:
                p = Vector(abs(self.end_pos.x - self.start_pos.x) + p.x, p.y)

            if self.start_pos.y < 0:
                p = Vector(p.x, abs(self.end_pos.y - self.start_pos.y) + p.y)

            p = abs(p * self.scale)
            new_positions.append(p)

        return new_positions

    def draw(self):
        for shape in self.cmd_proc.context.draw_queue:
            shape.positions = self.transform_positions(shape.positions)

            match shape.type:
                case ShapeType.APERTURE:
                    match shape.aperture:
                        case CircleAperture():
                            self.painter.circle(
                                position=shape.positions[0],
                                radius=shape.aperture.diameter / 2 * self.scale,
                                color=(1.0, 1.0, 1.0)
                            )

                        case RectangleAperture():
                            size = Vector(shape.aperture.x_size * self.scale, shape.aperture.y_size * self.scale)

                            self.painter.rectangle(
                                position=shape.positions[0],
                                size=size,
                                color=(1.0, 1.0, 1.0)
                            )

                        case ObroundAperture():
                            self.painter.obround(
                                position=shape.positions[0],
                                size=Vector(shape.aperture.x_size * self.scale, shape.aperture.y_size * self.scale),
                                color=(1.0, 1.0, 1.0)
                            )

                        case PolygonAperture():
                            # TODO
                            pass

                case ShapeType.POLYGON:
                    self.painter.polygon(
                        positions=shape.positions,
                        color=(1.0, 1.0, 1.0)
                    )

                case ShapeType.LINE:
                    self.painter.line(
                        positions=shape.positions,
                        stroke_width=shape.aperture.diameter * self.scale,
                        color=(1.0, 1.0, 1.0)
                    )

        self.painter.complete()
