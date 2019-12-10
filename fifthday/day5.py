import argparse
# result part1 should be: 9961446


def run_intcode(new_intcode):
    i = 0
    while i < len(new_intcode):
        entry = str(new_intcode[i])
        entry_array = []
        for char in entry:
            if char != "-":
                entry_array.append(int(char))
        number = entry_array[-1]
        if number == 1:
            if len(entry_array) < 3 or entry_array[-3] == 0:
                first_number = int(new_intcode[int(new_intcode[i+1])])
            else:
                first_number = new_intcode[i+1]
            if len(entry_array) < 4 or entry_array[-4] == 0:
                second_number = int(new_intcode[int(new_intcode[i+2])])
            else:
                second_number = new_intcode[i+2]
            result = int(first_number) + int(second_number)
            new_intcode[int(new_intcode[i+3])] = result
            i += 4
        elif number == 2:
            if len(entry_array) < 3 or entry_array[-3] == 0:
                first_number = new_intcode[int(new_intcode[i+1])]
            else:
                first_number = new_intcode[i+1]
            if len(entry_array) < 4 or entry_array[-4] == 0:
                second_number = new_intcode[int(new_intcode[i+2])]
            else:
                second_number = new_intcode[i+2]
            result = int(first_number) * int(second_number)
            new_intcode[int(new_intcode[i+3])] = result
            i += 4
        elif number == 3:
            input = 5
            new_intcode[int(new_intcode[i+1])] = input
            i += 2
        elif number == 4:
            if len(entry_array) < 3 or entry_array[-3] == 0:
                print("output: ", new_intcode[int(new_intcode[i + 1])])
            else:
                print("output: ", new_intcode[i + 1])
            i += 2
        elif number == 5:
            if len(entry_array) < 3 or entry_array[-3] == 0:
                zahl = int(new_intcode[int(new_intcode[i+1])])
            else:
                zahl = int(new_intcode[i+1])
            if zahl != 0:
                if len(entry_array) <4 or entry_array[-4] == 0:
                    i = int(new_intcode[int(new_intcode[i+2])])
                else:
                    i = int(new_intcode[i+2])
            else:
                i += 3
        elif number == 6:
            if len(entry_array) < 3 or entry_array[-3] == 0:
                zahl = int(new_intcode[int(new_intcode[i+1])])
            else:
                zahl= int(new_intcode[i+1])
            if zahl == 0:
                if len(entry_array) <4 or entry_array[-4] == 0:
                    i = int(new_intcode[int(new_intcode[i+2])])
                else:
                    i = int(new_intcode[i+2])
            else:
                i += 3
        elif number == 7:
            if len(entry_array) < 3 or entry_array[-3] == 0:
                number1 = int(new_intcode[int(new_intcode[i+1])])
            else:
                number1 = int(new_intcode[i+1])
            if len(entry_array) < 4 or entry_array[-4] == 0:
                number2 = int(new_intcode[int(new_intcode[i+2])])
            else:
                number2 = int(new_intcode[i+2])
            if number1 < number2:
                if len(entry_array) < 5 or entry_array[-5] == 0:
                    new_intcode[int(new_intcode[i+3])] = str(1)
                else:
                    new_intcode[i+3] = str(1)
            else:
                if len(entry_array) < 5 or entry_array[-5] == 0:
                    new_intcode[int(new_intcode[i + 3])] = str(0)
                else:
                    new_intcode[i+3] = str(0)
            i += 4
        elif number == 8:
            if len(entry_array) < 3 or entry_array[-3] == 0:
                number1 = new_intcode[int(new_intcode[i + 1])]
            else:
                number1 = int(new_intcode[i + 1])
            if len(entry_array) < 4 or entry_array[-4] == 0:
                number2 = new_intcode[int(new_intcode[i + 2])]
            else:
                number2 = int(new_intcode[i + 2])
            if number1 == number2:
                if len(entry_array) < 5 or entry_array[-5] == 0:
                    new_intcode[int(new_intcode[i + 3])] = str(1)
                else:
                    new_intcode[i + 3] = str(1)
            else:
                if len(entry_array) < 5 or entry_array[-5] == 0:
                    new_intcode[int(new_intcode[i + 3])] = str(0)
                else:
                    new_intcode[i + 3] = str(0)
            i += 4
        elif number == 9 and entry_array[-2] == 9:
            return
        else:
            print('ERROR')
            return


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--infile', required=True)
    args = parser.parse_args()

    input_values = []
    with open(args.infile) as file:
        input = file.readlines()
        line = input[0]
        values = line.split(',')
        for entry in values:
            input_values.append(entry)

    print("part2")
    run_intcode(input_values)
