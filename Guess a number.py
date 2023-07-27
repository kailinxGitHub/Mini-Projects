import random
import os

random_num = random.randint(0, 100)

while True:
    guessed_num = float(input("Guess a num: \n"))
    if random_num == guessed_num:
        print("Right on!")
        play_on = int(input("1. Play on, 2. Stop \n"))
        if play_on == 1:
            os.system("clear")
            random_num = random.randint(0, 100)
            continue
        else:
            break
    elif random_num < guessed_num:
        print("Too big")
        continue
    elif random_num > guessed_num:
        print("Too small")
        continue