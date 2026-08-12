class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_mult, r_mult = 1, 1

        left = [0] * len(nums)
        right = [0] * len(nums)
        res = [0] * len(nums)

        j = len(nums)

        # forwards is i, backwards is j
        for i in range(len(nums)):
            j -= 1

            left[i] = l_mult
            right[j] = r_mult

            l_mult *= nums[i]
            r_mult *= nums[j]

        i, j = 0, len(nums)-1

        for i in range(len(nums)):
            res[i] = left[i] * right[i]

        return res


