from Figure import Figure
from turtle import *


class Trapezoid(Figure):
    """ Клас Трапеція

    Використовується для зображення рівнобічної трапеції на екрані
    """

    def __init__(self, x, y, a, b, color):
        """ Конструктор
        Ініціалізує положення лівої нижньої вершини,
        довжини його основ і колір.
        :param x: координата x лівої нижньої вершини
        :param y: координата y лівої нижньої вершини
        :param a: довжина більшох основий трапеції
        :param b: довжина меншої основий трапеції
        :param color: колір трапеції
        """

        super().__init__(x, y, color)  # виклик конструктора базового класу
        self._a = a
        self._b = b
        self._h = ((a - b) / 2) * (3 ** 0.5)
        self._c = (self._h**2 + ((self._a - self._b) / 2)**2)**0.5

    def _draw(self, color):
        """ Віртуальний метод, що зображує трапецію на екрані заданим кольором
        :param color: колір
        """

        pencolor(color)
        up()
        setpos(self._x, self._y)
        down()
        goto(self._x + self._a, self._y)
        goto(self._x + self._a - ((self._a - self._b) / 2), self._y + self._h)
        goto(self._x + ((self._a - self._b) / 2), self._y + self._h)
        goto(self._x, self._y)
        up()
