class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # [2, 7, 11]
        # target = 9

        # 9-2 = 7
        # check if we already saw the number 7
        # if yes, we're done
        # if not, add 2 to the map and its position in nums
        # map = [2, 0]

        # 9-7 = 2
        # map contains a 2
        # return [0, 1]

        if len(nums) < 2:
            return null

        map = {}

        for i in range(len(nums)):
            sol = target - nums[i]

            if sol in map:
                return [map.get(sol), i]

            map.setdefault(nums[i], i)
