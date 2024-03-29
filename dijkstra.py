import heapq


class Dijkstra:
    """Dijkstra's algorithm"""
    def __init__(self, graph, S, D):
        """
        Initialize the algorithm with the given graph, source node S, and destination node D.
        """
        self.graph = graph  # the input graph, represented as a dictionary of node: {neighbor: distance} pairs
        self.S = S  # the source node
        self.D = D  # the destination node
        self.repetitions = 0  # initialize counter for total number of repetitions

    def find_shortest_path(self):
        """
        Find the shortest path from the source node to the destination node in the graph.
        """
        # Initialize distances to all nodes as infinite and distance to source as 0
        distances = {node: float('inf') for node in self.graph}
        distances[self.S] = 0

        # Initialize min heap with all nodes and their distances
        min_heap = []
        for node, distance in distances.items():
            heapq.heappush(min_heap, (distance, node))
        self.repetitions += 1  # increment counter for block of repetition

        # Initialize previous node for each node as None
        previous = {node: None for node in self.graph}

        # While there are nodes in the min heap
        while min_heap:
            # Extract node with minimum distance from min heap
            distance, current_node = heapq.heappop(min_heap)
            self.repetitions += 1  # increment counter for block of repetition

            # Stop if we have reached the destination node
            if current_node == self.D:
                break

            # Iterate through all neighbors of current node
            for neighbor, neighbor_distance in self.graph[current_node].items():
                self.repetitions += 1  # increment counter for block of repetition

                # Calculate new distance to neighbor
                new_distance = distance + neighbor_distance

                # If new distance is shorter than current distance, update distance and previous node
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous[neighbor] = current_node

                    # Add neighbor to min heap
                    heapq.heappush(min_heap, (new_distance, neighbor))

        # Create list to store shortest path
        shortest_path = []

        # Start from destination and work backwards to find shortest path
        current_node = self.D
        while current_node is not None:
            shortest_path.append(current_node)
            current_node = previous[current_node]
            self.repetitions += 1  # increment counter for block of repetition

        # Reverse the list to get the correct order of the shortest path
        shortest_path = shortest_path[::-1]
        repetitions = self.repetitions
        # Return the shortest path and the cost of the path
        return shortest_path, distances[self.D], repetitions

    def get_repetitions(self):
        """
        Returns the total number of repetitions.
        """
        return self.repetitions
