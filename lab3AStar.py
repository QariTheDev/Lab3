class Graph:
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def get_neighbors(self, node):
        return self.adjacency_list.get(node, [])

    def heuristic(self, node):
        heuristic_values = {
            "The": 4, "cat": 3, "dog": 3, "runs": 2, "fast": 1
        }
        return heuristic_values.get(node, float('inf'))

    def a_star_algorithm(self, start, goal):
        open_set = {start}
        closed_set = set()
        g_cost = {start: 0}
        parents = {start: None}

        while open_set:
            current_node = None
            current_f_cost = float('inf')

            for node in open_set:
                f_cost = g_cost[node] + self.heuristic(node)
                if f_cost < current_f_cost:
                    current_f_cost = f_cost
                    current_node = node

            if current_node == goal:
                # Reconstruct path
                path = []
                while current_node:
                    path.append(current_node)
                    current_node = parents[current_node]
                return list(reversed(path)), g_cost[goal]

            open_set.remove(current_node)
            closed_set.add(current_node)

            for neighbor, cost in self.get_neighbors(current_node):
                if neighbor in closed_set:
                    continue

                new_g_cost = g_cost[current_node] + cost

                if neighbor not in open_set or new_g_cost < g_cost.get(neighbor, float('inf')):
                    g_cost[neighbor] = new_g_cost
                    parents[neighbor] = current_node
                    open_set.add(neighbor)

        return None, float('inf')

adjacency_list = {
    "The": [("cat", 1), ("dog", 2)],
    "cat": [("runs", 2)],
    "dog": [("runs", 2)],
    "runs": [("fast", 1)]
}

graph = Graph(adjacency_list)
path, total_cost = graph.a_star_algorithm("The", "fast")

print("Sentence:", " ".join(path))
print("Total cost:", total_cost)