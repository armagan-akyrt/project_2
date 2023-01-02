from queue import PriorityQueue

class a_star:
    """Uses A* algorithm to find the shortest path between two nodes."""

    def __init__(self, graph, S, D):
        self.graph = graph  # graph
        self.S = S  # source
        self.D = D  # destination
        self.repetitions = 0    # number of repetitions
        self.g_cost = {S: 0}  # holds the g costs between any vertex and source
        self.f_cost = {S: self.heuristic(S, D)}  # hold the f costs between every vertex and destination

    def find_shortest_path(self):
        # Initialize the priority queue with the starting node
        queue = PriorityQueue()
        queue.put(self.S, 0)    # insert Source to priority queue

        # Initialize the parent dictionary
        parent = {self.S: None}

        while not queue.empty():
            # Extract the node with the lowest f_cost
            current = queue.get()
            self.repetitions += 1

            # Return the shortest path and cost if we have reached the destination
            if current == self.D:
                path = self.reconstruct_path(parent, self.S, self.D)    # reconstruct the path to return
                return path, self.g_cost[self.D], self.repetitions  # returns path, distance between S and D and number of repetitions.

            # Expand the neighbors of the current node
            for neighbor in self.graph[current]:
                self.repetitions += 1
                # Calculate the cost of the path from the starting node to the neighbor
                new_g_cost = self.g_cost[current] + self.graph[current][neighbor]

                # Update the g_cost and parent of the neighbor if the calculated cost is lower
                if neighbor not in self.g_cost or new_g_cost < self.g_cost[neighbor]:
                    self.g_cost[neighbor] = new_g_cost
                    self.f_cost[neighbor] = new_g_cost + self.heuristic(neighbor, self.D)
                    priority = self.f_cost[neighbor]
                    queue.put(neighbor, priority)
                    parent[neighbor] = current

        # Return None if no path was found
        return None, None, None

    def reconstruct_path(self, parent, S, D):
        # Initialize the path with the destination node
        path = [D]

        # Follow the parent pointers back to the starting node
        while D != S:
            self.repetitions += 1
            path.append(parent[D])
            D = parent[D]
        return path[::-1]

    def heuristic(self, i, j):
        return abs(i - j)

    def get_repetition(self):
        return self.repetitions

