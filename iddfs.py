import sys
import copy

class Node:
    def __init__(self, state, parent=None, action=None, depth=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.depth = depth

class Problem:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state
    
    def is_goal(self, state):
        return state == self.goal_state
        
    def get_successors(self, state):
        successors = []
        r, c = -1, -1
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    r, c = i, j
                    break
            if r != -1:
                break
        
        moves = [(-1, 0, 'UP'), (1, 0, 'DOWN'), (0, -1, 'LEFT'), (0, 1, 'RIGHT')]
        
        for dr, dc, action in moves:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 3 and 0 <= nc < 3:
                new_state = copy.deepcopy(state)
                new_state[r][c], new_state[nr][nc] = new_state[nr][nc], new_state[r][c]
                successors.append((action, new_state))
                
        return successors

def expand(problem, node):
    children = []
    for action, next_state in problem.get_successors(node.state):
        child_node = Node(
            state=next_state,
            parent=node,
            action=action,
            depth=node.depth + 1
        )
        children.append(child_node)
    return children

def is_cycle(node):
    current = node.parent
    while current is not None:
        if current.state == node.state:
            return True
        current = current.parent
    return False

def depth_limited_search(problem, limit):
    initial_node = Node(state=problem.initial_state, depth=0)
    frontier = [initial_node] 
    result = "failure"
    
    while len(frontier) > 0:
        node = frontier.pop()
        
        if problem.is_goal(node.state):
            return node
            
        if node.depth > limit:
            result = "cutoff"
        elif not is_cycle(node):
            for child in expand(problem, node):
                frontier.append(child)
                
    return result

def iterative_deepening_search(problem):
    for depth in range(sys.maxsize):
        result = depth_limited_search(problem, depth)
        if result != "cutoff":
            return result
    return "failure"

def print_solution(node):
    if node == "failure" or node == "cutoff":
        print("Không tìm thấy lời giải.")
        return
    path = []
    current = node
    while current.parent is not None:
        path.append((current.action, current.state))
        current = current.parent
    path.reverse()
    
    print("Trạng thái bắt đầu:")
    for row in current.state:
        print(row)
    print("-" * 15)
    
    for action, state in path:
        print(f"Di chuyển ô trống sang: {action}")
        for row in state:
            print(row)
        print("-" * 15)

if __name__ == "__main__":
    start = [
        [1, 2, 3],
        [4, 0, 6],
        [7, 5, 8]
    ]
    
    goal = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]
    
    puzzle_problem = Problem(start, goal)
    solution_node = iterative_deepening_search(puzzle_problem)
    print_solution(solution_node)