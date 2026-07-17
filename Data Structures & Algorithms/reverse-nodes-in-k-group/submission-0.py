# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(node, end):
            if node.next is None:
                return node
            prev = None
            curr = node
            while curr != end:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev
        if head is None:
            return None
        if head.next is None:
            return head
        fast = head
        slow = head
        check = head
        length = 0
        while check:
            check = check.next
            length+=1
        wrap = length // k
        count = 0
        checker = head
        while count < wrap:
            if count == 0:
                for _ in range(k):
                    fast = fast.next
                dummy = reverse(slow, fast)
                res = dummy
                while checker.next:
                    checker = checker.next

            else: 
                for _ in range(k):
                    fast = fast.next
                checker.next = reverse(slow, fast)
                while checker.next:
                    checker = checker.next
            count+=1
            slow = fast
        checker.next = fast
        return res


        
        