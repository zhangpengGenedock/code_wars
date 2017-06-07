def sort_array(source_array):
    # Return a sorted array.
    v = []
    index = []
    for i in range(len(source_array)):
        if source_array[i] % 2 != 0:
            index.append(i)
            v.append(source_array[i])
    v = sorted(v)
    for i in range(len(index)):
        source_array[index[i]] = v[i]
    return source_array


def sort_array2(source_array):
    odds = sorted((x for x in source_array if x % 2 != 0), reverse=True)
    return [x if x % 2 == 0 else odds.pop() for x in source_array]


if __name__ == '__main__':
    assert sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]
    assert sort_array2([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]
