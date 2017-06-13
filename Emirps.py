def is_prime(n):
    for i in range(2, int(n ** 0.5 + 1)):
        if n % i == 0:
            return False
    return True


def find_emirp(n):
    res = []
    for i in range(2, n):
        # rev = int(''.join(reversed(str(i))))
        rev = int(str(i)[::-1])
        if i != rev and is_prime(i) and is_prime(rev):
            res.append(i)
    return [0, 0, 0] if not res else [len(res), res[-1], sum(res)]


if __name__ == '__main__':
    assert find_emirp(50) == [4, 37, 98]
