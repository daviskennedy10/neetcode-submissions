# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def reversenode(node):
            prev = None
            curr = node
            while curr is not None:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev
        start = reversenode(head)
        if start is None:
            return start
        if n == 1:
            start = start.next
        else:
            curr = start
            for i in range(n-2):
                if curr is not None:
                    curr = curr.next
            if curr.next is not None:
                curr.next = curr.next.next
        res = reversenode(start)
        return res

