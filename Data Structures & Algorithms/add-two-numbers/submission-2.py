# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        p1 = l1
        p2 = l2
        dummy = ListNode(0)
        res = dummy
        while p1 or p2 or carry:
            valA = p1.val if p1 else 0
            valB = p2.val if p2 else 0

            total = valA + valB + carry
            carry = total // 10
            res.next = ListNode(total%10)
            res = res.next

            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next
        return dummy.next