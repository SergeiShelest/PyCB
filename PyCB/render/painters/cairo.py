import math

import cairo

from PyCB.adt import Vector
from PyCB.render.painters.interface import IPainter, Color


class PainterCairo(IPainter):
    def __init__(self, output_image_path):
        self.output_image_path = output_image_path
        self.surface = None
        self.context = None

    def init(self, image_size: Vector):
        self.surface = cairo.ImageSurface(cairo.FORMAT_RGB24, image_size.x, image_size.y)
        self.context = cairo.Context(self.surface)
        self.context.scale(1, 1)

    def line(self, positions: [Vector], stroke_width: float, color: Color):
        self.context.set_source_rgb(*color)
        self.context.set_line_width(stroke_width)
        self.context.set_line_cap(cairo.LINE_CAP_ROUND)
        self.context.set_line_join(cairo.LINE_JOIN_ROUND)
        self.context.move_to(positions[0].x, positions[0].y)

        for position in positions:
            self.context.line_to(position.x, position.y)

        self.context.stroke()

    def polygon(self, positions: [Vector], color: Color):
        self.context.set_line_width(0)
        self.context.set_source_rgb(*color)
        self.context.move_to(positions[0].x, positions[0].y)

        for position in positions[1: -1]:
            self.context.line_to(position.x, position.y)

        self.context.close_path()
        self.context.fill()

    def circle(self, position: Vector, radius: float, color: Color):
        self.context.set_line_width(0)
        self.context.set_source_rgb(*color)
        self.context.arc(position.x, position.y, radius, 0, 2 * math.pi)
        self.context.close_path()
        self.context.fill()

    def rectangle(self, position: Vector, size: Vector, color: Color):
        self.context.set_line_width(0)
        self.context.set_source_rgb(*color)
        self.context.rectangle(position.x - size.x / 2, position.y - size.y / 2, size.x, size.y)
        self.context.fill()

    def obround(self, position: Vector, size: Vector, color: Color):
        p1, p2, width = position.copy(), position.copy(), 0

        if size.x > size.y:
            p1 = p1 - Vector(size.x / 4, 0)
            p2 = p2 + Vector(size.x / 4, 0)

            width = size.y
        else:
            p1 = p1 - Vector(0, size.y / 4)
            p2 = p2 + Vector(0, size.y / 4)

            width = size.x

        self.context.set_source_rgb(*color)
        self.context.set_line_width(width)
        self.context.set_line_cap(cairo.LINE_CAP_ROUND)
        self.context.set_line_join(cairo.LINE_JOIN_ROUND)
        self.context.move_to(p1.x, p1.y)
        self.context.line_to(p2.x, p2.y)
        self.context.stroke()

    def complete(self):
        self.surface.write_to_png(self.output_image_path)
