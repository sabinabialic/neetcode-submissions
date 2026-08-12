class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Binary search on each row to identify which row the target belongs to
        # Once we find the row, perform a binary search on the row itself

        rows, cols = len(matrix), len(matrix[0])

        top = 0
        bottom = rows-1

        while top <= bottom:
            mid = (top + bottom) // 2
            if target > matrix[mid][-1]:
                # Move down by one row
                top = mid + 1
            elif target < matrix[mid][0]:
                # Move up by one row
                bottom = mid - 1
            else:
                # Escape
                break
        if not (top <= bottom):
            return False
        
        curr_row = (top + bottom)//2
        l = 0
        r = cols - 1

        while l<= r:
            mid = (l + r)// 2
            if target > matrix[curr_row][mid]:
                # search to the right
                l = mid + 1
            elif target < matrix[curr_row][mid]:
                # search to the left
                r = mid - 1
            else:
                return True
        return False

            