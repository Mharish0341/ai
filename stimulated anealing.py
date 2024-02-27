import math
import random

def objective_function(x):
    # Define the objective function to minimize
    return x**2 + 5 * math.sin(x)

def acceptance_probability(current_energy, new_energy, temperature):
    # Calculate the acceptance probability
    if new_energy < current_energy:
        return 1.0
    return math.exp((current_energy - new_energy) / temperature)

def simulated_annealing(initial_solution, temperature, cooling_rate, num_iterations):
    current_solution = initial_solution
    current_energy = objective_function(current_solution)

    best_solution = current_solution
    best_energy = current_energy

    for iteration in range(num_iterations):
        # Generate a neighboring solution
        new_solution = current_solution + random.uniform(-0.1, 0.1)
        new_energy = objective_function(new_solution)

        # Decide whether to accept the new solution
        if random.random() < acceptance_probability(current_energy, new_energy, temperature):
            current_solution = new_solution
            current_energy = new_energy

        # Update the best solution if needed
        if current_energy < best_energy:
            best_solution = current_solution
            best_energy = current_energy

        # Cool the temperature
        temperature *= cooling_rate

    return best_solution, best_energy

# Example usage:
initial_solution = 2.0
initial_temperature = 100.0
cooling_rate = 0.95
num_iterations = 1000

best_solution, best_energy = simulated_annealing(initial_solution, initial_temperature, cooling_rate, num_iterations)

print("Best Solution:", best_solution)
print("Best Energy:", best_energy)
