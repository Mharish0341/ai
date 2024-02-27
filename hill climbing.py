import random

def hill_climbing(initial_state, objective_function, neighbors_function, max_iter=1000):
    current_state = initial_state

    for _ in range(max_iter):
        neighbors = neighbors_function(current_state)
        neighbor_states = [(neighbor, objective_function(neighbor)) for neighbor in neighbors]
        neighbor_states.sort(key=lambda x: x[1], reverse=True)  # Sort by objective function value

        if neighbor_states[0][1] <= objective_function(current_state):
            break  # If the current state is better or equal, break the loop

        current_state = neighbor_states[0][0]

    return current_state

# Example usage:
def objective_function(state):
    return -sum(state)  # Example objective function (minimization)

def neighbors_function(state):
    neighbors = []
    for i in range(len(state)):
        neighbor = list(state)
        neighbor[i] += random.uniform(-1, 1)  # Add a small random value to one element
        neighbors.append(tuple(neighbor))
    return neighbors

initial_state = tuple([random.uniform(0, 10) for _ in range(5)])  # Example initial state
result = hill_climbing(initial_state, objective_function, neighbors_function)

print("Initial State:", initial_state)
print("Optimal State:", result)
print("Optimal Value:", objective_function(result))
