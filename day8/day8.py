import argparse

#25 pixels wide and 6 pixels tall

def build_layers(input):
    layer_array = []
    k = 0
    while k*25*6 < len(input)-1:
        layer_array.append([])
        for i in range(25):
            word = ""
            for j in range(6):
                char = input[j*k]
                word += char
            layer_array[-1].append(word)

            k += 1
    return layer_array

def count_zeros(layer_array):
    pass

def find_result(layer_array):
    most_zeros = []
    for layer in layer_array:
        number = count_zeros(layer)





if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--infile', required=True)
    parser.add_argument('-p', '--part', help="enter 'part1' or 'part2'. default: 'part1'", default='part1')
    args = parser.parse_args()

    input_string = ""
    with open(args.infile) as file:
        input = file.readlines()
        input_string += input[0]



    if args.part == "part1":
        print("part1")
        layer_array = build_layers(input_string)
        print(layer_array)

    if args.part == "part2":
        print("part2")