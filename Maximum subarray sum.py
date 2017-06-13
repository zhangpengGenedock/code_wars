def maxSequence(arr):
    max = 0
    sum = 0
    for x in arr:
        if sum + x > 0:
            sum += x
            if sum > max:
                max = sum
        else:
            if sum > max:
                max = sum
            sum = 0
    return max


def maxSequence2(arr):
    max, curr = 0, 0
    for x in arr:
        curr += x
        if curr < 0: curr = 0
        if curr > max: max = curr
    return max


if __name__ == '__main__':
    assert maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert maxSequence2([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
