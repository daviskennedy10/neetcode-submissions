# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def reverse(node, final):
            prev = None
            curr = node
            while curr != final:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev
        dummy = ListNode(0, head)
        currA = head
        tempA = dummy
        for _ in range(left-1):
            tempA = currA
            currA = currA.next
        currB = head
        for i in range(right):
            currB = currB.next
        tempA.next = reverse(currA, currB)
        currA.next = currB
        return dummy.next