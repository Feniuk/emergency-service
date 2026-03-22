from data import graph, hospitals
import sys
import heapq

def dijkstra(graph, starting_point, destination):
    infinity = sys.maxsize

    cost = {}
    for node in graph:
        cost[node] = infinity

    previous = {}
    for node in graph:
        previous[node] = None

    # initial_data = {"A":{"cost": infinity, "previous":[]},
    #                 "B":{"cost": infinity, "previous":[]},
    #                 "C":{"cost": infinity, "previous":[]},
    #                 "D":{"cost": infinity, "previous":[]},
    #                 "E":{"cost": infinity, "previous":[]},
    #                 "F":{"cost": infinity, "previous":[]},
    #                 "G":{"cost": infinity, "previous":[]},
    #                 "H":{"cost": infinity, "previous":[]},
    #                 "I":{"cost": infinity, "previous":[]}}
    
    visited = []