import argparse

# #asteroid
# . empty


def parse_input(file, input_array):
    for line in file:
        line_strip = line.strip()
        line_array = []
        for symbol in line_strip:
            line_array.append(symbol)
        input_array.append(line_array)


def is_visible(input_array, x, y, i, j):
    print("x,y,i,j", x, y, i, j)
    if x == i and y == j:
        return True
    elif x == i:
        if abs(y-j) == 1:
            return True
        elif j > y:
            for k in range(1,j-y):
                if input_array[i][j-k] == '#':
                    return False
                    break
            else:
                return True
        else:
            for k in range(1, y-j):
                if input_array[i][y-k] == '#':
                    return False
                    break
            else:
                return True
    elif y == j:
        if abs(i-x) == 1:
            return True
        elif i > x:
            for k in range(1, i-x):
                print(x, y, i, j, i+k, j)
                if input_array[i-k][j] == '#':
                    return False
                    break
            else:
                return True
        else:
            for k in range(1,x-i):
                if input_array[x-k][j] == '#':
                    return False
                    break
            else:
                return True

    else:
        # nur die Parallele abgehen? nein!
        # parallele und ob da drum rum jeweils #?!
        #for k in range(x-i):
         #   for l in range(y-j):
        print("else")
        return True


def count_asteroids(input_array, x, y):
    count = 0
    for i in range(len(input_array)):
        for j in range(len(input_array[i])):
            point = input_array[i][j]
            if point == '#':
                visible = is_visible(input_array, x, y, i, j)
                print(visible)
                if visible:
                    count += 1
    return count


def parse_space(input_array):
    number_asteroids = []
    for i in range(len(input_array)):
        for j in range(len(input_array[i])):
            point = input_array[i][j]
            if point == '#':
                asteroids = count_asteroids(input_array, i, j)
                number_asteroids.append(asteroids)
            j += 1
        i += 1

    return number_asteroids


def find_max(number_asteroids):
    number_asteroids.sort()
    max_asteroids = number_asteroids[-1]

    return max_asteroids


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--infile', required=True)
    parser.add_argument('-p', '--part', help="enter 'part1' or 'part2'. default: 'part1'", default='part1')
    args = parser.parse_args()

    input_array = []
    with open(args.infile) as file:
        parse_input(file, input_array)

    if args.part == "part1":
        print("part1")
        count = parse_space(input_array)
        print(count)
        max_count = find_max(count)
        print(max_count)

    if args.part == "part2":
        print("part2")