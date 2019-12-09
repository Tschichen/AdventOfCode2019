import argparse

#25 pixels wide and 6 pixels tall

def build_layers(input):
    layer_array = []
    i = 0
    while i < len(input):
        word = input[i:i+25]
        layer_array.append(word)
        i += 25

    final_layers = []
    for i in range(len(layer_array)):
        if i % 6 == 0:
            single_layer = []
            single_layer.append(layer_array[i])
            final_layers.append(single_layer)
        else:
            final_layers[-1].append(layer_array[i])

    return final_layers

def count_numbers(layer_array, number):
    count = 0
    for layer in layer_array:
        amount = layer.count(number)
        count += amount

    return count

def find_result(layer_array):
    zeros = []
    for layer in layer_array:
        number = count_numbers(layer, "0")
        zeros.append([number, layer])

    zeros.sort()

    print(zeros)

    min_zeros = zeros[0]
    layers_for_result = min_zeros[1]
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
        print(len(input_string))
        layer_array = build_layers(input_string)
        result = find_result(layer_array)
        print(result)

    if args.part == "part2":
        print("part2")
