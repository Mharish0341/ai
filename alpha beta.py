import math

def alpha_beta_pruning(node, depth, alpha, beta, maximizing_player):
    if depth == 0 or node.is_terminal():
        return node.evaluate()

    value = -math.inf if maximizing_player else math.inf

    for child in node.get_children():
        child_value = alpha_beta_pruning(child, depth - 1, alpha, beta, not maximizing_player)
        value = max(value, child_value) if maximizing_player else min(value, child_value)

        if maximizing_player:
            alpha = max(alpha, value)
        else:
            beta = min(beta, value)

        if beta <= alpha:
            break  # Pruning

    return value

# Hypothetical Node class representing a state in the game tree
class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def get_children(self):
        return self.children

    def is_terminal(self):
        return not self.children

    def evaluate(self):
        return self.value

# Example usage:
root = Node(0)
root.add_child(Node(3))
root.add_child(Node(5))
root.add_child(Node(2))

result = alpha_beta_pruning(root, 3, -math.inf, math.inf, True)
print("Optimal value:", result)
