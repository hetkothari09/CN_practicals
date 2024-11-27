graph = [
    [0, 7, 9, 0, 0, 4],
    [7, 0, 10, 15, 0, 0],
    [9, 10, 0, 11, 0, 2],
    [0, 15, 11, 0, 6, 0],
    [0, 0, 0, 6, 0, 9],
    [4, 0, 2, 0, 9, 0],
]

n = 6  # Number of vertices

dist = [9999] * n  # Initialize distances with a large number
parent = [-1] * n  # Initialize parent nodes with -1 (no parent)
visited = [0] * n  # Keep track of visited nodes

source = 0  # Define the source vertex
dist[source] = 0  # Distance to the source is 0

def extract_min():
    """Find the vertex with the minimum distance value that hasn't been visited."""
    return min((dist[i], i) for i in range(n) if not visited[i])[1]

def relax(u, v):
    """Relax the edge and update distance and parent."""
    if dist[v] > dist[u] + graph[u][v]:
        dist[v] = dist[u] + graph[u][v]
        parent[v] = u

# Dijkstra's Algorithm Execution
for _ in range(n):
    u = extract_min()  # Get the vertex with the smallest distance
    for v in range(n):
        if graph[u][v] != 0 and not visited[v]:  # Check connected, unvisited vertices
            relax(u, v)  # Relax the edge
    visited[u] = 1  # Mark the vertex as visited

# Generate Output
print("=== Shortest Paths Using Dijkstra's Algorithm ===\n")
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
