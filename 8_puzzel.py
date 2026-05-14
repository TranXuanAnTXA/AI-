from copy import deepcopy
from collections import deque


start =[[1,2,3],
         [5,'.',6],
         [4,7,8]]

goal = [[1,2,3],
        [4,5,6],
        [7,8,'.']]


def print_state(s):
    for row in s:
        print(row)
    print()


def find_blank(s):
    for r in range(3):
        for c in range(3):
            if s[r][c] == '.':
                return r, c



def rule_match(s):

    x, y = find_blank(s)

    rules = []

    if x > 0:
        rules.append("UP")

    if x < 2:
        rules.append("DOWN")

    if y > 0:
        rules.append("LEFT")

    if y < 2:
        rules.append("RIGHT")

    return rules


def move(s, direction):

    x, y = find_blank(s)

    new_state = deepcopy(s)

    if direction == "UP":

        new_state[x][y], new_state[x-1][y] = new_state[x-1][y], new_state[x][y]

    elif direction == "DOWN":

        new_state[x][y], new_state[x+1][y] = new_state[x+1][y], new_state[x][y]

    elif direction == "LEFT":

        new_state[x][y], new_state[x][y-1] = new_state[x][y-1], new_state[x][y]

    elif direction == "RIGHT":

        new_state[x][y], new_state[x][y+1] = new_state[x][y+1], new_state[x][y]

    return new_state


def to_string(s):

    result = ""

    for row in s:
        for value in row:
            result += str(value)

    return result


def bfs(start):

    queue = deque()

    queue.append((start, []))

    visited = set()

    visited.add(to_string(start))

    while queue:

        current_state, path = queue.popleft()

        # KIEM TRA GOAL
        if current_state == goal:

            print("TIM THAY LOI GIAI")
            print("So buoc:", len(path))
            print("Duong di:", path)

            return path

        # SINH CAC HUONG
        rules = rule_match(current_state)

        for r in rules:

            child = move(current_state, r)

            child_string = to_string(child)

            # NEU CHUA XET
            if child_string not in visited:

                visited.add(child_string)

                new_path = path + [r]

                queue.append((child, new_path))

    print("Khong tim thay loi giai")

print("TRANG THAI BAT DAU:")
print_state(start)

bfs(start)