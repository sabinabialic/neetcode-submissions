class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        g = len(grid)

        # Hashsets detect duplicates efficiently
        # We won't be able to add a number which already exists in the hashset
        seen = set()

        double = 0
        missing = 0

        # Traverse the set
        # If the current number is already in the set, we found the double number
        # If not in the set, add it
        for i in range(g):
            for j in range(g):
                if grid[i][j] in seen:
                    double = grid[i][j]
                seen.add(grid[i][j])
        
        # We know the grid is size g * g
        # We know the numbers in grid range from 1 ... g^2=g*g
        # Strart from 1 and go all the way to g*g + 1, but not including +1
        # Ie. only include 1 ... g*g
        for num in range(1, (g*g) + 1):
            if num not in seen:
                missing = num
                break

        return [double, missing]