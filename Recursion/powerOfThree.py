# 1st Solution
# https://leetcode.com/problems/power-of-three/

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        if n % 3 == 0:
            return self.isPowerOfThree(n//3)
        return False
    
    
# 2nd Solution
# One Line Solution

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return (n > 0) and 1162261467 % n == 0