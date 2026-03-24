from src.data import graph, hospitals, coordinates
import sys
from heapq import heappush, heapify, heappop
import math

def heuristic_algorithm(point, hospitals, coordinates):
    distance = []

    x, y = coordinates[point]

    for hospital in hospitals:
        x1, y1 = coordinates[hospital]
        distance1 = math.sqrt((x - x1) **2 + (y - y1) ** 2)
        distance.append(distance1)

    return min(distance)

def a_star(graph, starting_point, hospitals):
    infinity = sys.maxsize

    initial_data = {"Hbf":{"cost": infinity, "previous":[]},
                    "Brandenburger Tor":{"cost": infinity, "previous":[]},
                    "Sanssouci":{"cost": infinity, "previous":[]},
                    "University":{"cost": infinity, "previous":[]},
                    "Park":{"cost": infinity, "previous":[]},
                    "Babelsberg":{"cost": infinity, "previous":[]},
                    "FilmPark":{"cost": infinity, "previous":[]},
                    "Klinikum Ernst von Bergmann":{"cost": infinity, "previous":[]},
                    "Alexianer St. Josefs Krankenhaus":{"cost": infinity, "previous":[]}}
    
    initial_data[starting_point]["cost"] = 0
    visited = []
    visited_nodes_counter = 0
    min_heap = []
    first_priority = heuristic_algorithm(starting_point, hospitals, coordinates)
    heappush(min_heap, (first_priority, starting_point))
    while min_heap:
        temp = heappop(min_heap)
        current_smallest_priority_value = temp[0]
        current = temp[1]
        if current not in visited:
            visited.append(current)
            visited_nodes_counter += 1
        if current in hospitals:
            return current, initial_data, visited_nodes_counter
        for neighbor_node in graph[current]:
                if neighbor_node not in visited:
                    cost = initial_data[current]["cost"] + graph[current][neighbor_node]
                    if cost < initial_data[neighbor_node]["cost"]:
                        initial_data[neighbor_node]["cost"] = cost
                        initial_data[neighbor_node]["previous"] = initial_data[current]["previous"] + [current]
                        
                        heuristic = heuristic_algorithm(neighbor_node, hospitals, coordinates)
                        priority = cost + heuristic
                        heappush(min_heap, (priority, neighbor_node))

    return None, initial_data, visited_nodes_counter