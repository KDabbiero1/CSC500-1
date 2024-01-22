def add_and_subtract():
    num1 = float(input("Enter a number to add to/ subtract from: "))
    num2 = float(input("Enter the amount you want to add/ subtract: "))

    add = num1 + num2
    subtract = num1 - num2

    print(f"Addition: {add}\nSubtraction: {subtract}")
    return

def divide_and_multiply():
    num1 = float(input("Enter a number to divided and multiply: "))
    num2 = float(input("Enter a number to divide by (cannot be 0) and multiply by: "))

    divide = num1 / num2
    multiply = num1 * num2

    print(f"Division: {divide}\nMultiplication: {multiply}")

def determine_operation():
    operation = int(input("Input the number next to the operation you'd like to perform.\nWhat operation would you like to perform \n[1] Addition and Subtraction \n[2] Division and Multiplication\n>>>"))
    if operation == 1:
        add_and_subtract()
    elif operation == 2:
        divide_and_multiply()
    else:
        print("You've entered an invalid operation.")
    return 

determine_operation()