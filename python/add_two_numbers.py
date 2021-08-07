"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself

examples
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Input: l1 = [0], l2 = [0]
Output: [0]

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        str1 = ""
        str2 = ""

        #build str1
        curr1 = l1
        while curr1:
            str1 = str1 + str(curr1.val)
            curr1 = curr1.next

        #build str2
        curr2 = l2
        while curr2:
            str2 = str2 + str(curr2.val)
            curr2 = curr2.next
        #reverse both strings
        rev1 = str1[::-1]
        rev2 = str2[::-1]

        ##add the numbers then reverse them back and add to list
        answer = int(rev1) + int(rev2)
        answerStr = str(answer)
        answerRev = answerStr[::-1]
        answerList = list(answerRev)

        #build link list
        head = None
        for i in answerList:
            curr = head
            if not head:
                head = ListNode(i)
            while curr:
                if curr.next is None:
                    curr.next = ListNode(i)
                    break
                curr = curr.next
        return head
                
