# ask user for numbers
def display_filtered_numbers():
    numbers = []
    seen = set()
    filtered_numbers = []
    
    for i in range(10):
        num = int(input(f"Enter a value for number {i + 1}: "))
        numbers.append(num)
    if num not in seen: # check for duplicates
        seen.add(num)
        filtered_numbers.append(num)

    print(f"Here are the numbers that are filtered: {filtered_numbers} ")# display all numbers but only first entry for duplicated numbers

display_filtered_numbers()