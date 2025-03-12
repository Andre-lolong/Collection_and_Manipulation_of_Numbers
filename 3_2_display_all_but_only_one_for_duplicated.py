# ask user for numbers
numbers = []
seen = set()
filtered_numbers = []

def display_filtered_numbers():
    for i in range(10):
        num = int(input(f"Enter a value for number {i + 1}: "))
        numbers.append(num)

# check for duplicates
# display all numbers but only first entry for duplicated numbers