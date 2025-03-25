import math

from Figure import Figure
from turtle import *


class Triangle(Figure):
    """ Клас Трикутник

    Використовується для зображення правильного трикутника на екрані
    """

    def __init__(self, x, y, a, color):
        """ Конструктор
        Ініціалізує положення лівого нижньої вершини трикутника,
        довжину його сторони і колір.
        :param x: координата x лівої нижньої вершини трикутника
        :param y: координата y лівої нижньої вершини трикутника
        :param a: довжина сторони трикутника
        :param color: колір трикутника
        """

        super().__init__(x, y, color)  # виклик конструктора базового класу
        self._a = a

    def _draw(self, color):
        r = self._a /(2 * math.sqrt(3))

        pencolor(color)
        up()
        setpos(self._x - self._a / 2, self._y - r)
        down()
        for _ in range(3):
            fd(self._a)
            lt(120)
        up()
        """ Допоміжний віртуальний метод, що зображує трикутник заданим кольором
        :param color: колір
        """
