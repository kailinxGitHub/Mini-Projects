duration = int(input("How long is your loan in years? "))
rate = float(input("What is the interest rate? "))
amount = float(input("How much is your loan? "))
calculates = amount * (1 + rate / 100) ** duration
# calculates ignore the decimal
ignore_decimal = round(calculates, 2)
# convert the caculates to a string with a coma at the thousands place
convert = str(ignore_decimal)
# split the string into a list
split_list = convert.split(".")
# get the first element of the list
first_element = split_list[0]

# calculate the monthly payment
monthly_payment = (calculates / duration)
print("Your monthly payment is: ", monthly_payment)

def convert_to_string(number):
    string_number = str(number)
    slice_number = string_number[-3:]
    print(slice_number)

convert_to_string(first_element)