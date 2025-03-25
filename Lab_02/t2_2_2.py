import math
import random
import time
from turtle import *

from Labs.Lab_02.Triangle import Triangle


def draw_random():
    speed(0)
    colors = ['red', 'blue', 'green', 'yellow', 'pink', 'lime']

    for _ in range(100):
        x1, y1 = random.randint(10, 100), random.randint(10, 100)
        x2, y2 = random.randint(-100, 100), random.randint(-100, 100)
        x, y = random.randint(-100, 100), random.randint(-100, 100)
        color = random.choice(colors)

        t = Triangle(x1, y1, x2, y2)
        t.position = (x, y)
        t.color = color
        t.draw()


def animate_rotation():
    t = Triangle(50, 0, 25, 50)
    t.position = (0,0)
    t.color = 'blue'

    for angle in range(0, 360, 20):
        clear()
        t.rotation = math.radians(angle)
        t.draw()
        update()
        time.sleep(0.05)


def animate_scaling():
    t = Triangle(50, 0, 50, 50)
    t.position = (0,0)
    t.color = 'magenta'

    for scale in range(1, 50, 5):
        clear()
        t.scale = (scale * 0.1, scale * 0.1)
        t.draw()
        update()
        time.sleep(0.1)


t1 = Triangle(50,0, 25, 50)
t1.color = 'lime'
t1.draw()


t1.scale = (2,2)
t1.position = (100, 100)
t1.color = 'red'
t1.draw()

animate_rotation()

animate_scaling()


mainloop()
