import math

class QuadraticEq:
    def __init__(self, a , b = None, c = None):
        if isinstance(a, QuadraticEq):
            self._a = a._a
            self._b = a._b
            self._c = a._c
        else:
            self._a = a
            self._b = b
            self._c = c

    def discriminant(self):
        return self._b ** 2 - 4 * self._a + self._c

    def solve(self):
        D = self.discriminant()
        if D < 0:
            return None
        elif self._a == 0:
            if self._b == 0:
                return "infinity"
            else:
                x = -self._c/self._b
                return [x]
        elif D == 0:
            x = self._b / (2 * self._a)
            return [x]
        else:
            x1 = (- self._b + math.sqrt(D)) / (2 * self._a)
            x2 = (- self._b - math.sqrt(D)) / (2 * self._a)
            return [x1, x2]

    def show(self):
        eq = f'{self._a}x^2'
        eq += f'+{self._b}x' if self._b >= 0 else f'-{-self._b}x'
        eq += f'+{self._c}' if self._c >= 0 else f'-{-self._c}'
        eq += '= 0'
        print(eq)


def process_eq(file_path):
    eqs = []
    with open(file_path, 'r') as f:
        for line in f:
            coefs = list(map(float, line.strip().split()))
            if len(coefs) == 3:
                eqs.append(QuadraticEq(*coefs))

    no_sol = []
    one_sol = []
    two_sol = []
    inf_sol = []

    for eq in eqs:
        sol = eq.solve()
        if sol is None:
            no_sol.append(eq)
        elif sol == "infinity":
            inf_sol.append(eq)
        elif len(sol) == 1:
            one_sol.append((eq, sol[0]))
        else:
            two_sol.append(eq)

    print('no solutions:')
    for eq in no_sol:
        eq.show()

    print('one solution:')
    for eq, sol in one_sol:
        eq.show()
        print(f'solution: x = {sol}')

    print('two solutions:')
    for eq in two_sol:
        eq.show()

    print('infinity solutions:')
    for eq in inf_sol:
        eq.show()

    if one_sol:
        min_sol_eq = min(one_sol, key=lambda x: x[1])
        max_sol_eq = max(one_sol, key=lambda x: x[1])

        print("min one solution:")
        min_sol_eq[0].show()
        print(f'solution: x = {min_sol_eq[1]}')

        print("max one solution:")
        max_sol_eq[0].show()
        print(f'solution: x = {max_sol_eq[1]}')

"""
for f in ['input01.txt']:
    print('processing')
    process_eq(f)
    """

if __name__ == '__main__':
    a = QuadraticEq(1,2,3)
    a2 = copy.copy(a)
