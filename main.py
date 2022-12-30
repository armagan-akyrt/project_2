from a_star import a_star
import time
from dijkstra import Dijkstra
import matplotlib.pyplot as plt


def main():
    N = int(input("Please provide number of desired graphs: "))
    S = int(input("Please provide the source city: "))
    D = int(input("Please provide the destination city: "))
    # Creates the adjacency matrix for graph
    graph = {}
    for i in range(1, N + 1):   # project description clearly stated that first node should be 1
        set = {}    # set of outgoing edges for initial graph
        for j in range(1, N + 1):
            if abs(i - j) <= 3 and i != j:
                set[j] = i + j  # adds weights to the set

        graph[i] = set  # adds outgoing edges of initial number to graph

    a_star_test = a_star(graph, S, D)
    x = a_star_test.find_shortest_path()
    print(x)

    # Dijkstra Part 3
    c1 = 1
    # Set values for N
    ns = [10, 50, 100, 200, 500, 1000, 2000]

    # Set source and destination nodes
    S = 1

    # Initialize lists to store running times and total number of repetitions
    running_times = []
    repetitions = []

    # Loop through values of N
    for N in ns:
        # Creates the adjacency matrix for graph
        graph = {}
        for i in range(1, N + 1):  # project description clearly stated that first node should be 1
            set = {}  # set of outgoing edges for initial graph
            for j in range(1, N + 1):
                if abs(i - j) <= 3 and i != j:
                    set[j] = i + j  # adds weights to the set

            graph[i] = set  # adds outgoing edges of initial number to graph

        # Record start time
        start_time = time.perf_counter()

        # Create an instance of the Dijkstra class and find the shortest path
        dijkstra_test = Dijkstra(graph, S, N)
        shortest_path, path_cost = dijkstra_test.find_shortest_path()

        # Record end time
        end_time = time.perf_counter()

        # Calculate running time
        running_time = (end_time - start_time) * 1000000
        running_times.append(running_time)

        # Get total number of repetitions
        repetition = dijkstra_test.get_repetitions()
        repetitions.append(repetition)

    # Calculate theoretical running times
    theoretical_running_times = [c1 * m for N, m in zip(ns, repetitions)]

    # Plot actual and theoretical running times
    plt.plot(ns, running_times, label="Actual running time")
    plt.plot(ns, theoretical_running_times, label="Theoretical running time")
    plt.xlabel("Number of nodes (N)")
    plt.ylabel("Running time (seconds)")
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()


