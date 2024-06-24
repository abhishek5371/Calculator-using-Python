# Simple Calculator

while True:
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'quit' to end the program")
    
    user_input = input(": ")
    
    if user_input == "quit":
        break
    elif user_input == "add":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result:", num1 + num2)
    elif user_input == "subtract":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result:", num1 - num2)
    elif user_input == "multiply":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result:", num1 * num2)
    elif user_input == "divide":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error: Division by zero")
    else:
        print("Unknown input")
