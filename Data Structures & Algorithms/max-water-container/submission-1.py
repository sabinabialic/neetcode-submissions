class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        i = 0
        j = len(heights) - 1
        max_v = 0

        while i < j:
            v = 0
            if heights[i] < heights[j]:
                v = heights[i] * (j-i)
                i += 1
            else:
                v = heights[j] * (j-i)
                j -= 1
            max_v = max(max_v, v)

        return max_v
