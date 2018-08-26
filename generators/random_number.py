from random import randint


def random_number(low, high, n):
    for i in range(n):
        yield randint(low, high)


for num in random_number(1, 100, 20):
    print(num)
