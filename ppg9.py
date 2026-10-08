from itertools import permutations

#Functions to solve TSP 
def travelling_salesman(graph, start):
    cities = list(range(len(graph)))
    cities.remove(start)
    
    min_cost = float('inf')
    best_path = None
    
    #Generate all possible tours
    for perm in permutations(cities):
        current_cost = 0
        current_path = [start]
        k = start
        
        #visit each city in the permutation
        for city in perm:
            current_cost += graph[k][city]
            current_path.append(city)
            k = city
            
        #Return to starting city
        current_cost += graph[k][start]
        current_path.append(start)
        
        #Check if this is the minimum cost tour
        if current_cost < min_cost:
            min_cost = current_cost
            best_path = current_path
            
    return best_path, min_cost
        
#Main Program
n = int(input("Enter number of cities: "))

print("Enter the cost matrix :")
graph = []
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)
    
start = int(input("Enter starting city (0 to {}): ".format(n-1)))

path, cost = travelling_salesman(graph, start)

print("Optimal path:", path)
print("Minimum cost:", cost)