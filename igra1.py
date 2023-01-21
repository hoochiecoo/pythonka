previous_values = []
while True:
    try:
        value = int(input("Please enter an integer value: "))
        previous_values.append(value)
        print("Previous values:", previous_values)
    except ValueError:
        print("Invalid input. Please enter an integer.")
