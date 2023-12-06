from math import sqrt, floor, ceil

with open("./06/input.txt") as f:
    data = f.readlines()


def parse_data(data):
    times = list(map(int, data[0].split()[1:]))
    distances = list(map(int, data[1].split()[1:]))

    return times, distances


def find_winning_ways(t, d):
    delta = t**2 - 4 * d
    t1 = floor((-t + sqrt(delta)) / -2) + 1
    t2 = ceil((-t - sqrt(delta)) / -2) - 1

    return t2 - t1 + 1


def main():
    ret = 1
    times, distances = parse_data(data)
    for time, distance in zip(times, distances):
        ret *= find_winning_ways(time, distance)

    print(ret)


main()
