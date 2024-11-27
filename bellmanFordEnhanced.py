weight = [
    [0, 4, 0, 0],
    [0, 0, -2, 0],
    [0, 0, 0, 3],
    [0, 0, 0, 0],
]

n = 4  # Number of vertices
dist = [9999] * n  # Initialize distances with a large number
parent = [-1] * n  # Initialize parent nodes with -1 (no parent)

source = 0  # Define the source vertex
dist[source] = 0  # Distance to the source is 0

def relax(u, v):
    """Relax the edge and update distance and parent."""
    if dist[v] > dist[u] + weight[u][v]:
        dist[v] = dist[u] + weight[u][v]
        parent[v] = u

def BellmanFord():
    """Run the Bellman-Ford algorithm to find shortest paths."""
    for _ in range(n - 1):  # Relax all edges (n-1) times
        for u in range(n):
            for v in range(n):
                if weight[u][v] != 0:  # Only consider edges with weights
                    relax(u, v)

    # Check for negative weight cycles
    for u in range(n):
        for v in range(n):
            if weight[u][v] != 0 and dist[v] > dist[u] + weight[u][v]:
                return False  # Negative weight cycle found
    return True

if BellmanFord():
    print("=== Shortest Paths Using Bellman-Ford Algorithm ===\n")
    print(f"Source Vertex: {source + 1}")
    print("\nVertex\tDistance from Source\tPath")
    print("------\t--------------------\t----")
    
    for i in range(n):
        path = []
        current = i
        while current != -1:  # Trace the path back to the source
            path.append(current + 1)  # Convert to 1-based index
            current = parent[current]
        path.reverse()  # Reverse the path to start from the source

        print(f"{i + 1}\t{dist[i]:<20}\t{' -> '.join(map(str, path))}")
else:
    print("Graph contains a negative weight cycle. No solution.")
