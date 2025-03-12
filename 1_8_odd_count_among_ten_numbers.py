# ask user for ten numbers 
total = 0
for i in range(10):
    num = int(input(f"Enter a value for number {i + 1}: "))
    if num % 2 == 1: # ientify which is odd
        total += 1

# count the odds and print
print(f"The odd number counnt is: {total}")