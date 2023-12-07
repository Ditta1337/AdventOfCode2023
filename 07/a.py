with open("./07/input.txt") as f:
    data = f.readlines()

HIGH_CARDS_DICT = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
LOW_CARDS_DICT = {str(i): i for i in range(2, 10)}
CARDS_DICT = {**HIGH_CARDS_DICT, **LOW_CARDS_DICT}


def parse_data(data):
    hands = []
    bids = []
    for line in data:
        split_line = line.replace("\n", "").split()
        hands.append(split_line[0])
        bids.append(int(split_line[1]))

    return list(zip(hands, bids))


def find_type(hand):
    hand_dict = {}
    for card in hand:
        if card in hand_dict:
            hand_dict[card] += 1
        else:
            hand_dict.update({card: 1})

    hand_tab = sorted(hand_dict.items(), key=lambda item: item[1], reverse=True)
    hand_len = len(hand_tab)

    if hand_len == 1:
        return 6  # 6 - five of a kind
    elif hand_len == 2:
        if hand_tab[0][1] == 4:
            return 5  # 5 - four of a kind
        else:
            return 4  # 4 - full house
    elif hand_len == 3:
        if hand_tab[0][1] == 3:
            return 3  # 3 - three of a kind
        else:
            return 2  # 2 - two pairs
    elif hand_len == 4:
        return 1  # 1 - one pair
    else:
        return 0  # 0 - high card


def compare_draw_hands(hand1, hand2):
    for card1, card2 in zip(hand1, hand2):
        if CARDS_DICT[card1] > CARDS_DICT[card2]:
            return 1
        elif CARDS_DICT[card1] < CARDS_DICT[card2]:
            return 0

    return 1  # draw, no particular order


def compare_hands(hand1, hand2):
    hand1_type = find_type(hand1)
    hand2_type = find_type(hand2)

    if hand1_type > hand2_type:
        return 1
    elif hand1_type < hand2_type:
        return 0
    else:
        return compare_draw_hands(hand1, hand2)


def partition(hands_and_bids, low, high):
    pivot_hand = hands_and_bids[high][0]
    i = low - 1
    for j in range(low, high):
        if compare_hands(pivot_hand, hands_and_bids[j][0]):
            i += 1
            hands_and_bids[i], hands_and_bids[j] = hands_and_bids[j], hands_and_bids[i]
    hands_and_bids[i + 1], hands_and_bids[high] = (
        hands_and_bids[high],
        hands_and_bids[i + 1],
    )

    return i + 1


def quick_sort_hands(hands_and_bids, low, high):  # O(nlogn)
    if low < high:
        p = partition(hands_and_bids, low, high)
        quick_sort_hands(hands_and_bids, low, p - 1)
        quick_sort_hands(hands_and_bids, p + 1, high)


def main():
    ret = 0
    hands_and_bids = parse_data(data)
    quick_sort_hands(hands_and_bids, 0, len(hands_and_bids) - 1)
    for i, (_, bid) in enumerate(hands_and_bids):
        ret += (i + 1) * bid

    print(ret)


main()
