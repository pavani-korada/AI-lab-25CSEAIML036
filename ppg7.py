from collections import deque
def water_jug(cap1,cap2,target_state):
    visited =set()
    queue =deque()
    queue.append((0,0,[]))
    while queue:
        j1,j2,path = queue.popleft()
        if (j1,j2) in visited:
            continue
        visited.add((j1,j2))
        current_path = path + [(j1,j2)]
        if (j1,j2) == target_state:
            return current_path
        next_moves = [
            (cap1,j2), # Fill jug 1
            (j1,cap2), # Fill jug 2
            (0,j2), # Empty jug 1
            (j1,0), # Empty jug 2
            (j1 - min(j1,cap2-j2), j2 + min(j1,cap2-j2)), # Pour jug 1 to jug 2
            (j1 + min(j2,cap1-j1), j2 - min(j2,cap1-j1))  # Pour jug 2 to jug 1
        ]
        for move in next_moves:
            if move not in visited:
                queue.append((move[0],move[1],current_path))
        return True
    target_state=(4,2)
    solution=water_jug(4,3,target_state)
    if solution:
        print(f"steps to reach target state {target_state}:")  
        for step in solution: 
            print(step)
    else:
        print("No solution found.") 