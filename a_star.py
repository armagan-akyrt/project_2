import math
import heapq
from queue import PriorityQueue


class a_star:
    """Uses A* algorithm to find the shortest path between two nodes."""

    def __init__(self, graph, S, D):
        self.graph = graph
        self.S = S
        self.D = D
        self.repetitions = 0

    def find_shortest_path(self):
        # Initialize the priority queue with the starting node
        queue = PriorityQueue()
        queue.put(self.S, 0)

        # Initialize the cost and parent dictionaries
        cost = {self.S: 0}
        parent = {self.S: None}

        while not queue.empty():
            # Extract the node with the lowest cost
            current = queue.get()
            self.repetitions += 1

            # Return the shortest path and cost if we have reached the destination
            if current == self.D:
                path = self.reconstruct_path(parent, self.S, self.D)
                return path, cost[self.D], self.repetitions

            # Expand the neighbors of the current node
            for neighbor in self.graph[current]:
                self.repetitions += 1
                # Calculate the cost of the path from the starting node to the neighbor
                new_cost = cost[current] + self.graph[current][neighbor]

                # Update the cost and parent of the neighbor if the calculated cost is lower
                if neighbor not in cost or new_cost < cost[neighbor]:
                    cost[neighbor] = new_cost
                    priority = new_cost + self.heuristic(neighbor, self.D)
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

        # Reverse the path and return it
        return path[::-1]

    def heuristic(self, i, j):
        return abs(j - i)

    def get_repetition(self):
        return self.repetitions
