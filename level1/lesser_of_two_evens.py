def lesser_of_two_evens(first, second):
    if is_even(first) and is_even(second):
        return min(first, second)
    else:
        return max(first, second)

def is_even(number):
    return number % 2 == 0

print(lesser_of_two_evens(2,4))
print(lesser_of_two_evens(2,5))
