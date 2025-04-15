def gen(x, N):
    S = 1 # поверення 1-го члена
    yield S

    for n in range(1, N + 1):
        S *= x / n
        yield S # поверення n-го члена


for el in gen(1, 10):
    print(el)