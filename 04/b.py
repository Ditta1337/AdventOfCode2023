with open("./04/input.txt") as f:
    data = f.readlines()

def parse_line(line):
    winning, my = line.replace("\n", "").split(":")[1].split("|")
    winning = winning.split()
    my = my.split()

    return [int(num) for num in winning], [int(num) for num in my]

def bin_search(my, winning_num): # O(log(n))
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
    found_matches = 0
    winning.sort()
    my.sort()
    for winning_num in winning:
        if bin_search(my, winning_num):
            found_matches += 1
    
    return found_matches

def main():
    ret = 0
    all_copies = {i:1 for i in range(len(data))}
    for card, line in enumerate(data):
        winning, my = parse_line(line)
        found_matches = find_matching(winning, my)
        for card_copy in range(card + 1, found_matches + card + 1):
            all_copies[card_copy] += all_copies[card]

    for value in all_copies.values():
        ret += value
    
    print(ret)


main()