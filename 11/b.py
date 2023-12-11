with open("./11/input.txt") as f:
    data = f.readlines()


def parse_data(data):
    cosmos = [line.replace("\n", "") for line in data]
    return cosmos


def find_voids(cosmos):
    cosmos_h = len(cosmos)
    cosmos_l = len(cosmos[0])
    row_voids = []
    column_voids = []

    for i, row in enumerate(cosmos):
        if "#" not in row:
            row_voids.append(i)

    for j in range(cosmos_l):
        for i in range(cosmos_h):
            if cosmos[i][j] == "#":
                break
        else:
            column_voids.append(j)

    return row_voids, column_voids


def find_galaxies(cosmos):
    galaxies = []
    for i, row in enumerate(cosmos):
        for j, col in enumerate(row):
            if col == "#":
                galaxies.append([i, j])

    return galaxies


def main():
    ret = 0
    cosmos = parse_data(data)
    row_voids, column_voids = find_voids(cosmos)
    galaxies = find_galaxies(cosmos)

    for i, (y_a, x_a) in enumerate(galaxies):
        for y_b, x_b in galaxies[i + 1:]:
            for y in range(min(y_a, y_b), max(y_a, y_b)):
                ret += 1 if y not in row_voids else 1000000
            for x in range(min(x_a, x_b), max(x_a, x_b)):
                ret += 1 if x not in column_voids else 1000000

    print(ret)


main()
