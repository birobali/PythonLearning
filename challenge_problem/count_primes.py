def count_primes(nums):

    if nums <= 2:
        return 0

    primes = [2]

    for i in range(3, nums, 2):
        if is_prime(i, primes):
            primes.append(i)

    return len(primes)


def is_prime(num, primes):
    is_prime = False

    for i in primes:
        if num % i == 0:
            num + 2
            break
    else:
        is_prime = True

    return is_prime


print(count_primes(1))
print(count_primes(3))
print(count_primes(100))
