
# Smart Traffic Management System

This project implements a **Smart Traffic Management System** that manages traffic flow in real-time. The system uses a road network representation to optimize signal timings and guide vehicles along the shortest paths, helping to reduce congestion and improve vehicle movement efficiency.

## Table of Contents
- [Overview](#overview)
- [Concept and Application](#concept-and-application)
- [Features](#features)
- [Data Structures and Algorithms](#data-structures-and-algorithms)
  - [Graphs](#graphs)
  - [Dijkstra's Algorithm](#dijkstra-s-algorithm)
  - [Priority Queues](#priority-queues)
  - [Hash Tables](#hash-tables)
- [Time Complexity](#time-complexity)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [Running the System](#running-the-system)
- [Example Output](#example-output)
- [License](#license)

---

## Overview

The Smart Traffic Management System models a traffic network with intersections as nodes and roads as edges, using a graph data structure. Dijkstra's Algorithm calculates the shortest path for vehicle routing, ensuring efficient traffic flow. Additionally, a priority queue manages vehicle urgency at intersections, and a hash table stores traffic data for quick access.

## Concept and Application

- **Concept**: Simulate a real-time traffic system by representing road networks and managing vehicle routing.
- **Application**: Optimize traffic flow in cities by dynamically adjusting traffic signals and directing vehicles to reduce congestion.

## Features

- **Real-time Traffic Optimization**: Adjusts traffic flow based on current conditions.
- **Shortest Path Routing**: Calculates optimal paths for vehicles.
- **Vehicle Prioritization**: Manages intersections based on vehicle urgency.
- **Fast Data Access**: Uses a hash table for efficient data retrieval.

## Data Structures and Algorithms

### Graphs
The system uses an adjacency list to represent the road network:
- **Nodes** represent intersections.
- **Edges** represent roads with weights denoting distances or time to traverse.

### Dijkstra's Algorithm
Dijkstra's Algorithm finds the shortest path between intersections, ensuring efficient routing:
- **Time Complexity**: \(O((V + E) \log V)\), where \(V\) is the number of vertices, and \(E\) is the number of edges.

### Priority Queues
Priority queues handle vehicle prioritization at intersections, ensuring that urgent vehicles get preference.

### Hash Tables
Vehicle and traffic data are stored in a hash table, providing **O(1)** average-time complexity for quick access.

## Time Complexity

- **Dijkstra's Algorithm**: \(O((V + E) \log V)\)

## Project Structure

```plaintext
Smart_Traffic_Management_System/
├── graph.py             # Graph representation and shortest path algorithm
├── vehicle.py           # Vehicle data structure with movement logic
├── traffic_data.py      # Traffic data storage using hash tables
├── traffic_management.py # Main program for running the system
└── README.md            # Project documentation
```

## Setup and Installation

To set up the project locally, follow these steps:

### Clone the Repository:

```bash
git clone https://github.com/hanushrajputh/Smart_Traffic_Management_System.git
cd Smart_Traffic_Management_System
```

### Create a Virtual Environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Requirements (if applicable):

```bash
pip install -r requirements.txt
```

## Running the System

To run the Smart Traffic Management System:

### Activate the Virtual Environment:

```bash
source venv/bin/activate
```

### Run the Program:

```bash
python traffic_management.py
```

### Deactivate the Virtual Environment (when finished):

```bash
deactivate
```

## Example Output

Upon running `traffic_management.py`, you will see output like the following:

```plaintext
Shortest paths from A: {'A': 0, 'B': 4, 'C': 2, 'D': 5}
Vehicle V1 moved to C
```

### Explanation of Output

- **Shortest paths from A**: This dictionary shows the shortest distances from node A to each node in the network:
  - Node A has a distance of 0 to itself.
  - Node B is 4 units away from A.
  - Node C is 2 units away from A.
  - Node D is 5 units away from A.

- **Vehicle Movement**:
  - The program simulates a vehicle (V1) moving from A to C.
  - After moving, it confirms the new location of V1 as C.

This output verifies that Dijkstra’s Algorithm is correctly calculating the shortest paths, and that the vehicle can be successfully moved and tracked within the system.
