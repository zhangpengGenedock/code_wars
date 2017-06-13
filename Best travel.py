import itertools


def choose_best_sum(t, k, ls):
    try:
        return max(sum(i) for i in itertools.combinations(ls, k) if sum(i) <= t)
    except:
        return None


if __name__ == '__main__':
    assert choose_best_sum(230, 3, [91, 74, 73, 85, 73, 81, 87]) == 228
