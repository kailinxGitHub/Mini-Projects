#asks for a word
my_string = str(input("Question 3: Enter a word to find the middle character: \n"))
length_of_str = len(my_string)

#condition
if (length_of_str % 2) == 1:
    mid_char_num = length_of_str // 2
    mid_char = my_string[mid_char_num]
else: 
    mid_char_num = int(length_of_str / 2)
    lower_mid_char_num = mid_char_num - 1
    upper_mid_char_num = mid_char_num + 1
    mid_char = my_string[lower_mid_char_num: upper_mid_char_num]
    
#output
print("Your middle character(s) are:", mid_char)

class continuity:
    #transitioning code
    continue_direction = str(input("Continue? (y or n): "))
    if continue_direction == "y":
        os.system("clear")
    elif continue_direction == "n":
        exit()
    else:
        print("Restart the program again")
        exit()