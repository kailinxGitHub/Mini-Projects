import random

urls = dict()

alphabets = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
alnum = list(alphabets+alphabets.upper()+numbers)

def createShortURL():
    shortURL = ""
    while shortURL == "":
        while len(shortURL) < 6:
            shortURL += random.choice(alnum)
        if shortURL in urls.keys():
            shortURL = ""
    return shortURL

print(createShortURL())