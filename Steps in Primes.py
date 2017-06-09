def is_prime(n):
    if n > 2 and n % 2 == 0:
        return False
    for i in xrange(3, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def step(g, m, n):
    # your code
    for i in xrange(m, n + 1 - g):
        if is_prime(i) and is_prime(i + g):
            return [i, i + g]
    return None


if __name__ == '__main__':
    assert step(2, 100, 110) == [101, 103]
    assert step(4, 100, 110) == [103, 107]
