from collections import deque  # double-ended queue
# fnc bfs


def bfs(graph, start):
    visited = set()  # empty set to keep track of the visited vertices during traversal.
    queue = deque([start])  # deque object called queue, initialized with the start vertex.

    # queue used to store the vertices to visit
    while queue:
        vertex = queue.popleft()  # remove and return leftmost vertex from queue.
        # check if the vertex has not been visited before and visit each vertex only once
        if vertex not in visited:
            print(vertex)
            visited.add(vertex)  # marks visited vertex
            queue.extend(graph[vertex] - visited)  # extend queue adding all neighbors of vertex not visited yet
            # ensure only unvisited neighbors are added to the queue.


# fnc dfs; optional visited set that defaults to None
def dfs(graph, start, visited=None):
    # check if visited set has not been provided as an argument and to create new empty set
    if visited is None:
        visited = set()

    visited.add(start)  # mark visited vertices
    print(start)

    # iterate over the neighbors of start vertex not visited yet.
    # calculate set difference between neighbors of start and visited,
    # ensuring that only unvisited neighbors are traversed.
    for neighbor in graph[start] - visited:
        # recursively call dfs function with neighbor as new start vertex and visited set
        dfs(graph, neighbor, visited)


# Example graph represented as an adjacency list
graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}

print("BFS traversal:")
bfs(graph, 'A')

print("\nDFS traversal:")
dfs(graph, 'A')
