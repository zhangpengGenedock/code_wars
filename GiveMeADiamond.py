def diamond(n):
    # Make some diamonds!
    if n < 0 or n % 2 == 0:
        return None
    temp = []
    result = n * '*' + '\n'
    space = 0
    while n >= 2:
        space += 1
        temp.append(' ' * space + (n - 2) * '*' + '\n')
        n -= 2
    return ''.join(reversed(temp)) + result + ''.join(temp)


def diamond2(n):
    if n % 2 == 0 or n < 1: return None
    d = [' ' * i + (n - 2 * i) * '*' + '\n' for i in xrange(n / 2, 0, -1)]
    return ''.join(d) + '*' * n + '\n' + ''.join(d[::-1])


if __name__ == '__main__':
    expected = " *\n"
    expected += "***\n"
    expected += " *\n"
    assert diamond(3) == expected
    assert diamond2(3) == expected
    print diamond(3)
    print diamond(5)
    print diamond(11)
    print diamond(21)
    print diamond2(101)
    print diamond2(111)
