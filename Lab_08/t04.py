def gen(N):
    a0 = 1 # поверення 1-го члена
    P = a0 / 1
    yield P

    a1 = 1
    P *= a1 / 3
    yield P

    a2 = 3
    P *= a2 / 3**2
    yield P

    for n in range(3, N + 1):
        ak = a0 + a1 / (2 ** a2)
        a0 = a1
        a1 = a2
        a2 = ak

        P *= ak / (3 ** n)

        yield P # поверення n-го члена


for el in gen(4):
    print(el)