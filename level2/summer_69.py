def summer_69(arr):
    result = 0
    ignore = False

    for number in arr:
        if number == 6:
            ignore = True
        elif ignore and number == 9:
            ignore = False
        elif not ignore:
            result += number

    return result


print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([4, 5, 6, 7, 8, 9, 2, 1]))
print(summer_69([4, 5, 6, 7, 8, 9, 6, 1]))
print(summer_69([4, 5, 6, 7, 8, 9, 6, 1, 9, 1]))
print(summer_69([2, 1, 6, 9, 11]))
