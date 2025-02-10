from random import randint
print("Guess the number I am thinking!")
x = randint(1,100)
# print(x)

y = int(input("Enter any number between 1 and 100: "))

while y != x:
    if y > x:
        print("Too high!")
        y = int(input("Enter any number between 1 and 100: "))
    elif y < x:
        print("Too low!")
        y = int(input("Enter any number between 1 and 100: "))

print(f"correct! I was thinking of {x}")