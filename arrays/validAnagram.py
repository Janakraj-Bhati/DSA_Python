# https://leetcode.com/problems/valid-anagram/
# 1st Solution

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        newL = []
        oldL = []
        for i in s:
            newL.append(i)
        for j in t:
            oldL.append(j)
        newL.sort()
        oldL.sort()
        if newL == oldL:
            return True
        else:
            return False
        
# 2nd Solution
class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        l = "abcdefghijklmnopqrstuvwxyz"
        for c in l:
            if s.count(c) != t.count(c):
                return False
        return True
