def summation(num):
    sum = 0
    for i in xrange(1, num + 1):
        sum += i
    return sum


def summation2(num):
    return sum(xrange(1, num + 1))


def summation3(num):
    return num * (num + 1) / 2


if __name__ == '__main__':
    assert summation(6) == 21
    assert summation2(6) == 21
    assert summation3(6) == 21
