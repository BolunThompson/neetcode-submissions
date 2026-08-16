# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # stupid solution
        dummy = ListNode()
        while head is not None and head is not dummy:
            old_head = head
            head = head.next
            old_head.next = dummy
        return head is dummy