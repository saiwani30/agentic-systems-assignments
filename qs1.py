try:

    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")

    # Convert inputs to integers
    num1 = int(num1)
    num2 = int(num2)


    if num2 == 0:
        print("Cannot divide by zero")
    else:
        # Print sum
        print("Sum:", num1 + num2)
        
        # Print division result
        print("Division:", num1 / num2)

except ValueError:
    print("Invalid input")