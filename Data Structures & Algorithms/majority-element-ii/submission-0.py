class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        res = []
        myMap = {}

        for n in nums:
            if n in myMap:
                myMap[n] += 1
            else:
                myMap[n] = 1
        
        for k in myMap:
            if myMap[k] > len(nums)//3:
                res.append(k)
        
        return res