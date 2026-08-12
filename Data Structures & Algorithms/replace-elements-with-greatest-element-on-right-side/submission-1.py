class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = [0] * n

        rMax = -1

        for i in range(n-1, -1, -1):
            ans[i] = rMax
            rMax = max(arr[i], rMax)
        
        return ans