def check_multiply_by_2(previous_values, value):
    if value == 10:
        if previous_values and previous_values[-1] == 10:
            return True, False
        else:
            return True, False
    return False, False

def check_multiply_by_3(previous_values, value):
    if value == 10:
        if previous_values and previous_values[-1] == 10:
            return True, False
        else:
            return False, False
    return False, False

def multiply_value(multiply_by_2, multiply_by_3, value):
    if multiply_by_2:
        return value * 2, False, False
    elif multiply_by_3:
        return value * 3, False, False
    return value, False, False

def get_input():
    try:
        return int(input("Please enter an integer value: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return None

def print_status(value, sum, multiply_by_2, multiply_by_3, previous_values):
    print("Current value:", value)
    print("Current sum:", sum)
    print("multiply_by_2:", multiply_by_2)
    print("multiply_by_3:", multiply_by_3)
    print("Previous values:", previous_values)



def check_multiply_by_2(previous_values, value):
    if value == 10:
        if previous_values and previous_values[-1] == 10:
            return True, False
        else:
            return True, False
    return False, False

def check_multiply_by_3(previous_values, value):
    if value == 10:
        if previous_values and previous_values[-1] == 10:
            return True, False
        else:
            return False, False
    return False, False

def multiply_value(multiply_by_2, multiply_by_3, value):
    if multiply_by_2:
        return value * 2, False, False
    elif multiply_by_3:
        return value * 3, False, False
    return value, False, False

def get_input():
    try:
        return int(input("Please enter an integer value: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return None

def print_status(value, sum, multiply_by_2, multiply_by_3, previous_values):
    print("Current value:", value)
    print("Current sum:", sum)
    print("multiply_by_2:", multiply_by_2)
    print("multiply_by_3:", multiply_by_3)
    print("Previous values:", previous_values)

if __name__ == '__main__':
    previous_values = []
    sum = 0
    multiply_by_2 = False
    multiply_by_3 = False
    while True:
        value = get_input()
        if value is None:
            continue
        if len(previous_values) >= 2:
            if previous_values[-1] == 10 and previous_values[-2] == 10:
                multiply_by_3 = True
            else:
                if previous_values[-1] == 10:
                    multiply_by_2 = True
        if multiply_by_2:
            value = value * 2
            multiply_by_2 = False
        elif multiply_by_3:
            value = value * 3
            multiply_by_3 = False
        previous_values.append(value)
        sum += value
        print_status(value, sum, multiply_by_2, multiply_by_3, previous_values)
