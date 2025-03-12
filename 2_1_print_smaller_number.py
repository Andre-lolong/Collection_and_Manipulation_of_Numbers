# ask user for numbers
num1 = int(input("Enter a value for number 1: "))
num2 = int(input("Enter a value for number 2: "))

# identify which is smaller
# print smaller number
if num1 < num2:
    print(f"The smaller number is the first which is: {num1}")
elif num2 < num1:
    print(f"The smaller number is the second which is: {num2}")
else:
    print("The values entered are the same.")