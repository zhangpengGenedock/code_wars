import re


def is_pangram(s):
    pattern = re.compile('[a-zA-Z]+')
    s = ''.join([c.lower() for c in s if c.isalpha()])
    return len(set(s)) == 26 and pattern.match(s) is not None


if __name__ == '__main__':
    assert is_pangram('The quick, brown fox jumps over the lazy dog!') == True
