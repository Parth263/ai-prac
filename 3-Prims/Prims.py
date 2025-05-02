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



# Let’s break down the given **Prim’s Algorithm** code and explain it in **simple steps** — along with what the output will be and **why** it appears that way.

# ---

# ## ✅ **What is Prim’s Algorithm?**

# Prim’s algorithm finds the **Minimum Spanning Tree (MST)** of a graph:

# * A **spanning tree** connects all vertices (nodes) without any cycles.
# * A **minimum** spanning tree is the one with the **lowest total edge weight**.

# ---

# ## 📘 **Code Explanation Step-by-Step**

# ### **1. `class Graph:`**

# Defines a class to represent the graph using an **adjacency list** (dictionary of lists).

# ---

# ### **2. `__init__`**

# ```python
# def __init__(self):
#     self.graph = {}
# ```

# Initializes the graph as an empty dictionary. This will store the edges like:

# ```python
# { 'A': [('B', 4), ('C', 3)], ... }
# ```

# ---

# ### **3. `add_edge(self, u, v, weight)`**

# ```python
# self.graph[u].append((v, weight))
# self.graph[v].append((u, weight))
# ```

# * Adds an edge between `u` and `v` with the given `weight`.
# * Since the graph is **undirected**, both directions are added (i.e., A–B and B–A).

# ---

# ### **4. `prim(self, start)`**

# Main function that applies **Prim’s Algorithm** to find the MST from a given starting node.

# #### Key variables:

# * `visited`: Keeps track of which nodes have been visited.
# * `min_heap`: Priority queue of nodes to explore, sorted by weight.
# * `mst_cost`: Total cost of MST.
# * `mst_edges`: List of selected edges in the MST.

# ---

# ### **Step-by-step Inside `prim`:**

# ```python
# min_heap = [(0, start, None)]
# ```

# Start with 0 weight at the start node (`'A'`), with no previous node.

# Then in the loop:

# ```python
# while min_heap:
#     weight, current, prev = heapq.heappop(min_heap)
# ```

# * Always select the edge with **minimum weight** (min-heap behavior).

# ```python
# if current in visited:
#     continue
# ```

# * Skip if node already visited (to avoid cycles).

# ```python
# visited.add(current)
# mst_cost += weight
# ```

# * Mark node as visited.
# * Add edge's weight to total MST cost.

# ```python
# if prev is not None:
#     mst_edges.append((prev, current, weight))
# ```

# * Save the edge (unless it's the start node).

# ```python
# for neighbor, w in self.graph[current]:
#     if neighbor not in visited:
#         heapq.heappush(min_heap, (w, neighbor, current))
# ```

# * Add unvisited neighbors to heap with their edge weights.

# ---

# ## 🖥️ Example Graph Edges

# ```plaintext
# A - B (4)
# A - C (3)
# B - C (1)
# B - D (2)
# C - D (4)
# D - E (2)
# E - F (6)
# ```

# ---

# ## ✅ Output and Why

# Starting from `'A'`, the MST will include the **smallest-weight edges** that connect all nodes **without cycles**:

# 1. Start at `A`:

#    * Pick edge A–C (3)
# 2. From `C`, pick C–B (1)
# 3. From `B`, pick B–D (2)
# 4. From `D`, pick D–E (2)
# 5. From `E`, pick E–F (6)

# So the MST is:

# ```
# A -- C == 3
# C -- B == 1
# B -- D == 2
# D -- E == 2
# E -- F == 6
# ```

# **Total cost = 3 + 1 + 2 + 2 + 6 = 14**

# ---

# ## ✅ Final Output:

# ```
# Edges in the Minimum Spanning Tree:
# A -- C == 3
# C -- B == 1
# B -- D == 2
# D -- E == 2
# E -- F == 6
# Total cost of MST: 14
# ```


# ### 🔁 **Prim’s Algorithm (Step-by-Step)**

# 1. **Initialize**:

#    * Create a min-heap (priority queue).
#    * Set all node distances to infinity, except start node (0).
#    * Keep track of visited nodes.
#    * Store MST edges and total cost.

# 2. **Start with any node** (say `A`), push it into the heap with weight 0.

# 3. **While heap is not empty**:

#    * Pop the node with the smallest weight.
#    * If it's already visited, skip.
#    * Mark it as visited.
#    * Add edge to MST (if not starting node).
#    * Add all unvisited neighbors to the heap with their weights.

# 4. **Repeat** until all nodes are visited.

# ---

# ### ✅ Output:

# * List of edges in MST.
# * Total cost.

# ---

# Would you like this turned into pseudocode or a flowchart as well?
