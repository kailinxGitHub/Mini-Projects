mystring = str(input("Enter a string to check the shortest word: "))

words = mystring.split()
min = 100

for i in words: 
    length = len(i)
    if length < min: 
        min = length
print(min)