print("Multiplication and Exponent Calculator")
print("Choose option 1 for Multiplication")
print("Choose option 2 for Exponentiation")
print("Choose option 3 to Exit")
x = int(input(""))

while  x > 0:

    match x:
        case 1:
            operand = int(input("Enter an operand: "))
            other = int(input("Enter the other operand: "))
            total = 0
            for j in range(1):
                for i in range(other):
                    total += operand
            print(total)

        case 2:
            base = int(input("Enter the base: "))
            exponent = int(input("Enter the exponent: "))
            total = 1
            for j in range(1):
                for i in range(exponent):
                    total *= base
            print(total)
        case 3:
            print("Closing the Calculator...")
            break
        case _:
            print("Invalid Choice")

    print("Multiplication and Exponent Calculator")
    print("Choose option 1 for Multiplication")
    print("Choose option 2 for Exponentiation")
    print("Choose option 3 to Exit")
    x = int(input(""))