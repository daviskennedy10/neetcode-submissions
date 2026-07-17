# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = l1
        p2 = l2
        dummy = ListNode(0)
        res = dummy
        carry = 0
        while p1 and p2:
            number = p1.val + p2.val + carry
            res.next = ListNode((number%10))
            carry = number // 10
            p1 = p1.next
            p2 = p2.next
            res = res.next
        while p1:
            number = p1.val + carry
            res.next = ListNode((number%10))
            carry = number // 10
            p1 = p1.next
            res = res.next
        while p2: 
            number = p2.val + carry
            res.next = ListNode((number%10))
            carry = number // 10
            p2 = p2.next
            res = res.next
        if carry != 0:
            res.next = ListNode((carry%10))
            res = res.next
        return dummy.next
