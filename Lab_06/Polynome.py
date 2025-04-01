from collections import defaultdict
class PolynomIterator:
    def __init__(self, collection: dict):
        self._index = 0
        self.collection = {}
        for power, coef in collection.items():
            if coef != 0:
                self.collection[power] = coef

        self._degrees = sorted(self.collection.keys())[::-1]

    def __next__(self):
        if self._index >= len(self._degrees):
            raise StopIteration
        deg = self._degrees[self._index]
        coeff = self.collection[deg]
        self._index += 1
        return deg, coeff


class Polynome(defaultdict):
    def __iter__(self):
        return PolynomIterator(self)

    @staticmethod
    def fromstring(s):
        p = Polynome()
        s = s.replace('+',' ')
        ls = s.split()  #розбиваємо на список одночленів
        for m in ls:
            c = m.split('*x**') #виділяємо степінь та коефіцієнт
            k = int(c[1])
            v = float(c[0])
            p[k] = v
        return p

    # fromstring = staticmethod(fromstring)

    def add_monom(self, deg, coeff):
        if coeff != 0:
            self[deg] += coeff

    def get_degree(self):
        return max(self)

    def __str__(self):
        monomials = list(self.items())
        if not monomials:
            poly_str = "0.0*x**0"
        else:
            # Впорядковуємо за спаданням степенів
            monomials.sort(reverse=True)
            ls = ["{}*x**{}".format(mono[1], mono[0]) for mono in monomials]
            poly_str = ' + '.join(ls)
        return poly_str

    def __call__(self, x):
        return sum([self[k]*x**k for k in self])

    def __add__(self, other):
        p = Polynome()
        # утворюємо множину, що містить всі ключі self та other
        keys = set(self.keys()) | set(other.keys())
        for k in keys:
            p[k] = self[k] + other[k]
        return self._delzeroes(p)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        p = Polynome()
        keys = set(self.keys()) | set(other.keys())
        for k in keys:
            p[k] = self[k] - other[k]
        return self._delzeroes(p)

    def __rsub__(self, other):
        p = Polynome()
        keys = set(self.keys()) | set(other.keys())
        for k in keys:
            p[k] = other[k] - self[k]
        return self._delzeroes(p)

    def __mul__(self, other):
        p = Polynome()
        for k1 in self:
            for k2 in other:
                p[k1 + k2] += self[k1] * other[k2]
        return self._delzeroes(p)

    def __rmul__(self, other):
        return self.__rmul__(other)

    def deriv(self, n=1):
        p = self
        for i in range(n):
            p = self._deriv(p)
        return self._delzeroes(p)

    def _deriv(self, p):
        pp = Polynome()
        for k in p:
            if k != 0:
                pp[k - 1] = p[k] * k
        return pp

    def _delzeroes(self, p):
        pp = Polynome()
        for k in p:
            if p[k] != 0:
                pp[k] = p[k]
        return pp


if __name__ == '__main__':
    p1 = Polynome.fromstring('3.7*x**3 + 0.3*x**1 + -1.2*x**0')
    print('р1 =', p1)
    """p2 = Polynome.fromstring('2.2*x**3 + -1.3*x**2 + 0.2*x**1')
    print('р2 =', p2)
    print('Значення p1 у точці x=2:', p1(2))
    print('Сума p1+p2:', p1 + p2)
    print('Різниця p1-p2:', p1 - p2)
    print('Добуток p1*p2:', p1 * p2)
    p = p1.deriv(2)
    print('2 похідна р1:', p)"""


    for deg, coeff in p1:
        print(f"Степінь: {deg}, Коефіцієнт: {coeff}")

    for deg, coeff in p1:
        print(f"степінь: {deg}, коефіцієнт: {coeff}")