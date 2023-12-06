from math import sqrt, floor, ceil

with open("./06/input.txt") as f:
    data = f.readlines()


def parse_data(data):
    time = int(data[0].split(":")[1].replace(" ", ""))
    distance = int(data[1].split(":")[1].replace(" ", ""))
    return time, distance


def find_winning_ways(t, d):
    delta = t**2 - 4 * d
    t1 = floor((-t + sqrt(delta)) / -2) + 1
    t2 = ceil((-t - sqrt(delta)) / -2) - 1

    return t2 - t1 + 1


def main():
    ret = 1
    time, distance = parse_data(data)
    ret *= find_winning_ways(time, distance)

    print(ret)


main()
