def what_is_the_time(time_in_mirror):
    # Your code here
    ints = [int(i) for i in time_in_mirror.split(':')]
    if ints[1] == 0:
        if ints[0] == 12:
            return '12:00'
        else:
            return '%02d:00' % (12 - ints[0])
    else:
        if ints[0] in (11, 12):
            return '%02d:%02d' % (23 - ints[0], 60 - ints[1])
        else:
            return '%02d:%02d' % (11 - ints[0], 60 - ints[1])


def what_is_the_time2(time_in_mirror):
    h, m = map(int, time_in_mirror.split(':'))
    return '{:02}:{:02}'.format(-(h + (m != 0)) % 12 or 12, -m % 60)


if __name__ == '__main__':
    assert what_is_the_time("06:35") == "05:25"
    assert what_is_the_time("12:00") == "12:00"
    assert what_is_the_time("12:02") == "11:58"
    assert what_is_the_time("11:59") == "12:01"
    assert what_is_the_time2("06:35") == "05:25"
    assert what_is_the_time2("12:00") == "12:00"
    assert what_is_the_time2("12:02") == "11:58"
    assert what_is_the_time2("11:59") == "12:01"
