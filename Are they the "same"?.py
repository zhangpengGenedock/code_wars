def comp(array1, array2):
    return None not in (array1,array2) and [i*i for i in sorted(array1)] == sorted(array2)


if __name__ == '__main__':
    a1 = [121, 144, 19, 161, 19, 144, 19, 11]
    a2 = [11 * 11, 121 * 121, 144 * 144, 19 * 19, 161 * 161, 19 * 19, 144 * 144, 19 * 19]
    assert comp(a1, a2) == True
