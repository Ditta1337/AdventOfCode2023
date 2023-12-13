with open("./13/input.txt") as f:
    data = f.readlines()


def parse_data(data):
    mirrors = []
    mirror = []
    for line in data:
        if line != "\n":
            mirror.append(line)
        else:
            mirrors.append(mirror)
            mirror = []
    mirrors.append(mirror)
    mirrors = [[line.replace("\n", "") for line in mirror] for mirror in mirrors]

    return mirrors


def flip_mirror(mirror):
    flipped_mirror = []
    for i in range(len(mirror[0])):
        flipped_line = ""
        for line in mirror:
            flipped_line += line[i]
        flipped_mirror.append(flipped_line)

    return flipped_mirror


def find_mirror_horizontal(mirror):
    for distance in range(1, len(mirror)):
        first_half = mirror[:distance][::-1]
        second_half = mirror[distance:]

        first_half = first_half[: len(second_half)]
        second_half = second_half[: len(first_half)]

        if first_half == second_half:
            return distance
    return 0


def main():
    ret = 0
    mirrors = parse_data(data)
    for mirror in mirrors:
        horizontal_val = find_mirror_horizontal(mirror)
        vertical_val = find_mirror_horizontal(flip_mirror(mirror))

        ret += 100 * horizontal_val + vertical_val

    print(ret)


main()
