class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        # Get the index and the value
        for i, v in enumerate(temperatures):
            # While value is greater than the value at the top of the stack
            # stack[-1][0]  → temperature
            # stack[-1][1]  → index
            while stack and v > stack[-1][-1]:
                idx, val = stack.pop()
                res[idx] = i - idx
            stack.append((i, v))
        return res