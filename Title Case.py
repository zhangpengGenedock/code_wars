def title_case(title, minor_words=None):
    if not title:
        return title
    splited = title.split(' ')
    if len(splited) == 1:
        return splited[0].capitalize()
    return ' '.join([splited[0].capitalize(), ' '.join(
        s.capitalize() if (not minor_words or s.lower() not in minor_words.lower().split()) else s.lower() for s in
        splited[1::])])


def title_case2(title, minor_words=''):
    title = title.capitalize().split()
    minor_words = minor_words.lower().split()
    return ' '.join([word if word in minor_words else word.capitalize() for word in title])


def title_case3(title, minor_words=''):
    return ' '.join(
        w if w in minor_words.lower().split() and i else w.capitalize() for i, w in enumerate(title.lower().split()))


if __name__ == '__main__':
    assert 'The Wind in the Willows' == title_case('THE WIND IN THE WILLOWS', 'The In')
    assert 'The Wind in the Willows' == title_case2('THE WIND IN THE WILLOWS', 'The In')
    assert 'The Wind in the Willows' == title_case3('THE WIND IN THE WILLOWS', 'The In')
