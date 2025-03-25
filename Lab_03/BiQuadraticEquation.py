import math
from QuadraticEquation import QuadraticEquation


class BiQuadraticEquation(QuadraticEquation):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)

    def __str__(self):
        return f"{self.a}x^4 + {self.b}x^2 + {self.c} = 0"


    def solve(self):
        solutions_quad = super().solve()
        sols = []
        for sol in solutions_quad:
            if sol < 0:
                pass
            elif sol == 0:
                sols.append(sol)
            else:
                sols.append(math.sqrt(sol))
                sols.append(-math.sqrt(sol))

        sols.sort()
        return tuple(sols)

    def solutions_number(self):
        solutions = self.solve()
        if solutions == BiQuadraticEquation.INF:
            return BiQuadraticEquation.INF
        return len(solutions)


if __name__ == '__main__':
    bieq = BiQuadraticEquation(1, -5, 4)
    print(bieq)
    print(bieq.solve())