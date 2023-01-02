from queue import PriorityQueue


class a_star:
    """Uses A* algorithm to find the shortest path between two nodes."""

    def __init__(self, graph, S, D):
        # Initialize the instance variables for the class
        self.graph = graph  # The graph as an adjacency list
        self.S = S  # The source node
        self.D = D  # The destination node
        self.repetitions = 0  # Number of repetitions, initialized to 0
        self.g_cost = {S: 0}  # A dictionary that holds the g costs between any vertex and source
        self.f_cost = {S: self.heuristic(S, D)}  # A dictionary that holds the f costs between every vertex and destination

    def find_shortest_path(self):
        # Initialize the priority queue with the starting node
        queue = PriorityQueue()  # Create a new PriorityQueue object
        queue.put(self.S, 0)  # Insert the source node into the priority queue

        # Initialize the parent dictionary
        parent = {self.S: None}  # Initialize the parent of the source node to None

        while not queue.empty():  # While the queue is not empty
            # Extract the node with the lowest f_cost
            current = queue.get()  # Get the next node in the queue

            self.repetitions += 1  # Increment the number of repetitions

            # Return the shortest path and cost if we have reached the destination
            if current == self.D:
                path = self.reconstruct_path(parent, self.S, self.D)  # Reconstruct the path to return
                return path, self.g_cost[
                    self.D], self.repetitions  # Return the path, distance between S and D, and number of repetitions.

            # Expand the neighbors of the current node
            for neighbor in self.graph[current]:
                self.repetitions += 1  # Increment the number of repetitions

                # Calculate the cost of the path from the starting node to the neighbor
                new_g_cost = self.g_cost[current] + self.graph[current][neighbor]

                # Update the g_cost and parent of the neighbor if the calculated cost is lower
                if neighbor not in self.g_cost or new_g_cost < self.g_cost[neighbor]:
                    self.g_cost[neighbor] = new_g_cost
                    self.f_cost[neighbor] = new_g_cost + self.heuristic(neighbor, self.D)
                    priority = self.f_cost[neighbor]  # The priority of the neighbor is the f cost
                    queue.put(neighbor, priority)  # Insert the neighbor into the priority queue
                    parent[neighbor] = current  # Update the parent of the neighbor

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
