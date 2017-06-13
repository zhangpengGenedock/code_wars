def find_the_ball(start, swaps):
    for a, b in swaps:
        if start == a:
            start = b
        elif start == b:
            start = a
    return start


if __name__ == '__main__':
    assert find_the_ball(0, [(0, 1), (2, 1), (0, 1)]) == 2
