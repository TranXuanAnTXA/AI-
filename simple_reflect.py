from copy import deepcopy

GOAL = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, '.']
]


# =========================
# HIỂN THỊ BOARD
# =========================
def print_board(board):
    for row in board:
        print(row)
    print()


# =========================
# TÌM Ô TRỐNG
# =========================
def find_blank(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == '.':
                return i, j


# =========================
# KIỂM TRA GOAL
# =========================
def goal_test(board):
    return board == GOAL


# =========================
# TÍNH ĐỘ "TỐT"
# Bao nhiêu ô đúng vị trí
# =========================
def score(board):

    cnt = 0

    for i in range(3):
        for j in range(3):

            if board[i][j] == GOAL[i][j]:
                cnt += 1

    return cnt


# =========================
# SINH ACTION HỢP LỆ
# =========================
def possible_actions(board):

    x, y = find_blank(board)

    actions = []

    if x > 0:
        actions.append("UP")

    if x < 2:
        actions.append("DOWN")

    if y > 0:
        actions.append("LEFT")

    if y < 2:
        actions.append("RIGHT")

    return actions


# =========================
# THỰC HIỆN ACTION
# =========================
def apply_action(board, action):

    x, y = find_blank(board)

    new_board = deepcopy(board)

    if action == "UP":
        new_board[x][y], new_board[x - 1][y] = \
            new_board[x - 1][y], new_board[x][y]

    elif action == "DOWN":
        new_board[x][y], new_board[x + 1][y] = \
            new_board[x + 1][y], new_board[x][y]

    elif action == "LEFT":
        new_board[x][y], new_board[x][y - 1] = \
            new_board[x][y - 1], new_board[x][y]

    elif action == "RIGHT":
        new_board[x][y], new_board[x][y + 1] = \
            new_board[x][y + 1], new_board[x][y]

    return new_board


# =========================
# SIMPLE REFLEX AGENT
# =========================
def simple_reflex_agent(board):

    actions = possible_actions(board)

    best_action = None
    best_score = -1

    # RULE MATCHING
    for action in actions:

        temp_board = apply_action(board, action)

        s = score(temp_board)

        # chọn action làm board tốt hơn
        if s > best_score:
            best_score = s
            best_action = action

    return best_action


# =========================
# MAIN
# =========================
board = [
    [1, 3, 5],
    [4, 6, 8],
    [2, 7, '.']
]

print("INITIAL STATE:\n")
print_board(board)

step = 0

while not goal_test(board):

    action = simple_reflex_agent(board)

    if action is None:
        print("STUCK!")
        break

    print(f"Step {step + 1}: {action}")

    board = apply_action(board, action)

    print_board(board)

    step += 1

    # tránh lặp vô hạn
    if step > 20:
        print("LOOP DETECTED")
        break


if goal_test(board):
    print("GOAL REACHED!")