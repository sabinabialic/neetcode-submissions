class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Case where len is even (dood)
        # Sliding pointers to i and len-i
        # If i > len-i, break
                                    #
        # Case where len is off (racecar)
        # Sliding pointers to i and len-i
        # If i == len-i, break

        s = s.lower()
        s = re.sub(r'[^\w]', '', s)

        i, j = 0, len(s) - 1

        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
