def add_numbers():
    sum = 0
    a = int(input("How many numbers you required to add? "))
    numbers_to_add = 0
    for i in range(a):
        numbers_to_add=input("Enter you numbers one by one and click enter: ")
        sum = sum + int(numbers_to_add)
    return print(sum)
add_numbers()
