with open("./03/input.txt") as f:
    data = f.readlines()

NUMBERS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def find_numbers(data):
    numbers_info = []
    for row, line in enumerate(data):
        column = 0
        while column < len(line):
            number = ""
            number_length = 0
            while line[column] in NUMBERS:
                number += line[column]
                number_length += 1
                column += 1
            if number_length:
                numbers_info.append(
                    (row, column - number_length, number_length, int(number))
                )
            else:
                column += 1

    return numbers_info


def check_surroundings(
    number_info, data, data_bounds
):  # data_bounds = (length, height)
    length, height = data_bounds
    row, column, number_length, number = number_info
    gear_locations = []

    if data[row][-1] == "\n":
        length -= 1

    # check left to the number
    if column > 0 and data[row][column - 1] == "*":
        gear_locations.append((row, column - 1))

    # check right to the number
    if column < length - number_length and data[row][column + number_length] == "*":
        gear_locations.append((row, column + number_length))

    # check up to the number
    for i in range(number_length):
        if row > 0 and data[row - 1][column + i] == "*":
            gear_locations.append((row - 1, column + i))

    # check down to the number
    for i in range(number_length):
        if row < height - 1 and data[row + 1][column + i] == "*":
            gear_locations.append((row + 1, column + i))

    # check left upper corner of the number
    if column > 0 and row > 0 and data[row - 1][column - 1] == "*":
        gear_locations.append((row - 1, column - 1))

    # check right upper corner of the number
    if (
        column < length - number_length
        and row > 0
        and data[row - 1][column + number_length] == "*"
    ):
        gear_locations.append((row - 1, column + number_length))

    # check left lower corner of the number
    if column > 0 and row < height - 1 and data[row + 1][column - 1] == "*":
        gear_locations.append((row + 1, column - 1))

    # check right lower corner of the number
    if (
        column < length - number_length
        and row < height - 1
        and data[row + 1][column + number_length] == "*"
    ):
        gear_locations.append((row + 1, column + number_length))

    return number, gear_locations


def main():
    ret = 0
    numbers_info = find_numbers(data)
    data_bounds = (len(data[0]), len(data))
    gear_locations_dict = {}

    for number_info in numbers_info:
        number, gear_location = check_surroundings(number_info, data, data_bounds)

        for location in gear_location:
            if location in gear_locations_dict:
                gear_locations_dict[location].append(number)
            else:
                gear_locations_dict[location] = [number]

    for values in gear_locations_dict.values():
        if len(values) == 2:
            ret += values[0] * values[1]

    print(ret)


print()

main()
