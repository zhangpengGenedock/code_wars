def likes(names):
    if not names:
        return 'no one likes this'
    elif len(names) == 1:
        return '{} likes this'.format(names[0])
    elif len(names) == 2:
        return '{} and {} like this'.format(names[0], names[1])
    elif len(names) == 3:
        return '{}, {} and {} like this'.format(names[0], names[1], names[2])
    elif len(names) >= 4:
        return '{}, {} and {} others like this'.format(names[0], names[1], len(names) - 2)


def likes2(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this',
        2: '{} and {} like this',
        3: '{}, {} and {} like this',
        4: '{}, {} and {others} others like this',
    }[min(4, n)].format(*names[:3], others=n - 2)


if __name__ == '__main__':
    assert likes(['Alex', 'Jacob', 'Mark', 'Max']) == 'Alex, Jacob and 2 others like this'
    assert likes(['Jacob', 'Alex']) == 'Jacob and Alex like this'
    assert likes2(['Alex', 'Jacob', 'Mark', 'Max']) == 'Alex, Jacob and 2 others like this'
    assert likes2(['Jacob', 'Alex']) == 'Jacob and Alex like this'
