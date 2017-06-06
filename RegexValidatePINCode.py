import re


def validate_pin(pin):
    # return true or false
    if len(pin) != 4 and len(pin) != 6:
        return False
    for c in pin:
        if not c.isdigit():
            return False
    return True


def validate_pin2(pin):
    # return true or false
    return len(pin) in (4, 6) and pin.isdigit()


def validate_pin3(pin):
    # return true or false
    return bool(re.match(r'^(\d{4}|\d{6})$', pin))


if __name__ == '__main__':
    assert validate_pin('1123') == True
    assert validate_pin('1a123') == False
    assert validate_pin2('1123') == True
    assert validate_pin2('1a123') == False
    assert validate_pin3('1123') == True
    assert validate_pin3('1a123') == False
