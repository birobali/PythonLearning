def master_yoda(text):
    word_list = text.split()
    return ' '.join(word_list[::-1]).capitalize()


print(master_yoda("I am home"))
