class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Use a set
        # If the element is already in the set, return True - we found the duplicate
        # Otherwise add it to the set

        unique = set()

        for num in nums:
            if num in unique:
                return True
            else:
                unique.add(num)
        return False