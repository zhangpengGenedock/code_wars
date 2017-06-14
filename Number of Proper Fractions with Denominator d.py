from fractions import gcd


def proper_fractions(n):
    if n == 1: return 0
    cnt = 1
    for i in range(2, n):
        if gcd(i, n) == 1:
            cnt += 1
    return cnt


if __name__ == '__main__':
    assert proper_fractions(15) == 8
