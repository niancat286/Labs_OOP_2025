import random
from turtle import *
from random import randint


class Triangle:
    def __init__(self, x1, y1, x2, y2):
        self.position = (0,0)
        self.vertex1 = (x1, y1)
        self.vertex2 = (x2, y2)

        self.color = 'black'

    def set_position(self, x, y):
        self.position = (x, y)

    def set_color(self, color):
        self.color = color

    def draw(self):
        down()
        color(self.color)
        begin_fill()
        goto(self.position[0] + self.vertex1[0], self.position[1] + self.vertex1[1])
        goto(self.vertex1[0]+self.vertex2[0], self.vertex1[1]+self.vertex2[1])
        goto(self.position)
        end_fill()
        up()


def draw_random():
    speed(0)
    colors = ['red', 'blue', 'green', 'yellow', 'pink', 'lime']

    for _ in range(100):
        x1, y1 = random.randint(10, 100), random.randint(10, 100)
        x2, y2 = random.randint(-100, 100), random.randint(-100, 100)
        x, y = random.randint(-100, 100), random.randint(-100, 100)
        color = random.choice(colors)

        t = Triangle(x1, y1, x2, y2)
        t.set_position(x, y)
        t.set_color(color)
        t.draw()




"""t1 = Triangle(50,0, 25, 50)
t1.set_color('lime')
t1.draw()"""


draw_random()
mainloop()
