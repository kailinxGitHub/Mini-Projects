import os
#Question 2

#asking the user how many students are in a class
num_of_students = int(input("Question 2: How many students are there in a class?\n"))

stud_names = []

#main loop for the name input
for i in range(num_of_students):
    current_stu_name = str(input("Enter a student's name: \n"))
    stud_names.append(current_stu_name)

#final output of names
print("The names are:")
print("\n".join(stud_names))

class continuity:
    #transitioning code
    continue_direction = str(input("Clear? (y or n): "))
    if continue_direction == "y":
        os.system("clear")
    elif continue_direction == "n":
        exit()
    else:
        print("Restart the program again")
        exit()