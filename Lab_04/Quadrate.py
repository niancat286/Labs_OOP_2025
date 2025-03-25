from Figure import Figure
from turtle import *


class Quadrate(Figure):
    """ Клас Квадрат """

    def __init__(self, x, y, a, color):
        """ Конструктор
        Ініціалізує положення лівого нижнього кута квадрата,
        довжину його сторони і колір.
        :param x: координата x лівого нижнього кута квадрата
        :param y: координата y лівого нижнього кута квадрата
        :param a: довжина сторони квадрата
        :param color: колір квадрата
        """
        super().__init__(x, y, color)  # виклик конструктора базового класу
        self._a = a

    def _draw(self, color):
        """ Допоміжний метод, що зображує квадрат заданим кольором
        :param color: колір
        """
        pencolor(color)
        up()
        setpos(self._x - self._a/2, self._y - self._a/2)
        down()
        for _ in range(4):
            fd(self._a)
            lt(90)
        up()