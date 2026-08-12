class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        a = 0
        b = len(arr) - 1

        while b - a >= k:
            if abs(arr[a] - x) <= abs(arr[b]-x):
                b -= 1
            else:
                a +=1
        
        return arr[a: b+1]