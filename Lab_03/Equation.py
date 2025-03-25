import math

class Equation:
    INF = "Infinite number of solutions"

    def __init__(self, b, c):
        self.b = b
        self.c = c

    def __str__(self):
        return f"{self.b}x + {self.c} = 0"

    def show(self):
        print(self)

    def solve(self):
        if self.b == 0 :
            if self.c == 0:
                return Equation.INF
            elif self.c != 0:
                return ()
        return (- self.c / self.b,)

    def solutions_number(self):
        solutions = self.solve()
        if solutions == Equation.INF:
            return Equation.INF
        return len(solutions)


if __name__ == '__main__':
    eq1 = Equation(1,1)
    print(eq1)
    print(eq1.solve())

