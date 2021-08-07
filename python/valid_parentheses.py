"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

examples
Input: s = "()"
Output: true

Input: s = "()[]{}"
Output: true

Input: s = "([)]"
Output: false

Input: s = "(]"
Output: false

Input: s = "{[]}"
Output: true
"""

class Solution:
    def isValid(self, s: str) -> bool:
        holder:dict = {')': '(', ']':'[', '}':'{'}
        stack = []

        for i in s:
            if i not in holder:
                stack.append(i)
            elif stack and i in holder and stack[-1] == holder[i]:
                stack.pop()
            else:
                return False
        return True if not stack else False
            
