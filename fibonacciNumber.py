# 1st Solution
# https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        if n <= 0:
            return abs(n)
        return self.fib(n-1) + self.fib(n - 2)
    
# 2nd Solution

class Solution:
    def fib(self, N: int) -> int:
        a, b = 0, 1
        for i in range(N): a, b = b, a + b
        return a