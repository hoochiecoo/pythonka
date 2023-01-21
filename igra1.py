while True:
    try:
        value = int(input("Please enter an integer value: "))
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")

print("You entered:", value)
