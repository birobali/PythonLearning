def spy_game(nums):
    result = False
    my_spy = [0, 0, 7]

    for number in nums:
        if my_spy[0] == number:
            my_spy.pop(0)

        if not my_spy:
            result = True
            break

    return result


print(spy_game([1, 2, 4, 0, 0, 7, 5]))
print(spy_game([1, 0, 2, 4, 0, 5, 7]))
print(spy_game([1, 7, 2, 0, 4, 5, 0]))
print(spy_game([1, 0, 1, 0, 2, 0, 3, 7]))
