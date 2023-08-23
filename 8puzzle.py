import heapq
import copy

class PuzzleNode:
    def __init__(self, state, parent=None, move=""):
        self.state = state
        self.parent = parent
        self.move = move
        self.g = 0 if parent is None else parent.g + 1
        self.h = self.calculate_heuristic()

    def calculate_heuristic(self):
        count = 0
        for i in range(3):
            for j in range(3):
                if self.state[i][j] != 0:
                    goal_i = (self.state[i][j] - 1) // 3
                    goal_j = (self.state[i][j] - 1) % 3
                    count += abs(i - goal_i) + abs(j - goal_j)
        return count

    def __lt__(self, other):
        return (self.g + self.h) < (other.g + other.h)

class EightPuzzle:
    def __init__(self, initial_state):
        self.initial_state = initial_state
        self.goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    def get_possible_moves(self, node):
        i, j = self.find_blank(node.state)
        possible_moves = []
        if i > 0:
            possible_moves.append(("Up", i - 1, j))
        if i < 2:
            possible_moves.append(("Down", i + 1, j))
        if j > 0:
            possible_moves.append(("Left", i, j - 1))
        if j < 2:
            possible_moves.append(("Right", i, j + 1))
        return possible_moves

    def find_blank(self, state):
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    return i, j

    def solve(self):
        open_list = []
        heapq.heappush(open_list, PuzzleNode(self.initial_state))
        visited = set()

        while open_list:
            current_node = heapq.heappop(open_list)
            if current_node.state == self.goal_state:
                return self.trace_solution(current_node)

            visited.add(tuple(map(tuple, current_node.state)))
            possible_moves = self.get_possible_moves(current_node)

            for move, new_i, new_j in possible_moves:
                new_state = copy.deepcopy(current_node.state)
                blank_i, blank_j = self.find_blank(new_state)
                new_state[blank_i][blank_j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[blank_i][blank_j]
                new_node = PuzzleNode(new_state, current_node, move)
                if tuple(map(tuple, new_state)) not in visited:
                    heapq.heappush(open_list, new_node)

        return None

    def trace_solution(self, node):
        solution = []
        while node:
            solution.append(node.state)
            node = node.parent
        solution.reverse()
        return solution

def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    initial_state = [
        [1, 2, 3],
        [4, 0, 5],
        [7, 8, 6]
    ]

    puzzle = EightPuzzle(initial_state)
    solution_steps = puzzle.solve()

    if solution_steps:
        for step, state in enumerate(solution_steps):
            print(f"Step {step + 1}:")
            print_board(state)
            print()
    else:
        print("No solution found.")
