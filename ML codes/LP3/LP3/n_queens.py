#DAA exp5: Design n-Queens matrix having first Queen placed. Use backtracking
#to place remaining Queens to generate the final n-queen‘s matrix.		

def solveNQueens(n: int, first_queen_col: int):
    col = set()
    posDiag = set()  # r + c
    negDiag = set()  # r - c
    res = []

    # Initialize board
    board = [["."] * n for _ in range(n)]

    def backtrack(r):
        # If all queens are placed, store solution
        if r == n:
            res.append(["".join(row) for row in board])
            return

        for c in range(n):
            # Skip invalid positions
            if c in col or (r + c) in posDiag or (r - c) in negDiag:
                continue

            # Place queen
            col.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)
            board[r][c] = "Q"

            # Recurse for next row
            backtrack(r + 1)

            # Backtrack
            col.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)
            board[r][c] = "."

    # Place first queen manually
    col.add(first_queen_col)
    posDiag.add(0 + first_queen_col)
    negDiag.add(0 - first_queen_col)
    board[0][first_queen_col] = "Q"

    # Start recursion from second row
    backtrack(1)

    return res


# Example usage
if __name__ == "__main__":
    n = 5
    first_queen_col = 1  # You can change this (0-indexed)
    solutions = solveNQueens(n, first_queen_col)

    print(f"Total solutions with first Queen in column {first_queen_col}: {len(solutions)}\n")
    if solutions:
        print("One of the possible N-Queens boards:\n")
        for row in solutions[0]:
            print(" ".join(row))

