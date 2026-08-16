class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Binary search on each row to identify which row the target belongs to
        # Once we find the row, perform a binary search on the row itself

        rows = len(matrix)
        cols = len(matrix[0])

        # Set the boundaries to search for which row target is a part of
        top = 0
        bottom = rows - 1
            
        while top <= bottom:
            mid = (top + bottom) // 2
            # Check if target is greater than the last element in the current row
            if target > matrix[mid][-1]:
                # We need to move our search down
                top = mid + 1
            # Check of the target is less than the first element in the current row
            elif target < matrix[mid][0]:
                # We need to move our search up
                bottom = mid - 1
            else:
                break # We found the row where we should continue searching

        if  not top <= bottom:
            return False

        curr_row = mid
        # Set the boundaries for the search
        l = 0
        r = cols - 1

        while l <= r:
            mid = (l+r) // 2

            if target < matrix[curr_row][mid]:
                # That means target is to the left of mid
                # Continue the search to the left of mid
                r = mid - 1
            elif target > matrix[curr_row][mid]:
                # That means target is to the right of mid
                # Continue the search to the right of mid
                l = mid + 1
            else:
                return True
        
        return False

        #  l     m      r
        #           lm  r
        #              lrm
        # [4, 5, 8, 9, 11]