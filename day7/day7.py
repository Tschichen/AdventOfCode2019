import argparse

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
        print(input_values)

    if args.part == "part2":
        print("part2")