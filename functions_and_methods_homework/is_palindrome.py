def is_palindrome(text):
    return text.lower() == ''.join(reversed(text.lower()))

print(is_palindrome('Mom'))
print(is_palindrome('Dad'))
print(is_palindrome('Grandma'))
