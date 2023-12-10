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

OPENING_COMBO = {
    "F": "J",
    "L": "7",
    "|": "|",
}

CLOSING_COMBO = {"F": "7", "L": "J"}


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
    last_moves = []

    for y_n, x_n in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
        y_p, x_p = y + y_n, x + x_n
        if 0 <= x_p < maze_w and 0 <= y_p < maze_h:
            pipe = maze[y_p][x_p]
            if pipe in PIPES.keys() and [-y_n, -x_n] in PIPES[pipe]:
                last_moves.append([y_n, x_n])

    for new_pipe in PIPES.keys():
        if last_moves[0] in PIPES[new_pipe] and last_moves[1] in PIPES[new_pipe]:
            new_row = ""
            for i, pipe in enumerate(maze[y]):
                if i != x:
                    new_row += pipe
                else:
                    new_row += new_pipe
            maze[y] = new_row
            break

    return [y + last_moves[-1][0], x + last_moves[-1][1]], last_moves[-1]


def walk_through_maze(maze, s):
    path = [[] for _ in range(len(maze))]
    path[s[0]].append(s)
    [y, x], last_move = find_start_move(s, maze)

    while [y, x] != s:
        path[y].append([y, x])
        pipe = maze[y][x]
        for y_n, x_n in PIPES[pipe]:
            if [y_n, x_n] != [-last_move[0], -last_move[1]]:
                last_move = [y_n, x_n]
                y, x = y + y_n, x + x_n
                break

    for row in path:
        row.sort()

    return path


def print_path(maze, path):
    maze_h = len(maze)
    maze_w = len(maze[0])

    for i in range(maze_h):
        for j in range(maze_w):
            if [i, j] in path[i]:
                print(maze[i][j], end="")
            else:
                print(" ", end="")
        print()


def main():
    ret = 0
    maze, s = parse_data(data)
    path = walk_through_maze(maze, s)

    # print_path(maze, path)

    for row in path:
        o = 0
        combo = ""
        combo_pipes = []
        start_appended = False
        for pipe in row:
            y, x = pipe
            combo += maze[y][x]
            if o and not start_appended:
                combo_pipes.append(pipe)
                start_appended = True
            if OPENING_COMBO[combo[0]] == maze[y][x]:
                o += 1
                combo = ""
                if o == 1:
                    combo_pipes.append(pipe)
            if combo and CLOSING_COMBO[combo[0]] == maze[y][x]:
                if o == 1:
                    ret -= len(combo)
                combo = ""
                start_appended = False
            if o == 2:
                ret += max(abs(combo_pipes[-1][1] - combo_pipes[0][1]) - 1, 0)
                combo_pipes = []
                o = 0
                start_appended = False

    print(ret)


main()
