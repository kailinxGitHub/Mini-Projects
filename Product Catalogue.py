while True:
    print("1. Create a new catalogue")
    print("2. Create a new product")
    print("3. Read ")
    print("4. Quit")
    choice = int(input("Enter a number: "))

    if choice == 1:
        f = open("catalogue.txt", "w")
        f.close()
    elif choice == 2:
        product_code = input("Enter the product code: ")
        if product_code == "":
            break
        product_description = input("Enter the product description: ")
        product_price = input("Enter the product price: ")

        f = open("catalogue.txt", "a")
        f.write(product_code)
        f.write("\n")
        f.write(product_description)
        f.write("\n")
        f.write(product_price)
        f.write("\n")
        f.close()
    elif choice == 3:
        f = open("catalogue.txt", "r")
        print(f.read())
    elif choice == 4:
        break