import re

with open("./08/input.txt") as f:
    data = f.readlines()


def parse_data(data):
    moves = data[0].replace("\n", "")
    graph = {}
    for line in data[2:]:
        line = re.sub(r"[ \(\)\n]", "", line)
        left, right = line.split("=")
        right1, right2 = right.split(",")
        graph.update({left: (right1, right2)})

    return moves, graph


def main():
    ret = 0
    found = False
    moves, graph = parse_data(data)

    start = "AAA"
    end = "ZZZ"
    position = start

    while not found:
        if position != end:
            ret += 1
            if moves[0] == "R":
                position = graph[position][1]
            else:
                position = graph[position][0]
            moves = moves[1:] + moves[0]
        else:
            found = True
            break

    print(ret)


main()
