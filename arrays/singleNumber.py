# https://leetcode.com/problems/single-number/
# 1st Solution

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for i in nums:
            a ^= i
        return a
    
    
# 2nd Solution
# Time Limit Exceeded

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in nums:
            if nums.count(i) == 1:
                return i