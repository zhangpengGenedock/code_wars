def longest(s1, s2):
    # your code
    return ''.join(sorted(set(s1 + s2)))


if __name__ == '__main__':
    assert longest("aretheyhere", "yestheyarehere") == "aehrsty"
