def namelist(names):
    # your code here
    if not names:
        return ''
    if len(names) == 1:
        return ''.join(names[0].values())
    return ', '.join([''.join(name.values()) for name in names[:len(names) - 1]]) + " & " + ''.join(
        names[len(names) - 1].values())


def namelist2(names):
    if len(names) > 1:
        return '{} & {}'.format(', '.join(name['name'] for name in names[:-1]), names[-1]['name'])
    elif names:
        return names[0]['name']
    else:
        return ''


def namelist3(names):
    return ", ".join([name['name'] for name in names])[::-1].replace(',', '& ', 1)[::-1]


if __name__ == "__main__":
    assert namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]) == 'Bart, Lisa & Maggie'
    assert namelist2([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]) == 'Bart, Lisa & Maggie'
    assert namelist3([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]) == 'Bart, Lisa & Maggie'
