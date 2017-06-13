PRIME_CACHE = {}


def is_prime(n):
    if n not in PRIME_CACHE:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                PRIME_CACHE[n] = False
                return PRIME_CACHE[n]
        PRIME_CACHE[n] = True
        return PRIME_CACHE[n]
    return PRIME_CACHE[n]


def gap(g, m, n):
    for i in range(m, n + 1 - g):
        if is_prime(i) and is_prime(i + g):
            middle = True
            for j in range(i + 1, i + g):
                if is_prime(j):
                    middle = False
                    break
            if middle:
                return [i, i + g]
    return None


def gap2(g, m, n):
    previous_prime = n
    for i in range(m, n + 1):
        if is_prime(i):
            if i - previous_prime == g:
                return [previous_prime, i]
            previous_prime = i
    return None


if __name__ == '__main__':
    assert gap(2, 100, 110) == [101, 103]
    assert gap2(2, 100, 110) == [101, 103]
