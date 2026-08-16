class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Assume we can only move right and down, no diagonals

        # Start at [0, 0], find all possible moves [0, 1] and [1, 0]
        # Continue a search from [0, 1] and [1, 0]
        # Recursion problem with dynamic programming
        # We want to build the solution from the top down and avoid extra computations

       
        # At any point, the number of ways to reach [i, j] = number of ways to reach from above + number of ways to reach from left


        # m -> rows    n -> cols

        # Fill the entire first row with 1s, there is only 1 way to get to any of these positions; you can only move right to get to any of these points
        result = [1] * n

        # Process remaining rows; iterate on each row from row 1 to row m
        for r in range(1, m):
            # Process each column, iterate through every col from col 1 to col n
            for c in range(1, n):
                # result[c] is the number of ways to reach the cell above our current cell
                # result[c - 1] is the number of ways to reach the cell to the left
                result[c] += result[c-1]
        return result[-1]