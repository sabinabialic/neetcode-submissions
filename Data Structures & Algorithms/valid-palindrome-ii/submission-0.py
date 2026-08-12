class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        #     L     R
        # a b c b b d b a

        while l < r:
            if s[l] != s[r]:
                skipL = s[l+1 : r+1] # s[3 : 6] -> b b d
                skipR = s[l : r] # s[2: 5] -> c b b 
                # bbd != dbb and cbb != bbc
                return skipL == skipL[::-1] or skipR == skipR[::-1]
            l += 1
            r -= 1
        return True