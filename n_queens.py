def solve_n_queens(n):
    def is_safe(board, row, col):
        # Check if it's safe to place a queen at board[row][col]
        for i in range(row):
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True

    def solve(board, row):
        if row == n:
            result.append(board[:])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                solve(board, row + 1)
                # Backtrack
                board[row] = -1

    result = []
    solve([-1] * n, 0)
    return result

# Example usage:
n = 4
solutions = solve_n_queens(n)
for solution in solutions:
    print(solution)
