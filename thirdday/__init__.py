import argparse


def parse_input(file):
    input_array = []
    for line in file:
        line_fine = line.strip()
        line_split = line_fine.split(',')
        entry_array = []
        for entry in line_split:
            entry_array.append(entry)
        input_array.append(entry_array)
    return input_array


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--infile', help="path to input file", required=True)
    parser.add_argument('-p', '--part', help="enter 'part1' or 'part2'. default: 'part1'", default='part1')
    args = parser.parse_args()

    with open(args.infile) as file:
        input = parse_input(file)

    if args.part == "part1":
        print(input)
    if args.part == "part2":
        print(input)
