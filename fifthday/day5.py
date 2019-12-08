import argparse
#result shpuld be: 9961446

def run_intcode(new_intcode):
    output = []
    i = 0
    while i < len(new_intcode):
        entry = str(new_intcode[i])
        entry_array = []
        for char in entry:
            if char != "-":
                entry_array.append(int(char))
        #print(entry_array)
        number = entry_array[-1]
        if number == 1 and len(entry_array) > 1 and entry_array[-2] == 0:
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
        elif number == 2 and len(entry_array) > 1 and entry_array[-2] == 0:
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
        elif number == 3 and len(entry_array) < 2:
            input = 1
            new_intcode[int(new_intcode[i+1])] = input
            i += 2
        elif (number == 4 and len(entry_array) < 2) or (number == 9 and entry_array[-2] == 9 and len(entry_array) == 2):
            if new_intcode[int(new_intcode[i+1])] != 0:
                print("final output: ", new_intcode[int(new_intcode[i+1])])
                break
            else:
                print("diagnostic succesful. Output: ", new_intcode[int(new_intcode[i+1])])
            i += 2
            #output.append(new_intcode[int(new_intcode[i+1])])
            #new_intcode[0] = new_intcode[int(new_intcode[i + 1])]
            #print("output: ", new_intcode[int(new_intcode[i+1])])
        else:
           i += 1

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--infile', required=True)
    parser.add_argument('-p', '--part', help="enter 'part1' or 'part2'. default: 'part1'", default='part1')
    args = parser.parse_args()

    input_values = []
    with open(args.infile) as file:
        input = file.readlines()
        line = input[0]
        values = line.split(',')
        for entry in values:
            input_values.append(entry)

    if args.part == "part1":
        print("part1")
        code = run_intcode(input_values)
        #print(code[0])

    if args.part == "part2":
        print("part2")
