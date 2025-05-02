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


# Absolutely! Let's break this code down step-by-step in **easy language**. Then, I'll give you a **short algorithm summary** and explain any new terms like **path compression**, **union by rank**, etc.

# ---

# ## 🧠 What Is This Code Doing?

# It implements **Kruskal’s Algorithm** — another way to find the **Minimum Spanning Tree (MST)** of an undirected, weighted graph. Unlike Prim’s, Kruskal’s starts with **no edges** and adds the **smallest edges** one by one, avoiding cycles.

# ---

# ## 🔍 Code Explanation (Step-by-Step)

# ### 🔹 `__init__(self)`:

# ```python
# self.graph = []       # Stores edges as (weight, u, v)
# self.nodes = set()    # Stores unique nodes
# ```

# * Edges will be saved as tuples like `(weight, node1, node2)`.
# * `set()` ensures no duplicate nodes.

# ---

# ### 🔹 `add_edge(self, u, v, weight)`:

# Adds an edge and stores both nodes:

# ```python
# g.add_edge('A', 'B', 4)  →  (4, 'A', 'B')
# ```

# ---

# ### 🔹 `find(self, parent, i)`:

# This is part of the **Disjoint Set (Union-Find)** data structure.

# * Used to find the **root parent** of node `i`.
# * If not its own parent, recursively find the top parent.
# * Includes **path compression** for optimization: directly connects nodes to their root to make future searches faster.

# 👉 **New Term: Path Compression**
# Reduces the time of `find()` by flattening the structure of the tree. Speeds up the algorithm.

# ---

# ### 🔹 `union(self, parent, rank, x, y)`:

# * Connects two sets by joining their root parents.
# * Uses **rank** to attach the smaller tree under the bigger one.

# 👉 **New Term: Union by Rank**
# Each node has a "rank" (like depth). Lower-rank trees are joined under higher-rank ones to keep the tree shallow (fast `find()`).

# ---

# ### 🔹 `kruskal(self)`:

# This is the **main function** that applies **Kruskal’s Algorithm**.

# #### ✅ Key Steps:

# 1. **Sort all edges** in increasing order of weights.
# 2. **Initialize disjoint sets**:

#    * Each node is its own parent (initially).
#    * Ranks are 0.
# 3. **Go through sorted edges**:

#    * For each edge `(u, v, weight)`:

#      * Check if `u` and `v` belong to different sets using `find`.
#      * If yes, add it to MST (`result`) and `union` their sets.
# 4. **Print the MST edges and total cost.**

# ---

# ## 🧾 Output for Given Graph

# Edges added to MST (chosen in order of smallest weight without cycles):

# ```
# B -- C == 1
# B -- D == 2
# D -- E == 2
# A -- C == 3
# E -- F == 6
# ```

# ✅ **Total weight = 1 + 2 + 2 + 3 + 6 = 14**

# ---

# ## 📌 Short Algorithm Summary: **Kruskal’s Algorithm**

# > **Goal:** Find MST by selecting the **lowest weight edges**, making sure no cycles are formed.

# ### 🔁 **Steps:**

# 1. Sort all edges in increasing order.
# 2. Initialize disjoint sets (Union-Find).
# 3. For each edge `(u, v)`:

#    * If `u` and `v` are in **different sets**, add the edge to MST.
#    * Merge the sets using **union by rank**.
# 4. Stop when MST has `n-1` edges (n = number of nodes).

# ---

# ## 📚 New Terms Recap

# | Term                 | Meaning                                                                  |
# | -------------------- | ------------------------------------------------------------------------ |
# | **Disjoint Set**     | A data structure that keeps track of elements split into disjoint groups |
# | **Find**             | Checks which group a node belongs to                                     |
# | **Union**            | Joins two groups together                                                |
# | **Path Compression** | Optimizes `find()` by flattening tree structure                          |
# | **Union by Rank**    | Attaches smaller tree to root of larger tree to keep structure shallow   |

# ---

# Would you like a comparison between **Prim’s** and **Kruskal’s** in a table format next?

