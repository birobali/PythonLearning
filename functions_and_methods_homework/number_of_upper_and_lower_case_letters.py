def number_of_upper_and_lower_case_letters(text):
    only_letters = ''.join(filter(str.isalpha, text))
    print('Number of uppers: ' + str(len(''.join(filter(str.isupper, only_letters)))))
    print('Number of lowers: ' + str(len(''.join(filter(str.islower, only_letters)))))

number_of_upper_and_lower_case_letters('Hello Mr. Rogers, how are you this fin Tuesday?')