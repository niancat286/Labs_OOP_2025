import math
from turtle import *

AVAILABLE_COLORS = ['red', 'blue', 'green', 'yellow', 'pink', 'lime']

class Figure:
    def __init__(self):

        self.__position = (0, 0)
        self.__rotation = 0
        self.__scale = (1, 1)
        self.__pivot = (0, 0)
        self.__color = 'black'

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, pos: tuple):
        self.__position = pos

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        if color not in AVAILABLE_COLORS:
            self.__color = "black"
            return

        self.__color = color

    @property
    def rotation(self):
        return self.__rotation

    @rotation.setter
    def rotation(self, rotation):
        self.__rotation = rotation

    @property
    def scale(self):
        return self.__scale

    @scale.setter
    def scale(self, scale):
        if isinstance(scale, (float, int)):
            self.__scale = (scale, scale)
        elif isinstance(scale, (tuple, list)):
            if len(scale) == 2:
                self.__scale = (scale[0], scale[1])
            elif len(scale) == 1:
                self.__scale = (scale[0], scale[0])
            else:
                raise ValueError("Scale isn't correct")
        else:
            raise TypeError("float, int, tuple or list is expected")

    @property
    def pivot(self):
        return  self.__pivot

    @pivot.setter
    def pivot(self, pivot: tuple):
        self.__pivot = pivot

    def get_transformed_vertex(self, vertex):
        x0, y0 = self.__position
        px, py = self.__pivot
        sx, sy  = self.__scale
        angle = self.__rotation
        cos_phi, sin_phi = math.cos(angle), math.sin(angle)

        x, y = vertex
        x, y = x - px, y - py  # pivot -> (0, 0)
        x, y = sx * x, sy * y  # scale
        x, y  = cos_phi * x - sin_phi * y, sin_phi * x + cos_phi * y # rotation
        x, y = x0 + x, y0 + y
        x, y = x + px, y + py # pivot -> to the start pivot position

        return x, y

    def draw(self):
        color(self.color)
        up()



