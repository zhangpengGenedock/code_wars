def domain_name(url):
    return url.split('//')[-1].split('www.')[-1].split('.')[0]


def domain_name2(url):
    import re
    return re.search('(https?://(www\d?\.)?(?P<name>[\w-]+)\.)', url).group('name')


if __name__ == '__main__':
    assert domain_name('http://github.com/carbonfive/raygun') == 'github'
    assert domain_name('http://www.zombie-bites.com') == 'zombie-bites'
    assert domain_name2('http://github.com/carbonfive/raygun') == 'github'
    assert domain_name2('http://www.zombie-bites.com') == 'zombie-bites'
