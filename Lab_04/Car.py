from turtle import *
from Circle import Circle
from Lab_05.Figure import Figure
from Quadrate import Quadrate
from Triangle import Triangle
from Trapezoid import Trapezoid
from Rectangle import Rectangle


class Car:
    def __init__(self, *parts):
        self.parts: list[Figure] = list(parts)

    def show(self):
        for part in self.parts:
            part.show()

    def hide(self):
        for part in self.parts:
            part.hide()

    def move(self, dx, dy):
        for part in self.parts:
            part.move(dx, dy)


if __name__ == '__main__':
    x = 0
    y = 0

    body = Rectangle(x, y, x + 200, y + 70, 'red')
    roof = Trapezoid(x + 20, y + 70, 150, 100, 'lime')
    wheel1 = Circle(x + 40, y - 30, 30, 'blue')
    wheel2 = Circle(x + 160, y - 30, 30, 'blue')
    wheel1part = Triangle(x + 40, y - 30, 10, 'magenta')
    wheel2part = Triangle(x + 160, y - 30, 10, 'magenta')
    window1 = Quadrate(x + 60, y + 40, 30, 'lightblue')
    window2 = Quadrate(x + 120, y + 40, 30, 'lightblue')
    bmw = Car(body, roof, wheel1, wheel2, wheel1part, wheel2part, window2, window1)

    tracer(0, 0)

    bmw.show()
    for _ in range(100):
        bmw.move(1, 0)
        update()
    mainloop()
