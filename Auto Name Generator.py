import random

consonants =  ['b','c','d','f','g','j','k','l','m','n','p','r','s','t','v','w','z','r','s','t','r','s','t']
vowels = ['a', 'e', 'i', 'o', 'u']

first_num = random.randint(3,7)
second_num = random.randint(5, 15)

def first_name_create():
    first_name = ''
    for i in range(first_num):
        if (i % 2) == 0:
            random_consonant = random.choice(consonants)
            first_name += random_consonant
        else:
            random_vowel = random.choice(vowels)
            first_name += random_vowel
    return first_name

def second_name_create():
    second_name = ''
    for i in range(second_num):
        if (i % 2) == 0:
            random_consonant = random.choice(consonants)
            second_name += random_consonant
        else:
            random_vowel = random.choice(vowels)
            second_name += random_vowel
    return second_name

print("Your name is: ", first_name_create(), second_name_create())