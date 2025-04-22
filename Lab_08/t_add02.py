def non_div_seq():
    seq = []
    n = 2
    while True:
        if all(n % prev != 0 for prev in seq):
            seq.append(n)
            yield n
        n += 1


gen = non_div_seq()
for _ in range(30):
    print(next(gen), end=' ')

