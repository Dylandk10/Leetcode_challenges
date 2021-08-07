"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

examples
Input: strs = ["flower","flow","flight"]
Output: "fl"

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortestWord:str = strs[0]
        result:str = ""
        for i in strs:
            if len(i) < len(shortestWord):
                shortestWord = i

        for i in range(len(shortestWord)):
            holdstr:str = ""
            compare:str = shortestWord[i]
            for j in range(len(strs)):
                if compare == strs[j][i]:
                    holdstr = strs[j][i]
                else:
                    return result
            result = result + holdstr
        return result
