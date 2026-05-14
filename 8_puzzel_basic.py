from copy import deepcopy

state = [[1,3,5],
         [4,6,8],
         [2,7,'.']]

def print_state(s):
    for row in s:
        print(row)
    print()
    
def find_blank(s):
    for r in range(3):
        for c in range(3):
            if s[r][c] == '.':
                return r,c
def rule_match(s):
    x, y = find_blank(s)
    
    rules = []
    
    # lên
    if x > 0:
        rules.append("UP")

    # xuống
    if x < 2:
        rules.append("DOWN")

    # trái
    if y > 0:
        rules.append("LEFT")

    # phải
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


print("Trang thai ban dau:")
print_state(state)
RULE = rule_match(state)
for r in RULE:
    print("Trang thai tiep theo:")
    print("MOVE:", r)
    new_status = move(state, r)
    print_state(new_status)


    
    
    