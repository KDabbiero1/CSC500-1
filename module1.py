def addition():
    num1 = float(input("Enter an addend: "))

    num2 = float(input("Enter another addend: "))

    result = num1 + num2

    return result

def subtraction():
    minuend = float(input("Enter minuend: "))
    subtrahend = float(input("Enter subtrahend: "))

    result = minuend - subtrahend

    return result

def division():
    dividend = float(input("Enter dividend: "))
    divisor = float(input("Enter divisor (cannot be 0): "))

    result = dividend / divisor

    return result

def multiplication():
    multiplicand = float(input("Enter multiplicand: "))
    multiplier = float(input("Enter multiplier: "))

    result = multiplicand * multiplier

    return result

def determine_operation():
    operation = int(input("Input the number next to the operation you'd like to perform.\nWhat operation would you like to perform \n[1] Addition\n[2] Subtraction \n[3] Division\n[4] Multiplication\n>>>"))
    if operation == 1:
        print(addition())
    elif operation == 2:
        print(subtraction())
    elif operation == 3:
        print(division())
    elif operation == 4:
        print(multiplication())
    else:
        print("You've entered an invalid operation.")
    return 

determine_operation()
