def max_min(numbers: list):
    """Returns the max and min numbers from a list without using max() or min()"""
    max_num = min_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
    return [max_num, min_num]
