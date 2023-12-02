with open('./02/input.txt') as f:
    data = f.readlines()

MAX_CUBES = {"red":12, "green":13, "blue":14}

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
        flag = 1
        game, subsets = parse_line(line)
        for subset in subsets:
            for key in subset.keys():
                if subset[key] > MAX_CUBES[key]:
                    flag = 0
                    break
            if not flag:
                break

        if flag:
            ret += game

    print(ret)

main()
