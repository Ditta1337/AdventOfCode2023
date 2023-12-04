with open("./04/input.txt") as f:
    data = f.readlines()


def parse_line(line):
    winning, my = line.replace("\n", "").split(":")[1].split("|")
    winning = winning.split()
    my = my.split()

    return [int(num) for num in winning], [int(num) for num in my]


def bin_search(my, winning_num):  # O(log(n))
    low = 0
    high = len(my) - 1
    while low <= high:
        mid = (low + high) // 2
        if my[mid] == winning_num:
            return True
        elif my[mid] > winning_num:
            high = mid - 1
        else:
            low = mid + 1
    return False


def find_matching(winning, my):
    found_matches = -1
    winning.sort()
    my.sort()
    for winning_num in winning:
        if bin_search(my, winning_num):
            found_matches += 1

    return found_matches


def main():
    ret = 0
    for line in data:
        winning, my = parse_line(line)
        found_matches = find_matching(winning, my)
        if found_matches != -1:
            ret += 2**found_matches

    print(ret)


main()
