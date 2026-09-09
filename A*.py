import heapq
# GPS road network: city -> list of (neighbour city, road distance)
graph = {
'A': [('B', 6), ('C', 4)],
'B': [('A', 6), ('D', 5)],
'C': [('A', 4), ('D', 7), ('E', 3)],
'D': [('B', 5), ('C', 7), ('F', 4)],
'E': [('C', 3), ('F', 9)],
'F': [('D', 4), ('E', 9)]
}

# Straight-line heuristic distance from each city to the destination 'F'
heuristic = {
'A': 10, 'B': 6, 'C': 7,
'D': 4, 'E': 8, 'F': 0
}
def a_star(graph, start, goal):
# priority queue holds tuples: (f(n), g(n), node, path)
open_set = [(heuristic[start], 0, start, [start])]
g_score = {start: 0}
visited = set()
while open_set:
f, g, node, path = heapq.heappop(open_set)
if node in visited:
continue
visited.add(node)
print(f'Visiting: {node} g={g} h={heuristic[node]} f={f}')
if node == goal:
return path, g
for neighbour, distance in graph[node]:
new_g = g + distance
if neighbour not in g_score or new_g < g_score[neighbour]:
g_score[neighbour] = new_g
new_f = new_g + heuristic[neighbour]
heapq.heappush(open_set, (new_f, new_g, neighbour, path + [neighbour]))

return None, float('inf')
# Run the search
start_city = 'A'
goal_city = 'F'
best_path, total_cost = a_star(graph, start_city, goal_city)
print('\n--- RESULT ---')
print('Start :', start_city)
print('Goal :', goal_city)
print('Best Path :', ' -> '.join(best_path))
print('Total Cost :', total_cost)
