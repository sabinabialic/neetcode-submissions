class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        total = 0
        res = float("inf")

        for n in range(len(nums)):
            total += nums[n]

            while total >= target:
                res = min(n-l+1, res)
                total -= nums[l]
                l += 1
        
        if res == float("inf"):
            return 0
        else:
            return res