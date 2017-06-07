def series_sum(n):
    # Happy Coding ^_^
    result = 0
    for i in range(n):
        result += 1.0 / (1 + i * 3)
    return '%.2f' % result


def series_sum2(n):
    return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))


if __name__ == '__main__':
    assert series_sum(3) == '1.39'
    assert series_sum(2) == '1.25'
    assert series_sum(1) == '1.00'
    assert series_sum2(3) == '1.39'
    assert series_sum2(2) == '1.25'
    assert series_sum2(1) == '1.00'
