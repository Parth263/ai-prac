class Graph:
    def __init__(self):
        self.graph = []       # List to store edges as (weight, u, v)
        self.nodes = set()    # Set to store unique nodes

    def add_edge(self, u, v, weight):
        self.graph.append((weight, u, v))
        self.nodes.add(u)
        self.nodes.add(v)

    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])  # Path compression
        return parent[i]

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[yroot] < rank[xroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal(self):
        result = []
        self.graph.sort()  # Sort edges by weight

        parent = {}
        rank = {}

        for node in self.nodes:
            parent[node] = node
            rank[node] = 0

        for weight, u, v in self.graph:
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                result.append((u, v, weight))
                self.union(parent, rank, x, y)

        print("Edges in the Minimum Spanning Tree:")
        total_weight = 0
        for u, v, weight in result:
            print(f"{u} -- {v} == {weight}")
            total_weight += weight
        print(f"Total weight of MST: {total_weight}")

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

    g.kruskal()



# ### Answer 3: Detailed Step-by-Step Explanation of Kruskal’s Algorithm Code

# The provided code implements **Kruskal’s Algorithm** to find the **Minimum Spanning Tree (MST)** of a connected, undirected, weighted graph with character-labeled nodes (e.g., 'A', 'B'). The algorithm uses a list of edges, a Union-Find data structure with path compression and union by rank, and sorts edges by weight to greedily build the MST. Below is a detailed, step-by-step explanation of the code to help you understand it thoroughly for your AI practical exam.

# ---

# #### 1. **Graph Class and Initialization**
# ```python
# class Graph:
#     def __init__(self):
#         self.graph = []       # List to store edges as (weight, u, v)
#         self.nodes = set()    # Set to store unique nodes
# ```
# - **Class `Graph`**:
#   - Initializes two data structures:
#     - `self.graph`: A list to store edges as tuples `(weight, u, v)`, where `weight` is the edge weight, and `u` and `v` are the nodes it connects.
#     - `self.nodes`: A set to store unique nodes (vertices) in the graph.
#   - Example: After adding an edge ('A', 'B', 4), `self.graph = [(4, 'A', 'B')]`, `self.nodes = {'A', 'B'}`.

# **Purpose**: Sets up the graph representation using an edge list and tracks all nodes.

# ---

# #### 2. **Adding Edges**
# ```python
# def add_edge(self, u, v, weight):
#     self.graph.append((weight, u, v))
#     self.nodes.add(u)
#     self.nodes.add(v)
# ```
# - **Function `add_edge(u, v, weight)`**:
#   - Adds an edge to the graph by appending `(weight, u, v)` to `self.graph`.
#   - Adds nodes `u` and `v` to `self.nodes` to ensure all vertices are tracked.
#   - Note: The graph is undirected, but the code doesn’t store the reverse edge (v, u, weight) explicitly since Kruskal’s processes edges symmetrically (an edge u-v is equivalent to v-u).
#   - Example:
#     ```python
#     g.add_edge('A', 'B', 4)
#     # Updates:
#     # self.graph = [(4, 'A', 'B')]
#     # self.nodes = {'A', 'B'}
#     ```

# **Purpose**: Builds the graph by collecting edges and nodes for processing in Kruskal’s algorithm.

# ---

# #### 3. **Union-Find: Find Operation**
# ```python
# def find(self, parent, i):
#     if parent[i] != i:
#         parent[i] = self.find(parent, parent[i])  # Path compression
#     return parent[i]
# ```
# - **Function `find(parent, i)`**:
#   - Part of the Union-Find data structure to find the root (representative) of the set containing node `i`.
#   - Uses **path compression**:
#     - If `parent[i]` is not `i` (i.e., `i` is not the root), recursively finds the root.
#     - Updates `parent[i]` to point directly to the root, flattening the tree for future lookups.
#   - Returns the root of the set.
#   - Example:
#     ```python
#     parent = {'A': 'B', 'B': 'B'}
#     g.find(parent, 'A')  # Returns 'B', updates parent['A'] = 'B'
#     ```

# **Purpose**: Identifies which component a node belongs to, used to check for cycles.

# ---

# #### 4. **Union-Find: Union Operation**
# ```python
# def union(self, parent, rank, x, y):
#     xroot = self.find(parent, x)
#     yroot = self.find(parent, y)

#     if rank[xroot] < rank[yroot]:
#         parent[xroot] = yroot
#     elif rank[yroot] < rank[xroot]:
#         parent[yroot] = xroot
#     else:
#         parent[yroot] = xroot
#         rank[xroot] += 1
# ```
# - **Function `union(parent, rank, x, y)`**:
#   - Merges the sets containing nodes `x` and `y` using **union by rank** for efficiency.
#   - Steps:
#     - Finds the roots of `x` and `y` using `find` (`xroot`, `yroot`).
#     - Compares the ranks (tree heights) of the roots:
#       - If `rank[xroot] < rank[yroot]`, makes `yroot` the parent of `xroot`.
#       - If `rank[yroot] < rank[xroot]`, makes `xroot` the parent of `yroot`.
#       - If ranks are equal, arbitrarily chooses `xroot` as parent and increments its rank by 1.
#   - Example:
#     ```python
#     parent = {'A': 'A', 'B': 'B'}
#     rank = {'A': 0, 'B': 0}
#     g.union(parent, rank, 'A', 'B')
#     # Updates: parent = {'A': 'A', 'B': 'A'}, rank = {'A': 1, 'B': 0}
#     ```

# **Purpose**: Combines two components into one, maintaining a balanced tree to optimize future `find` operations.

# ---

# #### 5. **Kruskal’s Algorithm Implementation**
# ```python
# def kruskal(self):
#     result = []
#     self.graph.sort()  # Sort edges by weight

#     parent = {}
#     rank = {}

#     for node in self.nodes:
#         parent[node] = node
#         rank[node] = 0
# ```
# - **Function `kruskal()`**:
#   - Implements Kruskal’s algorithm to find the MST.
# - **Initialization**:
#   - `result`: List to store MST edges as tuples `(u, v, weight)`.
#   - `self.graph.sort()`: Sorts `self.graph` by the first element (`weight`) in ascending order.
#     - Example: `[(4, 'A', 'B'), (3, 'A', 'C'), (1, 'B', 'C')]` → `[(1, 'B', 'C'), (3, 'A', 'C'), (4, 'A', 'B')]`.
#   - `parent`: Dictionary where each node is initially its own parent (disjoint sets).
#   - `rank`: Dictionary to track the height of each tree, initialized to 0 for all nodes.
#   - Example:
#     ```python
#     self.nodes = {'A', 'B', 'C'}
#     parent = {'A': 'A', 'B': 'B', 'C': 'C'}
#     rank = {'A': 0, 'B': 0, 'C': 0}
#     ```

# **Purpose**: Prepares the MST result list, sorts edges, and initializes Union-Find structures.

# ---

# #### 6. **Main Loop: Processing Edges**
# ```python
# for weight, u, v in self.graph:
#     x = self.find(parent, u)
#     y = self.find(parent, v)

#     if x != y:
#         result.append((u, v, weight))
#         self.union(parent, rank, x, y)
# ```
# - **Loop**:
#   - Iterates through sorted edges in `self.graph` (smallest weight first).
#   - For each edge `(weight, u, v)`:
#     - Finds the roots of `u` and `v` using `find` (`x` and `y`).
#     - If `x != y` (u and v are in different components, so no cycle):
#       - Adds `(u, v, weight)` to `result` (includes edge in MST).
#       - Calls `union` to merge the components of `x` and `y`.
#     - If `x == y`, skips the edge (it would form a cycle).

# **Purpose**: Greedily selects edges that don’t form cycles, building the MST.

# ---

# #### 7. **Output Results**
# ```python
# print("Edges in the Minimum Spanning Tree:")
# total_weight = 0
# for u, v, weight in result:
#     print(f"{u} -- {v} == {weight}")
#     total_weight += weight
# print(f"Total weight of MST: {total_weight}")
# ```
# - **Output**:
#   - Prints each edge in `result` as `u -- v == weight` (e.g., `B -- C == 1`).
#   - Accumulates `total_weight` by summing edge weights.
#   - Prints the total weight of the MST.
# - **Example Output**:
#   ```
#   Edges in the Minimum Spanning Tree:
#   B -- C == 1
#   B -- D == 2
#   D -- E == 2
#   A -- C == 3
#   E -- F == 6
#   Total weight of MST: 14
#   ```

# **Purpose**: Displays the MST edges and their total weight for verification.

# ---

# #### 8. **Main Execution and Example Graph**
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

#     g.kruskal()
# ```
# - **Graph Setup**:
#   - Creates a `Graph` object `g`.
#   - Adds edges to form the following weighted undirected graph:
#     - A -- B (4), A -- C (3), B -- C (1), B -- D (2), C -- D (4), D -- E (2), E -- F (6).
# - **Edge List** (before sorting):
#   ```python
#   self.graph = [(4, 'A', 'B'), (3, 'A', 'C'), (1, 'B', 'C'), (2, 'B', 'D'), (4, 'C', 'D'), (2, 'D', 'E'), (6, 'E', 'F')]
#   self.nodes = {'A', 'B', 'C', 'D', 'E', 'F'}
#   ```
# - **Run Kruskal’s**:
#   - Calls `g.kruskal()` to find and print the MST.

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
# Let’s trace Kruskal’s algorithm for the example graph:
# 1. **Initialize**:
#    - `result = []`, `parent = {'A': 'A', 'B': 'B', ..., 'F': 'F'}`, `rank = {'A': 0, ..., 'F': 0}`.
#    - Sort `self.graph`: `[(1, 'B', 'C'), (2, 'B', 'D'), (2, 'D', 'E'), (3, 'A', 'C'), (4, 'A', 'B'), (4, 'C', 'D'), (6, 'E', 'F')]`.
# 2. **Edge 1: (B, C, 1)**:
#    - `find('B') = 'B'`, `find('C') = 'C'`. Different sets.
#    - Add `(B, C, 1)` to `result`.
#    - `union('B', 'C')`: `parent['C'] = 'B'`, `rank['B'] = 1`.
# 3. **Edge 2: (B, D, 2)**:
#    - `find('B') = 'B'`, `find('D') = 'D'`. Different sets.
#    - Add `(B, D, 2)` to `result`.
#    - `union('B', 'D')`: `parent['D'] = 'B'`, `rank['B'] = 1`.
# 4. **Edge 3: (D, E, 2)**:
#    - `find('D') = 'B'`, `find('E') = 'E'`. Different sets.
#    - Add `(D, E, 2)` to `result`.
#    - `union('B', 'E')`: `parent['E'] = 'B'`, `rank['B'] = 1`.
# 5. **Edge 4: (A, C, 3)**:
#    - `find('A') = 'A'`, `find('C') = 'B'`. Different sets.
#    - Add `(A, C, 3)` to `result`.
#    - `union('A', 'B')`: `parent['A'] = 'B'`, `rank['B'] = 1`.
# 6. **Edge 5: (A, B, 4)**:
#    - `find('A') = 'B'`, `find('B') = 'B'`. Same set (cycle).
#    - Skip.
# 7. **Edge 6: (C, D, 4)**:
#    - `find('C') = 'B'`, `find('D') = 'B'`. Same set (cycle).
#    - Skip.
# 8. **Edge 7: (E, F, 6)**:
#    - `find('E') = 'B'`, `find('F') = 'F'`. Different sets.
#    - Add `(E, F, 6)` to `result`.
#    - `union('B', 'F')`: `parent['F'] = 'B'`, `rank['B'] = 1`.
# 9. **End**:
#    - `result` has 5 edges (V-1 = 6-1), covering all nodes.
#    - Output:
#      ```
#      Edges in the Minimum Spanning Tree:
#      B -- C == 1
#      B -- D == 2
#      D -- E == 2
#      A -- C == 3
#      E -- F == 6
#      Total weight of MST: 14
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
# Running `python3 kruskals_algorithm.py` in the VS Code terminal produces:
# ```
# Edges in the Minimum Spanning Tree:
# B -- C == 1
# B -- D == 2
# D -- E == 2
# A -- C == 3
# E -- F == 6
# Total weight of MST: 14
# ```

# ---

# ### Notes for Your Exam
# - **Key Concepts**: Understand the greedy approach, edge sorting, Union-Find with path compression and union by rank, and cycle detection.
# - **Code Structure**: Be ready to explain `add_edge`, `find`, `union`, and the `kruskal` function, especially how Union-Find prevents cycles.
# - **Edge Cases**: The code assumes a connected graph. For disconnected graphs, Kruskal’s would stop early (fewer than V-1 edges). Mention this if asked.
# - **Running in VS Code**: Save as `kruskals_algorithm.py`, ensure `python3` works, and run `python3 kruskals_algorithm.py` in the terminal.
# - **Customization**: If your exam provides a different graph, modify the `add_edge` calls in the main block.

# This explanation should help you master Kruskal’s algorithm for your AI practical exam. If you have more practicals or need further clarification, let me know!