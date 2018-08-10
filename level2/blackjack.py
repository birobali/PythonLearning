def blackjack(*args):
    sum_of_args = sum(args)
    result = 'BUST'

    if sum_of_args <= 21:
        result = sum_of_args
    elif 11 in args:
        result = sum_of_args - 10

    return result



print(blackjack(5, 6, 7))
print(blackjack(9, 9, 9))
print(blackjack (9, 9, 11))
