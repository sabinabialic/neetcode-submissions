class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # We only need to pass through the array once
        # Maintain a count of consecutive 1s
        # When we see a 1, increment the count
        # When we see a 0, compare the current count with the maximum
        # Adjust the maximum accordingly and reset count

        res = 0
        count = 0

        for num in nums:
            if num == 0:
                res = max(res, count)
                count = 0
            else:
                count += 1
        
        # Final check because it's possibe that the longest sequence may end at the last element
        return max(res, count)