import re

months_30 = '(04|06|09|11)'
months_31 = '(01|03|05|07|08|10|12)'
months_28 = '02'
days_30 = '(0[1-9]|[1-2][0-9]|30)'
days_31 = '(0[1-9]|[1-2][0-9]|3[01])'
days_28 = '(0[1-9]|[1][0-9]|2[0-8])'
valid_date = re.compile('\[(%s-%s|%s-%s|%s-%s)\]' % (months_30, days_30, months_31, days_31, months_28, days_28))
if __name__ == '__main__':
    assert valid_date.search("[3] [12-04] [09-tenth]") is not None
