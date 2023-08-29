from collections import deque
class State:
    def __init__(self, missionaries_left, cannibals_left, boat_left, missionaries_right, cannibals_right):
        self.missionaries_left = missionaries_left
        self.cannibals_left = cannibals_left
        self.boat_left = boat_left
        self.missionaries_right = missionaries_right
        self.cannibals_right = cannibals_right

    def is_valid(self):
        if self.missionaries_left < 0 or self.missionaries_right < 0 or \
           self.cannibals_left < 0 or self.cannibals_right < 0:
            return False
        if self.missionaries_left > 3 or self.missionaries_right > 3 or \
           self.cannibals_left > 3 or self.cannibals_right > 3:
            return False
        if (self.cannibals_left > self.missionaries_left > 0) or \
           (self.cannibals_right > self.missionaries_right > 0):
            return False
        return True

    def is_goal(self):
        return self.missionaries_left == 0 and self.cannibals_left == 0

    def __eq__(self, other):
        return self.missionaries_left == other.missionaries_left and \
               self.cannibals_left == other.cannibals_left and \
               self.boat_left == other.boat_left and \
               self.missionaries_right == other.missionaries_right and \
               self.cannibals_right == other.cannibals_right

    def __hash__(self):
        return hash((self.missionaries_left, self.cannibals_left, self.boat_left,
                     self.missionaries_right, self.cannibals_right))
def bfs():
    start_state = State(3, 3, 1, 0, 0)
    goal_state = State(0, 0, 0, 3, 3)

    if start_state == goal_state:
        return [start_state]

    visited = set()
    queue = deque([start_state])
    parent = {}

    while queue:
        current_state = queue.popleft()

        if current_state.is_goal():
            path = []
            while current_state:
                path.append(current_state)
                current_state = parent.get(current_state)
            path.reverse()
            return path

        visited.add(current_state)

        for action in [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]:
            new_state = move(current_state, action)
            if new_state.is_valid() and new_state not in visited:
                queue.append(new_state)
                parent[new_state] = current_state

    return None

def move(state, action):
    missionaries_left = state.missionaries_left - action[0] * state.boat_left
    cannibals_left = state.cannibals_left - action[1] * state.boat_left
    boat_left = 1 - state.boat_left
    missionaries_right = state.missionaries_right + action[0] * state.boat_left
    cannibals_right = state.cannibals_right + action[1] * state.boat_left
    return State(missionaries_left, cannibals_left, boat_left,
                 missionaries_right, cannibals_right)

def print_solution(solution):
    for i, state in enumerate(solution):
        print(f"Step {i}:\n"
              f"Left: {state.missionaries_left}M {state.cannibals_left}C\n"
              f"Right: {state.missionaries_right}M {state.cannibals_right}C\n"
              f"Boat: {'Left' if state.boat_left == 1 else 'Right'}\n")

if __name__ == "__main__":
    solution = bfs()
    if solution:
        print("Solution found:")
        print_solution(solution)
    else:
        print("No solution found.")
