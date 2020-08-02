def area_of_triangle():
    a = int(input("Enter length in cm of fist side : "))
    b = int(input("Enter length in cm of second side : "))
    c = int(input("Enter length in cm of third side : "))
    s = (a + b + c)/2
    area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
    return print("The area of tringle with sides {}, {} , {} is {} sq.cm".format(a,b,c,area))
area_of_triangle()