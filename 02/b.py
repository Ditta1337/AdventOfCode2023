with open('./02/input.txt') as f:
    data = f.readlines()

def parse_line(line):
    ret_subsets = []
    game, str_subsets = line.split(":")
    subsets = str_subsets.split(";")
    for subset in subsets:
        dict_stubset = {}
        parsed_subset = subset.replace(",", "").split()
        for i in range(0, len(parsed_subset), 2):
            dict_stubset.update({parsed_subset[i+1]:int(parsed_subset[i])})
        ret_subsets.append(dict_stubset)
        
    return int(game.split()[-1]), ret_subsets

def main():
    ret = 0
    for line in data:
        min_dict = {"red":0, "green":0, "blue":0}
        _, subsets = parse_line(line)
        for subset in subsets:
            for key in subset.keys():
                min_dict[key] = max(min_dict[key], subset[key])

        power = 1
        for value in min_dict.values():
            power *= value

        ret += power

    print(ret)

main()
