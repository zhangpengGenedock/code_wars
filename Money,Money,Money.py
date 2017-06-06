from math import ceil, log


def calculate_years(principal, interest, tax, desired):
    year = 0
    while principal < desired:
        principal = principal + principal * interest * (1 - tax)
        year += 1
    return year


def calculate_years2(principal, interest, tax, desired):
    return ceil(log(float(desired) / principal, 1 + interest * (1 - tax)))


if __name__ == '__main__':
    assert calculate_years(1000, 0.05, 0.18, 1100) == 3
    assert calculate_years(1000, 0.01625, 0.18, 1200) == 14
    assert calculate_years2(1000, 0.05, 0.18, 1100) == 3
    assert calculate_years2(1000, 0.01625, 0.18, 1200) == 14
