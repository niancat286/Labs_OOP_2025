from turtle import *

from Labs.Lab_02.Figure import Figure

class Triangle(Figure):
    def __init__(self, x0, y0, x1, y1, x2, y2):
        super().__init__()
        self.__vertex0 = (x0, y0)
        self.__vertex1 = (x1, y1)
        self.__vertex2 = (x2, y2)


    def draw(self):
        super().draw()

        v0 = self.get_transformed_vertex(self.__vertex0)
        v1 = self.get_transformed_vertex(self.__vertex1)
        v2 = self.get_transformed_vertex(self.__vertex2)

        goto(v0)
        down()
        goto(v1)
        goto(v2)
        goto(v0)
        up()



if __name__ == '__main__':
    t = Triangle(0, 0, 100, 0, 100, 100)
    t.draw()

    t.color = "green"
    t.scale = (2,2)
    t.draw()

    t.color = "red"
    t.scale = (2, 3)
    t.draw()

    mainloop()
