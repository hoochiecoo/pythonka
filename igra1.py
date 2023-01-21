while True:
    try:
        value = int(input("Please enter an integer value: "))
        print("You entered:", value)
    except ValueError:
        print("Invalid input. Please enter an integer.")
