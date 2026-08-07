def bfs(graph, start_node):
    visited = []
    queue = [start_node]

    while queue:
        current_node = queue.pop(0)

        if current_node not in visited:
            print(f"Exploring node: {current_node}")
            visited.append(current_node)

            #.get() prevents errors if a node has no outgoing edges
            for neighbour in graph.get(current_node, []):
                if neighbour not in visited and neighbour not in queue:
                    queue.append(neighbour)

    return visited

#---user input section ---
print("---Build your graph---")
student_graph = {}

#get the total number of connections
num_edges = int(input("how many edges (connections) does your graph have"))

print("enter each edge separated by a space(e.g., A B):")
for i in range(num_edges):
    #read the input and split it into two variables
    u, v = input(f"Edge {i+1}: ").split()

    #initialize the lists if the nodes dont exist yet
    if u not in student_graph:
        student_graph[u] = []
    if v not in student_graph:
        student_graph[v] = []

    # add the connection (undirected graph)
    student_graph[u].append(v)
    student_graph[v].append(u)

#get the sytarting point
start = input("enter the starting node for bfs: ")

print(f"\nYour graph dictionary: {student_graph}:")
print("starting BFS traversal...")


bfs(student_graph, start)