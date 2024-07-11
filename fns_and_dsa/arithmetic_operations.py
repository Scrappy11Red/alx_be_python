def perform_operation(num1, num2, operation):
   match operation: 
    case "add":
        result = num1 + num2
        print(f"The result is {result}.")
    case "subtract":
        result = num1 - num2
        print(f"The result is {result}.")
    case "multiply":
        result = num1 * num2
        print(f"The result is {result}.")
    case "divide":
        result = num1 / num2
        print(f"The result is {result}.")
    case "divide" if num2 == 0:
        result = num1 / num2
        print("Cannot divide by zero.")