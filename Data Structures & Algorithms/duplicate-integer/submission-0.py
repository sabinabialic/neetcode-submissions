class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Create a hashmap
        # For i in nums, if i is already in the set then return True
        # If not, then add it to the set

        result = set()

        for i in nums:
            if i in result:
                return True
            result.add(i)
        
        return False

        

