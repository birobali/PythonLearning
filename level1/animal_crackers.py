def animal_crackers(text):
    words = str(text).lower().split()
    return words[0][0] == words[1][0]


print(animal_crackers("Levelheaded lama"))
print(animal_crackers("Crazy Kangaroo"))
