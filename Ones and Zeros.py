def binary_array_to_number(arr):
    # your code
    result = 0
    for i in xrange(len(arr)):
        result += 2 ** i * arr[::-1][i]
    return result


def binary_array_to_number2(arr):
    return int(''.join(map(str, arr)), 2)


def binary_array_to_number3(arr):
    return reduce(lambda t, b: t * 2 + b, arr)


if __name__ == '__main__':
    assert binary_array_to_number([1, 1, 1, 1]) == 15
    assert binary_array_to_number2([1, 1, 1, 1]) == 15
    assert binary_array_to_number3([1, 1, 1, 1]) == 15
