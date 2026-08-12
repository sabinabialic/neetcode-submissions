class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = [0] * n

        for i in range(n):
            rMax = -1
            for j in range(i+1, n):
                rMax = max(rMax, arr[j])
            ans[i] = rMax
        
        return ans