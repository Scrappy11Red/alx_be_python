#Variables that prompt users to enter three pieces of information.
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
operation = str(input("Choose the operation (+, -, *, /):"))

#Match, case allows the user to do a calculation.
match operation: 
    case "+":
        result = num1 + num2
        print(f"The result is {result}.")
    case "-":
        result = num1 - num2
        print(f"The result is {result}.")
    case "*":
        result = num1 * num2
        print(f"The result is {result}.")
    case "/":
        result = num1 / num2
        print(f"The result is {result}.")
    case "/" if num2 == 0:
        result = num1 / num2
        print("Cannot divide by zero.")
