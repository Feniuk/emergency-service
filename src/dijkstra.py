from data import graph, hospitals
import sys
import heapq

def dijkstra(graph, starting_point, destination):
    infinity = sys.maxsize

    initial_data = {"1":{"cost": infinity, "previous":[]},
                    "2":{"cost": infinity, "previous":[]},
                    "3":{"cost": infinity, "previous":[]},
                    "4":{"cost": infinity, "previous":[]},
                    "5":{"cost": infinity, "previous":[]},
                    "6":{"cost": infinity, "previous":[]},
                    "7":{"cost": infinity, "previous":[]},
                    "8":{"cost": infinity, "previous":[]},
                    "9":{"cost": infinity, "previous":[]}}
    
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
                    if cost < initial_data[current]["cost"]:
                        initial_data[current]["cost"] = cost