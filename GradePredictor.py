import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'
    UNDERLINE = '\033[4m'
    CEND      = '\33[0m'

    CBOLD     = '\33[1m'
    CITALIC   = '\33[3m'
    CURL      = '\33[4m'
    CBLINK    = '\33[5m'
    CBLINK2   = '\33[6m'
    CSELECTED = '\33[7m'

    CBLACK  = '\33[30m'
    CRED    = '\33[31m'
    CGREEN  = '\33[32m'
    CYELLOW = '\33[33m'
    CBLUE   = '\33[34m'
    CVIOLET = '\33[35m'
    CBEIGE  = '\33[36m'
    CWHITE  = '\33[37m'

    CBLACKBG  = '\33[40m'
    CREDBG    = '\33[41m'
    CGREENBG  = '\33[42m'
    CYELLOWBG = '\33[43m'
    CBLUEBG   = '\33[44m'
    CVIOLETBG = '\33[45m'
    CBEIGEBG  = '\33[46m'
    CWHITEBG  = '\33[47m'

    CGREY    = '\33[90m'
    CRED2    = '\33[91m'
    CGREEN2  = '\33[92m'
    CYELLOW2 = '\33[93m'
    CBLUE2   = '\33[94m'
    CVIOLET2 = '\33[95m'
    CBEIGE2  = '\33[96m'
    CWHITE2  = '\33[97m'

    CGREYBG    = '\33[100m'
    CREDBG2    = '\33[101m'
    CGREENBG2  = '\33[102m'
    CYELLOWBG2 = '\33[103m'
    CBLUEBG2   = '\33[104m'
    CVIOLETBG2 = '\33[105m'
    CBEIGEBG2  = '\33[106m'
    CWHITEBG2  = '\33[107m'

def print_menu():
    print(25 * f"{bcolors.HEADER}-", "Main MENU", 25 * "-")
    print("1. Start Survey")
    print("2. Saved Results")
    print("3. Helper & Info")    
    print("4. Exit")
    print(61 * "-")

def startSurvey():

    text_file = open("GradePredicted.txt", "w")
    text_file.write("Thank you for using the MYP5 Grade Predictor!\n\nHere are your answers:\n")
    text_file.close

    score = 4
    
    #Question 1
    q1 = int(input("Question 1: Is this a humanities or a STEM class? (type '1' = Humanities or '2' = STEM): "))
    converted_q1 = f'{q1}'
    text_file.write("Question 1: Is this a humanities or a STEM class? (type '1' = Humanities or '2' = STEM): ")
    text_file.write(converted_q1)

    if q1 == 1:
        q2 = int(input("Question 2: Rate your skill in remember names, locations, etc. (range '1' = negative TO '4' = positive): "))
        converted_q2 = f'{q2}'
        text_file.write("\nQuestion 2: Rate your skill in remember names, locations, etc. (range '1' = negative TO '4' = positive): ")
        text_file.write(converted_q2)
    elif q1 == 2:
        q2 = int(input("Question 2: How  would you rate your skill of logical thinking? (range '1' = negative TO '4' = positive): "))
        converted_q2 = f'{q2}'
        text_file.write("\nQuestion 2: How  would you rate your skill of logical thinking? (range '1' = negative TO '4' = positive): ")
        text_file.write(converted_q2)
    score += 8

    #Question 2
    if q2 == 1:
        score +=2
    elif q2 == 2:
        score +=4
    elif q2 == 3:
        score +=6
    elif q2 == 4:
        score +=8
    else:
        return

    #Question 3
    q3 = int(input("Question 3: How much do you like the class? (range '1' = negative TO '4' = positive): "))
    converted_q3 = f'{q3}'
    text_file.write("\nQuestion 3: How much do you like the class? (range '1' = negative TO '4' = positive): ")
    text_file.write(converted_q3)
    if q3 == 1:
        score +=2
    elif q3 == 2:
        score +=4
    elif q3 == 3:
        score +=6
    elif q3 == 4:
        score +=8
    else:
        return

    #Question 4
    q4 = int(input("Question 4: Do you feel confident with this test? (range '1' = negative TO '4' = positive): "))
    converted_q4 = f'{q4}'
    text_file.write("\nQuestion 4: Do you feel confident with this test? (range '1' = negative TO '4' = positive): ")
    text_file.write(converted_q4)
    if q4 == 1:
        score +=2
    elif q4 == 2:
        score +=4
    elif q4 == 3:
        score +=6
    elif q4 == 4:
        score +=8
    else:
        return

    #Question 5
    q5 = int(input("Question 5: Does this class interest you? (type '1' = No or '2' = Yes): "))
    converted_q5 = f'{q5}'
    text_file.write("\nQuestion 5: Does this class interest you? (type '1' = No or '2' = Yes): ")
    text_file.write(converted_q5)
    if q5 == 1:
        score +=4
    elif q5 == 2:
        score +=8
    else:
        return

    #Question 6
    if q5 == 1:
        q6 = int(input("Question 6: How much time do you think you spend studying? (range '1' = a lot TO '4' = not a lot): "))
        converted_q6 = f'{q6}'
        text_file.write("\nQuestion 6: How much time do you think you spend studying? (range '1' = a lot TO '4' = not a lot): ")
        text_file.write(converted_q6)
    elif q5 == 2:
        q6 = int(input("Question 6: Do you have any motivation when you study? (range '1' = negative TO '4' = positive): "))
        converted_q6 = f'{q6}'
        text_file.write("\nQuestion 6: Do you have any motivation when you study? (range '1' = negative TO '4' = positive): ")
        text_file.write(converted_q6)

    if q6 == 1:
        score +=2
    elif q6 == 2:
        score +=4
    elif q6 == 3:
        score +=6
    elif q6 == 4:
        score +=8
    else:
        return
    
    #Question 7
    q7 = int(input("Question 7: Rate tthe easiness of the day you test is on. (range '1' = negative TO '4' = positive): "))
    converted_q7 = f'{q7}'
    text_file.write("\nQuestion 7: Rate tthe easiness of the day you test is on. (range '1' = negative TO '4' = positive): ")
    text_file.write(converted_q7)

    if q7 == 1:
        score +=2
    elif q7 == 2:
        score +=4
    elif q7 == 3:
        score +=6
    elif q7 == 4:
        score +=8
    else:
        return

    #Question 8
    if q7 == 1 or q7 == 2:
        q8 = int(input("Question 8: If applicable, what's your condition on the day of test. (range '1' = bad TO '4' = good): "))
        converted_q8 = f'{q8}'
        text_file.write("\nQuestion 8: If applicable, what's your condition on the day of test. (range '1' = bad TO '4' = good): ")
        text_file.write(converted_q8)
    elif q7 == 3 or q7 == 4:
        q8 = int(input("Question 8: Does this test consist of something uncertain to you? (range '1' = negative TO '4' = positive): "))
        converted_q8 = f'{q8}'
        text_file.write("\nQuestion 8: Does this test consist of something uncertain to you? (range '1' = negative TO '4' = positive): ")
        text_file.write(converted_q8)
    
    if q8 == 1:
        score +=2
    elif q8 == 2:
        score +=4
    elif q8 == 3:
        score +=6
    elif q8 == 4:
        score +=8
    else:
        return
    
    #Question 9
    q9 = int(input("Question 9: Does this test touch on something you like? (range '1' = negative TO '4' = positive): "))
    converted_q9 = f'{q9}'
    text_file.write("\nQuestion 9: Does this test touch on something you like? (range '1' = negative TO '4' = positive): ")
    text_file.write(converted_q9)
    if q9 == 1:
        score +=2
    elif q9 == 2:
        score +=4
    elif q9 == 3:
        score +=6
    elif q9 == 4:
        score +=8
    else:
        return

    #Question 10
    q10 = int(input("Question 10: How well do you think you are prepared for the test? (range '1' = negative TO '4' = positive): "))
    converted_q10 = f'{q10}'
    text_file.write("\nQuestion 10: How well do you think you are prepared for the test? (range '1' = negative TO '4' = positive): ")
    text_file.write(converted_q10)
    if q10 == 1:
        score +=2
    elif q10 == 2:
        score +=4
    elif q10 == 3:
        score +=6
    elif q10 == 4:
        score +=8
    else:
        return

    #Question 11
    if q10 == 1 or 2:
        q11 = int(input("Question 11: Do you feel worried about the test? (range '1' = a lot TO '4' = not a lot): "))
        converted_q11 = f'{q11}'
        text_file.write("\nQuestion 11: Do you feel worried about the test? (range '1' = a lot TO '4' = not a lot): ")
        text_file.write(converted_q11)
    elif q10 == 3 or 4:
        q11 = int(input("Question 11: How confident are you about the test? (range '1' = negative TO '4' = positive): "))
        converted_q11 = f'{q11}'
        text_file.write("\nQuestion 11: How confident are you about the test? (range '1' = negative TO '4' = positive): ")
        text_file.write(converted_q11)

    if q11 == 1:
        score +=2
    elif q11 == 2:
        score +=4
    elif q11 == 3:
        score +=6
    elif q11 == 4:
        score +=8
    else:
        return

    #Question 12
    q12 = int(input("Question 12: How are you? (range '1' = negative TO '4' = positive): "))
    converted_q12 = f'{q12}'
    text_file.write("\nQuestion 12: How are you? (range '1' = negative TO '4' = positive): ")
    text_file.write(converted_q12)

    if q12 == 1:
        score +=2
    elif q12 == 2:
        score +=4
    elif q12 == 3:
        score +=6
    elif q12 == 4:
        score +=8
    else:
        return

    #Print Score
    score_text = print("Your final score out of 100 is: ", score, "The full result has been saved to the same folder!")

    converted_score = f'{score}'

    #Convert Tuple into String for saving to file
    def convertTuple(tup): 
        str =  ''.join(tup) 
        return str

    score_text = "\n\nYour final score out of 100 is: ", converted_score

    score_text_printable = convertTuple(score_text)

    text_file.write(score_text_printable)

    #Comment
    if score <= 50:
        comment_under50 = "\nYou really aren't feeling too well about the test, I recommend you talking to your counselor about the test. You supposedly shouldn't take the test."
        grade_predicted_under50 = "\nYou will most likely not do too well on this test, as you are not in your best condition."
        quote_under50 = "\nHere's a motivational quote for you: \n"
        motivational_quote_under50 = "Nothing is impossible. The word itself says ‘I’m Possible - Audrey Hepburn"
        comments_combined_under50 = comment_under50 + grade_predicted_under50 + quote_under50 + motivational_quote_under50
        print(comments_combined_under50)
        text_file.write(comments_combined_under50)
    elif score <= 75:
        comment_under75 = "\nYou might be stressing a little bit too much, you should relax and listen to some music to help releaf that stress. Everything should be fine!"
        grade_predicted_under75 = "\nYou should be able to get an average grade with no problem so don't stress over it."
        quote_under75 = "\nHere's a motivational quote for you: \n"
        motivational_quote_under75 = "Everybody is a genius. But if you judge a fish by its ability to climb a tree, it will spend its whole life believing that it is stupid. – Albert Einstein"
        comments_combined_under75 = comment_under75 + grade_predicted_under75 + quote_under75 + motivational_quote_under75
        print(comments_combined_under75)
        text_file.write(comments_combined_under75)
    elif score <= 90:
        comment_under90 = "\nYou are just on the right track to success! You have already beaten 90 percent of all other students by not stressing out that much on your upcoming exam!"
        grade_predicted_under90 = "\n You probably can get into the top 10 of your class with no problem!"
        quote_under90 = "\nHere's a motivational quote for you: \n"
        motivational_quote_under90 = "My advice is, never do tomorrow what you can do today. Procrastination is the thief of time. – Charles Dickens David Copperfield"
        comments_combined_under90 = comment_under90 + grade_predicted_under90 + quote_under90 + motivational_quote_under90
        print(comments_combined_under90)
        text_file.write(comments_combined_under90)
    elif score == 100:
        comment_100 = "\nGo play some video games, why did you even do this test... ;)"
        grade_predicted_100 = "\nGo play, you are gonna nail this exam with a 100%."
        quote_100 = "\nHere's a motivational quote for you: \n"
        motivational_quote_100 = "It’s a-me, Mario! – Assassin’s Creed II"
        comments_combined_100 = comment_100 + grade_predicted_100 + quote_100 + motivational_quote_100
        print(comments_combined_100)
        text_file.write(comments_combined_100)



def helper():
    print(25 * "-", "Helper & Info", 25 * "-")
    print("1. About the program")
    print("2. Why did I make this")
    print("3. Navigating through the survey")    
    print("4. Exit")
    print(61 * "-")


loop = True

while loop:

    print_menu()
    
    choice = int(input("Enter a number: "))

    if choice == 1:
        os. system('clear')
        print(f"{bcolors.CBLUE}Survey started!")
        startSurvey()
    elif choice == 2:
        os. system('clear')
        print(f"{bcolors.CGREEN}Results saved: ")
        os. system('clear')
        text_file = open("GradePredicted.txt", "r")
        print(text_file.read())
    elif choice == 3:
        os. system('clear')
        print(f"{bcolors.CBEIGE}Helper & Info")
        choice_loop = True
        while choice_loop:
            helper()
            helper_choice = int(input("Enter a number: "))
            if helper_choice == 1:
                os. system('clear')
                print("This program is based on a project MYP5 students that attend Advanced Programming worked on. \nThe topic I focused on was about test anxiety and how that can severely effect someon's performance.")
            elif helper_choice == 2:
                os. system('clear')
                print("Anxiety students have prior to a vital exam is very stressful. \nAccording to Healthline, Anxiety disorder attacks an estimated 25 percent of 13 to 18-year-olds, \nwhile test anxiety affects roughly 10 to 40 percent of all students. \nMore critically, untreated childhood anxiety is statistically proven to be a burden for students to get even worse grades in school and on exams. \nAnd that loop goes on and on. \nThe audience of this solution then is pretty clear, \nstudents are benefited the most from this project. \nWhile all students from kindergarten to PHD are affected by this, \nstudents starting from fourth grade to middle and high school students suffer the most from test anxiety, \ndue to their burgeoning hormone release and maturing mental health. \nAccording to Verywell Mind, testing anxiety is a type of performance anxiety. \nWhere one is under a high level of stress and strains, \nmaking them believe that they won’t perform at their maximum potentials.")    
            elif helper_choice == 3:
                os. system('clear')
                print("The survey consists of two types of questions:\n")
                print("1. Yes or no, two choiced questions\n")
                print("2. Out of 4 questions")
            elif helper_choice == 4:
                os. system('clear')
                choice_loop = False
            else:
                os. system('clear')
                print("Invalid menu selection. Enter any key to try again..")
                choice_loop = True
    elif choice == 4:
        os. system('clear')
        print(f"{bcolors.CVIOLET}Thank you for using Grade Predictor MYP5! Goodbye!")
        loop = False  
    else:
        print("Invalid menu selection. Enter any key to try again..")