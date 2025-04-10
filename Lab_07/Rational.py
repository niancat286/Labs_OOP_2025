from math import gcd


class RationalError(ZeroDivisionError):
    ZERO_DIVISION = 0

    def __init__(self, err_code, message):
        super().__init__()
        self.err_code = err_code
        self.message = message

    def __str__(self):
        return f'code error {self.err_code} RationalError: {self.message}'


class RationalValueError(ValueError):
    VALUE_ERR = 0

    def __init__(self, err_code, message):
        super().__init__()
        self.err_code = err_code
        self.message = message

    def __str__(self):
        return f'code error {self.err_code} RationalValueError: {self.message}'


class Rational:
    def __init__(self, n, d=None):
        if d is None:
            if isinstance(n, str):
                try:
                    n, d = map(int, n.strip().split('/'))
                except Exception:
                    raise RationalValueError(RationalValueError.VALUE_ERR,
                                             f'Invalid string format for Rational: {n}')
            else:
                d = 1
        if d == 0:
            raise RationalError(RationalError.ZERO_DIVISION, 'zero division!')
        self.n = n
        self.d = d
        self._simplify()

    def _simplify(self):
        g = gcd(self.n, self.d)
        self.n //= g
        self.d //= g
        if self.d < 0:
            self.n *= -1
            self.d *= -1

    def __add__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)

        if isinstance(other, Rational):
            new_n = self.n * other.d + other.n * self.d
            new_d = self.d * other.d
            return Rational(new_n, new_d)

        raise RationalValueError(RationalValueError.VALUE_ERR, 'Not Implemented')

    def __sub__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)

        if isinstance(other, Rational):
            new_n = self.n * other.d - other.n * self.d
            new_d = self.d * other.d
            return Rational(new_n, new_d)

        raise RationalValueError(RationalValueError.VALUE_ERR, 'Not Implemented')

    def __mul__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)

        if isinstance(other, Rational):
            return Rational(self.n * other.n, self.d * other.d)

        raise RationalValueError(RationalValueError.VALUE_ERR, 'Not Implemented')

    def __truediv__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)

        if isinstance(other, Rational):
            if other.n == 0:
                raise RationalError(RationalError.ZERO_DIVISION, 'zero division!')
            return Rational(self.n * other.d, self.d * other.n)

        raise RationalValueError(RationalValueError.VALUE_ERR, 'Not Implemented')

    def __call__(self):
        return self.n / self.d

    def __getitem__(self, key):
        if key == "n":
            return self.n
        elif key == "d":
            return self.d
        else:
            raise KeyError

    def __setitem__(self, key, value):
        if key == "n":
            self.n = value
        elif key == "d":
            if value == 0:
                raise RationalError(RationalError.ZERO_DIVISION, 'zero division!')
            self.d = value
        else:
            raise KeyError

        self._simplify()

    def __str__(self):
        return f"{self.n}/{self.d}" if self.d != 1 else f"{self.n}"


def parse_expression(expr):
    tokens = expr.strip().split()
    if not tokens:
        return None

    def to_rational(token):
        try:
            if '/' in token:
                return Rational(token)
            else:
                return Rational(int(token), 1)
        except Exception as e:
            raise RationalValueError(RationalValueError.VALUE_ERR, f'Invalid token: {token} ({e})')

    values = []
    operators = []

    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token in "+-*/":
            operators.append(token)
        else:
            values.append(to_rational(token))
        i += 1

    i = 0
    while i < len(operators):
        op = operators[i]
        if op in '*/':
            a = values[i]
            b = values[i + 1]
            try:
                if op == '*':
                    res = a * b
                else:
                    res = a / b
            except RationalValueError as e:
                raise e
            values[i] = res
            del values[i + 1]
            del operators[i]
        else:
            i += 1

    result = values[0]
    for i, op in enumerate(operators):
        try:
            if op == '+':
                result += values[i + 1]
            elif op == '-':
                result -= values[i + 1]
        except RationalValueError as e:
            raise e

    return result


if __name__ == '__main__':
    test_input = [
        "3/4 + 5/6",
        "1/2 + abc",
        "1/2 + '3/4'",
        "1/2 + [1,2]",
        "1/2 + 3/0",
    ]

    for line in test_input:
        try:
            res = parse_expression(line)
            print(f"Результат: {res} = {res():.3f}")
        except RationalValueError as e:
            print(f"RationalValueError у рядку: {line.strip()} -> {e}")
        except RationalError as e:
            print(f"RationalError у рядку: {line.strip()} -> {e}")

