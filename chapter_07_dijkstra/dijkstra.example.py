graph = {}

graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["end"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["end"] = 5

graph["end"] = {}

infinity = float("inf")

costs = {}
costs["a"] = 6
costs["b"] = 2
costs["end"] = infinity

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["end"] = None

processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None

    for node in costs:
        cost = costs[node]

        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node

    return lowest_cost_node

node = find_lowest_cost_node(costs)

while node is not None:
    cost = costs[node]
    neighbors = graph[node]

    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

def reconstruct_path(parents, start, end):
    path = []
    current = end
    
    while current != start:
        path.append(current)
        current = parents[current]
    
    path.append(start)
    path.reverse()
    return path

print("=== DIJKSTRA'S ALGORITHM RESULTS ===")
print(f"Minimum costs from 'start':")
for node, cost in costs.items():
    print(f"  {node}: {cost}")

print(f"\nShortest path to 'end': {reconstruct_path(parents, 'start', 'end')}")
print(f"Total cost: {costs['end']}")

print(f"\nShortest path to 'a': {reconstruct_path(parents, 'start', 'a')}")
print(f"Total cost: {costs['a']}")

print(f"\nShortest path to 'b': {reconstruct_path(parents, 'start', 'b')}")
print(f"Total cost: {costs['b']}")

