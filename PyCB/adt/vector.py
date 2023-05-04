import math


class Vector:
    def __init__(self, x: float = 0, y: float = 0):
        self.__vec = [x, y]

    def __str__(self):
        return f"({self.x}, {self.y})"

    @property
    def x(self):
        return self.__vec[0]

    @property
    def y(self):
        return self.__vec[1]

    def __mul__(self, other):
        if type(other) in (int, float):
            return Vector(self.x * other, self.y * other)

        return Vector(self.x * other.x, self.y * other.y)

    def __sub__(self, other):
        if type(other) in (int, float):
            return Vector(self.x - other, self.y - other)

        return Vector(self.x - other.x, self.y - other.y)

    def __add__(self, other):
        if type(other) in (int, float):
            return Vector(self.x + other, self.y + other)

        return Vector(self.x + other.x, self.y + other.y)

    def __abs__(self):
        return Vector(abs(self.x), abs(self.y))

    def floor(self):
        return Vector(math.floor(self.x), math.floor(self.y))

    def copy(self):
        return Vector(self.x, self.y)
