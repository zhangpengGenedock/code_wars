import re


def alphabet_position(text):
    res = []
    for c in text:
        if c.isalpha():
            res.append(ord(c.lower()) - ord('a') + 1)
    return ' '.join(map(str, res))


def alphabet_position2(text):
    return ' '.join(str(ord(c) - ord('a') + 1) for c in text.lower() if c.isalpha())


def alphabet_position3(text):
    return ' '.join([str(ord(c) - ord('a') + 1) for c in re.findall('[a-z]', text.lower())])


if __name__ == '__main__':
    assert "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" == alphabet_position(
        "The sunset sets at twelve o' clock.")
    assert "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" == alphabet_position2(
        "The sunset sets at twelve o' clock.")
    assert "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" == alphabet_position3(
        "The sunset sets at twelve o' clock.")
