#To Prompt user to enter number.
number = int(input("Enter a number to see it's multiplication table: "))

#To generate and print mult table.
for i in range(1, 11):
       result = number * i
       print(f"{number} * {i} = {result}")