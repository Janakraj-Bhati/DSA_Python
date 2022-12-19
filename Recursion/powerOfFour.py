# 1st Solution
# https://leetcode.com/problems/power-of-four/submissions/

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        while n%4 == 0 and n > 0:
            return self.isPowerOfFour(n/4)
        return n == 1