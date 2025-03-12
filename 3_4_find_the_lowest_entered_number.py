lowest = None

while True:
    num = input("Enter a number: ") # ask the user for numbers
    if not num.isdigit():
        print(f"Lowest number entered: {lowest}") # print the lowest when an error occured
        print("Invalid input. Goodbye!") 
        break
    num = int(num) # sets the lowest value
    if lowest is None or num < lowest:
        lowest = num
