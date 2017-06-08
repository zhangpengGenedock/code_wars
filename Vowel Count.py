def getCount(inputStr):
    num_vowels = 0
    # your code here
    for s in inputStr:
        if s in ['a', 'e', 'i', 'o', 'u']:
            num_vowels += 1

    return num_vowels


def getCount2(inputStr):
    return sum(1 for let in inputStr if let in 'aeiou')


def getCount3(inputStr):
    return sum(c in 'aeiou' for c in inputStr)


if __name__ == '__main__':
    assert getCount("abracadabra") == 5
    assert getCount2("abracadabra") == 5
    assert getCount3("abracadabra") == 5
