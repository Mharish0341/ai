class State:
    def __init__(self, missionaries, cannibals, boat):
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat = boat
        self.parent = None  # Added parent attribute

    def is_valid(self):
        if self.missionaries < 0 or self.cannibals < 0 or self.missionaries > 3 or self.cannibals > 3:
            return False
        if self.missionaries < self.cannibals and self.missionaries > 0:
            return False
        if 3 - self.missionaries < 3 - self.cannibals and 3 - self.missionaries > 0:
            return False
        return True

    def is_goal(self):
        return self.missionaries == 0 and self.cannibals == 0 and self.boat == 0

    def successors(self):
        moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
        next_states = []

        for move in moves:
            if self.boat == 1:
                next_state = State(self.missionaries - move[0], self.cannibals - move[1], 0)
            else:
                next_state = State(self.missionaries + move[0], self.cannibals + move[1], 1)

            if next_state.is_valid():
                next_state.parent = self  # Set the parent state
                next_states.append(next_state)

        return next_states

def bfs(initial_state):
    queue = [initial_state]

    while queue:
        current_state = queue.pop(0)
        if current_state.is_goal():
            print_path(current_state)  # Print the path when the goal is reached
            return True
        queue.extend(current_state.successors())

    return False

def print_path(state):
    if state:
        print("Solution found:")
        while state:
            if state.parent:
                if state.boat == 1:
                    print(f"Move {state.missionaries} missionaries and {state.cannibals} cannibals from right to left.")
                else:
                    print(f"Move {state.missionaries} missionaries and {state.cannibals} cannibals from left to right.")
            state = state.parent
    else:
        print("No solution found.")

# Initial state: 3 missionaries, 3 cannibals, boat on the left side
initial_state = State(3, 3, 1)

result = bfs(initial_state)
