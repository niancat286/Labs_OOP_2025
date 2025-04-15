def increasing_digit_sum():
    n = 0
    prev_sum = sum(int(d) for d in str(n))
    yield n
    n += 1
    while True:
        current_sum = sum(int(d) for d in str(n))
        if current_sum > prev_sum:
            yield n
            prev_sum = current_sum
        n += 1


gen = increasing_digit_sum()
for _ in range(30):
    print(next(gen), end=' ')
