class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0 
        res = [0] * len(nums)

        for i in range(len(nums)):
            new_index = (i + k) % len(nums)
            res[new_index] = nums[i]

        nums[:] = res