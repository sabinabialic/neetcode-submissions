class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest_seq = 0

        for n in nums:
            # Check if it's the start of a sequence
            if (n-1) not in s:
                curr_length = 0
                while (n+curr_length) in s:
                    curr_length += 1
                longest_seq = max(longest_seq, curr_length)

        return longest_seq