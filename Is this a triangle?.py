def is_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    return a + b > c and a + c > b and b + c > a


def is_triangle2(a, b, c):
    return a < b + c and b < a + c and c < a + b


if __name__ == "__main__":
    assert is_triangle(1, 2, 2) == True
    assert is_triangle(7, 2, 2) == False
    assert is_triangle2(1, 2, 2) == True
    assert is_triangle2(7, 2, 2) == False
