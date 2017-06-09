def chained(functions):
    def f(x):
        for function in functions:
            x = function(x)
        return x

    return f


def chained2(functions):
    return lambda x: reduce(lambda v, f: f(v), functions, x)


def f1(x): return x * 2


def f2(x): return x + 2


def f3(x): return x ** 2


def f4(x): return x.split()


def f5(xs): return [x[::-1].title() for x in xs]


def f6(xs): return "_".join(xs)


if __name__ == '__main__':
    assert chained([f3, f2, f1])(2) == 12
    assert chained2([f3, f2, f1])(2) == 12
