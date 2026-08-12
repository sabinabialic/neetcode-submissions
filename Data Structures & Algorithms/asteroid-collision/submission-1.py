class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []

        for a in asteroids:
            while s and a < 0 and s[-1] > 0:
                diff = a + s[-1]

                if diff == 0:
                    s.pop()
                    a = 0
                elif diff > 0:
                    a = 0
                else:
                    s.pop()
            if a:
                s.append(a)
        
        return s