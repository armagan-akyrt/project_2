# This is a sample Python script.
import heapq
import math
import networkx as nx
import numpy as np
import time
from dijsktra import Dijkstra
import matplotlib.pyplot as plt
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from a_star import a_star


def main():
    N = int(input("Please provide number of desired graphs: "))

    S = int(input("Starting city: "))
    D = int(input("Destination city: "))

    time_interval = 5
    # Creates the adjacency matrix for graph
    graph = {}
    for i in range(1, N + 1):   # project description clearly stated that first node should be 1
        set = {}    # set of outgoing edges for initial graph
        for j in range(1, N + 1):
            if abs(i - j) <= 3 and i != j:
                set[j] = i + j  # adds weights to the set
            else:
                set[j] = math.inf
        graph[i] = set  # adds outgoing edges of initial number to graph


    a_star_test = a_star(graph, S, D)
    x = a_star_test.find_shortest_path()
    print('Result of A* algorithm: \nPath from {} to {} is : {}, with the cost of {}kms'.format(S, D, x[0], x[1]))
    print(x[2])

    # Create a directed graph
    G = nx.DiGraph()

    # Add nodes and edges to the graph
    for i in range(1, len(graph) + 1):
        for j in range(1, len(graph) + 1):
            if graph[i][j] != math.inf:
                G.add_edge(i, j, weight=graph[i][j])

    # Set node positions
    pos = nx.spring_layout(G)

    # Draw the first graph
    fig1 = plt.figure()
    nx.draw(G, pos, with_labels=True, node_size=600, font_size=8)

    # Add edge labels
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=8)

    # Highlight the shortest path found by the A* algorithm in red
    shortest_path_edges = [(x[0][i], x[0][i + 1]) for i in range(len(x[0]) - 1)]
    nx.draw_networkx_edges(G, pos, edgelist=shortest_path_edges, edge_color='r', width=3)

    # Adjust plot size to fit graph
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)

    # Show the plot
    plt.show()

    # Wait for specified time interval
    time.sleep(time_interval)

    # Close the first plot
    plt.close(fig1)

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


