def sum(a, b):
    sum = a + b
    print(sum)

def diff(a, b):
    difference = a-b
    print(difference)

def quot(a, b):
    quotient = a/b
    print(quotient)

def prod(a, b):
    product = a * b
    print(product)

choice = str(input("What do you want to do? sum, diff, quot, prod\n"))
num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))

if choice == "sum":
    sum(num1, num2)
elif choice == "diff":
    diff(num1, num2)
elif choice == "quot":
    quot(num1, num2)
elif choice == "prod":
    prod(num1, num2)
else:
    print("Try again")