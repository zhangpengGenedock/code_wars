from math import pi


def iter_pi(epsilon):
    a = 0
    # your code
    i = 0
    while abs(pi - a * 4) > epsilon:
        a += ((-1) ** i) * (1.0 / (2 * i + 1))
        i = i + 1
    return [i, round(a * 4, 10)]


def iter_pi2(epsilon):
    n = 1
    approxy = 4
    while abs(approxy - pi) > epsilon:
        n += 1
        approxy += (-4, 4)[n % 2] / (2 * n - 1.0)
    return [n, round(approxy, 10)]


if __name__ == '__main__':
    result = iter_pi(0.1)
    assert result == [10, 3.0418396189]
    assert iter_pi2(0.1) == [10, 3.0418396189]
    print iter_pi2(0.0000001)
