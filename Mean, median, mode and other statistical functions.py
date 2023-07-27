list = [2, 3, 3, 2, 3, 2, 3, 9, 7, 3, 4, 8, 1, 2, 8, 7, 6, 5, 8, 9, 1, 2, 3, 2, 1, 4, 3, 2, 1, 4, 5, 4, 1, 6, 9, 6, 1,
        4, 2, 3, 5]

sum = 0
num = 0
max_mode = 0
list.sort()

print(list)
frequency = []

while True:
    choice = input("1. Mean, 2. Mode, 3. Median, 4. Exit\n")
    if choice == "1":
        for i in list:
            sum += i
            num += 1
            mean = sum / num
        print("Sum:", sum, ",Num:", num, ",Mean:", mean)
    elif choice == "2":
        for i in list:
            elm_count = list.count(i)
            frequency.append(elm_count)
            highest = max(frequency)
        print(i, highest)
    elif choice == "3":
        num_of_elm = len(list)
        median_num = num_of_elm / 2
        int_median = int(median_num)
        print(int_median)
    elif choice == "4":
        break