import math
from turtle import *

from Labs.Lab_02.Figure import Figure


class Rectangle(Figure):
    def __init__(self, x0, y0, x2, y2):
        super().__init__()
        self.__vertex0 = (x0, y0)
        self.__vertex1 = (x2, y0)
        self.__vertex2 = (x2, y2)
        self.__vertex3 = (x0, y2)

    def draw(self):
        super().draw()

        v0 = self.get_transformed_vertex(self.__vertex0)
        v1 = self.get_transformed_vertex(self.__vertex1)
        v2 = self.get_transformed_vertex(self.__vertex2)
        v3 = self.get_transformed_vertex(self.__vertex3)

        goto(v0)
        down()
        goto(v1)
        goto(v2)
        goto(v3)
        goto(v0)
        up()


if __name__ == '__main__':
    r = Rectangle(0, 0, 100, 100)
    r.pivot = (50, 50)
    r.draw()

    r.color = "green"
    r.scale = (2, 2)
    r.draw()

    r.color = "red"
    r.rotation = math.radians(30)
    # r.position = (-100, -100)
    # r.scale = (2, 3)
    r.draw()

    mainloop()
