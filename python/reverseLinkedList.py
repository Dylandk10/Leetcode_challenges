#list class node to hold data
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

##function to reverse list
def reverseList(first_node) -> ListNode:
    prev = None
    curr = first_node
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev


#driver and printer
if __name__ == '__main__':
    head = ListNode(1)
    curr = head
    for i in range(2,10):
        curr.next = ListNode(i)
        curr = curr.next

    #before the reverse
    curr1 = head
    print("Before reverse:")
    while curr1:
        print(curr1.val)
        curr1 = curr1.next

    #call the reverse
    curr2 = reverseList(head)

    print("After Reverse")
    while curr2:
        print(curr2.val)
        curr2 = curr2.next
