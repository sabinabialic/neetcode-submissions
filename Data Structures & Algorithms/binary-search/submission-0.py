class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #       -1
        #     /    \
        #    0      2
        #   / \    /
        #  4   6  8

        # nums = [-1, 0, 2, 4, 6, 8]   t=4
        #        l=0             r=5

        l = 0
        r = len(nums)-1
        
        while l <= r:
            # Find midpoint
            m = l + ((r-l) // 2)

            if nums[m] < target:
                l = m + 1
            elif nums [m] > target:
                r = m - 1
            else:
                return m

        return -1
            