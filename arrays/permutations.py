# https://leetcode.com/problems/permutations/
# 1st Solution

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.permutations(nums))