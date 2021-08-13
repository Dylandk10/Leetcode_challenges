"""
Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists

example:
Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4

Input: l1 = [], l2 = [0]
Output: [0]
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_curr = l1
        l2_curr = l2
        holdList = []
        returnList = self.getList(l1_curr, l2_curr, holdList)
        print(returnList)

        head = None
        for i in returnList:
            curr = head
            if not head:
                head = ListNode(i)
            while curr:
                if curr.next is None:
                    curr.next = ListNode(i)
                    break
                curr = curr.next

        return head

    def getList(self, l1, l2, l) -> List:
        if l1 is None:
            curr2 = l2
            while curr2:
                l.append(curr2.val)
                curr2 = curr2.next
            return l
        if l2 is None:
            curr1 = l1
            while curr1:
                l.append(curr1.val)
                curr1 = curr1.next
            return l
        if l1.val == l2.val:
            l.append(l1.val)
            l.append(l2.val)
            return self.getList(l1.next, l2.next, l)
        elif l1.val > l2.val:
            l.append(l2.val)
            return self.getList(l1, l2.next, l)
        elif l1.val < l2.val:
            l.append(l1.val)
            return self.getList(l1.next, l2, l)
