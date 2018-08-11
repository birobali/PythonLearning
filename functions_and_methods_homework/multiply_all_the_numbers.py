def multiply_all_the_numbers(my_list):
    result = 1
    for number in my_list:
        result *= number

    return result


print(multiply_all_the_numbers([1, 2, 3, 6]))
