import math
from Equation import Equation


class QuadraticEquation(Equation):

    INF = "Infinite number of solutions"

    def __init__(self, a, b, c):
        self.a = a
        super().__init__(b, c)

    def __str__(self):
        return f"{self.a}x^2 + {self.b}x + {self.c} = 0"

    @property
    def discriminant(self):
        return self.b ** 2 - 4 * self.a * self.c


    def solutions_number(self):
        solutions = self.solve()
        if solutions == QuadraticEquation.INF:
            return QuadraticEquation.INF
        return len(solutions)

    def solve(self):
        if self.a == 0:
            return super().solve()
        else:  # a != 0, повноцінне квадратне рівняння
            d = self.discriminant # маленька оптимізація, щоб не рахувати дискримінант багато разів.
            if d < 0: # розвʼязків немає
                return () # множина розвʼязків порожня, отже повертаємо порожній кортеж
            elif d == 0: # один розвʼязок
                x1 = -self.b / (2.0 * self.a)
                return (x1,)
            else: # d > 0, два розвʼязки
                d = d ** 0.5  # рахуємо корінь з дискримінанта, щоб потім в явному вигляді відшукання розвʼязків не робити цього.
                x1 = (-self.b + d) / (2.0 * self.a)
                x2 = (-self.b - d) / (2.0 * self.a)
                solutions = [x1, x2]
                solutions.sort()
                # return x1, x2
                return tuple(solutions)


if __name__ == '__main__':
    eq5 = QuadraticEquation(1, 4, 4)
    print(eq5)
    print(eq5.solve())