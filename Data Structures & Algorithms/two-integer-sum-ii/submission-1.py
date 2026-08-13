class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        i = 0
        j = len(nums) - 1

        while i < j:
            currSum = nums[i] + nums[j]

            if currSum > target:
                j -= 1
            
            elif currSum < target:
                i += 1
            
            else:
                return [i+1 , j+1]

        return []