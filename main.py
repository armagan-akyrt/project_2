# This is a sample Python script.
import heapq
import math
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from a_star import a_star


def main():
    N = input("Please provide number of desired graphs: ")
    N = int(N)
    # Creates the adjacency matrix for graph
    graph = {}
    for i in range(1, N + 1):   # project description clearly stated that first node should be 1
        set = {}    # set of outgoing edges for initial graph
        for j in range(1, N + 1):
            if abs(i - j) <= 3 and i != j:
                set[j] = i + j  # adds weights to the set
        graph[i] = set  # adds outgoing edges of initial number to graph

    a_star_test = a_star(graph, 1, len(graph) - 1)
    x = a_star_test.find_shortest_path()
    print(x)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
