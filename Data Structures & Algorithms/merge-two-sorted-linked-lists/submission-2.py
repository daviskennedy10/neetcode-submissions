# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        res = ListNode(0)
        dummy = res
        while curr1 is not None and curr2 is not None:
            if curr1.val <= curr2.val:
                res.next = ListNode(curr1.val)
                curr1 = curr1.next
            else:
                res.next = ListNode(curr2.val)
                curr2 = curr2.next
            res = res.next
        while curr1 is not None and curr2 is None:
            res.next = ListNode(curr1.val)
            curr1 = curr1.next
            res = res.next
        while curr2 is not None and curr1 is None:
            res.next = ListNode(curr2.val)
            curr2 = curr2.next
            res = res.next
        return dummy.next
