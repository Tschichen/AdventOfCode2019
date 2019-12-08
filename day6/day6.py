import argparse
import networkx as nx


def parse_input(file, input_array):
    for line in file:
        line_strip = line.strip()
        input_array.append(line_strip)


def add_edge(G, node_name_1, node_name_2):
    for node in G.nodes(data=True):
        if node_name_1 == node[1]['name']:
            break
    else:
        G.add_node(node_name_1, name=node_name_1)

    for node in G.nodes(data=True):
        if node_name_2 == node[1]['name']:
            break
    else:
        G.add_node(node_name_2, name=node_name_2)

    G.add_edge(node_name_2, node_name_1)

def parse_input_list(G, input_array):
    for entry in input_array:
        node1 = entry[0:3]
        node2 = entry[4:]
        add_edge(G, node1, node2)

def calculate_path_length_to_COM(G, node_name):
    length = nx.shortest_path_length(G, node_name, 'COM')
    return length

def calculate_result(G):
    result = 0
    for node in G.nodes:
        length = calculate_path_length_to_COM(G, node)
        result += length

    return result

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--infile', required=True)
    parser.add_argument('-p', '--part', help="enter 'part1' or 'part2'. default: 'part1'", default='part1')
    args = parser.parse_args()

    input_array = []
    with open(args.infile) as file:
        parse_input(file, input_array)

    if args.part == "part1":
        print("part1")
        G = nx.DiGraph()
        G.add_node('COM', name='COM')
        parse_input_list(G, input_array)
        length = calculate_result(G)
        print("total length: ", length)

    if args.part == "part2":
        print("part2")
        G = nx.Graph()
        G.add_node('COM', name='COM')
        parse_input_list(G, input_array)
        length = nx.shortest_path_length(G, 'SAN', 'YOU')
        print(length)
        print("result: ", length-2)