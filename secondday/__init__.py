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


def run_intcode(new_intcode):
    for i in range(len(new_intcode)):
        if i % 4 == 0:
            operation = new_intcode[i]
            first_place = new_intcode[i+1]
            second_place = new_intcode[i+2]
            storage_place = new_intcode[i + 3]
            if operation == 99:
                return new_intcode
            if first_place < len(new_intcode) and second_place < len(new_intcode) and storage_place < len(new_intcode):
                first_number = new_intcode[first_place]
                second_number = new_intcode[second_place]
                if operation == 1:
                    result = first_number + second_number
                    new_intcode[storage_place] = result
                if operation == 2:
                    result = first_number * second_number
                    new_intcode[storage_place] = result
        i += 1


def find_result(intcode):
    for i in range(0, 100):
        for j in range(0,100):
            new_intcode = [g for g in intcode]
            new_intcode[1] = i
            new_intcode[2] = j
            array = run_intcode(new_intcode)
            if int(array[0]) == 19690720:
                result = array[1] * 100 + array[2]
                return[array, result]


file = sys.argv[1]
int_array = parse_file(file)
end_result = find_result(int_array)
print(end_result)