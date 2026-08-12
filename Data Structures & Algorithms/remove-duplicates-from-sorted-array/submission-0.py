class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # unique = sorted(set(nums))
        # nums[:len(unique)] = unique
        # return len(unique)

        # Start at the second element bc nums[0] will always be unique
        l = 1
        r = 1

        while r < len(nums):
            # Case where nums[r] is unique
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
            r += 1
            
        return l