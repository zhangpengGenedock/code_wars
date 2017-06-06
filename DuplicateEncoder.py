def duplicate_encode(word):
    # your code here
    word = word.lower()
    return ''.join('(' if word.count(c) == 1 else ')' for c in word)


if __name__ == "__main__":
    assert duplicate_encode("din") == "((("
