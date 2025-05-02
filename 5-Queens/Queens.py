def is_safe(board, row, col, n):
    # Check column above
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper right diagonal
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def solve_n_queens(board, row, n):
    if row == n:
        for r in board:
            print(" ".join("Q" if c == 1 else "." for c in r))
        print()
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            if solve_n_queens(board, row + 1, n):
                return True
            board[row][col] = 0  # Backtrack

    return False

# Main
if __name__ == "__main__":
    n = 4
    board = [[0 for _ in range(n)] for _ in range(n)]
    solve_n_queens(board, 0, n)






# ### Answer 3: Detailed Step-by-Step Explanation of the N-Queens Problem Code

# The provided code solves the **N-Queens Problem**, a classic Constraint Satisfaction Problem (CSP), using **backtracking** with a **branch and bound** approach. The goal is to place N queens on an NxN chessboard such that no two queens threaten each other (i.e., no queens share the same row, column, or diagonal). The code uses a 2D board to track queen placements and recursively explores valid configurations. Below is a detailed, step-by-step explanation of the code to help you understand it thoroughly for your AI practical exam.

# ---

# #### 1. **Function: `is_safe(board, row, col, n)`**
# ```python
# def is_safe(board, row, col, n):
#     # Check column above
#     for i in range(row):
#         if board صدای[i][col] == 1:
#             return False

#     # Check upper left diagonal
#     i, j = row, col
#     while i >= 0 and j >= 0:
#         if board[i][j] == 1:
#             return False
#         i -= 1
#         j -= 1

#     # Check upper right diagonal
#     i, j = row, col
#     while i >= 0 and j < n:
#         if board[i][j] == 1:
#             return False
#         i -= 1
#         j += 1

#     return True
# ```
# - **Purpose**: Checks if it’s safe to place a queen at position `(row, col)` on the NxN `board` without violating the N-Queens constraints.
# - **Steps**:
#   1. **Check Column Above**:
#      - Loops through rows `i` from 0 to `row-1` in the same column `col`.
#      - If `board[i][col] == 1` (a queen exists), returns `False` (unsafe).
#   2. **Check Upper Left Diagonal**:
#      - Starts at `(row, col)` and moves up-left (`i -= 1`, `j -= 1`) while `i >= 0` and `j >= 0`.
#      - If `board[i][j] == 1` (a queen exists), returns `False`.
#   3. **Check Upper Right Diagonal**:
#      - Starts at `(row, col)` and moves up-right (`i -= 1`, `j += 1`) while `i >= 0` and `j < n`.
#      - If `board[i][j] == 1` (a queen exists), returns `False`.
#   4. **Return**:
#      - If no queens are found in the column or diagonals, returns `True` (safe to place a queen).
# - **Example**:
#   ```python
#   board = [[0, 0, 1, 0],  # Row 0: Queen at col 2
#            [1, 0, 0, 0],  # Row 1: Queen at col 0
#            [0, 0, 0, 0],  # Row 2: Empty
#            [0, 0, 0, 0]]  # Row 3: Empty
#   is_safe(board, 2, 1, 4)  # Check (row=2, col=1)
#   # Returns False (queen at (0, 2) is on upper-right diagonal)
#   ```

# **Purpose**: Ensures a queen can be placed without being attacked, enforcing CSP constraints.

# ---

# #### 2. **Function: `solve_n_queens(board, row, n)`**
# ```python
# def solve_n_queens(board, row, n):
#     if row == n:
#         for r in board:
#             print(" ".join("Q" if c == 1 else "." for c in r))
#         print()
#         return True

#     for col in range(n):
#         if is_safe(board, row, col, n):
#             board[row][col] = 1
#             if solve_n_queens(board, row + 1, n):
#                 return True
#             board[row][col] = 0  # Backtrack

#     return False
# ```
# - **Purpose**: Recursively places queens row by row, using backtracking to find a valid solution.
# - **Steps**:
#   1. **Base Case**:
#      - If `row == n`, all queens are placed (one per row).
#      - Prints the board:
#        - For each row `r`, converts `1` to `"Q"` (queen) and `0` to `"."` (empty).
#        - Joins elements with spaces and prints each row, followed by a blank line.
#      - Returns `True` to indicate a solution is found and stop further exploration.
#   2. **Column Loop**:
#      - For the current `row`, tries each column `col` from 0 to `n-1`.
#      - Calls `is_safe(board, row, col, n)` to check if placing a queen is valid.
#   3. **Place Queen**:
#      - If safe, sets `board[row][col] = 1` to place a queen.
#      - Recursively calls `solve_n_queens(board, row + 1, n)` to place a queen in the next row.
#   4. **Backtrack**:
#      - If the recursive call returns `False` (no solution with this placement), sets `board[row][col] = 0` to remove the queen.
#      - Tries the next column.
#   5. **Return**:
#      - If no column in the current row works, returns `False` to trigger backtracking in the previous row.
#      - If a solution is found, returns `True` to stop and propagate success.

# **Purpose**: Explores all valid queen placements using backtracking, printing the first valid solution.

# ---

# #### 3. **Main Execution**
# ```python
# if __name__ == "__main__":
#     n = 4
#     board = [[0 for _ in range(n)] for _ in range(n)]
#     solve_n_queens(board, 0, n)
# ```
# - **Setup**:
#   - Sets `n = 4` for a 4x4 board.
#   - Creates a 4x4 board initialized with zeros (empty):
#     ```python
#     board = [[0, 0, 0, 0],
#              [0, 0, 0, 0],
#              [0, 0, 0, 0],
#              [0, 0, 0, 0]]
#     ```
#   - Calls `solve_n_queens(board, 0, n)` to start placing queens from row 0.
# - **Execution**:
#   - The algorithm places queens row by row, checking constraints and backtracking as needed.
#   - Prints the first valid solution found.

# **Purpose**: Initializes the board and starts the backtracking process.

# ---

# ### Execution Walkthrough (for n=4)
# Let’s trace the algorithm for a 4x4 board:
# 1. **Initialize**:
#    - `board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]`.
#    - Start at `row = 0`.
# 2. **Row 0**:
#    - Try `col = 0`: `is_safe(0, 0, 4)` → `True`. Place queen: `board[0][0] = 1`.
#    - Call `solve_n_queens(board, 1, 4)`.
# 3. **Row 1**:
#    - Try `col = 0`: `is_safe(1, 0, 4)` → `False` (queen in column 0).
#    - Try `col = 1`: `is_safe(1, 1, 4)` → `False` (upper-left diagonal conflict).
#    - Try `col = 2`: `is_safe(1, 2, 4)` → `True`. Place queen: `board[1][2] = 1`.
#    - Call `solve_n_queens(board, 2, 4)`.
# 4. **Row 2**:
#    - Try `col = 0, 1, 2`: All `False` (conflicts with queens above).
#    - Try `col = 3`: `is_safe(2, 3, 4)` → `True`. Place queen: `board[2][3] = 1`.
#    - Call `solve_n_queens(board, 3, 4)`.
# 5. **Row 3**:
#    - Try `col = 0, 2, 3`: All `False`.
#    - Try `col = 1`: `is_safe(3, 1, 4)` → `True`. Place queen: `board[3][1] = 1`.
#    - Call `solve_n_queens(board, 4, 4)`.
# 6. **Base Case**:
#    - `row = 4`: All queens placed. Print board:
#      ```
#      Q . . .
#      . . Q .
#      . . . Q
#      . Q . .
#      ```
#    - Return `True`, stopping further exploration.
# 7. **Backtrack**:
#    - Since `True` is returned, the algorithm stops (first solution found).

# **Board State**:
# - Queens at `(0, 0)`, `(1, 2)`, `(2, 3)`, `(3, 1)` satisfy all constraints.

# ---

# ### Expected Output
# Running `python3 n_queens.py` in the VS Code terminal produces (for n=4):
# ```
# Q . . .
# . . Q .
# . . . Q
# . Q . .
# ```

# - **Explanation**:
#   - `"Q"` indicates a queen, `"."` indicates an empty cell.
#   - The output shows one valid configuration where 4 queens are placed without attacking each other.
#   - Note: For n=4, there are two solutions, but the code prints the first one found and stops (due to `return True`).

# ---

# ### Notes for Your Exam
# - **Key Concepts**: Understand backtracking, branch and bound, CSP constraints, and the `is_safe` checks for rows, columns, and diagonals.
# - **Code Structure**: Be ready to explain `is_safe`, `solve_n_queens`, and how backtracking reverts invalid placements.
# - **Edge Cases**:
#   - For n=2 or n=3, no solutions exist (code returns `False`).
#   - For n=1, a trivial solution exists.
#   - The code finds one solution; modify to find all by removing `return True` in the base case.
# - **Running in VS Code**: Save as `n_queens.py`, ensure `python3` works, and run `python3 n_queens.py` in the terminal.
# - **Customization**: If your exam specifies a different `n`, change `n = 4` in the main block.

# This explanation should help you master the N-Queens problem for your AI practical exam. If you have more practicals or need further clarification, let me know!