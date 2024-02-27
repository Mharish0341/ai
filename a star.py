import heapq

class Node:
    def __init__(self, state, parent=None, action=None, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.heuristic = heuristic
    
    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def astar_search(initial_state, goal_test, successors, heuristic):
    frontier = []
    heapq.heappush(frontier, Node(initial_state, None, None, 0, heuristic(initial_state)))
    explored = set()
    
    while frontier:
        current_node = heapq.heappop(frontier)
        current_state = current_node.state
        
        if goal_test(current_state):
            return get_solution_path(current_node)
        
        explored.add(current_state)
        
        for action, next_state, step_cost in successors(current_state):
            if next_state not in explored:
                new_cost = current_node.cost + step_cost
                new_node = Node(next_state, current_node, action, new_cost, heuristic(next_state))
                heapq.heappush(frontier, new_node)
    
    return None  

def get_solution_path(node):
    path = []
    while node:
        path.append((node.action, node.state))
        node = node.parent
    return list(reversed(path))

def euclidean_distance(state):
    goal_state = (0, 0) 
    return ((state[0] - goal_state[0])**2 + (state[1] - goal_state[1])**2)**0.5

def goal_test(state):
    return state == (0, 0)  

def successors(state):
    x, y = state
    possible_actions = [('up', (x, y + 1), 1), ('down', (x, y - 1), 1),
                        ('left', (x - 1, y), 1), ('right', (x + 1, y), 1)]
    return [(action, next_state, cost) for action, next_state, cost in possible_actions
            if 0 <= next_state[0] <= 10 and 0 <= next_state[1] <= 10]  

initial_state = (5, 5) 
solution = astar_search(initial_state, goal_test, successors, euclidean_distance)
print(solution)
