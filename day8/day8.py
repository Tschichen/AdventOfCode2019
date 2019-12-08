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

def count_numbers(layer_array, number):
    count = 0
    for layer in layer_array:
        number = sentence.count(number)
        count += number

    return count

def find_result(layer_array):
    zeros = []
    for layer in layer_array:
        number = count_zeros(layer, "0")
        zeros.append([number, layer])

    zeros.sort(reverse=True)

    max_zeros = zeros[0]
    layers_for_result = max_zeros[1]
    einser = count_numbers(layers_for_result, "1")
    zweier = count_numbers(layers_for_result, "2")
    result = einser * zweier

    return result




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
        result = find_result(layer_array)
        print(result)

    if args.part == "part2":
        print("part2")