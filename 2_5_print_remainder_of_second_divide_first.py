# ask the user for numbers
num1 = int(input("Enter value for number 1: "))
num2 = int(input("Enter value for number 2: "))

# perform modulus division (first number divided by the second number)
# print remainder
if num2 != 0:
    print(f"The remainder is {num1 % num2}")
else:
    print("Cannot divide by zero")