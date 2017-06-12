# def isPrime(n):
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % 2 == 0:
#             return False
#     return True
#
#
# def primeFactors(n):
#     result = []
#     for i in range(2, n):
#         if (isPrime(i)):
#             cnt = 0
#             while (n % i == 0):
#                 n = n / i
#                 cnt += 1
#             if cnt != 0:
#                 result.append((i, cnt))
#             if n == 1:
#                 break
#     res = []
#     for i, c in result:
#         if c == 1:
#             res.append('({})'.format(i))
#         else:
#             res.append('({}**{})'.format(i, c))
#     return res


def primeFactors2(n):
    ret = ''
    for i in xrange(2, n + 1):
        num = 0
        while (n % i == 0):
            num += 1
            n = n / i
        if num > 0:
            ret += '({}{})'.format(i, '**%d' % num if num > 1 else '')
        if n == 1:
            return ret


if __name__ == '__main__':
    assert primeFactors2(7775460) == "(2**2)(3**3)(5)(7)(11**2)(17)"
    print primeFactors2(23804300590000)
    print primeFactors2(2320940853009300000)
