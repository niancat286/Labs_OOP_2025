from math import gcd


class Rational:
    def __init__(self, n, d=1):
        if d == 0:
            raise ZeroDivisionError
        self._n = n
        self._ = d
        self._simplify()

    def _simplify(self):
        # Скорочуємо дріб
        g = gcd(self._n, self._d)
        self._n //= g
        self._d //= g

    def __add__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)

        if isinstance(other, Rational):
            new_n = self._n * other._d + other._n * self._d
            new_d = self._d * other._d
            return Rational(new_n, new_d)

        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)

        if isinstance(other, Rational):
            new_n = self._n * other._d - other._n * self._d
            new_d = self._d * other._d
            return Rational(new_n, new_d)

        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)

        if isinstance(other, Rational):
            return Rational(self._n * other._n, self._d * other._d)

        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)

        if isinstance(other, Rational):
            if other._n == 0:
                raise ZeroDivisionError
            return Rational(self._n * other._d, self._d * other._n)

        return NotImplemented

    def __call__(self):
        return self._n / self._d

    def __getitem__(self, key):
        if key == "n":
            return self._n
        elif key == "d":
            return self._d
        else:
            raise KeyError

    def __setitem__(self, key, value):
        if key == "n":
            self._n = value
        elif key == "d":
            if value == 0:
                raise ZeroDivisionError
            self._d = value
        else:
            raise KeyError

        common_divisor = gcd(self._n, self._d)
        self._n //= common_divisor
        self._d //= common_divisor

    def __str__(self):
        return f"{self._n}/{self._d}" if self._d != 1 else f"{self._n}"


