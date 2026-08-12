class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #       -1
        #     /    \
        #    0      2
        #   / \    /
        #  4   6  8

        # nums = [-1, 0, 2, 4, 6, 8]     t=4
        #        l=0              r=5    m=0+(5/2)=2
        #            l=1          r=5    m=1+(4/2)=3
        #               l=2       r=5    m=2+(3/2)=3
        #                  l=3    r=5    nums[m]=t=4 -> done

        l = 0
        r = len(nums)-1
        
        while l <= r:
            # Find midpoint, // is floor division
            m = l + ((r-l) // 2)

            if nums[m] < target:
                l = m + 1
            elif nums [m] > target:
                r = m - 1
            else:
                return m

        return -1
            