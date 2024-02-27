
from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbors):
        self.graph[node] = neighbors

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        current_node = queue.popleft()
        print(current_node, end=" ")

        for neighbor in graph.graph[current_node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

# Example Usage:
# Create a graph and add edges
example_graph = Graph()
example_graph.add_edge(0, [1, 2])
example_graph.add_edge(1, [2])
example_graph.add_edge(2, [0, 3])
example_graph.add_edge(3, [3])

# Perform BFS starting from node 2
print("BFS starting from node 2:")
bfs(example_graph, 2)
