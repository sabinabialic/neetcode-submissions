class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        d1 = dict()
        d2 = dict()

        # Populate d1
        for c in s:
            d1[c] = d1.get(c, 0) + 1
        
        # Populate d2
        for c in t:
            d2[c] = d2.get(c, 0) + 1

        # Compare
        if d1 == d2:
            return True
        
        return False
        