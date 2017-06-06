def remove_smallest(numbers):
    if not numbers:
        return []
    min = numbers[0]
    minIndex = 0
    for i in xrange(1, len(numbers)):
        if numbers[i] < min:
            min = numbers[i]
            minIndex = i
    del numbers[minIndex]
    return numbers

def remove_smallest2(numbers):
    if(numbers):
        numbers.remove(min(numbers))
    return numbers


if __name__ == '__main__':
    assert remove_smallest([1, 2, 3, 1, 1]) == [2, 3, 1, 1]
    assert remove_smallest2([1, 2, 3, 1, 1]) == [2, 3, 1, 1]
