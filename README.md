A* GPS Road Network

This project demonstrates the A* (A-star) search algorithm for finding the shortest path between cities in a GPS-style road network.

The program uses:

A graph representing cities and road distances.
A straight-line heuristic for estimating the distance to the destination.
A priority queue (heapq) to efficiently select the next city to explore.
A* search to calculate the best route and its total cost.
Features
Finds the shortest path between two cities.
Uses the A* search algorithm.
Displays each city visited during the search.
Calculates the total road distance of the selected route.
Uses a heuristic function to improve search efficiency.
Requirements
Python 3.x
No external libraries are required.

The program uses Python's built-in heapq module.

Project Structure
.
├── main.py
└── README.md

How It Works

The road network is represented as a graph:

graph = {
    'A': [('B', 6), ('C', 4)],
    'B': [('A', 6), ('D', 5)],
    'C': [('A', 4), ('D', 7), ('E', 3)],
    'D': [('B', 5), ('C', 7), ('F', 4)],
    'E': [('C', 3), ('F', 9)],
    'F': [('D', 4), ('E', 9)]
}


Each entry represents:

(city, road distance)


For example:

A -> B = 6
A -> C = 4


The heuristic estimates the remaining distance from each city to the destination F:

heuristic = {
    'A': 10,
    'B': 6,
    'C': 7,
    'D': 4,
    'E': 8,
    'F': 0
}


A* calculates:

f(n) = g(n) + h(n)


Where:

g(n) = actual cost from the starting city to city n
h(n) = estimated cost from city n to the goal
f(n) = estimated total cost of a route through n
Running the Program

Save the Python code in a file named:

main.py


Then run:

python main.py

Example

The search starts at:

A


and attempts to reach:

F


One optimal route is:

A -> B -> D -> F


Its total cost is:

6 + 5 + 4 = 15


Another route is:

A -> C -> E -> F


with cost:

4 + 3 + 9 = 16


Therefore, the shortest route is:

A -> B -> D -> F


with a total cost of:

15

Sample Output
Visiting: A g=0 h=10 f=10
Visiting: B g=6 h=6 f=12
Visiting: C g=4 h=7 f=11
Visiting: D g=11 h=4 f=15
Visiting: F g=15 h=0 f=15

--- RESULT ---
Start : A
Goal : F
Best Path : A -> B -> D -> F
Total Cost : 15


The exact visiting order can depend on the priority-queue ordering when multiple nodes have similar priority values.

Algorithm

The A* algorithm follows these steps:

Add the starting city to the priority queue.
Select the city with the smallest f(n) value.
Mark the city as visited.
If it is the destination, return the path and cost.
Otherwise, examine all neighboring cities.
Calculate the new path cost g(n).
If the new path is cheaper, update the city and add it to the priority queue.
Continue until the destination is reached or there are no more cities to explore.
Time and Space Complexity

The complexity of A* depends on the graph structure and the quality of the heuristic.

In general:

Time complexity: Can be exponential in the worst case.
Space complexity: Can be exponential in the worst case.

A good heuristic can significantly reduce the number of nodes explored.

Heuristic

For A* to guarantee an optimal solution, the heuristic should generally be admissible, meaning it never overestimates the actual remaining cost.

For a GPS application, straight-line distance is commonly used as a heuristic because the shortest road distance cannot normally be less than the direct straight-line distance between two locations.

Applications

A* search is commonly used in:

GPS navigation
Route planning
Robot pathfinding
Video game AI
Maze solving
Network routing
Map-based applications
License

This project is provided for educational purposes. You are free to modify and use the code for learning and experimentation.
