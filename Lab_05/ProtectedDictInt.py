class ProtectedDictInt:
    def __init__(self):
        self.__dict = {}

    def __setitem__(self, key, value):
        if not isinstance(key, int):
            raise KeyError
        if key in self.__dict:
            raise PermissionError
        self.__dict[key] = value

    def __getitem__(self, item):
        if item not in self.__dict:
            raise KeyError
        return self.__dict[item]

    def __add__(self, other):
        result = ProtectedDictInt()
        for key, value in self.__dict.items():
            result[key] = value

        if isinstance(other, ProtectedDictInt):
            for key, value in other.__dict.items():
                result[key] = value

        elif isinstance(other, tuple) and len(other) == 2:
            result[other[0]] = other[1]
        else:
            raise ValueError
        return result

    def __sub__(self, other):
        if not isinstance(other, int):
            raise TypeError
        if other not in self.__dict:
            raise KeyError
        new_dict = ProtectedDictInt()
        for key, value in self.__dict.items():
            if key != other:
                new_dict.__dict[key] = value
        return new_dict

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError
        if key not in self.__dict:
            raise KeyError
        del self.__dict[key]

    def __len__(self):
        return len(self.__dict)

    def __contains__(self, item):
        return item in self.__dict

    def __call__(self):
        return sum(self.__dict.keys())

    def __str__(self):
        return str(self.__dict)


if __name__ == '__main__':
    d = ProtectedDictInt()
    d[1] = 2
    print(d[1])