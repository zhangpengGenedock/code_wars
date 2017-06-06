def high_and_low(numbers):
    nums = [int(x) for x in numbers.split()]
    return ' '.join((str(max(nums)), str(min(nums))))


def high_and_low2(numbers):
    return " ".join(x(numbers.split(), key=int) for x in (max, min))


def high_and_low3(numbers):
    n = map(int, numbers.split())
    return "%i %i" % (max(n), min(n))

    if __name__ == '__main__':
        assert high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6") == "542 -214"
        assert high_and_low2("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6") == "542 -214"
        assert high_and_low3("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6") == "542 -214"
