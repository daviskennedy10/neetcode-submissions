# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head
        # Find the midpoint
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        mid = slow.next
        slow.next = None

        # Reverse from midpoint
        curr = mid
        prev = None
        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        first = head
        last = prev
        
        # Switch them up
        while last:
            tempA = first.next 
            tempB = last.next
            first.next = last
            last.next = tempA 
            first = tempA
            last = tempB
