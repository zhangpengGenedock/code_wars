def prefill(n=0, v=None):
    try:
        return int(n) * [v]
    except:
        raise TypeError(str(n) + ' is invalid')


if __name__ == '__main__':
    assert prefill(2, 'abc') == ['abc', 'abc']
