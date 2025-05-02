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



# Absolutely! Let’s break down your **N-Queens problem** code in **easy, step-by-step language**, explain the **concept**, and summarize it with a **short algorithm** and **new terms** at the end.

# ---

# ## 👑 What is the **N-Queens Problem**?

# You need to place **N queens** on an **N×N chessboard** such that:

# * No two queens attack each other.
# * Queens attack:

#   * **Vertically (same column)**
#   * **Diagonally (both directions)**
#   * **Horizontally (same row)** → this is avoided by placing one queen per row only.

# ---

# Of course! Here's a **clear, detailed, and easy-to-understand** step-by-step explanation of your **N-Queens code**.

# ---

# ## 🎯 **Goal of the Code**

# Place `N` queens on an `N x N` chessboard so that **no two queens** threaten each other (i.e., no two in the same **row**, **column**, or **diagonal**).

# This solution uses **Backtracking** — trying one option at a time and **undoing** choices when necessary.

# ---

# ## ✅ Step-by-Step Code Breakdown

# ### ---

# ### 1. `is_safe(board, row, col, n)`

# Checks if it is safe to place a queen at position `(row, col)`.

# ```python
# for i in range(row):
#     if board[i][col] == 1:
#         return False
# ```

# * ✔️ **Check vertical column** (above current row).
# * ❌ If any queen is already there, **unsafe**.

# ```python
# i, j = row, col
# while i >= 0 and j >= 0:
#     if board[i][j] == 1:
#         return False
#     i -= 1
#     j -= 1
# ```

# * ✔️ **Check upper-left diagonal** (`↖`)
# * ❌ If any queen found, **unsafe**.

# ```python
# i, j = row, col
# while i >= 0 and j < n:
#     if board[i][j] == 1:
#         return False
#     i -= 1
#     j += 1
# ```

# * ✔️ **Check upper-right diagonal** (`↗`)
# * ❌ If any queen found, **unsafe**.

# ```python
# return True
# ```

# * ✅ If all checks pass, it’s **safe** to place a queen.

# ---

# ### ---

# ### 2. `solve_n_queens(board, row, n)`

# Tries to place a queen in each row using **recursion and backtracking**.

# ```python
# if row == n:
#     for r in board:
#         print(" ".join("Q" if c == 1 else "." for c in r))
#     print()
#     return True
# ```

# * ✅ **Base case**: if we've placed queens in all `n` rows, print the board.
# * `"Q"` is where a queen is placed, `"."` is an empty cell.
# * Return `True` to signal success.

# ---

# ```python
# for col in range(n):
#     if is_safe(board, row, col, n):
# ```

# * 🔁 Try placing a queen in each column of the current `row`.
# * ✔️ If `is_safe()` returns true:

# ```python
# board[row][col] = 1
# ```

# * ✅ Place the queen.

# ```python
# if solve_n_queens(board, row + 1, n):
#     return True
# ```

# * 🔄 Recurse to place a queen in the **next row**.
# * ✅ If this leads to a solution, return `True`.

# ```python
# board[row][col] = 0  # Backtrack
# ```

# * ❌ If the choice leads to a dead-end, **remove the queen** and try next column.
# * This is called **backtracking**.

# ```python
# return False
# ```

# * ❌ If no column worked in this row, return False to backtrack further.

# ---

# ### ---

# ### 3. `main` function

# ```python
# n = 4
# board = [[0 for _ in range(n)] for _ in range(n)]
# solve_n_queens(board, 0, n)
# ```

# * Initializes a **4x4 board** filled with 0s (empty).
# * Starts solving from **row 0**.

# ---

# ## 📌 What Does the Output Look Like?

# For `n = 4`, it prints:

# ```
# . Q . .
# . . . Q
# Q . . .
# . . Q .
# ```

# That’s a valid arrangement of 4 queens.

# ---

# ## 📚 Summary: Short Algorithm

# ### 🔁 Backtracking Algorithm for N-Queens:

# 1. Start from row 0.
# 2. For each column in the row:

#    * If safe, place queen.
#    * Recur to next row.
#    * If failure, remove queen (backtrack).
# 3. If all rows filled, print solution.

# ---

# ## 🧱 New Terms

# | Term                   | Meaning                                                    |
# | ---------------------- | ---------------------------------------------------------- |
# | **Backtracking**       | Try a solution, and undo it if it leads to a dead end.     |
# | **Recursive Function** | A function that calls itself to explore smaller problems.  |
# | **Base Case**          | The condition to stop recursion. (`row == n`)              |
# | **Diagonal Check**     | Ensures queens don’t attack each other diagonally.         |
# | **is\_safe()**         | Checks whether a queen can be placed safely at a position. |

# ---

# Would you like me to modify this to **print all solutions**, not just the first one?


