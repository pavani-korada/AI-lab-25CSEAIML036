from collections import deque

def is_clear(state, block):
    for b, position in state:
        if position == block:
            return False
    return True

def generate_moves(state, blocks):
    moves = []
    for block in blocks:
        if not is_clear(state, block):
            continue
        current_position = None
        for b, position in state:
            if b == block:
                current_position = position
                break
        if current_position != 'table':
            new_state = set(state)
            new_state.remove((block, current_position))
            new_state.add((block, 'table'))
            moves.append(
                (frozenset(new_state),
                 f"Move {block} from {current_position} to table")
            )
        for destination in blocks:
            if block == destination:
                continue
            new_state = set(state)
            new_state.remove((block, current_position))
            new_state.add((block, destination))
            moves.append(
                (frozenset(new_state),
                 f"Move {block} from {current_position} to {destination}")
            )
    return moves

def block_world(initial_state, goal_state, blocks):
    queue = deque()
    queue.append((frozenset(initial_state), []))
    visited = set()
    visited.add(frozenset(initial_state))

    while queue:
        current_state, path = queue.popleft()
        if current_state == frozenset(goal_state):
            return path  # Found solution

        for new_state, action in generate_moves(current_state, blocks):
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [action]))
    return None  # No solution found

# Example usage
initial_state = {('A', 'table'), ('B', 'A'), ('C', 'table')}
goal_state = {('A', 'B'), ('B', 'C'), ('C', 'table')}
blocks = ['A', 'B', 'C']

solution = block_world(initial_state, goal_state, blocks)

if solution:
    print("Solution found:")
    for step in solution:
        print(step)
else:
    print("No solution exists.")
