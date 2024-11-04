from graph import Graph
from vehicle import Vehicle
from traffic_data import TrafficData

def main():
    # Create a graph representing the road network
    graph = Graph()
    graph.add_edge('A', 'B', 4)
    graph.add_edge('A', 'C', 2)
    graph.add_edge('B', 'C', 5)
    graph.add_edge('B', 'D', 10)
    graph.add_edge('C', 'D', 3)

    # Create traffic data storage
    traffic_data = TrafficData()

    # Add vehicles to the system
    vehicle1 = Vehicle('V1', 'A')
    traffic_data.add_vehicle(vehicle1.vehicle_id, vehicle1)

    # Find shortest paths from a source
    shortest_paths = graph.dijkstra('A')
    print("Shortest paths from A:", shortest_paths)

    # Move vehicle
    vehicle1.move('C')
    print(f"Vehicle {vehicle1.vehicle_id} moved to {vehicle1.location}")

if __name__ == "__main__":
    main()
