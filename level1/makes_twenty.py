def makes_twenty(a, b):
    return a + b == 20 or a == 20 or b == 20

print(makes_twenty(10, 20))
print(makes_twenty(10, 10))
print(makes_twenty(5, 5))