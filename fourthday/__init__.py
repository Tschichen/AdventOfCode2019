import argparse

def double_number(input_string):
    for i in range(len(input_string) - 1):
        first = input_string[i]
        second = input_string[i + 1]
        if first == second:
            return True
    return False

def new_double(input_string):
    for i in range(len(input_string)-1):
        first = input_string[i]
        second = input_string[i+1]
        if first == second:
            if i > 0:
                before = input_string[i-1]
                if before != first:
                    if len(input_string)-i > 2:
                        after = input_string[i+2]
                        if after != second:
                            return True
                    else:
                        return True
            else:
                if len(input_string) - i > 2:
                    after = input_string[i + 2]
                    if after != second:
                        return True
                else:
                   return True
    return False


def increasing(input_string):
    for i in range(len(input_string) - 1):
        first = int(input_string[i])
        second = int(input_string[i+1])
        if first > second:
            return False
    return True


def numbers(value1, value2, part):
    valid_numbers = []
    for i in range(value1, value2+1):
        if part == 'part1':
            if increasing(str(i)) and double_number(str(i)):
                valid_numbers.append(i)
        if part == 'part2':
            if increasing(str(i)) and new_double(str(i)):
                valid_numbers.append(i)
    count = len(valid_numbers)
    return count

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--infile', required=True)
    parser.add_argument('-p', '--part', help="enter 'part1' or 'part2'. default: 'part1'", default='part1')
    args = parser.parse_args()

    value1 = 0
    value2 = 0
    with open(args.infile) as file:
        input = file.readlines()
        values = input[0].split('-')
        value1 = int(values[0])
        value2 = int(values[1])

    if args.part == "part1":
        print("part1")
        result = numbers(value1, value2, "part1")
        print(result)
    if args.part == "part2":
        print("part2")
        result = numbers(value1, value2, "part2")
        print(result)
