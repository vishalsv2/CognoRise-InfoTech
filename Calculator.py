print("Welcome to Calculator")
print(" ")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Power")
print("6.Exit")

a=True

while a:
    print("Choose the arithmetic operation From (1-6).")
    key = int(input("Enter the operation (eg 1 or 2):"))
    if key == 6:
        a=False
        print("Exit !!!")
        continue
    number1 = int(input("Enter the First number: "))
    number2 = int(input("Enter the Second number: "))
    if key == 1:
        total = number1 + number2
    elif key ==2:
        total = number1 - number2
    elif key ==3:
        total = number1 * number2
    elif key ==4:
        total = number1 / number2
    elif key ==5:
        total = number1 ** number2
    else:
        print("Invalid input")
    print("Your Result is ",total)
