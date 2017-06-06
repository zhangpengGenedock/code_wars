def isValidWalk(walk):
    # determine if walk is valid
    if len(walk) != 10:
        return False
    ns_count = 0
    ew_count = 0
    for d in walk:
        if d == 'n':
            ns_count += 1
        elif d == 's':
            ns_count -= 1
        elif d == 'e':
            ew_count += 1
        elif d == 'w':
            ew_count -= 1
    if ns_count == 0 and ew_count == 0:
        return True
    else:
        return False


def isValidWalk2(walk):
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')


if __name__ == '__main__':
    assert isValidWalk(['n', 's']) == False
    assert isValidWalk2(['n', 's']) == False
