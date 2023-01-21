previous_values = []
multiply_by_2 = False

while True:
    try:
        value = int(input("Please enter an integer value: "))
        if value == 10:
            multiply_by_2 = True
        elif multiply_by_2:
            value = value * 2
            multiply_by_2 = False
        previous_values.append(value)
        print("Previous values:", previous_values)
    except ValueError:
        print("Invalid input. Please enter an integer.")
