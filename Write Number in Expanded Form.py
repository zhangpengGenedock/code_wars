def expanded_form(num):
    res = []
    for i in range(len(str(num))):
        v = num % 10 * (10 ** i)
        if v:
            res.append(v)
        num = num / 10
    return ' + '.join(map(str, reversed(res)))


def expanded_form2(num):
    return ' + '.join([str(int(d) * 10 ** p) for p, d in enumerate(str(num)[::-1]) if d != '0'][::-1])


if __name__ == '__main__':
    assert '70000 + 300 + 4' == expanded_form(70304)
    assert expanded_form(12) == '10 + 2'
    assert expanded_form2(12) == '10 + 2'
    assert '70000 + 300 + 4' == expanded_form2(70304)
