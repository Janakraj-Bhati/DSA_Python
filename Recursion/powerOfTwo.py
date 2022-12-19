# 1st Solution
# https://leetcode.com/problems/power-of-two/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        if n % 2 == 1 and n != 1:
            return False
        if n % 2 == 0:
            return self.isPowerOfTwo(n//2)
        return True
    
# 2nd Solution
# One line solution

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n&(n - 1) == 0