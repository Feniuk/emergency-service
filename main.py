from src.data import graph, hospitals
from src.dijkstra import dijkstra

starting_point = "Hbf"

shortest_path_calculator = dijkstra(graph, starting_point)

closest_hostpital = hospitals[0]

shortest_path = shortest_path_calculator[closest_hostpital]["cost"]

for hospital in hospitals:
    if shortest_path_calculator[hospital]["cost"] < shortest_path:
        closest_hostpital = hospital
        shortest_path = shortest_path_calculator[hospital]["cost"]

print("Closest hospital: ", closest_hostpital)
print("Shortest distance: " + str(shortest_path) + " km")
print("Shortest path ", shortest_path_calculator[closest_hostpital]["previous"] + [closest_hostpital])
