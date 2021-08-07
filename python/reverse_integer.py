"""
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

examples
Input: x = 123
Output: 321

Input: x = -123
Output: -321

Input: x = 120
Output: 21

"""
class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            txt = str(x)
            removeFirst = txt[1:]
            rev = removeFirst[::-1]
            value = int("-"+rev)
        else:
            txt = str(x)
            rev = txt[::-1]
            value = int(rev)

        maxV = 2**31
        minV = -2**31
        if value > minV and value < maxV:
            return value
        else:
            return 0
