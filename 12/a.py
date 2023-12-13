with open("./12/input.txt") as f:
    data = f.readlines()


def parse_data(data):
    springs_row = []

    for line in data:
        row, record = line.replace("\n", "").split(" ")
        record = [int(val) for val in record.split(",")]

        springs_row.append([row, record])

    return springs_row


def check_finish(row, record):
    sequences = []
    counter = 0
    for i, field in enumerate(row):
        if field == "#":
            counter += 1
            if i == len(row) - 1:
                sequences.append(counter)
        elif counter:
            sequences.append(counter)
            counter = 0

    return True if sequences == record else False


def brute_force(row, record):
    arrangements = 0
    counter = 0
    unknown = []
    for i, field in enumerate(row):
        if field == "?":
            counter += 1
            unknown.append(i)

    max_checks = 2**counter

    for i in range(max_checks):
        bin_str = bin(i)[2:].zfill(counter)
        for j, val in enumerate(bin_str):
            row[unknown[j]] = "#" if val == "1" else "."

        if check_finish(row, record):
            arrangements += 1

    return arrangements


def main():
    ret = 0
    springs_row = parse_data(data)
    for i, (row, record) in enumerate(springs_row):
        print(f"Checking {i + 1}/{len(springs_row)}")
        ret += brute_force(list(row), record)

    print(ret)


main()


parse_data(data)
