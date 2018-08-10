def print_big(letter):
    patterns = {1: '  *  ', 2: ' * * ', 3: '*   *', 4: '*****', 5: '**** ', 6: '   * ', 7: ' *   ', 8: '*  * ', 9: '*    '}

    alphabet = {'A': [1, 2, 4, 3, 3], 'B': [5, 3, 5, 3, 5]}

    print('')
    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])


print_big('a')
print_big('b')
