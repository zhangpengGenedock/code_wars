def multiplication_table(row, col):
    # Good Luck!
    result = [[0 for i in range(col)] for j in range(row)]
    for i in xrange(row):
        for j in xrange(col):
            if i == 0:
                result[i][j] = j + 1
            if j == 0:
                result[i][j] = i + 1
            else:
                result[i][j] = result[i][0] * result[0][j]
    return result


def multiplication_table2(row, col):
    return [[(i + 1) * (j + 1) for j in range(col)] for i in range(row)]


if __name__ == '__main__':
    assert multiplication_table(3, 3) == [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
    assert multiplication_table2(3, 3) == [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
