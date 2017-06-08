import re


def count_smileys(arr):
    return sum(1 if re.compile('[:;][-~]?[)D]').match(s) else 0 for s in arr)


def count_smileys2(arr):
    return sum(bool(re.match('[:;][-~]?[)D]', s)) for s in arr)


def count_smileys3(arr):
    return len(list(re.findall('[:;][-~]?[)D]', ' '.join(arr))))


if __name__ == '__main__':
    assert count_smileys([':D', ':~)', ';~D', ':)']) == 4
    assert count_smileys2([':D', ':~)', ';~D', ':)']) == 4
    assert count_smileys3([':D', ':~)', ';~D', ':)']) == 4
