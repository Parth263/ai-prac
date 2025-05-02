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




# Great! Let's start by explaining this graph traversal code **step-by-step** (Part 1). This code demonstrates **DFS and BFS** on an **undirected graph** using a class-based approach.

# ---

# ## 🔹 Step-by-Step Breakdown

# ### 1. **Class Initialization:**

# ```python
# class Graph:
#     def __init__(self, vertices):
#         self.vertices = vertices
#         self.graph = {}
#         for i in range(vertices):
#             self.graph[i] = []
# ```

# * `vertices`: Number of nodes in the graph.
# * `self.graph`: Dictionary acting as an **adjacency list**, where key = node, value = list of neighbors.

# Example result after `Graph(6)`:

# ```python
# {
#   0: [],
#   1: [],
#   2: [],
#   3: [],
#   4: [],
#   5: []
# }
# ```

# ---

# ### 2. **Adding Edges:**

# ```python
# def add_edge(self, u, v):
#     self.graph[u].append(v)
#     self.graph[v].append(u)
# ```

# * Adds an edge **both ways** (undirected graph).
# * `u` is connected to `v` and vice versa.

# Example after:

# ```python
# g.add_edge(0, 1)
# g.add_edge(0, 2)
# ```

# Graph becomes:

# ```python
# {
#   0: [1, 2],
#   1: [0],
#   2: [0],
#   ...
# }
# ```

# ---

# ### 3. **DFS Utility Function (Recursive):**

# ```python
# def dfs_util(self, v, visited):
#     visited[v] = True
#     print(v, end=' ')
#     for neighbor in self.graph[v]:
#         if not visited[neighbor]:
#             self.dfs_util(neighbor, visited)
# ```

# * Visits a node, marks it visited, and calls itself recursively on unvisited neighbors.
# * `visited` list keeps track of visited nodes.

# ---

# ### 4. **DFS Wrapper:**

# ```python
# def dfs(self, start):
#     visited = [False] * self.vertices
#     print("DFS Traversal:")
#     self.dfs_util(start, visited)
# ```

# * Initializes all nodes as unvisited and starts DFS from the `start` node.

# ---

# ### 5. **BFS Traversal (Queue Based):**

# ```python
# def bfs(self, start):
#     visited = [False] * self.vertices
#     queue = deque()
#     visited[start] = True
#     queue.append(start)

#     while queue:
#         vertex = queue.popleft()
#         print(vertex, end=' ')
#         for neighbor in self.graph[vertex]:
#             if not visited[neighbor]:
#                 visited[neighbor] = True
#                 queue.append(neighbor)
# ```

# * Uses a **queue** to explore nodes **level by level**.
# * `visited` ensures each node is visited once.

# ---

# ### 6. **Main Code Execution:**

# ```python
# if __name__ == "__main__":
#     g = Graph(6)
#     g.add_edge(0, 1)
#     g.add_edge(0, 2)
#     g.add_edge(1, 3)
#     g.add_edge(1, 4)
#     g.add_edge(2, 5)
    
#     g.dfs(0)
#     g.bfs(0)
# ```

# Creates this graph:

# ```
#         0
#        / \
#       1   2
#      / \   \
#     3   4   5
# ```

# * DFS Output (starting from 0): `0 1 3 4 2 5`
# * BFS Output (starting from 0): `0 1 2 3 4 5`

# ---

# Say **next** when you want the **concepts, algorithm, and new terms explained**.





# Let's break down the **concepts**, the **algorithm** used here, and introduce any **new terms**.

# ---

# ## **Concepts**

# ### 1. **Graph Representation**:

# A **graph** is a collection of nodes (vertices) connected by edges. It can be represented in several ways:

# * **Adjacency List** (used here): A dictionary where each key is a node and its value is a list of adjacent nodes (its neighbors).
# * **Adjacency Matrix**: A 2D array where each cell represents if an edge exists between two nodes.
# * **Edge List**: A list of all edges, represented as pairs of connected nodes.

# ### 2. **Depth-First Search (DFS)**:

# * **DFS** is a **graph traversal algorithm** that explores as far down a branch of the graph as possible before backtracking.
# * It is implemented using **recursion** or a **stack**.

# ### 3. **Breadth-First Search (BFS)**:

# * **BFS** is another **graph traversal algorithm** that explores nodes level by level.
# * It uses a **queue** to explore the nearest neighbors first before moving to the next level.

# ---

# ## **Algorithm**

# ### **DFS (Depth-First Search)** Algorithm:

# 1. Start from the given node and mark it as visited.
# 2. Visit each neighbor recursively (using a stack or recursion).
# 3. Backtrack when there are no more unvisited neighbors.
# 4. Continue until all reachable nodes are visited.

# #### **Steps in DFS**:

# * Visit the starting node.
# * For each unvisited neighbor, call `dfs_util()` recursively.
# * **Backtrack** when you reach a dead end.

# ### **BFS (Breadth-First Search)** Algorithm:

# 1. Start from the given node and mark it as visited.
# 2. Use a queue to explore the graph level by level.
# 3. For each node, enqueue its unvisited neighbors.
# 4. Repeat until all nodes are visited.

# #### **Steps in BFS**:

# * Visit the starting node and enqueue it.
# * While the queue has elements:

#   * Dequeue a node and visit all its unvisited neighbors.
#   * Enqueue each of those neighbors.

# ---

# ## **New Terms**

# ### 1. **Adjacency List**:

# A common way to represent a graph where each vertex stores a list of adjacent vertices.

# ### 2. **DFS (Depth-First Search)**:

# A graph traversal algorithm where you go as deep as possible down a branch before backtracking. It's useful for tasks like **searching** and **pathfinding**.

# ### 3. **BFS (Breadth-First Search)**:

# A graph traversal algorithm that visits all neighbors of a node before moving to the next level. It's useful for finding the **shortest path** in an unweighted graph.

# ### 4. **Stack**:

# A data structure that follows the **Last-In-First-Out (LIFO)** principle. In DFS, it can be implemented using recursion or manually using a stack.

# ### 5. **Queue**:

# A data structure that follows the **First-In-First-Out (FIFO)** principle. It is used in BFS to explore nodes level by level.

# ---

# ### **Recap of Key Differences**:

# | Aspect                  | **DFS (Depth-First Search)**                    | **BFS (Breadth-First Search)**                                    |
# | ----------------------- | ----------------------------------------------- | ----------------------------------------------------------------- |
# | **Order of Traversal**  | Explores deeply before backtracking.            | Explores all neighbors level by level.                            |
# | **Data Structure Used** | Stack (or Recursion)                            | Queue                                                             |
# | **Use Cases**           | Pathfinding, solving puzzles, topological sort. | Shortest path in unweighted graphs, finding connected components. |

# ---

# That's the breakdown for this code! Let me know if you want to go deeper into any of these concepts or terms.
