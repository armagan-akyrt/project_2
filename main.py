import math
import networkx as nx
import time
from dijkstra import Dijkstra
from a_star import a_star
import matplotlib.pyplot as plt


def main():

    N = int(input("Please provide number of desired graphs: "))
    S = int(input("Starting city: "))
    D = int(input("Destination city: "))

    graph = create_adjacency_matrix(N)
    a_star_test = a_star(graph, S, D)
    a_star_results = a_star_test.find_shortest_path()
    print('Result of A* algorithm: \nPath from {} to {} is: {}, with the cost of {}kms'.format(S, D, a_star_results[0],
                                                                                                a_star_results[1]))
    print('Repetition of A* algorithm:', a_star_results[2])
    print('***********************************************')

    dijkstra_test = Dijkstra(graph, S, D)
    dijkstra_results = dijkstra_test.find_shortest_path()
    print('Result of Dijkstra algorithm: \nPath from {} to {} is: {}, with the cost of {}kms'.format(S, D,
                                                                                                      dijkstra_results[
                                                                                                          0],
                                                                                                      dijkstra_results[
                                                                                                          1]))
    print('Repetition of Dijkstra algorithm:', dijkstra_test.get_repetitions())
    print()
    decision = input('D=>Dijkstra, A=> A* to visualize the graph: ').lower()

    if decision == 'd':
        visualize_matrix(graph, dijkstra_results, 'Dijkstra')
    elif decision == 'a':
        visualize_matrix(graph, a_star_results, 'A*')
    else:
        decision = input('Wrong input proceeding, write A or D:')
        if decision == 'd':
            visualize_matrix(graph, dijkstra_results, 'Dijkstra')
        elif decision == 'a':
            visualize_matrix(graph, a_star_results, 'A*')

    # Dijkstra-A* Questions 3-6
    c1 = 1
    # Set values for N
    ns = [10, 25, 50, 100, 200, 500, 1000, 2000]

    # Set source and destination nodes
    S = 1

    # Initialize lists to store running times and total number of repetitions
    running_times_d = []
    repetitions_d = []

    running_times_a = []
    repetitions_a = []

    # Loop through values of N
    for N in ns:
        graph = create_adjacency_matrix(N)
        # Record start time
        # Create an instance of the a_star class and find the shortest path
        a_star_test = a_star(graph, S, N)

        start_time_a = time.perf_counter()
        a_star_test.find_shortest_path()
        end_time_a = time.perf_counter()

        running_time_a = (end_time_a - start_time_a) * 1000000
        running_times_a.append(running_time_a)

        # Get total number of repetitions
        repetition_a = a_star_test.get_repetition()
        repetitions_a.append(repetition_a)

        # Create an instance of the Dijkstra class and find the shortest path
        dijkstra_test = Dijkstra(graph, S, N)

        start_time_d = time.perf_counter()
        dijkstra_test.find_shortest_path()
        end_time_d = time.perf_counter()  # Record end time

        # Calculate running time
        running_time_d = (end_time_d - start_time_d) * 1000000
        running_times_d.append(running_time_d)

        # Get total number of repetitions
        repetition_d = dijkstra_test.get_repetitions()
        repetitions_d.append(repetition_d)

    # Calculate theoretical running times
    theoretical_running_times_d = [c1 * m for N, m in zip(ns, repetitions_d)]
    theoretical_running_times_a = [c1 * m for N, m in zip(ns, repetitions_a)]
    print('Running times of Dijkstra:\n' + str(running_times_d))
    print()
    print('Running times of A*:\n' + str(running_times_a))

    # plot actual and theoretical running time results of two algorithms
    figure, axis = plt.subplots(2, 2, figsize=(10, 10))

    axis[0, 0].plot(ns, theoretical_running_times_d, )
    axis[0, 0].set_title("Dijkstra Theoretical Running Time")
    axis[0, 0].set_ylim(0)

    axis[0, 1].plot(ns, running_times_d)
    axis[0, 1].set_title("Actual Running Time (Dijkstra)")

    axis[1, 0].plot(ns, theoretical_running_times_a, )
    axis[1, 0].set_title("A* theoretical Running Time")
    axis[1, 0].set_ylim(0)

    axis[1, 1].plot(ns, running_times_a)
    axis[1, 1].set_title("Actual Running Time (a*)")

    # Plot actual and theoretical running times
    # plt.plot(ns, running_times, label="Actual running time")
    # plt.plot(ns, theoretical_running_times, label="Theoretical running time")
    plt.xlabel("Number of nodes (N)")
    plt.ylabel("Running time (seconds)")

    plt.show()


def visualize_matrix(graph, path, algorithm):
    # Create a directed graph
    G = nx.DiGraph()

    # Add nodes and edges to the graph
    for i in range(1, len(graph) + 1):
        for j in range(1, len(graph) + 1):
            if graph[i][j] != math.inf:
                G.add_edge(i, j, weight=graph[i][j])

    # choose layout

    layout = input('Choose a layout for graph\n1:spring\n2:circular\n3:spiral\n4:random\n')

    # Set node positions
    match layout:
        case '1':
            pos = nx.spring_layout(G)

        case '2':
            pos = nx.circular_layout(G)
        case '3':
            pos = nx.spiral_layout(G)
        case '4':
            pos = nx.random_layout(G)
        case _:
            pos = nx.spring_layout(G)  # default is spring layout

    # Draw the first graph
    plt.figure()
    nx.draw(G, pos, with_labels=True, node_size=600, font_size=8)

    # Add edge labels
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=8)

    # Highlight the shortest path found by the A* algorithm in red
    shortest_path_edges = [(path[0][i], path[0][i + 1]) for i in range(len(path[0]) - 1)]
    nx.draw_networkx_edges(G, pos, edgelist=shortest_path_edges, edge_color='r', width=1)

    # Add a title to the graph
    plt.suptitle('{} Graph'.format(algorithm))

    # Show the plot
    print('Close the figure to continue!\n')
    plt.show(block=True)  # waits until the window is closed


def create_adjacency_matrix(n):
    # Creates the adjacency matrix for graph
    graph = {}
    for i in range(1, n + 1):  #
        edges = {}  # set of outgoing edges for initial graph
        for j in range(1, n + 1):
            if abs(i - j) <= 3 and i != j:
                edges[j] = i + j  # adds weights to the set
            else:
                edges[j] = math.inf
        graph[i] = edges  # adds outgoing edges of initial number to graph
    return graph


if __name__ == '__main__':
    main()
