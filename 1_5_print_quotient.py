# ask user for number
num1 = int(input("Enter a value for number 1: "))
num2 = int(input("Enter a value for number 2: "))

# perfrom arithmetic operation (division)
# check for undefined answer
# print quotient
if  num1 != 0 and num2 != 0:
    print(f"The first number divided by the second number will resuslt to {num1/num2}")
    print("and")
    print(f"The second number divided by the first number will resuslt to {num2/num1}")
elif num1 != 0 and num2 == 0:
    print("The first number divided by the second number will be undefined")
    print("and")
    print("The second number divided by the first number will resuslt to zero")
elif num1 == 0 and num2 != 0:
    print("The first number divided by the second number will resuslt to zero")
    print("and")
    print("The second number divided by the first number will be undefined")
elif num1 == 0 and num2 == 0:
    print("This operation is unforgivable")
else:
    print("Try again")