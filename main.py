from src.data import graph, hospitals
from src.dijkstra import dijkstra
from src.aStar import a_star

starting_point = "Hbf"

djikstra_call = dijkstra(graph, starting_point)

shortest_path_calculator = djikstra_call[0]

dijkstra_nodes_count = djikstra_call[1]

closest_hostpital = hospitals[0]

shortest_path = shortest_path_calculator[closest_hostpital]["cost"]

for hospital in hospitals:
    if shortest_path_calculator[hospital]["cost"] < shortest_path:
        closest_hostpital = hospital
        shortest_path = shortest_path_calculator[hospital]["cost"]


print("Closest hospital: ", closest_hostpital)
print("Shortest distance: " + str(shortest_path) + " km")
print("Shortest path ", shortest_path_calculator[closest_hostpital]["previous"] + [closest_hostpital])



astar_call = a_star(graph, starting_point, hospitals)

closest_hospital = astar_call[0]
shortest_dist = astar_call[1]
astar_nodes_count = astar_call[2]

print("Closest hospital:", closest_hospital)
print("Shortest distance: " + str(shortest_dist[closest_hospital]["cost"]) + " km")
print("Shortest path:", shortest_dist[closest_hospital]["previous"] + [closest_hospital])

### Comparison of efficiency of algorithms
print("Dijkstra visited: ", dijkstra_nodes_count, " nodes")
print("A* visited: ", astar_nodes_count, " nodes")

