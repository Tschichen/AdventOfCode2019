import math
import sys

def parse_input(file):
    values = []
    with open(file) as handle:
        for line in handle:
            value = line.strip()
            values.append(int(value))
    return values

def calculate_fuel_module(mass):
    result = int(math.floor(mass / 3)) - 2
    return result

def calculate_result(values):
    result = 0
    for value in values:
        module = 0
        while value > 0:
            step = calculate_fuel_module(value)
            if step > 0:
                module += step
                value = step
            else:
                break
        print(module)
        result += module
    print("the result is: ", result)

input = sys.argv[1]
values = parse_input(input)
calculate_result(values)