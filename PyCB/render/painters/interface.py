from abc import ABCMeta, abstractmethod

from PyCB.adt.vector import Vector

Color = (float, float, float)


class IPainter(metaclass=ABCMeta):
    @abstractmethod
    def init(self, image_size: Vector):
        """ Initialize """

    @abstractmethod
    def line(self, positions: [Vector], stroke_width: float, color: Color):
        """ Draw track """

    @abstractmethod
    def rectangle(self, position: Vector, size: Vector, color: Color):
        """ Draw rect """

    @abstractmethod
    def polygon(self, positions: [Vector], color: Color):
        """ Draw polygon """

    @abstractmethod
    def circle(self, position: Vector, radius: float, color: Color):
        """ Draw circle """

    def obround(self, position: Vector, size: Vector, color: Color):
        """ Draw obround """

    @abstractmethod
    def complete(self):
        """ It will be called after the drawing is completed """
