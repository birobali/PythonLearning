import string

def is_pangram(text, alphabet = string.ascii_lowercase):
    lower_case_letters = ''.join(filter(str.islower, text))
    return alphabet == ''.join(sorted(set(lower_case_letters)))

print(is_pangram('The quick brown fox jumps over the lazy dog!'))
print(is_pangram('The quick blue fox jumps over the lazy dog'))