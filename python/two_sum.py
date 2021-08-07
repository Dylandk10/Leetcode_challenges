"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

examples
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Input: nums = [3,2,4], target = 6
Output: [1,2]

Input: nums = [3,2,4], target = 6
Output: [1,2]
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        returnList:List[int] = []
        vals = dict()
        for i in range(len(nums)):
            answer:int = target-nums[i]
            if answer not in vals:
                vals[nums[i]]=i
            else:
                return [vals[answer], i]
