def decrypt(encrypted_text, n):
    if not encrypted_text or n <= 0:
        return encrypted_text

    while n > 0:
        temp = ''
        for i in xrange(len(encrypted_text) / 2):
            temp += encrypted_text[i + len(encrypted_text) / 2]
            temp += encrypted_text[i]
        if len(encrypted_text) % 2 != 0:
            temp += encrypted_text[-1]
        n -= 1
        encrypted_text = temp
    return encrypted_text


def encrypt(text, n):
    if not text or n <= 0:
        return text
    while n > 0:
        text = text[1::2] + text[0::2]
        n -= 1
    return text


def decrypt2(encrypted_text, n):
    if not encrypted_text or n <= 0:
        return encrypted_text
    o, l = len(encrypted_text) // 2, list(encrypted_text)
    for _ in range(n):
        l[1::2], l[0::2] = l[:o], l[o:]
    return ''.join(l)


def encrypt2(text, n):
    if not text or n <= 0:
        return text
    for _ in range(n):
        text = text[1::2] + text[0::2]
    return text


if __name__ == '__main__':
    assert encrypt('This is a test!', 3) == ' Tah itse sits!'
    assert encrypt("This is a test!", 4) == 'This is a test!'
    assert encrypt2('This is a test!', 3) == ' Tah itse sits!'
    assert encrypt2("This is a test!", 4) == 'This is a test!'
    assert decrypt("hsi  etTi sats!", 1) == 'This is a test!'
    assert decrypt2("hsi  etTi sats!", 1) == 'This is a test!'
