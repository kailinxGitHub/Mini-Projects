myword = str(input("Enter a word to check the middle character: "))

length = len(myword)

if length / 2 == 0: 
    print("Try again.")
else: 
    middle = length/2
    int_mid = int(middle)
    print(myword[int_mid])