previous_values = []
steps = []
multiply_by_2 = False
sum = 0

while True:
    try:
        value = int(input("Please enter an integer value: "))
        if value == 10:
            multiply_by_2 = True
        elif multiply_by_2:
            value = value * 2
            multiply_by_2 = False
        previous_values.append(value)
        sum += value
        steps.append({'value': value, 'sum': sum, 'previous_values': previous_values.copy(), 'multiply_by_2': multiply_by_2})
        print("Current value:", value)
        print("Current sum:", sum)
        print("multiply_by_2:", multiply_by_2)
        print("Previous values:", previous_values)
    except ValueError:
        print("Invalid input. Please enter an integer.")
