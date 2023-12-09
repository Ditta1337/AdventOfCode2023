with open("./09/input.txt") as f:
    data = f.readlines()


def parse_data(data):
    return [list(map(int, line.split())) for line in data]


def find_differences(sequence):
    length = len(sequence)
    differences = []
    for i in range(length - 1):
        differences.append(sequence[i + 1] - sequence[i])

    return differences


def main():
    ret = 0
    sequences = parse_data(data)

    for sequence in sequences:
        diff = sequence
        extrapolated = diff[-1]
        while diff[-1]:
            diff = find_differences(diff)
            extrapolated += diff[-1]

        ret += extrapolated

    print(ret)


main()
