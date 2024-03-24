import heapq

def get_neighbors(arrangement):
    """
    Generate a list of possible neighbors for a given arrangement.
    """
    neighbors = []
    empty_index = arrangement.index(0)
    n = len(arrangement)
    
    for i in range(max(0, empty_index - 2), min(n, empty_index + 3)):
        if i != empty_index:
            new_arrangement = arrangement[:]
            new_arrangement[empty_index], new_arrangement[i] = new_arrangement[i], new_arrangement[empty_index]
            neighbors.append(tuple(new_arrangement))  # Using tuple
            
    return neighbors

def dijkstra_shortest_path(start, goal):
    """
    Find the shortest path from the initial arrangement to the goal arrangement using Dijkstra's algorithm.
    """
    visited = set()
    heap = [(0, tuple(start), [])]  # Using tuple for the initial node
    
    while heap:
        cost, node, path = heapq.heappop(heap)
        
        if list(node) == goal:  # Convert back to list when comparing with the goal node
            return path
        
        if node not in visited:
            visited.add(node)
            neighbors = get_neighbors(list(node))  # Convert back to list to get neighbors
            
            for neighbor in neighbors:
                if neighbor not in visited:
                    heapq.heappush(heap, (cost + 1, neighbor, path + [list(neighbor)]))  # Using list

    return None  # No path found

# Initial and goal nodes
S = [0, 2, 8, 5, 4, 9]
F = [0, 9, 8, 5, 4, 2]

# Find the shortest path from S to F
shortest_path = dijkstra_shortest_path(S, F)

if shortest_path:
    print("Shortest path found:", shortest_path)
    print("Number of moves:", len(shortest_path) - 1)
else:
    print("No path found from the initial arrangement to the goal arrangement.")
