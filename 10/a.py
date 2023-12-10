with open("./10/input.txt") as f:
    data = f.readlines()

PIPES = {
    "|": [[-1, 0], [1, 0]],
    "-": [[0, 1], [0, -1]],
    "L": [[-1, 0], [0, 1]],
    "J": [[-1, 0], [0, -1]],
    "7": [[1, 0], [0, -1]],
    "F": [[1, 0], [0, 1]],
}


def parse_data(data):
    maze = [line.replace("\n", "") for line in data]
    s = None
    for i, line in enumerate(maze):
        if "S" in line:
            s = [i, line.index("S")]

    return maze, s


def find_start_move(s, maze):
    y, x = s
    maze_h = len(maze)
    maze_w = len(maze[0])
    distance = 1
    last_move = None

    for y_n, x_n in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
        y_p, x_p = y + y_n, x + x_n
        if 0 <= x_p < maze_w and 0 <= y_p < maze_h:
            pipe = maze[y_p][x_p]
            if pipe in PIPES.keys() and [-y_n, -x_n] in PIPES[pipe]:
                last_move = [y_n, x_n]
                return [y_p, x_p], distance, last_move

    return -1


def main():
    maze, s = parse_data(data)

    [y, x], distance, last_move = find_start_move(s, maze)

    while [y, x] != s:
        pipe = maze[y][x]
        for y_n, x_n in PIPES[pipe]:
            if [y_n, x_n] != [-last_move[0], -last_move[1]]:
                last_move = [y_n, x_n]
                y, x = y + y_n, x + x_n
                distance += 1
                break

    ret = distance // 2

    print(ret)


main()
