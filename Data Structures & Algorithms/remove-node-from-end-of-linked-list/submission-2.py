# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        assert head is not None
        def count():
            i = 0
            p = head
            while p is not None:
                i += 1
                p = p.next
            return i

        def remove(n):
            i = 0
            p = head
            prev_head = None
            while i < n:
                i += 1
                assert p is not None
                prev_head = p
                p = p.next
            if prev_head is None:
                return head.next
            prev_head.next = p.next
            return head
        
        l = count()
        index = l - n
        return remove(index)
