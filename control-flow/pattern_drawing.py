positive_integer = int(input("Enter the size of the pattern: "))
i = 0

#To iterate through each row of the pattern.
while i <= positive_integer:
    #To print asterisks (*) side by side without advancing to a new line
    for _ in range(positive_integer):
        print("*", end="")
    #To prints a newline character to move to the next row
    print()
    #To increment the row counter
    i += 1