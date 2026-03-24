from data import graph, hospitals
import sys
from heapq import heappush, heapify

def dijkstra(graph, starting_point, destination):
    infinity = sys.maxsize

    initial_data = {"Hbf":{"cost": infinity, "previous":[]},
                    "Brandenburger Tor":{"cost": infinity, "previous":[]},
                    "Sanssouci":{"cost": infinity, "previous":[]},
                    "University":{"cost": infinity, "previous":[]},
                    "Park":{"cost": infinity, "previous":[]},
                    "Babelsberg":{"cost": infinity, "previous":[]},
                    "FilmPark":{"cost": infinity, "previous":[]},
                    "Klinikum Ernst von Bergmann":{"cost": infinity, "previous":[]},
                    "St. Josefs Krankenhaus":{"cost": infinity, "previous":[]}}
    
    initial_data[starting_point]["cost"] = 0
    visited = []
    current = starting_point
    for punkt in range(9):
        if current not in visited:
            visited.append(current)
            min_heap = []
            for neighbor_node in graph[current]:
                if neighbor_node not in visited:
                    cost = initial_data[current]["cost"] + graph[current][neighbor_node]
                    if cost < initial_data[neighbor_node]["cost"]:
                        initial_data[neighbor_node]["cost"] = cost
                        initial_data[neighbor_node]["previous"] = initial_data[current]["previous"] + [current]
                    heappush(min_heap, (initial_data[neighbor_node]["cost"], neighbor_node))
                    print(min_heap)
                    print(heapify(min_heap))
                    current = min_heap[0][1]
                    print(current)

        print("Shortest Distance: " + str(initial_data[destination]["cost"]))
        print("Shortest Path: " + str(initial_data[destination]["previous"] + list(destination)))

dijkstra(graph, "Hbf", "University")