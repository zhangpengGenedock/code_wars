def opposite(number):
    return -number


#fastest solution returned 94ms with parens around multiplication 87ms without for results
    # return number - number * 2

#middle solution returned 109ms time period for result
#    return number * -1
#slowest solution returned 150ms time period for result
#    return -number

if  __name__ == '__main__':
    assert opposite(3) == -3
