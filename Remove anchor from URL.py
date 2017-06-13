def remove_url_anchor(url):
    return url.split('#')[0]


def remove_url_anchor2(url):
    import re
    return re.sub('#.*$', '', url)


