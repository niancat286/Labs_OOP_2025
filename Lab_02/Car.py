import math
from turtle import mainloop

from Labs.Lab_02.Figure import Figure
from Labs.Lab_02.Rectangle import Rectangle
from Labs.Lab_02.Triangle import Triangle


class Car(Figure):

    def __init__(self, *parts):
        super().__init__()
        self.parts: list[Figure] = list(parts)

    def draw(self):
        super().draw()

        for part in self.parts:
            part.scale = self.scale
            part.rotation = self.rotation
            part.position = self.position
            part.pivot = self.pivot

            part.draw()


if __name__ == '__main__':

    car = Car(
        Rectangle(-100, 25, 100, 100), # body
        Triangle(-100, 0, -50, 0, -75, 30),
        Triangle(100, 0, 50, 0, 75, 30),
        Triangle(-100, 100, 100, 100, -50, 150)
    )
    car.draw()

    car.rotation = math.radians(30)
    car.draw()


    mainloop()
