from Figure import Figure
from turtle import *


class Rectangle(Figure):
    """ Клас Прямокутник

    Використовується для зображення прямокутника на екрані
    """

    def __init__(self, x, y, a, b, color):
        """ Конструктор
        Ініціалізує положення лівої нижньої вершини,
        довжини його основ і колір.
        :param x: координата x лівої нижньої вершини
        :param y: координата y лівої нижньої вершини
        :param a: перша сторона прямокутника
        :param b: друга сторона прямокутника
        :param color: колір прямокутника
        """
        super().__init__(x, y, color)  # виклик конструктора базового класу
        self._a = a
        self._b = b

    def _draw(self, color):
        """ Віртуальний метод, що зображує прямокутник на екрані заданим кольором
        :param color: колір
        """
        pencolor(color)
        up()
        setpos(self._x, self._y)
        down()
        for _ in range(2):
            fd(self._a)
            lt(90)
            fd(self._b)
            lt(90)
        up()