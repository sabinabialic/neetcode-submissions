class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sol = set()

        for k in range(len(nums)):
            i = k + 1
            j = len(nums) - 1

            while i < j:
                total = nums[k] + nums[i] + nums[j]

                if total < 0:
                    i += 1
                elif total > 0:
                    j -= 1
                else:
                    sol.add((nums[k], nums[i], nums[j]))
                    i += 1
                    j -= 1

        return list(sol)