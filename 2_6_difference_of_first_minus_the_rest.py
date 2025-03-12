# ask the user for numbers
# get the minuend, let variable "min" be the minuend
min = int(input("Enter a value for number 1: "))

# get the total of the subtrahend, let the variable "subtot" be the total subtrahend
subtot = 0
for i in range(2, 10 +1):
    num = int(input(f"Enter a value for number {i}: "))
    subtot += num
# perform subtraction
difference = min - subtot
# print the difference
print(f"The difference of the first number minus the total of the rest is: {difference}")