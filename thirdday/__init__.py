import argparse
import math


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


def find_new_coordinate(last_coordinate, dir, value):
    if dir == "L":
        x = last_coordinate[0] - value
        new_coordinate = [x, last_coordinate[1]]
        return new_coordinate
    if dir == "R":
        x = last_coordinate[0] + value
        new_coordinate = [x, last_coordinate[1]]
        return new_coordinate
    if dir == "U":
        y = last_coordinate[1] + value
        new_coordinate = [last_coordinate[0], y]
        return new_coordinate
    if dir == "D":
        y = last_coordinate[1] - value
        new_coordinate = [last_coordinate[0], y]
        return new_coordinate


def make_way_array(last_coordinate, new_coordinate, way):
    for i in range(1, abs(last_coordinate[0] - new_coordinate[0])):
        if last_coordinate[0] > new_coordinate[0]:
            way.append([last_coordinate[0] - i, new_coordinate[1]])
        else:
            way.append([last_coordinate[0] + i, new_coordinate[1]])

    for j in range(1, abs(last_coordinate[1] - new_coordinate[1])):
        if last_coordinate[1] > new_coordinate[1]:
            way.append([last_coordinate[0], last_coordinate[1]-j])
        else:
            way.append([last_coordinate[0], last_coordinate[1]+j])
    way.append(new_coordinate)


def calculate_manhattan(value1, value2):
    distance = abs(value1) + abs(value2)
    return distance


def run(first_module, second_module):
    first_way = [[0,0]]
    second_way = [[0,0]]

    for entry in first_module:
        old_coordinates = first_way[-1]
        dir = entry[0]
        value = int(entry[1:])
        new_coordinates = find_new_coordinate(old_coordinates, dir, value)
        make_way_array(old_coordinates, new_coordinates, first_way)

    print("first way done")

    for entry in second_module:
        old_coordinates = second_way[-1]
        dir = entry[0]
        value = int(entry[1:])
        new_coordinates = find_new_coordinate(old_coordinates, dir, value)
        make_way_array(old_coordinates, new_coordinates, second_way)

    print("second way done")

    set_way_one = set()
    set_way_two = set()

    for coordinate in first_way:
        set_way_one.add((coordinate[0], coordinate[1]))

    for coordinate in second_way:
        set_way_two.add((coordinate[0], coordinate[1]))

    common_coordinates = set_way_one.intersection(set_way_two)

    print(common_coordinates)

    shortest_manhattan = math.inf
    for entry in common_coordinates:
        distance = calculate_manhattan(entry[0], entry[1])
        if distance < shortest_manhattan and distance > 0:
            shortest_manhattan = distance

    print(shortest_manhattan)

def run_part2(first_module, second_module):
    first_way = [[0, 0]]
    second_way = [[0, 0]]

    for entry in first_module:
        old_coordinates = first_way[-1]
        dir = entry[0]
        value = int(entry[1:])
        new_coordinates = find_new_coordinate(old_coordinates, dir, value)
        make_way_array(old_coordinates, new_coordinates, first_way)

    print("first way done")

    for entry in second_module:
        old_coordinates = second_way[-1]
        dir = entry[0]
        value = int(entry[1:])
        new_coordinates = find_new_coordinate(old_coordinates, dir, value)
        make_way_array(old_coordinates, new_coordinates, second_way)

    print("second way done")

    set_way_one = set()
    set_way_two = set()

    for coordinate in first_way:
        set_way_one.add((coordinate[0], coordinate[1]))

    for coordinate in second_way:
        set_way_two.add((coordinate[0], coordinate[1]))

    common_coordinates = set_way_one.intersection(set_way_two)

    print(common_coordinates)

    pathways = []
    for coordinate in common_coordinates:
        value = [coordinate[0], coordinate[1]]
        value_index_1 = first_way.index(value)
        value_index_2 = second_way.index(value)
        steps = value_index_1 + value_index_2
        if steps > 0:
            pathways.append(steps)

    min_steps = min(pathways)
    print(min_steps)


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--infile', help="path to input file", required=True)
    parser.add_argument('-p', '--part', help="enter 'part1' or 'part2'. default: 'part1'", default='part1')
    args = parser.parse_args()

    with open(args.infile) as file:
        input = parse_input(file)
        first_module = input[0]
        second_module = input[1]

    if args.part == "part1":
        print("part1")
        run(first_module, second_module)
    if args.part == "part2":
        print("part2")
        run_part2(first_module, second_module)

