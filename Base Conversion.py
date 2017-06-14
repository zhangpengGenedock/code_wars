def convert(input, source, target):
    base_in = len(source)
    base_out = len(target)
    acc = 0
    out = ''
    for d in input:
        acc *= base_in
        acc += source.index(d)
    while acc != 0:
        d = target[acc % base_out]
        acc = acc / base_out
        out = d + out
    return out if out else target[0]


