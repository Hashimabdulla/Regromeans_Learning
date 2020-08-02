def solve_quadratic_eqn():
    a = int(input("Enter  a : "))
    b = int(input("Enter b : "))
    c = int(input("Enter c : "))
    # discriminant
    d = (b ** 2) - (4 * a * c)
    # find two solutions
    sol1 = (-b - d**0.5) / (2 * a)
    sol2 = (-b + d**0.5) / (2 * a)
    return print("The solutions are {} and {}!".format(sol1,sol2))
solve_quadratic_eqn()