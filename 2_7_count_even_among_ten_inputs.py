# ask the user for numbers
even = 0 
for i in range(10):
    num = int(input(f"Enter a value for number {i + 1}: "))
    if i % 2 == 0: 
        even += 1 # count even numbers

# print how many even
print(f"The even numbers entered are: {even}")