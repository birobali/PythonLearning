def squares(n):
    for i in range(1, n):
        yield i ** 2


i = 0
for square in squares(10):
    i += 1
    print(f'Square of {i} is {square}')
