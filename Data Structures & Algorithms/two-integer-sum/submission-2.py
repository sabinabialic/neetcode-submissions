class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # x + y = target
        # x = target - y

        # For each num in nums, calculate target-num
        # If we have already seen target-num, return the index of target-num and num
        # We can use a dict to store (k, v) where k is target-num and v is the index

        # Edge case: only 1 number in the input
        if len(nums) < 2:
            return null

        seen = {}

        for i in range(len(nums)):
            res = target - nums[i]

            if res in seen:
                return [seen.get(res), i]
            
            seen[nums[i]] = i