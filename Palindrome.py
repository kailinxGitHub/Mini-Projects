def palindrome(word):
    return word == word[::-1]

word = str(input("Enter a palindrome: "))

answer = palindrome(word)

if answer: 
    print(word, "is a palindrome")
else: 
    print(word, "is not a plaindrome")