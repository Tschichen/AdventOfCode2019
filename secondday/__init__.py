import sys


def parse_file(file):
    file_open = open(file, "r")
    for line in file_open:
        intcode = []
        array = line.split(',')
        for number in array:
            intcode.append(int(number))
        #intcode[1] = 12
        #intcode[2] = 2
        return intcode

def run_intcode(intcode):
    for i in range(len(intcode)):
        if i % 4 == 0:
            operation = intcode[i]
            first_number = intcode[i+1]
            second_number = intcode[i+2]
            storage_place = intcode[i+3]
            if operation == 1:
                result = first_number + second_number
                intcode[storage_place] = result
            if operation == 2:
                result = first_number * second_number
                intcode[storage_place] = result
            if operation == 99:
                return intcode
            print(intcode)
        i += 1


file = sys.argv[1]
int_array = parse_file(file)
print(int_array)
new_int_array = run_intcode(int_array)
print(new_int_array)