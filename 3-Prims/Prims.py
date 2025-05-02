import heapq

class Graph:
    def __init__(self):
        self.graph = {}  # Ad sairjacency list

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []

        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))  # Undirected

    def prim(self, start):
        visited = set()
        min_heap = [(0, start, None)]  # (weight, current_node, previous_node)
        mst_cost = 0
        mst_edges = []

        while min_heap:
            weight, current, prev = heapq.heappop(min_heap)

            if current in visited:
                continue

            visited.add(current)
            mst_cost += weight
            if prev is not None:
                mst_edges.append((prev, current, weight))

            for neighbor, w in self.graph[current]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (w, neighbor, current))

        print("Edges in the Minimum Spanning Tree:")
        for u, v, weight in mst_edges:
            print(f"{u} -- {v} == {weight}")
        print(f"Total cost of MST: {mst_cost}")

# Example Usage
if __name__ == "__main__":
    g = Graph()
    g.add_edge('A', 'B', 4)
    g.add_edge('A', 'C', 3)
    g.add_edge('B', 'C', 1)
    g.add_edge('B', 'D', 2)
    g.add_edge('C', 'D', 4)
    g.add_edge('D', 'E', 2)
    g.add_edge('E', 'F', 6)

    g.prim('A')




# ### Answer 3: Detailed Step-by-Step Explanation of Prim’s Algorithm Code

# The provided code implements **Prim’s Algorithm** to find the **Minimum Spanning Tree (MST)** of a connected, undirected, weighted graph with character-labeled nodes (e.g., 'A', 'B'). The algorithm uses an adjacency list to represent the graph, a min-heap to select the smallest-weight edge, and a visited set to track included nodes. Below is a detailed, step-by-step explanation of the code to help you understand it thoroughly for your AI practical exam.

# ---

# #### 1. **Imports and Graph Class**
# ```python
# import heapq

# class Graph:
#     def __init__(self):
#         self.graph = {}  # Adjacency list
# ```
# - **Import**:
#   - `heapq`: Python’s module for a min-heap priority queue, used to efficiently select the edge with the smallest weight.
# - **Class `Graph`**:
#   - Initializes an empty dictionary `self.graph` to store the graph as an adjacency list.
#   - Keys are nodes (e.g., 'A', 'B'), and values are lists of tuples `(neighbor, weight)` representing edges and their weights.
#   - Example: `self.graph['A'] = [('B', 4), ('C', 3)]` means node 'A' connects to 'B' (weight 4) and 'C' (weight 3).

# **Purpose**: Sets up the graph structure to store nodes and weighted edges.

# ---

# #### 2. **Adding Edges**
# ```python
# def add_edge(self, u, v, weight):
#     if u not in self.graph:
#         self.graph[u] = []
#     if v not in self.graph:
#         self.graph[v] = []

#     self.graph[u].append((v, weight))
#     self.graph[v].append((u, weight))  # Undirected
# ```
# - **Function `add_edge(u, v, weight)`**:
#   - Adds an edge between nodes `u` and `v` with the given `weight` to the undirected graph.
#   - Steps:
#     - If `u` or `v` is not in `self.graph`, initializes an empty list for them.
#     - Appends `(v, weight)` to `u`’s adjacency list and `(u, weight)` to `v`’s list, since the graph is undirected (edges go both ways).
#   - Example:
#     ```python
#     g.add_edge('A', 'B', 4)
#     # Updates:
#     # self.graph['A'] = [('B', 4)]
#     # self.graph['B'] = [('A', 4)]
#     ```

# **Purpose**: Builds the graph by adding edges with weights, ensuring bidirectionality for undirected edges.

# ---

# #### 3. **Prim’s Algorithm Implementation**
# ```python
# def prim(self, start):
#     visited = set()
#     min_heap = [(0, start, None)]  # (weight, current_node, previous_node)
#     mst_cost = 0
#     mst_edges = []
# ```
# - **Function `prim(start)`**:
#   - Implements Prim’s algorithm to find the MST starting from the node `start` (e.g., 'A').
# - **Initialization**:
#   - `visited`: A set to track nodes included in the MST (initially empty).
#   - `min_heap`: A priority queue (min-heap) storing tuples `(weight, current_node, previous_node)`.
#     - Starts with `(0, start, None)` to include the starting node with zero cost (no edge to add yet).
#     - `previous_node` is `None` for the start node since it has no predecessor.
#   - `mst_cost`: Tracks the total weight of the MST (initially 0).
#   - `mst_edges`: List to store the edges in the MST as tuples `(prev, current, weight)`.

# **Purpose**: Sets up the data structures and begins Prim’s algorithm from the specified start node.

# ---

# #### 4. **Main Loop of Prim’s Algorithm**
# ```python
# while min_heap:
#     weight, current, prev = heapq.heappop(min_heap)

#     if current in visited:
#         continue

#     visited.add(current)
#     mst_cost += weight
#     if prev is not None:
#         mst_edges.append((prev, current, weight))
# ```
# - **Loop**:
#   - Continues while `min_heap` is not empty (edges remain to explore).
# - **Pop Edge**:
#   - `heapq.heappop(min_heap)`: Removes and returns the tuple with the smallest `weight`.
#   - Extracts `weight` (edge weight), `current` (node to visit), and `prev` (previous node).
# - **Visited Check**:
#   - If `current` is already in `visited`, skips to avoid cycles (since another path to this node was chosen earlier).
# - **Update MST**:
#   - Adds `current` to `visited`, marking it as part of the MST.
#   - Adds `weight` to `mst_cost` to update the total cost.
#   - If `prev` is not `None` (i.e., not the start node), appends `(prev, current, weight)` to `mst_edges` to record the edge in the MST.

# **Purpose**: Selects the smallest-weight edge to a new node, includes it in the MST, and updates the cost and edges.

# ---

# #### 5. **Exploring Neighbors**
# ```python
# for neighbor, w in self.graph[current]:
#     if neighbor not in visited:
#         heapq.heappush(min_heap, (w, neighbor, current))
# ```
# - **Neighbor Loop**:
#   - Iterates through `self.graph[current]`, which contains tuples `(neighbor, w)` for each neighbor of `current` and its edge weight `w`.
#   - If `neighbor` is not in `visited`, pushes `(w, neighbor, current)` to `min_heap`.
#     - `w`: Weight of the edge to `neighbor`.
#     - `neighbor`: The node to potentially include next.
#     - `current`: The previous node (for tracking the edge if chosen).

# **Purpose**: Adds all unvisited neighbors of the current node to the min-heap for consideration, allowing the algorithm to explore new edges.

# ---

# #### 6. **Output Results**
# ```python
# print("Edges in the Minimum Spanning Tree:")
# for u, v, weight in mst_edges:
#     print(f"{u} -- {v} == {weight}")
# print(f"Total cost of MST: {mst_cost}")
# ```
# - **Output**:
#   - Prints the edges in the MST, formatted as `u -- v == weight` (e.g., `A -- C == 3`).
#   - Prints the total cost of the MST (`mst_cost`).
# - **Example**:
#   ```
#   Edges in the Minimum Spanning Tree:
#   A -- C == 3
#   C -- B == 1
#   B -- D == 2
#   D -- E == 2
#   E -- F == 6
#   Total cost of MST: 14
#   ```

# **Purpose**: Displays the MST’s edges and total weight for verification.

# ---

# #### 7. **Main Execution and Example Graph**
# ```python
# if __name__ == "__main__":
#     g = Graph()
#     g.add_edge('A', 'B', 4)
#     g.add_edge('A', 'C', 3)
#     g.add_edge('B', 'C', 1)
#     g.add_edge('B', 'D', 2)
#     g.add_edge('C', 'D', 4)
#     g.add_edge('D', 'E', 2)
#     g.add_edge('E', 'F', 6)

#     g.prim('A')
# ```
# - **Graph Setup**:
#   - Creates a `Graph` object `g`.
#   - Adds edges to form the following weighted undirected graph:
#     - A -- B (4), A -- C (3), B -- C (1), B -- D (2), C -- D (4), D -- E (2), E -- F (6).
# - **Adjacency List**:
#   ```python
#   self.graph = {
#       'A': [('B', 4), ('C', 3)],
#       'B': [('A', 4), ('C', 1), ('D', 2)],
#       'C': [('A', 3), ('B', 1), ('D', 4)],
#       'D': [('B', 2), ('C', 4), ('E', 2)],
#       'E': [('D', 2), ('F', 6)],
#       'F': [('E', 6)]
#   }
#   ```
# - **Run Prim’s**:
#   - Calls `g.prim('A')` to find the MST starting from node 'A'.

# **Graph Visualization**:
# ```
#    A ---4--- B
#    | \       | \
#    |  3      |  1
#    |   \     |   \
#    C ---4--- D ---2--- E ---6--- F
# ```

# ---

# ### Execution Walkthrough
# Let’s trace Prim’s algorithm for the example graph starting from 'A':
# 1. **Initialize**:
#    - `visited = {}`, `min_heap = [(0, 'A', None)]`, `mst_cost = 0`, `mst_edges = []`.
# 2. **Iteration 1**:
#    - Pop `(0, 'A', None)`.
#    - Add 'A' to `visited`.
#    - `mst_cost = 0` (no edge added yet).
#    - Neighbors of 'A': [('B', 4), ('C', 3)].
#    - Push `(4, 'B', 'A')`, `(3, 'C', 'A')` to `min_heap`.
# 3. **Iteration 2**:
#    - Pop `(3, 'C', 'A')` (smallest weight).
#    - Add 'C' to `visited`.
#    - `mst_cost = 3`, `mst_edges = [('A', 'C', 3)]`.
#    - Neighbors of 'C': [('A', 3), ('B', 1), ('D', 4)].
#    - 'A' is visited, so push `(1, '킬', 'C')`, `(4, 'D', 'C')`.
# 4. **Iteration 3**:
#    - Pop `(1, 'B', 'C')`.
#    - Add 'B' to `visited`.
#    - `mst_cost = 3 + 1 = 4`, `mst_edges = [('A', 'C', 3), ('C', 'B', 1)]`.
#    - Neighbors of 'B': [('A', 4), ('C', 1), ('D', 2)].
#    - 'A', 'C' visited, so push `(2, 'D', 'B')`.
# 5. **Iteration 4**:
#    - Pop `(2, 'D', 'B')`.
#    - Add 'D' to `visited`.
#    - `m відвід_cost = 4 + 2 = 6`, `mst_edges = [('A', 'C', 3), ('C', 'B', 1), ('B', 'D', 2)]`.
#    - Neighbors of 'D': [('B', 2), ('C', 4), ('E', 2)].
#    - 'B', 'C' visited, so push `(2, 'E', 'D')`.
# 6. **Iteration 5**:
#    - Pop `(2, 'E', 'D')`.
#    - Add 'E' to `visited`.
#    - `mst_cost = 6 + 2 = 8`, `mst_edges = [('A', 'C', 3), ('C', 'B', 1), ('B', 'D', 2), ('D', 'E', 2)]`.
#    - Neighbors of 'E': [('D', 2), ('F', 6)].
#    - 'D' visited, so push `(6, 'F', 'E')`.
# 7. **Iteration 6**:
#    - Pop `(6, 'F', 'E')`.
#    - Add 'F' to `visited`.
#    - `mst_cost = 8 + 6 = 14`, `mst_edges = [('A', 'C', 3), ('C', 'B', 1), ('B', 'D', 2), ('D', 'E', 2), ('E', 'F', 6)]`.
#    - Neighbors of 'F': [('E', 6)]. 'E' visited, so no pushes.
# 8. **End**:
#    - `min_heap` is empty, all nodes visited.
#    - Output:
#      ```
#      Edges in the Minimum Spanning Tree:
#      A -- C == 3
#      C -- B == 1
#      B -- D == 2
#      D -- E == 2
#      E -- F == 6
#      Total cost of MST: 14
#      ```

# **MST Visualization**:
# ```
#    A ---3--- C ---1--- B
#                        |
#                        2
#                        |
#                        D ---2--- E ---6--- F
# ```

# ---

# ### Expected Output
# Running `python3 prims_algorithm.py` in the VS Code terminal produces:
# ```
# Edges in the Minimum Spanning Tree:
# A -- C == 3
# C -- B == 1
# B -- D == 2
# D -- E == 2
# E -- F == 6
# Total cost of MST: 14
# ```

# ---

# ### Notes for Your Exam
# - **Key Concepts**: Understand the greedy approach, min-heap for selecting smallest edges, adjacency list for graph representation, and visited set to avoid cycles.
# - **Code Structure**: Be ready to explain `add_edge`, the `prim` function, and how the min-heap drives the algorithm.
# - **Edge Cases**: The code assumes a connected graph. For disconnected graphs, Prim’s would need modification to handle multiple components.
# - **Running in VS Code**: Save as `prims_algorithm.py`, ensure `python3` works, and run `python3 prims_algorithm.py` in the terminal.
# - **Customization**: If your exam provides a different graph, modify the `add_edge` calls in the main block.

# This explanation should help you master Prim’s algorithm for your AI practical exam. If you have more practicals or need further clarification, let me know!