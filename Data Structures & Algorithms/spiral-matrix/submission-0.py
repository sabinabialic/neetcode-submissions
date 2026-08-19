class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Number of cols
        l = 0
        r = len(matrix[0])

        # Number of rows
        t = 0
        b = len(matrix)

        result = []

        # Always start at the top left position and go right (first row)
        # Keep moving right until we reach the right boundary
        # Once we have reached the right boundary, shift the top boundary by -1 and move down
        # Once we reach the bottom boundary, shift the right boundary by -1 and move left
        # Keep moving left until we reach the left boundary
        # Once we reach the left boundary, shift the bottom boundary by +1 and move up
        # Continue moving up until we reach the top boundary
        # Once we reach the top boundary, shift the left boundary by +1 

        # O(n*m) time
        # Keep looping until one of the pointers cross
        while l<r and t<b:
            # Get every i in the top row
            for i in range(l, r):
                result.append(matrix[t][i])
            # Adjust the top boundary
            t += 1

            # Get every i in the rightmost col
            for i in range(t, b):
                result.append(matrix[i][r-1])
            # Adjust the right boundary
            r -= 1

            # At this point it's possible that the pointers have crossed
            if not (l<r and t<b):
                break

            # Get every i in the bottom row
            for i in range(r-1, l-1, -1):
                result.append(matrix[b-1][i])
            # Adjust the bottom boundary
            b -= 1

            # Get every i in the leftmost col
            for i in range(b-1, t-1, -1):
                result.append(matrix[i][l])
            # Adjust the left boundary
            l += 1
        
        return result