from collections import deque

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = {}  # Adjacency list

        # Initialize empty list for each vertex
        for i in range(vertices):
            self.graph[i] = []

    # Add edge for undirected graph
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # Because it's undirected

    # Recursive DFS
    def dfs_util(self, v, visited):
        visited[v] = True
        print(v, end=' ')
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.dfs_util(neighbor, visited)

    # DFS wrapper
    def dfs(self, start):
        visited = [False] * self.vertices
        print("DFS Traversal:")
        self.dfs_util(start, visited)
        print()

    # BFS traversal
    def bfs(self, start):
        visited = [False] * self.vertices
        queue = deque()
        visited[start] = True
        queue.append(start)

        print("BFS Traversal:")
        while queue:
            vertex = queue.popleft()
            print(vertex, end=' ')
            for neighbor in self.graph[vertex]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        print()

# Example usage
if __name__ == "__main__":
    # Create a graph with 6 vertices
    g = Graph(6)

    # Add edges
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 5)

    # Run DFS and BFS
    g.dfs(0)
    g.bfs(0)
