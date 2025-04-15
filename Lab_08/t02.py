def gen(N):
    S = 1 # поверення 1-го члена
    yield S

    for n in range(2, N + 1):
        S += 1 / n
        yield S # поверення n-го члена


for el in gen(10):
    print(el)