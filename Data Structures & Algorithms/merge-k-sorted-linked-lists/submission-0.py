# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def combine(n1, n2):
            dummy = ListNode(0)
            res = dummy
            while n1 and n2:
                if n1.val <= n2.val:
                    res.next = n1
                    res = res.next
                    n1 = n1.next
                else:
                    res.next = n2
                    res = res.next
                    n2 = n2.next
            if n1:
                res.next = n1
            if n2: 
                res.next = n2
            return dummy.next
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        res = lists[0]
        for i in range(len(lists)-1):
            res = combine(res, lists[i+1])
        return res
     