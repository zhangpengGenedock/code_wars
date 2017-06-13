def list_squared(m, n):
    r = []
    for i in range(m, n + 1):
        square = 0
        for k in range(1, i + 1):
            if i % k == 0:
                square += k * k
        sqr = int(square ** 0.5)
        if sqr * sqr == square:
            r.append([i, square])
    return r


CACHE = {}


def squared_cache(number):
    if number not in CACHE:
        divisors = [x for x in range(1, number + 1) if number % x == 0]
        CACHE[number] = sum([x * x for x in divisors])
        return CACHE[number]
    return CACHE[number]


def list_squared2(m, n):
    ret = []
    for num in range(m, n + 1):
        divisor_sum = squared_cache(num)
        if (divisor_sum ** 0.5).is_integer():
            ret.append([num, divisor_sum])
    return ret


if __name__ == '__main__':
    assert list_squared(42, 250) == [[42, 2500], [246, 84100]]
    print list_squared(1, 10000)
    print list_squared2(1, 10000)
