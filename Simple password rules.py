print("Please enter a password\n")
print("The password must: 1. have 8 characters of more. 2. have at least one number. 3. have at least one symbol")

user_password = input("Please enter your password: ")
confirm_user_password = input("Please confirm your password: ")


def containsNumber(value):
    for character in value:
        if character.isdigit():
            return True
    return False


if user_password != confirm_user_password:
    print("Error: your passwords do not match.")
elif len(user_password) < 8:
    print("please create a password with more than 8 characters.")
elif not containsNumber:
    print("Please include a number.")
elif user_password.isalnum():
    print("Error: You need a symbol")
else:
    print("Nice! Your password is set!")