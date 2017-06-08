# timeout
def sum_pairs(ints, s):
    for i in xrange(len(ints)):
        for j in xrange(i):
            if ints[i] + ints[j] == s:
                return [ints[j], ints[i]]


def sum_pairs2(ints, s):
    m = {}
    for i in xrange(len(ints)):
        t = s - ints[i]
        if t in m:
            return [t, ints[i]]
        elif ints[i] not in m:
            m[ints[i]] = i


def sum_pairs3(ints, s):
    seen = set()
    for num in ints:
        if s - num in seen:
            return [s - num, num]
        seen.add(num)


if __name__ == '__main__':
    assert sum_pairs([10, 5, 2, 3, 7, 5], 10) == [3, 7]
    assert sum_pairs2([10, 5, 2, 3, 7, 5], 10) == [3, 7]
    assert sum_pairs3([10, 5, 2, 3, 7, 5], 10) == [3, 7]
