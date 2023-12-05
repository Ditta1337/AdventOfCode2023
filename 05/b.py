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


def find_intersection(range1, range2):
    a, b = range1
    c, d = range2
    if c <= a <= b <= d:
        return [a, b]
    elif a <= c <= d <= b:
        return [c, d]
    elif a <= c <= b <= d:
        return [c, b]
    elif c <= a <= d <= b:
        return [a, d]
    else:
        return None


def split_range(range1, range2):
    a, b = range1
    c, d = range2
    result = []
    if a <= c <= d <= b:
        ranges = [[a, c], [c, d], [d, b]]
    elif a <= c <= b <= d:
        ranges = [[a, c], [c, b]]
    elif c <= a <= d <= b:
        ranges = [[a, d], [d, b]]
    else:
        ranges = [[a, b]]

    for r in ranges:
        if r[0] != r[1]:
            result.append(r)

    return result


def pass_through_maps(seed_range, maps):
    mapped_seed_ranges = [seed_range]
    for m in maps:
        for d, s, r in m:  # d - destination, s - source, r - range
            new_seed_ranges = []
            for range in mapped_seed_ranges:
                mapped_seed_ranges.remove(range)
                mapping_range = [s, s + r - 1]
                new_seed_ranges.extend(split_range(range, mapping_range))
                for new_seed_range in new_seed_ranges:
                    if new_seed_range == find_intersection(
                        new_seed_range, mapping_range
                    ):
                        new_seed_ranges.remove(new_seed_range)
                        new_seed_ranges.append(
                            [d + new_seed_range[0] - s, d + new_seed_range[1] - s]
                        )
            mapped_seed_ranges.extend(new_seed_ranges)

    return mapped_seed_ranges


def main():
    ret = 9**9
    mapped_seeds = []
    seed_ranges, maps = parse_data(data)

    for seed_range in seed_ranges:
        mapped_seeds.extend(pass_through_maps(seed_range, maps))

    for seed_range in mapped_seeds:
        ret = min(ret, seed_range[0])

    print(ret)


main()
