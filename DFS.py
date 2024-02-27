class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbors):
        self.graph[node] = neighbors

def dfs(graph, start, visited):
    if start not in visited:
        print(start, end=" ")
        visited.add(start)

        for neighbor in graph.graph[start]:
            dfs(graph, neighbor, visited)

# Example Usage:
# Create a graph and add edges
example_graph = Graph()
example_graph.add_edge(0, [1, 2])
example_graph.add_edge(1, [2])
example_graph.add_edge(2, [0, 3])
example_graph.add_edge(3, [3])

# Perform DFS starting from node 2
visited_nodes = set()
print("DFS starting from node 2:")
dfs(example_graph, 2, visited_nodes)
