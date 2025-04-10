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


class RationalListTypeError(TypeError):
    TYPE_ERR = 0

    def __init__(self, err_code, message):
        super().__init__()
        self.err_code = err_code
        self.message = message

    def __str__(self):
        return f'code error {self.err_code} RationalListTypeError: {self.message}'


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

        raise RationalListTypeError(RationalListTypeError.TYPE_ERR, 'Not Implemented')

    def __sub__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)

        if isinstance(other, Rational):
            new_n = self.n * other.d - other.n * self.d
            new_d = self.d * other.d
            return Rational(new_n, new_d)

        raise RationalListTypeError(RationalListTypeError.TYPE_ERR, 'Not Implemented')

    def __mul__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)

        if isinstance(other, Rational):
            return Rational(self.n * other.n, self.d * other.d)

        raise RationalListTypeError(RationalListTypeError.TYPE_ERR, 'Not Implemented')

    def __truediv__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)

        if isinstance(other, Rational):
            if other.n == 0:
                raise RationalError(RationalError.ZERO_DIVISION, 'zero division!')
            return Rational(self.n * other.d, self.d * other.n)

        raise RationalListTypeError(RationalListTypeError.TYPE_ERR, 'Not Implemented')

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


class RationalList:
    def __init__(self, iterable=None):
        self._data = []
        if iterable:
            for item in iterable:
                self.append(item)

    def append(self, value):
        if isinstance(value, Rational):
            self._data.append(value)
        elif isinstance(value, int):
            self._data.append(Rational(value))
        else:
            raise RationalListTypeError(RationalListTypeError.TYPE_ERR, 'not rational or int')

    def __getitem__(self, index):
        return self._data[index]

    def __setitem__(self, index, value):
        if isinstance(value, Rational):
            self._data[index] = value
        elif isinstance(value, int):
            self._data[index] = Rational(value)
        else:
            raise RationalListTypeError(RationalListTypeError.TYPE_ERR, 'not rational or int')

    def __len__(self):
        return len(self._data)

    def __add__(self, other):
        result = RationalList(self._data)
        if isinstance(other, RationalList):
            for el in other:
                result.append(el)
        elif isinstance(other, (Rational, int)):
            result.append(other)
        else:
            raise RationalListTypeError(RationalListTypeError.TYPE_ERR, 'not rational list or rational or int')
        return result

    def __iadd__(self, other):
        if isinstance(other, RationalList):
            for el in other:
                self.append(el)
        elif isinstance(other, (Rational, int)):
            self.append(other)
        else:
            raise RationalListTypeError(RationalListTypeError.TYPE_ERR, 'not rational list or rational or int')
        return self

    def sum(self):
        result = Rational(0)
        for r in self._data:
            result += r
        return result


def read_rational_list_from_file(filename):
    with open(filename, 'r') as f:
        for idx, line in enumerate(f, 1):
            rlist = RationalList()
            tokens = line.strip().split()
            try:
                for token in tokens:
                    try:
                        if '/' in token:
                            rlist += Rational(token)
                        else:
                            rlist += int(token)
                    except (ValueError, RationalValueError) as e:
                        raise RationalListTypeError(RationalListTypeError.TYPE_ERR,
                                                     f"Invalid token '{token}' in line {idx}")
                print(f"Рядок {idx}: сума = {rlist.sum()}")
            except RationalListTypeError as e:
                print(f"Помилка у рядку {idx}: {e}")


if __name__ == '__main__':
    read_rational_list_from_file("input01_1.txt")
