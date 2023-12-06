with open("./05/input.txt") as f:
    data = f.readlines()


def parse_data(data):
    data = [line.replace(" map:", "").split() for line in data if line != "\n"]
    seeds = [int(seed) for seed in data[0][1:]]
    seed_ranges = []
    i = 0
    while i < len(seeds):
        seed_ranges.append([seeds[i], seeds[i] + seeds[i + 1]])
        i += 2

    maps = []
    new_map = []
    for line in data[1:]:
        if len(line) == 1:
            if len(new_map):
                maps.append(new_map)
            new_map = []
        else:
            new_map.append([int(number) for number in line])

    maps.append(new_map)

    return seed_ranges, maps


def pass_through_maps(seed_ranges, maps):
    for map in maps:
        new_ranges = []
        while seed_ranges:
            r_start, r_stop = seed_ranges.pop()
            for d, s, r in map:
                o_start = max(r_start, s)
                o_stop = min(r_stop, s + r)
                if o_start < o_stop:
                    new_ranges.append([o_start - s + d, o_stop - s + d])
                    if o_start > r_start:
                        seed_ranges.append([r_start, o_start])
                    if o_stop < r_stop:
                        seed_ranges.append([o_stop, r_stop])
                    break
            else:
                new_ranges.append([r_start, r_stop])
        seed_ranges = new_ranges

    return seed_ranges


def main():
    ret = 9**9
    seed_ranges, maps = parse_data(data)

    mapped_seeds = pass_through_maps(seed_ranges, maps)

    for a, _ in mapped_seeds:
        ret = min(ret, a)

    print(ret)


main()
