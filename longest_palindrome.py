def longest_palindrome(s):
    longest = 0
    for left in xrange(len(s)):
        for right in xrange(len(s), left, -1):
            if s[left:right] == s[left:right][::-1]:
                longest = max(right - left, longest)
                break
    return longest


def longest_palindrome2(s):
    for c in xrange(len(s), -1, -1):
        for i in xrange(len(s) - c + 1):
            if s[i:i + c] == s[i:i + c][::-1]:
                return c


if __name__ == '__main__':
    assert longest_palindrome('baablkj12345432133d') == 9
    assert longest_palindrome2('baablkj12345432133d') == 9
