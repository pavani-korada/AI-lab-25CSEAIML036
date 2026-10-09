import heapq

# Uniform Cost Search
def ucs(graph, start, goal):

    # Priority queue
    priority_queue = []

    # (cost, node, path)
    heapq.heappush(priority_queue, (0, start, [start]))

    # Store the lowest cost found for each node
    visited = {}

    while priority_queue:

        cost, current, path = heapq.heappop(priority_queue)

        # If node was already reached with lower cost
        if current in visited and visited[current] <= cost:
            continue

        visited[current] = cost

        # Goal found
        if current == goal:
            return path, cost

        # Explore neighbors
        for neighbor, edge_cost in graph[current]:

            new_cost = cost + edge_cost

            new_path = path + [neighbor]

            heapq.heappush(
                priority_queue,
                (new_cost, neighbor, new_path)
            )

    return None, float('inf')


# Main Program

print("===== UNIFORM COST SEARCH =====")

n = int(input("Enter number of nodes: "))
graph = {}

for i in range(n):
    graph[i] = []

# Enter edges
e = int(input("Enter number of edges: "))

print("Enter edges as:")
print("source destination cost")

for i in range(e):

    u, v, cost = map(int, input().split())

    graph[u].append((v, cost))
    graph[v].append((u, cost))

start = int(input("Enter starting node: "))
goal = int(input("Enter goal node: "))

# Perform UCS
path, cost = ucs(graph, start, goal)

# Display result
if path:

    print("\nGoal Found!")

    print("Optimal Path:",
          " -> ".join(map(str, path)))

    print("Minimum Cost:", cost)

else:

    print("\nGoal not found.")