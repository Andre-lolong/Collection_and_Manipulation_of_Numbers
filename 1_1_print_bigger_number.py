# ask user for inputs
num1 = int(input("Enter a value for number 1: "))
num2 = int(input("Enter a value for number 2: "))

# verify and evaluate inputs 
# print bigger number
if num1 > num2:
    print(f"The bigger number is the first which is: {num1}")
elif num2 > num1:
    print(f"The bigger number is the second which is: {num2}")
else:
    print("The values entered are the same.")