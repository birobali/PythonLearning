def is_in_range(num, low, high):
    return num in range(low - 1, high + 1)


print(is_in_range(10, 1, 100))
print(is_in_range(1, 1, 100))
print(is_in_range(100, 1, 100))
print(is_in_range(101, 1, 100))
