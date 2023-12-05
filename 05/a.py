with open("./05/input.txt") as f:
    data = f.readlines()

def parse_data(data):
    data = [line.replace(" map:", "").split() for line in data if line != "\n"]
    seeds = [int(seed) for seed in data[0][1:]]
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
    
    return seeds, maps

def pass_through_maps(seed, maps):
    mapped_seed = seed
    for m in maps:
        for (d, s, r) in m: # d - destination, s - source, r - range
            dist = mapped_seed - s
            if 0 <= dist < r:
                mapped_seed = d + dist
                break
    
    return mapped_seed

def main():
    mapped_seeds = []
    seeds, maps = parse_data(data)
    for seed in seeds:
        mapped_seeds.append(pass_through_maps(seed, maps))

    print(min(mapped_seeds))

main()