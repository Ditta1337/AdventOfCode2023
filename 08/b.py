# taken from the internet (yt/HyperNeutrino) because
# the information given in the puzzle does not hint
# it should be solved with greatest common multiple
# the input data was crafted this way so it would
# create only one cycle, so the solution is not
# general.

import re
from math import gcd


with open("./08/input.txt") as f:
    data = f.readlines()

def parse_data(data):
    moves = data[0].replace("\n", "")
    graph = {}
    for line in data[2:]:
        line = re.sub(r"[ \(\)\n]", "", line)
        left, right = line.split("=")
        right1, right2 = right.split(",")
        graph.update({left:(right1, right2)})

    return moves, graph


def main():
    ret = 0
    cycles = []
    moves, graph = parse_data(data)
    starts = [key for key in graph.keys() if key[-1] == "A"]
    positions = starts

    for position in positions:
        count = 0
        cycle = []
        this_cycle_moves = moves
        found_cycle = False
        first_found_end = None
        while not found_cycle:
            while count == 0 or not position[-1] == "Z":
                count += 1
                if this_cycle_moves[0] == "R":
                    position = graph[position][1]
                else:
                    position = graph[position][0]
                this_cycle_moves = this_cycle_moves[1:] + this_cycle_moves[0]

            cycle.append(count)

            if first_found_end is None:
                first_found_end = position
                count = 0
            elif position == first_found_end:
                found_cycle = True

        cycles.append(cycle)

    nums = [cycle[0] for cycle in cycles]

    lcm = nums.pop()

    for num in nums:
        lcm = lcm * num // gcd(lcm, num)

    ret = lcm
     
    print(ret)

main()


