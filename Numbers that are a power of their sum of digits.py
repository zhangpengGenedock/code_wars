import math

#
# def power_sumDigTerm(n):
#     cnt, i = 0, 10
#     while cnt < n:
#         i += 1
#         base = sum(map(int, str(i)))
#         if base != 1 and math.log(i, base).is_integer():
#             cnt += 1
#     return i

series = [0]
for a in range(2,99):
    for b in range(2,42):
        c = a**b
        if a==sum(map(int, str(c))):
            series.append(c)
power_sumDigTerm = sorted(series).__getitem__


if __name__ == '__main__':
    # assert power_sumDigTerm(1) == 81
    assert power_sumDigTerm(2) == 512
