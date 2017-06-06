import operator


def find_it(seq):
    seq_unique = set(seq)
    for x in seq_unique:
        if seq.count(x) % 2 == 1:
            return x


def find_it2(seq):
    return reduce(operator.xor, seq)


if __name__ == '__main__':
    assert find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]) == 5
    assert find_it2([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]) == 5
