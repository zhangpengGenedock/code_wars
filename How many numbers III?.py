def find_all(sum_dig, digs):
    res = []
    for i in range(10 ** (digs - 1), 10 ** digs):
        digits = map(int, str(i))
        if sorted(digits) == digits and sum(digits) == sum_dig:
            res.append(i)
    return [] if not res else [len(res), res[0], res[-1]]


def find_all2(s, d):
    xs = [x for x in digs(d) if sum(x) == s]
    if not xs:
        return []
    else:
        reduce_int = lambda xs: int(''.join(map(str, xs)))
        min = reduce_int(xs[0])
        max = reduce_int(xs[-1])
        return [len(xs), min, max]


def digs(d, start=1):
    """
    >>> list(digs(3, start=9))
    [[9, 9, 9]]
    >>> list(digs(2, start=8))
    [[8, 8], [8, 9], [9, 9]]
    """
    if d == 1:
        for x in range(start, 10):
            yield [x]
    else:
        for x in range(start, 10):
            for y in digs(d - 1, x):
                yield [x] + y


if __name__ == '__main__':
    # assert find_all(35, 6) == [123, 116999, 566666]
    assert find_all2(35, 6) == [123, 116999, 566666]
