import heapq

# Goal state for reference
goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# Convert 2D list to tuple for hashing
def to_tuple(state):
    return tuple(tuple(row) for row in state)

# Get the position of a number in a matrix
def find_pos(state, num): 
    for i in range(3):
        for j in range(3):
            if state[i][j] == num:
                return i, j

# Manhattan Distance Heuristic
def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                goal_i, goal_j = find_pos(goal_state, val)
                distance += abs(goal_i - i) + abs(goal_j - j)
    return distance

# Generate possible moves
def get_neighbors(state):
    neighbors = []
    x, y = find_pos(state, 0)
    moves = [(-1,0), (1,0), (0,-1), (0,1)]  # up, down, left, right
    for dx, dy in moves:
        nx, ny = x+dx, y+dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

# A* Algorithm
def a_star(start_state):
    start_tuple = to_tuple(start_state)
    goal_tuple = to_tuple(goal_state)

    open_list = []
    heapq.heappush(open_list, (manhattan_distance(start_state), 0, start_state))
    visited = set()
    parent = {to_tuple(start_state): None}
    cost_so_far = {start_tuple: 0}

    while open_list:
        _, cost, current = heapq.heappop(open_list)
        current_tuple = to_tuple(current)

        if current_tuple == goal_tuple:
            path = []
            while current:
                path.append(current)
                current = parent[to_tuple(current)]
            return path[::-1]

        if current_tuple in visited:
            continue
        visited.add(current_tuple)

        for neighbor in get_neighbors(current):
            neighbor_tuple = to_tuple(neighbor)
            new_cost = cost + 1

            if neighbor_tuple not in cost_so_far or new_cost < cost_so_far[neighbor_tuple]:
                cost_so_far[neighbor_tuple] = new_cost
                priority = new_cost + manhattan_distance(neighbor)
                heapq.heappush(open_list, (priority, new_cost, neighbor))
                parent[neighbor_tuple] = current

    return None

# Main Execution
if __name__ == "__main__":
    start_state = [
        [1, 2, 3],
        [0, 4, 5],
        [6, 7, 8]
    ]

    solution = a_star(start_state)

    if solution:
        print("Solution steps:")
        for step in solution:
            for row in step:
                print(' '.join(str(x) if x != 0 else '_' for x in row))
            print()
    else:
        print("No solution found.")





# Great! Let's begin with a **step-by-step explanation** of the A\* algorithm code for solving the **8-puzzle problem**.

# ---

# ## 🔹 Step-by-Step Code Explanation (Part 1)

# ### ✅ Part 1: Setup and Helper Functions

# ---

# ### 1. **Goal State Definition**

# ```python
# goal_state = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 0]
# ]
# ```

# * This represents the target configuration for the 8-puzzle.
# * The `0` represents the empty tile.

# ---

# ### 2. **`to_tuple(state)`**

# ```python
# def to_tuple(state):
#     return tuple(tuple(row) for row in state)
# ```

# * Converts the 2D list (matrix) to a tuple of tuples.
# * Why? So it can be **used in sets/dictionaries** (tuples are hashable, lists are not).

# ---

# ### 3. **`find_pos(state, num)`**

# ```python
# def find_pos(state, num): 
#     for i in range(3):
#         for j in range(3):
#             if state[i][j] == num:
#                 return i, j
# ```

# * Finds and returns the **(row, col)** position of a number (`num`) in the state.

# ---

# ### 4. **`manhattan_distance(state)`**

# ```python
# def manhattan_distance(state):
#     distance = 0
#     for i in range(3):
#         for j in range(3):
#             val = state[i][j]
#             if val != 0:
#                 goal_i, goal_j = find_pos(goal_state, val)
#                 distance += abs(goal_i - i) + abs(goal_j - j)
#     return distance
# ```

# * **Heuristic function** for A\*.
# * Calculates total **Manhattan distance**:

#   * For each tile (excluding 0), compute how far it is from its position in the goal state using:

#     ```
#     |current_row - goal_row| + |current_col - goal_col|
#     ```
# * Lower values = closer to the goal.

# ---

# ### 5. **`get_neighbors(state)`**

# ```python
# def get_neighbors(state):
#     ...
# ```

# * Generates **valid moves** by sliding the blank tile (0) in all possible directions (up, down, left, right).
# * Returns all resulting new states.

# ---

# Let me know when you're ready to proceed with the **A* algorithm part*\* and key concepts behind it. Just say **next**.
