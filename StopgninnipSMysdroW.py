

import re


def spin_words(sentence):
    # Your code goes here
    strlist = str(sentence).split()
    result = []
    for word in strlist:
        if len(word) >= 5:
            result.append(word[::-1])
        else:
            result.append(word)
    return ' '.join(result)


def spin_words2(sentence):
    return ' '.join([x[::-1] if len(x) >= 5 else x for x in sentence.split(' ')])


def spin_words3(sentence):
    return re.sub(r"\w{5,}", lambda w: w.group(0)[::-1], sentence)


if __name__ == '__main__':
    assert spin_words('Hey fellow warriors') == 'Hey wollef sroirraw'
    assert spin_words2('Hey fellow warriors') == 'Hey wollef sroirraw'
    assert spin_words3('Hey fellow warriors') == 'Hey wollef sroirraw'
