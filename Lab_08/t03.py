def gen(N):
    D1 = 5 # поверення 1-го члена
    yield D1

    D2 = 19
    yield D2

    for n in range(3, N + 1):
        D = 5 * D1 - 6 * D2
        D1 = D2
        D2 = D
        yield D # поверення n-го члена


for el in gen(10):
    print(el)