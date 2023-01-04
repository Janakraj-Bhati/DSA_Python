# https://leetcode.com/problems/valid-parentheses/
# 1st Solution
class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'{': '}', '(': ')', '[': ']'}
        
        stack = []
        for char in s:
            if char in brackets:
                stack.append(char)
            elif not stack or brackets[stack.pop()] != char:
                return False
            
        return not stack