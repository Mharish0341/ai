class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []

        self.graph[u].append(v)
        self.graph[v].append(u)

    def color_graph(self):
        color_map = {}
        colors = ['Red', 'Green', 'Blue', 'Yellow', 'Orange', 'Purple']  # Add more colors if needed

        for node in self.graph:
            used_colors = set(color_map.get(neighbour, None) for neighbour in self.graph[node])

            for color in colors:
                if color not in used_colors:
                    color_map[node] = color
                    break

        return color_map

# Example usage:
map_graph = Graph()
map_graph.add_edge('A', 'B')
map_graph.add_edge('A', 'C')
map_graph.add_edge('B', 'C')
map_graph.add_edge('B', 'D')
map_graph.add_edge('C', 'D')
map_graph.add_edge('D', 'E')

coloring = map_graph.color_graph()
print(coloring)
